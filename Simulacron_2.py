from Environment import *

env = EnvManager()
def setup():
  fullScreen(P3D)
  frameRate(60)
  env.setup()

def draw():
  env.loop()
  

  



  