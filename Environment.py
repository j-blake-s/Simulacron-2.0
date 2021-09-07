
from Graphics import floor,draw_line
from Camera import Cam
from Input import InputManager
from Particle import Particle

_inp = InputManager()
def keyPressed():
  _inp.press_key(keyCode)
def keyReleased():
  _inp.release_key(keyCode)

part = Particle(p=PVector(0,100,0))
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
    self._cam.film()
    directionalLight(150,150,150,0,-1,0)
    floor(size=3000)

    
  def scene(self):
    dist = PVector.sub(PVector(0,500,0),(part.pos))
    dist.div(1000)
    part.apply_force(dist)
    dist.mult(500)
    stroke(0,255,0)
    draw_line(part.pos,dist,offset=True)
    part.loop()


   
  def clean_scene(self):
    pass

