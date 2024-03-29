import serial
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

@app.route('/on')
def tænd():
    with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as kabel:
        kabel.write(b"on\n")
    return render_template('tændt.html')

@app.route('/off')
def sluk():
    with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as kabel:
        kabel.write(b"off\n")
    return render_template('slukket.html')

@app.after_request
def add_header(response):
    response.cache_control.no_cache = True
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2001)

