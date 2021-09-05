from InputManager import *
from Camera import Cam

scene_camera = Cam().static()
def setup():
  fullScreen(P3D)

def draw():
  background(0)
  sphere(20)
  scene_camera.film()

  