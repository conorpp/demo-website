from flask import Flask, render_template, redirect, url_for, abort

app = Flask(__name__)

class Device(object):
    name = 'Device'
    power = False

    def turn_on(self):
        self.power = True
        f = open('/tmp/'+self.name, 'w')
        f.write('ON')

    def turn_off(self):
        self.power = False
        f = open('/tmp/'+self.name, 'w')
        f.write('OFF')

    def set_speed(self):
        'example'
        raise NotImplementedError('set_speed')

    def __repr__(self):
        'Give readable information about device state'
        return '%s, powered: %s' % (self.name,self.power)



class LightSwitch(Device):
    name = 'light'
    def turn_on(self):
        super(LightSwitch, self).turn_on()
        print self
    def turn_off(self):
        super(LightSwitch, self).turn_off()
        print self

class FanSwitch(Device):
    name = 'fan'
    def turn_on(self):
        super(LightSwitch, self).turn_on()
        print self
    def turn_off(self):
        super(LightSwitch, self).turn_off()
        print self

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

