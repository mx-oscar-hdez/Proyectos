import pandas as pd
import matplotlib.pyplot as plt

# Solicita al usuario la ruta del archivo CSV.
ruta_archivo = input("Ingresa la ruta del archivo CSV a analizar: ").strip().strip('"')
# Lee el CSV detectando automaticamente el separador.
df = pd.read_csv(ruta_archivo, sep=None, engine="python")

# Intenta convertir columnas tipo texto a numericas
# para soportar decimales con coma y separador de miles.
for columna in df.columns:
    if df[columna].dtype == "object":
        serie_limpia = (
            df[columna]
            .astype(str)
            .str.strip()
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
        )
        # Mantiene el valor original si no se puede convertir.
        df[columna] = pd.to_numeric(serie_limpia, errors="ignore")

# Muestra una vista previa de los datos.
print("Primeras 5 filas:")
print(df.head())

# Muestra estructura del DataFrame: tipos, nulos y memoria.
print("\nInformacion general:")
print(df.info())

# Selecciona solo columnas numericas para calcular estadisticas.
print("\nEstadisticas solicitadas (media, mediana y desviacion estandar):")
df_numerico = df.select_dtypes(include=["number"])
if df_numerico.empty:
    print("No hay columnas numericas para calcular estadisticas.")
    print("Revisa separador del CSV (',' o ';') y formato decimal ('.' o ',').")
else:
    # Construye una tabla con estadisticas por columna numerica.
    estadisticas = pd.DataFrame(
        {
            "media": df_numerico.mean(),
            "mediana": df_numerico.median(),
            "desviacion_estandar": df_numerico.std(),
        }
    )
    print(estadisticas)

    if len(df_numerico.columns) >= 2:
        # Toma las dos primeras columnas numericas para el grafico.
        x_col = df_numerico.columns[0]
        y_col = df_numerico.columns[1]

        # Genera una grafica de dispersion X vs Y.
        plt.figure(figsize=(8, 5))
        plt.scatter(df_numerico[x_col], df_numerico[y_col], alpha=0.7)
        plt.title(f"Grafica de dispersion: {x_col} vs {y_col}")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()
    else:
        print("\nNo hay suficientes columnas numericas para la grafica de dispersion.")
