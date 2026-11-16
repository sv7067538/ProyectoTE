import glob
import pandas as pd

# Carpeta con las partes descargadas de HDFS (part-00000, ...)
partes = sorted(glob.glob("resultado_actores/part-*"))

df = pd.concat(
    (pd.read_csv(p, sep="\t", header=None, names=["actor", "cantidad_titulos"],
                 encoding="utf-8", keep_default_na=False, dtype={"actor": str})
     for p in partes),
    ignore_index=True,
)

df = df.groupby("actor", as_index=False)["cantidad_titulos"].sum()
df = df.sort_values(["cantidad_titulos", "actor"], ascending=[False, True])
df.to_csv("mapreduce_actores.csv", index=False, encoding="utf-8")

print(f"Partes leídas: {len(partes)} | Actores: {len(df)}")
print(df.head(10).to_string(index=False))
