from interpreter import interpret_query
from utils import load_csv, log_result, extract_signals,handle_plot
import numpy as np

def execute_operation(df, intent):
    """Performs the intended operation on given signals in the DataFrame."""
    print("Available columns:", df.columns.tolist())

    signals = extract_signals(df, intent)
    op = intent["operation"]

    if op == "mean":
        return {sig: np.mean(df[sig]) for sig in signals}
    elif op == "rms":
        return {sig: np.sqrt(np.mean(df[sig] ** 2)) for sig in signals}
    elif op == "max":
        return {sig: np.max(df[sig]) for sig in signals}
    elif op == "min":
        return {sig: np.min(df[sig]) for sig in signals}
    elif op == "abs max":
        return {sig: np.max(np.abs(df[sig])) for sig in signals}
    elif op == "abs min":
        return {sig: np.min(np.abs(df[sig])) for sig in signals}
    elif op == "integr":
        return {sig: np.trapz(df[sig]) for sig in signals}
    elif op == "derive":
        return {sig: np.gradient(df[sig]).tolist() for sig in signals}
    elif op == "sqrt":
        return {sig: np.sqrt(df[sig]) for sig in signals}
    elif op == "sqr":
        return {sig: df[sig] ** 2 for sig in signals}
    elif op in ["+", "-", "*", "/", "div", "mod"]:
        if len(signals) != 2:
            raise ValueError(f"Binary operation '{op}' requires exactly two signals.")
        s1, s2 = df[signals[0]], df[signals[1]]

        if op == "+":
            return s1 + s2
        elif op == "-":
            return s1 - s2
        elif op == "*":
            return s1 * s2
        elif op == "/":
            return s1 / s2
        elif op == "div":
            return s1 // s2
        elif op == "mod":
            return s1 % s2
    else:
        raise ValueError(f"Unknown operation: {op}")

def run_query(csv_file, save=False, log=False):
    df = load_csv(csv_file)

    while True:
        query = input("Enter your query (or 'exit'): ").strip()
        if query.lower() == 'exit':
            break

        try:
            # Get the intent from the query
            intent = interpret_query(query, df.columns)
            print(f"Intent: {intent}")  # Debugging the intent structure

            # Ensure signals are valid
            signals = intent.get("signals", [])
            if not signals:
                raise ValueError("No valid signals extracted from the query.")

            # Execute the operation
            result = execute_operation(df, intent)

            # Plot if needed
            if intent["operation"] == "plot":
                handle_plot(df, intent, save)
            else:
                print("Result:", result)

            # Log the result if requested
            if log:
                log_result(query, result)

        except Exception as e:
            print("Error:", str(e))
            if log:
                log_result(query, f"Error: {str(e)}")
