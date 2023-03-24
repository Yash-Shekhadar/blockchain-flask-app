from flask import Flask
import urllib3.request
import pandas as pd

app = Flask(__name__)

df_e, df_l, df_p = None, None, None

print("Its me, hi, I am the problem its me!")
urllist = ['https://drive.google.com/file/d/1fGCocjbtGwEYBYmIiKn7IgRdqD45toL7/view?usp=share_link', 'https://drive.google.com/file/d/1eyAwWBHtXGghYmZn_tKNZ53cVury1jT1/view?usp=share_link', 'https://drive.google.com/file/d/1WSrIw5tZIDbUQm30-TK09Ru2NpvzL2cZ/view?usp=share_link']
filenames = ['encounter.csv', 'loitering.csv', 'port.csv']

for i in range(len(filenames)):
    urllib3.request.urlretrieve(urllist[i], filenames[i])

df_e = pd.read_csv("./encounter.csv")
df_l = pd.read_csv("./loitering.csv")
df_p = pd.read_csv("./port.csv")
print(len(df_e), len(df_l), len(df_p))

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    # return 'Hello World!'
    return str(len(df_e))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    

