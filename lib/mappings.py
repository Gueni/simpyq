# mappings.py

action_synonyms = {
    "draw": "plot",
    "plot graph": "plot",
    "display": "plot"
}

metric_synonyms = {
    "mean": "average",
    "avg": "average",
    "root mean square": "rms"
}

# You can later add more:
# operation_synonyms = {
#     "find": "calculate",
#     "compute": "calculate"
# }
HEADERS = [
    'Time',
    'Source_Voltage',
    'Source_Current',
    'Source_Power',
    'RCD_Clamp_Current',
    'RCD_Clamp_Voltage',
    'RCD_Clamp_Dissipation',
    'Load1',
    'Load_Current',
    'Load_Power',
    'Primary_Winding_Voltage',
    'Primary_Winding_Current',
    'Secondary_Winding_Voltage',
    'Secondary_Winding_Current',
    'MOSFET_Voltage',
    'MOSFET_Current',
    'MOSFET_Junction_Temp',
    'MOSFET_Switching_Losses',
    'MOSFET_Conduction_Losses',
    'Diode_Voltage',
    'Diode_Current',
    'Diode_Junction_Temp',
    'Diode_Conduction_Losses',
    'Diode_Switching_Losses',
    'Cout_Voltage',
    'Cout_Current',
    'Cout_Dissipation',
    'Power',
    'Vout',
    'Iout',
    'Total_Power_Loss',
    'Input_Power',
    'Output_Power',
    'Efficiency',
    'SHUNT_Voltage',
    'SHUNT_Current',
    'SHUNT_Dissipation'
]
	