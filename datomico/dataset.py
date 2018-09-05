class ModelData():
    def __init__(self, path, trn_dl, val_dl, test_dl=None):
        self.path, self.trn_dl, self.val_dl, self.test_dl = path, trn_dl, val_dl, test_dl

    @classmethod
    def from_dls(cls, path, trn_dl, val_dl, test_dl=None):
        return cls(path, trn_dl, val_dl, test_dl)

    @property
    def is_reg(self): return self.trn_ds.is_reg

    @property
    def is_multi(self): return self.trn_ds.is_multi

    @property
    def trn_ds(self): return self.trn_dl.dataset

    @property
    def val_ds(self): return self.val_dl.dataset

    @property
    def test_ds(self): return self.test_dl.dataset

    @property
    def trn_y(self): return self.trn_ds.y

    @property
    def val_y(self): return self.val_ds.y
