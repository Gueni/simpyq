## plotter.py
import matplotlib.pyplot as plt
import os

def handle_plot(df, intent, save):
    signals = intent['signals']
    df[signals].plot(title=f"Plot of {', '.join(signals)}")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.grid(True)
    if save:
        os.makedirs("output/plots", exist_ok=True)
        filename = f"output/plots/plot_{'_'.join(signals)}.png"
        plt.savefig(filename)
        print(f"Plot saved to {filename}")
    else:
        plt.show()
