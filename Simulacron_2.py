from Input import InputManager
from Camera import Cam
from Graphics import floor

inp = InputManager()
camera_ = Cam().manual(inp)
def setup():
  fullScreen(P3D)

def draw():
  background(0)
  directionalLight(155,155,155,0,-1,0)

  

  floor(size=3000)
  noStroke()
  fill(100)
  pushMatrix()
  translate(0,200,0)
  sphere(50)
  popMatrix()

  camera_.film()


def keyPressed():
  inp.press_key(keyCode)

def keyReleased():
  inp.release_key(keyCode)

  