import random
import pandas as pd
import os

operations   = [
                    "mean", "average", "rms", "std", "variance", "sum", "median", "integral", "diff", "derivative",
                    "max", "min", "abs max", "abs min", "sqr", "sqrt", "abs", "peak-to-peak", "squared mean",
                    "log", "exp", "clip", "normalize", "mod", "div","peak"
                ]
signals      = [
                    "load voltage", "input voltage", "output voltage", "battery voltage", "supply voltage",
                    "gate voltage", "drain voltage", "source voltage", "reference voltage",
                    "input current", "output current", "load current", "battery current", "switch current",
                    "charging current", "discharging current", "phase current", "inrush current",
                    "power", "input power", "output power", "loss power",
                    "temperature", "ambient temperature", "junction temperature",
                    "duty cycle", "frequency", "switching frequency", "efficiency",
                    'Time','Source_Voltage','Source' 'Current','Source' 'Power','RCD' 'Clamp' 'Current',
                    'RCD' 'Clamp' 'Voltage','RCD' 'Clamp' 'Dissipation','Load1','Load' 'Current',
                    'Load' 'Power','Primary' 'Winding' 'voltage','Primary' 'Winding' 'Current',
                    'Secondary' 'Winding' 'voltage','Secondary' 'Winding' 'Current',
                    'MOSFET' 'voltage','MOSFET' 'Current','MOSFET' 'junction' 'Temp'
                ]
queries      = []
for op in operations:
    for sig in signals:
        queries.append(f"{op} of {sig}")
random.shuffle(queries)
df = pd.DataFrame(queries, columns=["Query"])
df['Intent'] = df['Query'].apply(lambda x: x.split()[0])
base_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = base_dir+ "/queries_dataset.csv"
df.to_csv(dataset_path, index=False)
print(f"Dataset generated and saved as  {dataset_path}")