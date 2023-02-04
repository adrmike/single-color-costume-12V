from flask import Flask, render_template, request
import pigpio
import threading
import time

app = Flask(__name__)
MainPin = 17

currentBrightness = 50

setBrightness = 50
t1 = None
pi = pigpio.pi()
stop_threads = False

@app.route('/', methods=['GET'])
def Main():

    global stop_threads
    global currentBrightness
    global t1

    if t1 is None:
        print("no thread running")
    elif t1.is_alive():
        stop_threads = True
        t1.join()
        stop_threads = False

    if request.args.get('Bright'):
        currentBrightness=request.args.get('Bright')
        t1 = threading.Thread(target=Fade,args=(int(currentBrightness),lambda : stop_threads))
        

    if request.args.get('Breath'):
        max=request.args.get('Breath')
        t1 = threading.Thread(target=Breath,args=(int(max),lambda : stop_threads,))
    
    if t1 is None:
        print("no thread running")
    elif not t1.is_alive():
        t1.start()
        

    return render_template('index.html')

def Fade(target,stop):
    # Fade up to a target PWN duty cycle.
    print("Entering Fading")
    global setBrightness
    if setBrightness < target:
        while setBrightness < target:
            time.sleep(0.01)
            setBrightness +=1
            pi.set_PWM_dutycycle(MainPin, setBrightness)
            if stop():
                break
    elif setBrightness > target:
        while setBrightness > target:
            time.sleep(0.01)
            setBrightness -=1
            pi.set_PWM_dutycycle(MainPin, setBrightness)
            if stop():
                break
    print("Exiting Fading")

def Breath(max,stop):
    # breath LED between some max target and 0
    print ("Breathing")
    global setBrightness
    lightSet = setBrightness
    ledSpeed = 1 

    while True:
        if stop():
            print("Stop Breathing")
            break
        
        time.sleep(0.01)
        if lightSet >= max:
            ledSpeed = -1
        elif lightSet <= 0:
            ledSpeed = 1

        lightSet += ledSpeed
        setBrightness = lightSet
        pi.set_PWM_dutycycle(MainPin, lightSet)




if __name__ == "__main__":
    pi.set_PWM_dutycycle(MainPin,setBrightness)
    app.run(host="0.0.0.0")
