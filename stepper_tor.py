import RPi.GPIO as GPIO
from time import sleep
from tornado.ioloop import IOLoop
import tornado.httpserver
import tornado.template
import tornado.process
import tornado.ioloop
import tornado.web
import requests
import os
api_port = 3022
p_dir = 22  # Controller p_direction Bit (High for Controller default / LOW to Force a p_direction Change).
p_stop = 24  # Controller Enable Bit (High to Enable / LOW to Disable).
t_dir=27
t_stop=17
GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only. 

GPIO.setup(p_dir, GPIO.OUT)
GPIO.setup(p_stop, GPIO.OUT)
GPIO.setup(t_dir, GPIO.OUT)
GPIO.setup(t_stop, GPIO.OUT)
print('Initialization Completed')


def pan_forward():
    GPIO.output(p_stop, GPIO.HIGH)
    print('p_stop set to HIGH - Controller Enabled')
    GPIO.output(p_dir, GPIO.LOW)
    
def pan_rev():
    GPIO.output(p_stop, GPIO.HIGH)
    GPIO.output(p_dir, GPIO.HIGH)
def pan_stop():
    GPIO.output(p_stop, GPIO.LOW)
    print('p_stop set to LOW - Controller Enabled')
    
def tilt_forward():
    GPIO.output(t_stop, GPIO.HIGH)
    print('t_stop set to HIGH - Controller Enabled')
    GPIO.output(t_dir, GPIO.LOW)
def tilt_rev():
    GPIO.output(t_stop, GPIO.HIGH)
    GPIO.output(t_dir, GPIO.HIGH)
def tilt_stop():
    GPIO.output(t_stop, GPIO.LOW)
    print('t_stop  set to LOW - Controller Enabled')
class BaseHandler(tornado.web.RequestHandler):
         #blog.csdn.net/moshowgame Solving cross-domain issues
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',#'*')
                        'authorization, Authorization, Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
class StepperAPI(BaseHandler):
    def get(self):
        self.render('stepper.html')
class Rotate_left(BaseHandler):
    def get(self):
        pan_forward()
class Rotate_right(BaseHandler):
    def get(self):
        pan_rev()
class Rotate_down(BaseHandler):
    def get(self):
        tilt_forward()
class Rotate_up(BaseHandler):
    def get(self):
        tilt_rev()
class Stop(BaseHandler):
    def get (self):
        pan_stop()
class TiltStop(BaseHandler):
    def get (self):
        tilt_stop()

def make_app():
    return tornado.web.Application([("/", StepperAPI), ("/rot_right", Rotate_right),("/rot_left", Rotate_left),("/poff", Stop),("/step_up",Rotate_up),("/step_down",Rotate_down),("/tilt_stop",TiltStop)],template_path=os.path.join(os.path.dirname(__file__), "templates"))


if __name__ == '__main__':
    app = make_app()
    app.listen(api_port)
    print("\nStepper API is listening on http://127.0.0.1:"+str(api_port))
    IOLoop.instance().start()
    

GPIO.cleanup()
