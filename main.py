from flask import Flask
import pandas as pd

app = Flask(__name__)

df_e = pd.read_csv('./mock_data/encounter_final.csv')
df_s = pd.read_csv('./mock_data/ship.csv')
df_p = pd.read_csv('./mock_data/port.csv')



@app.route('/data/<mmsi>')
def checkExistence(mmsi):
    if int(mmsi) in df_s.v1MMSI.values:
        return {"mmsi":mmsi}
    else:
        return {"mmsi":999999999}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    

