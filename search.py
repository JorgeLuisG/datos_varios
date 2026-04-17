from pathlib import Path
import pandas as pd
import unicodedata
import re

def normalizar(texto):
    texto = str(texto)

    # quitar acentos
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')

    # pasar a minúsculas
    texto = texto.lower()

    # reemplazar guiones y underscores por espacio
    texto = re.sub(r'[-_]', ' ', texto)

    # eliminar espacios múltiples
    texto = re.sub(r'\s+', ' ', texto).strip()

    return texto

def cargar_datos():
    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"

    archivos = {
        "cuil contratista": data_dir / "cuil contratista.csv",
        "contrato": data_dir / "contrato.csv",
        "cronograma poda": data_dir / "cronograma poda.csv",
        "certificacion poda": data_dir / "certificacion poda.csv",
    }

    faltantes = [str(path) for path in archivos.values() if not path.exists()]
    if faltantes:
        raise FileNotFoundError(
            "No se encontraron los archivos de datos necesarios. "
            f"Asegúrate de que existan en la carpeta {data_dir}:\n"
            f"- {archivos['cuil contratista']}\n"
            f"- {archivos['contrato']}\n"
            f"- {archivos['cronograma poda']}\n"
            f"- {archivos['certificacion poda']}"
        )

    vacios = [str(path) for path in archivos.values() if path.exists() and path.stat().st_size == 0]
    if vacios:
        raise ValueError(
            "Se encontraron archivos de datos vacíos. "
            f"Revisa el contenido en la carpeta {data_dir}:\n"
            + "\n".join(f"- {path}" for path in vacios)
        )

    cuil_contratista = pd.read_csv(archivos["cuil contratista"])
    contratos = pd.read_csv(archivos["contrato"])
    cronograma_poda = pd.read_csv(archivos["cronograma poda"])
    certificacion_poda = pd.read_csv(archivos["certificacion poda"],sep=";")
    return cuil_contratista, contratos, cronograma_poda, certificacion_poda


def buscar(query, dfs):
    resultados = []
    query = normalizar(query)

    for nombre, df in dfs.items():
        # normalizar todo el dataframe
        df_normalizado = df.astype(str).applymap(normalizar)

        mask = df_normalizado.apply(
            lambda row: row.str.contains(query).any(), axis=1
        )

        if mask.any():
            resultados.append((nombre, df[mask]))

    return resultados