class Cam():


  def __init__( self,
                eye   = PVector(0,300,-200),
                center= PVector(0,0,0),
                up    = PVector(0,-1,0)):

    self.pos = eye
    self.center = center
    self.up = up
    self.static()


################################## Main Loop ###########################################

  def film(self):
    self._move()
    self._draw_()

  def _move(self):
    pass # Gets reassigned later
  
  def _draw_(self):
    e = self.pos
    c = self.center
    u = self.up
    camera(e.x,e.y,e.z,c.x,c.y,c.z,u.x,u.y,u.z)

################################## Monkey Patching #####################################

  def static(self):
    self._move = self._static
    return self

  def manual(self):
    self._move = self._manual
    return self
  
################################# Camera Movement ######################################

  def _static(self):
    pass

  def _manual(self):
    pass













