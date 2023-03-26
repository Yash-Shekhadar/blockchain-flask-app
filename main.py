from flask import Flask
import pandas as pd
import random
# from datetime import datetime
import math


app = Flask(__name__)

# Reading the datasets into dataframes
df_e = pd.read_csv('./mock_data/encounter_final.csv')
df_s = pd.read_csv('./mock_data/ship.csv')
df_p = pd.read_csv('./mock_data/port.csv')


# API to check the existence of a ship 
@app.route('/data/<mmsi>')
def checkExistence(mmsi):
    if int(mmsi) in df_s.v1MMSI.values:
        return {"mmsi": int(mmsi)}
    else:
        return {"mmsi":999999999}
    
# API to check if a given ship has been involved in illegal encountering activity
@app.route('/encounter/<mmsi>/<start>/<end>')
def encounterCheck(mmsi, start, end):

    if random.random() >= 0.95:
        return {'iuuInvolved': True}
    
    else:
        flaggedMMSI = df_e.query("@start <= endTime and startTime <= @end")['v1MMSI'].values.tolist()
        print(flaggedMMSI)
        if int(mmsi) in flaggedMMSI:
            return {'iuuInvolved': True}
        else:
            return {'iuuInvolved': False}
        

# API to validate the location of a ship and make sure that it is not involved in fishing in illegal waters
@app.route('/location/<mmsi>/<lat>/<lon>')
def locationCheck(mmsi, lat, lon):

    if random.random() < 0.95:
        return {'sentLat': lat,
                'sentLon': lon,
                'actualLat': lat,
                'actualLon': lon,
                'nearby': True
                }
    
    else:
        # reqDist/earthRadius
        distRad = 101/6371

        # Mathematics to simulate a live coordinate of the ship
        latRad = math.radians(float(lat))
        lonRad = math.radians(float(lon))
        newLatRad = math.asin(math.sin(latRad) * math.cos(distRad) + math.cos(latRad) * math.sin(distRad) * math.cos(0))
        newLonRad = math.asin(math.sin(lonRad) * math.cos(distRad) + math.cos(lonRad) * math.sin(distRad) * math.cos(0))
        newLat = math.degrees(newLatRad)
        newLon = math.degrees(newLonRad)
        return {'sentLat': lat,
                'sentLon': lon,
                'actualLat': str(newLat),
                'actualLon': str(newLon),
                'nearby': False
                }

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    