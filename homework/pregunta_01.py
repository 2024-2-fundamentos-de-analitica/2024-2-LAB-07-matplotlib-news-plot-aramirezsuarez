import matplotlib
matplotlib.use("Agg")  # Usar backend sin interfaz gráfica

import matplotlib.pyplot as plt
import pandas as pd
import os

def pregunta_01():
    OUTPUT_PATH = "files/plots/news.png"
    INPUT_PATH = "files/input/news.csv"   

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    
    plt.figure(figsize=(10, 6))
    
    colors = {
        "Television": "dimgray",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey",
    }
    
    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }
    
    linewidths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 4,
        "Radio": 2,
    }

    try:
        df = pd.read_csv(INPUT_PATH, index_col=0)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {INPUT_PATH}")
        return
    
    for column in df.columns:
        plt.plot(df[column], color=colors[column], label=column, zorder=zorder[column], linewidth=linewidths[column])

    plt.title("How people get their news", fontsize=16)
    plt.legend()

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for column in df.columns:
        first_year = df.index[0]
        plt.scatter(x=first_year, y=df[column][first_year], color=colors[column], zorder=zorder[column])
        plt.text(first_year - 0.2, df[column][first_year], column + " " + str(df[column][first_year]) + "%", ha="right", va="center", color=colors[column])

        last_year = df.index[-1]
        plt.scatter(x=last_year, y=df[column][last_year], color=colors[column], zorder=zorder[column])
        plt.text(last_year + 0.2, df[column][last_year], str(df[column][last_year]) + "%", ha="left", va="center", color=colors[column])

    plt.xticks(ticks=df.index, labels=df.index, ha="center")

    try:
        plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight')
        print(f"Imagen guardada en {OUTPUT_PATH}")
    except Exception as e:
        print(f"Error al guardar la imagen: {e}")

    plt.close()
    
if __name__ == "__main__":
    pregunta_01()
