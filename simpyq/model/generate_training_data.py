import random
import pandas as pd

# Define operations and electronics signals
operations = [
    "mean", "average", "rms", "std", "variance", "sum", "median", "integral", "diff", "derivative",
    "max", "min", "abs max", "abs min", "sqr", "sqrt", "abs", "peak-to-peak", "squared mean",
    "log", "exp", "clip", "normalize", "mod", "div"
]
signals = [
    "load voltage", "input voltage", "output voltage", "battery voltage", "supply voltage",
    "gate voltage", "drain voltage", "source voltage", "reference voltage",
    "input current", "output current", "load current", "battery current", "switch current",
    "charging current", "discharging current", "phase current", "inrush current",
    "power", "input power", "output power", "loss power",
    "temperature", "ambient temperature", "junction temperature",
    "duty cycle", "frequency", "switching frequency", "efficiency"
]

# Generate combinations of operations and signals
queries = []
for op in operations:
    for sig in signals:
        queries.append(f"{op} of {sig}")

# Shuffle the queries to create more variety
random.shuffle(queries)

# Create a DataFrame
df = pd.DataFrame(queries, columns=["Query"])
df['Intent'] = df['Query'].apply(lambda x: x.split()[0])  # The operation (e.g., 'mean', 'rms', etc.)


# Save to CSV
df.to_csv("D:/WORKSPACE/simpyq/simpyq/model/data/queries_dataset.csv", index=False)

print("Dataset generated and saved as 'queries_dataset.csv'")
