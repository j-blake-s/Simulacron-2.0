from Input import * 
from Camera import Cam
from Graphics import floor

scene_camera = Cam().manual()
def setup():
  fullScreen(P3D)
  #noCursor()

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

  scene_camera.film()

  