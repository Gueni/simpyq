import random
import pandas as pd

# Define operations and electronics signals
operations = ['mean', 'rms', 'max', 'min', 'sqrt', 'sqr', 'abs']
signals = ['load voltage', 'input current', 'battery voltage', 'current', 'load current', 'switch current']

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
