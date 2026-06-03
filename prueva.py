import pandas as pd

archivos = {
    "cuil_contratista": "data/cuil contratista.csv",
    "contratos": "data/contrato.csv",
    "cronograma_poda": "data/cronograma poda.csv",
    "certificacion_poda": "data/certificacion poda.csv",
    "contactos_internos": "data/contactos internos.csv",
}

for nombre, archivo in archivos.items():

    if nombre in ["certificacion_poda", "contactos_internos"]:
        df = pd.read_csv(archivo, sep=";")
    else:
        df = pd.read_csv(archivo)

    print("\n" + "="*50)
    print(nombre)
    print(df.columns.tolist())
    