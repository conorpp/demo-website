from flask import Flask, render_template, redirect, url_for, abort

app = Flask(__name__)

class LightSwitch(object):
    def turn_on(self):
        print 'Light on!'
        f = open('/tmp/light', 'w')
        f.write('ON')
    def turn_off(self):
        print 'Light now off!'
        f = open('/tmp/light', 'w')
        f.write('OFF')

class FanSwitch(object):
    def turn_on(self):
        print 'Fan on!'
        f = open('/tmp/fan', 'w')
        f.write('ON')
    def turn_off(self):
        print 'Fan off!'
        f = open('/tmp/fan', 'w')
        f.write('OFF')

@app.route('/', methods = ['GET'])
def home():
    'Return a page with control widgets for all devices.'
    return render_template('index.html')

@app.route('/devices/<device_name>/turn_on', methods = ['POST'])
def turn_on(device_name):
    'Turn on the given device.'
    if device_name not in DEVICES.keys():
        abort(404)
    DEVICES[device_name].turn_on()
    return redirect(url_for('home'))

@app.route('/devices/<device_name>/turn_off', methods = ['POST'])
def turn_off(device_name):
    'Turn off the given device.'
    if device_name not in DEVICES.keys():
        abort(404)
    DEVICES[device_name].turn_off()
    return redirect(url_for('home'))

if __name__ == '__main__':
    DEVICES = {
        '0' : LightSwitch(),
        '1' : FanSwitch(),
    }
    app.run(debug = True, host = '0.0.0.0')

