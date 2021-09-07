from Environment import *

env = EnvManager()
def setup():
  fullScreen(P3D)
  frameRate(60)
  env.populate_system()

def draw():
  env.loop()
  

  

  



  