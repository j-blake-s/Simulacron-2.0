from Environment import *

env = EnvManager()
def setup():
  fullScreen(P3D)
  frameRate(60)

def draw():
  env.loop()
  

  

  



  