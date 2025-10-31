from flask import Flask, render_template, request
from services.gold_api import make_gapi_request

app = Flask(__name__)

@app.route('/')
def index():
    period = request.args.get("period", "7")
    days = int(period)
    
    data = make_gapi_request(days)
    return render_template('index.html', data=data, period=period)

if __name__ == '__main__':
    app.run(debug=True)