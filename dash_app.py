
import dash
import pandas as pd

# --- Module Imports ---
import layout

# --- Hide SettingWithCopy Warnings --- 
pd.set_option('chained_assignment',None)

# --- Initialize App ---
app = dash.Dash(__name__)

# --- Server ---
server = app.server

# --- Set Name and Layout ---
app.title = 'Moving US Forward'
app.layout = layout.html_obj

# --- Run on Import ---
if __name__ == "__main__":
    app.run_server(debug=True)