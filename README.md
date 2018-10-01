# Librería

Porfa descarguen el env a ver si funciona en Windows y/o MacOS.


## Requisitos:
- Anaconda python 3.7

# Instalación
1. `git clone https://github.com/datomicomx/datomico.git`
2. `cd datomico`
3. `conda env update`
4. Para linux/Mac: `source activate datomico` Para Windows (wakatelas): `conda activate datomico` 
5. Corran prueba.ipynb por si hay errores. Les debera de crear un archivo que se llama TPV_10mil_adultos.csv en data/

#### Nota:
Pasos para que el kernel de jupyter funcione de acuerdo al env en anaconda: 
1. `source activate datomico` o `conda activate datomico`.
2. `conda install ipykernel jupyter`
3. `python -m ipykernel install --user --name datomico --display-name "Python (datomico)"`
4. Revisar que sys.executable sea python de tu env.
- Si no sirve el paso 3, utilizar: ` /path/to/kernel/env/bin/python -m ipykernel install --prefix=/path/to/jupyter/env --name 'python-my-env'`

### Para descargar los datos de Kaggle cuando se requieran en ciertos modelos del Blog:
1. Instalen kaggle-cli
`pip install kaggle-cli`
2. Configuren su cuenta de kaggle
`kg config -u <usuario (email)> -p <contraseña> -c <nombre-competencia>`
3. Descargar los datos
`kg download`
4. Archivos zip
`unzip -q <filename.zip>`
5. Archivos tar 
`7za x <filename.tar.7za>` Esto nos deja filename.tar. 
6. Para extraer los archivos de filename.tar => `tar -xf <filename.tar>`
7. Pongan los datos en un folder `data/` dentro de `datomico/`
