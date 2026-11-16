#!/usr/bin/env python3
"""Reto 1 - Generar el archivo limpio.

Entrada : netflix_titles.csv
Salida  : netflix_clean.csv

Uso: python 01_limpiar_netflix.py [entrada.csv] [salida.csv]
"""
import sys

import pandas as pd

ENTRADA = sys.argv[1] if len(sys.argv) > 1 else "netflix_titles.csv"
SALIDA = sys.argv[2] if len(sys.argv) > 2 else "netflix_clean.csv"

# ---------------------------------------------------------------- 1.1 Lectura
# dtype=str y keep_default_na=False: no se interpreta nada por adelantado
# (p. ej. un titulo "None" o "NA" no debe volverse nulo sin que lo decidamos).
df = pd.read_csv(ENTRADA, dtype=str, keep_default_na=False, encoding="utf-8")
registros_iniciales, columnas_originales = df.shape
columnas = list(df.columns)

# 1. Eliminar espacios al inicio y al final de los campos de texto
df = df.apply(lambda s: s.str.strip())

# 2. Saltos de linea y tabulaciones -> espacio (un registro = una linea)
df = df.apply(lambda s: s.str.replace(r"[\r\n\t]+", " ", regex=True).str.strip())

# 3. Textos vacios -> nulos
df = df.replace(r"^\s*$", pd.NA, regex=True)

# 4. Eliminar filas completamente duplicadas
n = len(df)
df = df.drop_duplicates()
duplicadas_completas = n - len(df)

# 5. Eliminar registros sin show_id
n = len(df)
df = df.dropna(subset=["show_id"])
sin_show_id = n - len(df)

# 6. show_id repetido: conservar la primera aparicion
n = len(df)
df = df.drop_duplicates(subset=["show_id"], keep="first")
show_id_repetido = n - len(df)

# 7. date_added -> dd/mm/aaaa (vacio si falta o no se puede interpretar)
fechas = pd.to_datetime(df["date_added"], format="%B %d, %Y", errors="coerce")
df["date_added"] = fechas.dt.strftime("%d/%m/%Y")

# 8. duration_min: minutos solo para type == Movie (entero que admite nulos)
minutos = df["duration"].str.extract(r"^\s*(\d+)\s*min\s*$", expand=False)
minutos = pd.to_numeric(minutos, errors="coerce").astype("Int64")
es_pelicula = df["type"].eq("Movie").fillna(False).astype(bool)
df["duration_min"] = minutos.where(es_pelicula).astype("Int64")

# 9. Columnas originales + duration_min al final
df = df[columnas + ["duration_min"]]

# 10. Los datos desconocidos se mantienen como nulos (no se imputa nada).

# 11. Guardar: UTF-8, cabecera, comas, sin indice
df.to_csv(SALIDA, index=False, encoding="utf-8", sep=",", header=True)

# ------------------------------------------------- 1.2 Comprobar el resultado
peliculas = df[df["type"] == "Movie"]
con_duracion = int((peliculas["duration_min"] > 0).sum())
sin_duracion = len(peliculas) - con_duracion

print("=" * 62)
print("RESULTADO DE LA LIMPIEZA")
print("=" * 62)
print(f"Registros del archivo original (sin cabecera) : {registros_iniciales}")
print(f"Columnas del archivo original                 : {columnas_originales}")
print(f"Filas completamente duplicadas eliminadas     : {duplicadas_completas}")
print(f"Registros sin show_id eliminados              : {sin_show_id}")
print(f"Registros con show_id repetido eliminados     : {show_id_repetido}")
print(f"Registros del archivo limpio                  : {len(df)}")
print(f"Peliculas con duration_min > 0                : {con_duracion}")
print(f"Peliculas sin duracion numerica > 0           : {sin_duracion}")
print("-" * 62)
print(f"Verificacion: {registros_iniciales} - {duplicadas_completas} - "
      f"{sin_show_id} - {show_id_repetido} = "
      f"{registros_iniciales - duplicadas_completas - sin_show_id - show_id_repetido}")
print(f"Archivo generado: {SALIDA}")
