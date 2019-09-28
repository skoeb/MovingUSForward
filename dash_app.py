
import dash
import pandas as pd

# --- Module Imports ---

# --- Hide SettingWithCopy Warnings --- 
pd.set_option('chained_assignment',None)

# --- Server ---
server = functions.app.server

# --- Initialize App ---
app = dash.Dash(__name__)

# --- Set Name and Layout ---
app.title = 'Moving US Forward'
app.layout = layout.html_obj

# --- Run on Import ---
if __name__ == "__main__":
    functions.app.run_server(debug=False)