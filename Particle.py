import Graphics

class Particle:
  
  def __init__(
    self,
    p=None,
    v=None,
    a=None,
    m=1
  ):

    self.pos = p if p is not None else PVector(0,0,0)
    self.vel = v if v is not None else PVector(0,0,0)
    self.acc = a if a is not None else PVector(0,0,0)
    self.mass = m if m > 0 else 100
    self.net_force = PVector(0,0,0)



################################################ CONSTANTS #########################################################

    self.SIZE_ = 50





#####################################################################################################################
  def update(self):
    self.acc.set(PVector.div(self.net_force,self.mass))
    self.vel.add(self.acc)
    self.pos.add(self.vel)
    self.net_force.set(0,0,0)
  
  def apply_force(self,force_vector):
    self.net_force.add(force_vector)


  def _draw_(self):
    noStroke()
    fill(255,0,0)
    Graphics.draw_sphere(self.SIZE_,self.pos)

  def loop(self):
    self.update()
    self._draw_()

  
