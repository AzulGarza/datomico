import numpy as np
from dataset import ModelData


class ColumnarDataset(Dataset):
    def __init__(self, cats, conts, y, is_reg, is_multi):
        n = len(cats[0]) if cats else len(conts[0])
        self.cats = np.stack(cats, 1).astype(np.int64) if cats else np.zeros((n,1))
        self.conts = np.stack(conts, 1).astype(np.float32) if conts else np.zeros((n,1))
        self.y = np.zeros((n, 1))                       if y is None else y
        if is_reg:
            self.y = self.y[:, None]
            self.is_reg = is_reg
            self.is_multi = is_multi

    def __len__(self): return len(self.y)

    def __getitem__(self, idx):
        return [self.cats[idx], self.conts[idx], self.y[idx]]

    @classmethod
    def from_data_frames(cls, df_cat, df_cont, y=None, is_reg=True, is_multi=False):
        cat_cols = [c.values for n, c in df_cat.items()]
        cont_cols = [c.values for n, c in df_cont.items()]
        return cls(cat_cols, cont_cols, y, is_reg, is_multi)

    @classmethod
    def from_data_frame(cls, df, cat_flds, y=None, is_reg=True, is_multi=False):
        return cls.from_data_frames(df[cat_flds], df.drop(cat_flds, axis=1), y, is_reg, is_multi)


class ColumnarModelData(ModelData):
    def __init__(self, path, trn_ds, val_ds, bs, test_ds=None, shuffle=True):
        test_dl = DataLoader(test_ds, bs, shuffle=False, num_workers=1) if test_ds is not None else None
        super().__init__(path, DataLoader(trn_ds, bs, shuffle=shuffle, num_workers=1),
            DataLoader(val_ds, bs*2, shuffle=False, num_workers=1), test_dl)

        @classmethod
        def from_arrays(cls, path, val_idxs, bs, test_ds=None, shuffle=True):
            ((val_xs, trn_xs), (val_y, trn_y)) = split_by_idx(val_idxs, xs, y)
            test_ds = PassthruDataset(*(test_xs.T), [0]*len(test_xs), is_reg=is_reg, is_multi=is_multi) if test_xs is not None else None
            return cls(path, PassthruDataset(*(trn_xs.T), trn_y, is_reg=is_reg, is_multi=is_multi),
                       PassthruDataset(*(val_xs.T), val_y, is_reg=is_reg, is_multi=is_multi),
                       bs=bs, shuffle=shuffle, test_ds=test_ds)

        @classmethod
        def from_data_frames(cls, path, trn_df, val_df, trn_y, val_y, cat_flds, bs=64, is_reg=True, is_multi=False, test_df=None, shuffle=True):
            trn_ds = ColumnarDataset.from_data_frame(trn_df, cat_flds, trn_y, is_reg, is_multi)
            val_ds = ColumnarDataset.from_data_frames(val_df, cat_flds, val_y, is_reg, is_multi)
            test_ds = ColumnarDataset.from_data_frame(test_df, cat_flds, None, is_reg, is_multi) if test_df is not None else None
            return cls(path, trn_ds, val_ds, bs, test_ds=test_ds, shuffle=shuffle)

        @classmethod
        def from_data_frame(cls, path, val_idxs, df, y, cat_flds, bs=64, is_reg=True, is_multi=False, test_df=None, shuffle=True):
            ((val_df, trn_df), (val_y, trn_y)) = split_by_idx(val_idxs, df, y)
            return cls.from_data_frames(path, trn_df, val_df, trn_y, val_y, cat_flds, bs, is_reg, is_multi, test_df=test_df, shuffle=shuffle)

        def get_learner(self, emb_szs, n_cont, emb_drop, out_sz, szs, drops,
                        y_range=None, use_bn=False, **kwargs):
            model = MixedInputModel(emb_szs, n_cont, emb_drop, out_sz, szs, drops, y_range, use_bn, self.is_reg, self.is_multi)
            return StructuredLearner(self, StructuredModel(to_gpu(model)), opt_fn=Adam, **kwargs)
