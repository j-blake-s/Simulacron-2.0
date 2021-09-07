
from Graphics import floor,draw_line
from Camera import Cam
from Input import InputManager
from Particle import Particle
from System import System
from PMath import rand_vector
from PEngine import converge

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


    self.sys = System()

    for i in range(10):
      self.sys.add(self.rand_particle(1000,5))

############################################ CONSTANTS #################################################



    self.FLOOR_SIZE_ = 6000



########################################################################################################    
    

  def rand_particle(self,pos_range,vel_range=0):
      p = rand_vector(pos_range)
      v = rand_vector(vel_range)
      return Particle(p=p,v=v)



  def loop(self):
    self.prep_scene()
    self.scene()
    self.clean_scene()

  def prep_scene(self):
    background(100)
    directionalLight(150,150,150,-1,-1,0)
    self._cam.film()

    
  def scene(self):
    
    self.sys.apply_force_function(converge)
    self.sys.loop_all()
 
  def clean_scene(self):
    pass

