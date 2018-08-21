# Librería

Porfa descarguen el env a ver si funciona en Windows y/o MacOS.


## Requisitos:
- Anaconda python 3.7

# Instalación
1. `git clone https://github.com/datomicomx/datomico.git`
2. `cd datomico`
3. `conda env update`
4. `conda activate datomico`
5. Corran prueba.ipynb por si hay errores. 


### Para que ustedes tengan los datos también y no tener que subirlos al repositorio:
kaggle cli.



#### Nota:
Pasos para que el kernel de jupyter funcione de acuerdo al env en anaconda: 
1. source activate datomico.
2. conda install ipykernel jupyter
3. ` /path/to/kernel/env/bin/python -m ipykernel install --prefix=/path/to/jupyter/env --name 'python-my-env'`
4. Revisar que sys.executable sera python de tu env.

