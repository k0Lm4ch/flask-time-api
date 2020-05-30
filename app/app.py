from flask import Flask
import datetime
import jsondatetime as json

app = Flask(__name__)

@app.route("/")
def index():
    timeDict ={
        "currentTimeUTC" : datetime.datetime.utcnow().strftime("%c"),
        "currentSystemTime" : datetime.datetime.now().strftime("%c")
    }
    return json.dumps(timeDict)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')