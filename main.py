from flask import Flask
import pandas as pd

app = Flask(__name__)

df_e = pd.read_csv('./mock_data/encounter_final.csv')
df_s = pd.read_csv('./mock_data/ship.csv')
df_p = pd.read_csv('./mock_data/port.csv')



@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return len(df_e)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    

