
from Graphics import floor
from Camera import Cam
from Input import InputManager

_inp = InputManager()
def keyPressed():
  _inp.press_key(keyCode)
def keyReleased():
  _inp.release_key(keyCode)

class EnvManager:


  def __init__(self):
    self._cam = Cam(
      eye = PVector(0,200,0),
      center = PVector(1,199,1)
    ).manual(_inp)

  


  def loop(self):
    self.prep_scene()
    self.scene()
    self.clean_scene()

  def prep_scene(self):
    background(0)
    #directionalLight(155,155,155,0,-1,0)

  def scene(self):
    self._cam.film()

    floor(size=3000)

    noStroke()
    fill(100)
    pushMatrix()
    translate(0,200,0)
    sphere(50)
    popMatrix()

  def clean_scene(self):
    pass

