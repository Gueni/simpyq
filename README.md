# SimQuery: Command-Line Tool for Simulation Data Queries

SimQuery is a command-line tool that allows users to query and analyze simulation data stored in CSV files. With this tool, you can easily visualize signals, calculate statistical metrics (e.g., RMS, average), and automate post-processing of your simulation results.

This project is designed to be simple and extendable, allowing you to analyze different signals, plot them, and perform various analyses based on natural language queries.

## Features

- **Natural Language Query Interface**: Query simulation results using easy-to-understand commands such as "Plot voltage across R1" or "Compute average of Source Voltage".
- **Support for Various Metrics**: Calculate RMS, average, or other metrics on the signal data.
- **Plotting Capabilities**: Generate plots of signals over time.
- **Batch Querying**: Support for batch queries from a file, enabling you to automate repeated analyses.
- **Flexible CSV Format**: Automatically add headers to your CSV files based on your signal list, ensuring consistency and clarity in your analysis.
- **Logging and Saving**: Optionally log results to a file and save generated plots for future use.
- **Extendable**: Easily add more synonyms, signals, and operations as needed.

## Prerequisites

Before using the tool, ensure you have the following dependencies installed:

- **Python 3.x**: This tool is built with Python 3.
- **Required Libraries**:
  - `pandas`
  - `matplotlib`
  - `difflib` (Python standard library)

You can install the necessary libraries with the following command:

```bash
pip install -r requirements.txt
```

## Installation

To get started with SimQuery, follow these steps:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/simquery.git
cd simquery
```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 3. Make the Script Executable (Optional)

To make the script executable from the terminal without needing to specify `python` each time, you can create a simple shell script (`install.sh`):

```bash
chmod +x install.sh
./install.sh
```

This will allow you to run the tool directly as `simquery` from the terminal.

## Usage

### Running the Tool

To run SimQuery, use the following command:

```bash
simquery <path_to_csv_file> [OPTIONS]
```

#### Example

```bash
simquery 'path/to/your/file.csv' --save --log
```

### Available Options

- **`--save`**: Automatically saves the generated plots as image files.
- **`--log`**: Logs the computed results to a log file.
- **`--batch <file_path>`**: Executes multiple queries from a text file (one query per line).
- **`--help`**: Displays help information about the tool.

### Query Format

SimQuery uses natural language queries. Here are some examples:

- **Plot signals**:  
  `Plot voltage across R1`

- **Compute RMS**:  
  `Calculate RMS of Source Voltage`

- **Compute average**:  
  `Compute average of Source Current`

The tool will try to match your queries to the available signals, and will provide suggestions if necessary.

### Adding Custom Headers

If your CSV files do not have headers, you can automatically add them using the utility script. The headers will be added based on the list of signals defined in the `mappings.py` file.

To add headers:

1. Modify the `HEADERS` list in the `mappings.py` file to include your desired signals.
2. Run the `add_headers.py` script to insert the headers:

```bash
python add_headers.py path/to/your/file.csv
```

## License

This project is licensed under the MIT License.
