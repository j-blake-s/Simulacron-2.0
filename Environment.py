
from Graphics import floor,draw_line
from Camera import Cam
from Input import InputManager
from Particle import Particle
from System import System
from PMath import rand_vector
from PEngine import single_gravity, system_gravity
from Path import Path

_inp = InputManager()
def keyPressed():
  _inp.press_key(keyCode)

def keyReleased():
  _inp.release_key(keyCode)



class EnvManager:


  def __init__(self):


    self._cam = Cam(
      eye = PVector(-1500,500,-1500),
      center = PVector(-1499,500,-1499),
      inp_src = _inp
    ).manual()


    self.sys = System()
    self.paths = []

############################################ CONSTANTS #################################################



    self.FLOOR_SIZE_ = 6000



########################################################################################################    
    

  def setup(self):
    self.set_perspective(0.5)
    for _ in range(10):
      part = self.rand_particle(1000,2)
      part.mass = 100
      self.paths.append(Path(part))
      self.sys.add(part)

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
    p = PVector(0,2000,0)
    point = Particle(p=p,m=1000)
    system_gravity(self.sys)
    self.sys.apply_force_function(single_gravity,point)
    self.sys.loop_all()
    for path in self.paths: path.loop()
 
  def clean_scene(self):
    pass



  def set_perspective(self,fov_ratio):
    fov = PI * fov_ratio
    cameraZ = (height/2.0) / tan(fov/2.0)
    perspective(fov, float(width)/float(height), 
                cameraZ/10.0, cameraZ*10.0)