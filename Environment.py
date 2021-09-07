
from Graphics import floor,draw_line
from Camera import Cam
from Input import InputManager
from Particle import Particle
from System import System

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
    

############################################ CONSTANTS #################################################



    self.FLOOR_SIZE_ = 6000



########################################################################################################    
    
  def populate_system(self):
     for i in range(10):
      x = random(-self.FLOOR_SIZE_/2,self.FLOOR_SIZE_/2)
      y = random(100,1000)
      z = random(-self.FLOOR_SIZE_/2,self.FLOOR_SIZE_/2)
      p = PVector(x,y,z)



      r = 5
      x = random(-r,r)
      y = random(-r,r)
      z = random(-r,r)
      v = PVector(x,y,z)
      self.sys.add(Particle(p=p,v=v))
  


  def loop(self):
    self.prep_scene()
    self.scene()
    self.clean_scene()

  def prep_scene(self):
    background(100)
    directionalLight(150,150,150,-1,-1,0)
    #floor(size=self.FLOOR_SIZE_)
    self._cam.film()

    
  def scene(self):


    def converge(obj):
      G = 1000000
      diff = PVector.sub(PVector(0,1000,0),obj.pos)
      dist = diff.mag()
      diff.normalize().mult(G)
      diff.div(sq(dist))
      obj.apply_force(diff)

    def rand_force(obj):
      r_ = 0.5
      x = random(-r_,r_)
      y = random(-r_,r_)
      z = random(-r_,r_)
      r_f = PVector(x,y,z)
      obj.apply_force(r_f)
    
    self.sys.apply_force_function(converge)
    self.sys.apply_force_function(rand_force)
    #self.sys.apply_global_force(PVector(0,-0.5,0))
    self.sys.loop_all()


   
  def clean_scene(self):
    pass

