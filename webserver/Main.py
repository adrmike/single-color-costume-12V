from flask import Flask, render_template, request
import pigpio
import threading

app = Flask(__name__)
MainPin = 17

currentBrightness = 50

setBrightness = 50

pi = pigpio.pi()

@app.route('/', methods=['GET'])
def Main():

    global currentBrightness
    if request.args.get('Bright'):
         currentBrightness=request.args.get('Bright')

    threading.Thread(target=Fade,args=(int(currentBrightness),)).start()

    return render_template('index.html')

def Fade(target):
    print("in fading")
    global setBrightness
    if setBrightness < target:
        while setBrightness < target:
            setBrightness +=1
            pi.set_PWM_dutycycle(MainPin, setBrightness)
    elif setBrightness > target:
        while setBrightness > target:
            setBrightness -=1
            pi.set_PWM_dutycycle(MainPin, setBrightness)


if __name__ == "__main__":
    pi.set_PWM_dutycycle(MainPin,setBrightness)
    app.run(host="0.0.0.0")
