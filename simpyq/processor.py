## processor.py
import numpy as np


def execute_operation(df, intent):
    signals = intent['signals']
    operation = intent['operation']

    if operation == 'mean':
        return {sig: df[sig].mean() for sig in signals}
    elif operation == 'rms':
        return {sig: np.sqrt(np.mean(df[sig] ** 2)) for sig in signals}
    elif operation == 'max':
        return {sig: df[sig].max() for sig in signals}
    elif operation == 'min':
        return {sig: df[sig].min() for sig in signals}
    elif operation == 'abs_max':
        return {sig: df[sig].abs().max() for sig in signals}
    elif operation == 'abs_min':
        return {sig: df[sig].abs().min() for sig in signals}
    elif operation == 'sum':
        return sum(df[sig] for sig in signals)
    elif operation == 'product':
        result = df[signals[0]]
        for sig in signals[1:]:
            result *= df[sig]
        return result.mean()
    else:
        raise ValueError(f"Unsupported operation: {operation}")