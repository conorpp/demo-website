from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

LIGHT_STATE = False

@app.route('/', methods = ['GET'])
def home():
    'Return a page with control widgets for all devices.'
    return render_template(
        'index.html',
        light_state_on_click = 'Turn Off' if LIGHT_STATE else 'Turn On')

@app.route('/update', methods = ['POST'])
def update():
    'Toggle the device state.'
    global LIGHT_STATE
    LIGHT_STATE = not LIGHT_STATE
    if LIGHT_STATE:
        print 'Light now on!'
    else:
        print 'Light now off!'
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug = True)
    
