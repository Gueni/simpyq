import pandas as pd
from mappings import HEADERS

def add_headers_to_csv(csv_file: str):
    # Load CSV file without headers
    data = pd.read_csv(csv_file, header=None)

    # Add headers from mappings.HEADERS to the first row
    data.columns = HEADERS

    # Save the modified CSV back to the same file
    data.to_csv(csv_file, index=False)

    print(f"Headers have been added to {csv_file}.")

