class Cam():




  def __init__( self, eye=None, center=None, up=None):
    self.pos = eye if eye is not None else PVector(0,0,0)
    self.center = center if center is not None else PVector(self.pos.x+1,self.pos.y,self.pos.z+1)
    self.up = up if up is not None else PVector(0,-1,0)
    self.static()
    
################################################ CONSTANTS #######################################################

    self._CAM_FORWARD_SPEED = 20
    self._CAM_HORIZONTAL_SPEED = 20
    self._CAM_VERTICAL_SPEED = 20
    
    self._VERT_PAN_SPEED = 0.13 # Up and Down
    self._HORI_PAN_SPEED = 0.13 # Left and Right

    self._SPRINT_SPEED = 3

    self._UP_KEY = 32 # SPACE
    self._DOWN_KEY = 16 # LEFT SHIFT
    self._SPRINT_KEY = 18 # LEFT ALT

##################################################################################################################




################################################# Main Loop ######################################################

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

############################################## Monkey Patching ###################################################

  def static(self):
    self._move = self._static
    return self

  def manual(self,some_input_src):
    self._move = self._manual
    self.theta = -45
    self.phi = 90
    self.input_ = some_input_src
    return self
  
############################################# Camera Movement ####################################################

  def _static(self):
    pass

  def _manual(self):
    # Helper Methods
    self._camera_move(self.input_)
    self._camera_pan()
    
############################################# Helper Methods ####################################################

  def _camera_move(self,input_src):

    # Get user input from the input src
    keys = input_src.check("W","A","S","D",self._UP_KEY,self._DOWN_KEY,self._SPRINT_KEY)
    s_w = keys["S"] - keys["W"]
    a_d = keys["A"] - keys["D"]
    u_d = keys[self._UP_KEY] - keys[self._DOWN_KEY]
    sprint = (keys[self._SPRINT_KEY] * (self._SPRINT_SPEED - 1)) + 1

    # Pre-Calc useful things
    forward = PVector.sub(self.pos,self.center)
    horizontal = PVector.cross(forward,self.up)
    vertical = PVector.cross(forward,horizontal)

    # Calculate Forward-Back Movement
    for_back = PVector.mult(forward.normalize(),self._CAM_FORWARD_SPEED*s_w*sprint)

    # Calculate Side-to-Side Movement
    side_side = PVector.mult(horizontal.normalize(),self._CAM_HORIZONTAL_SPEED*a_d*sprint)

    # Calculate Up-Down Movement
    up_down = PVector.mult(vertical.normalize(),self._CAM_VERTICAL_SPEED*u_d)

    # Add changes to Cam
    final_ = PVector.add(PVector.add(for_back,side_side),up_down)
    self.pos.add(final_)
    self.center.add(final_)

  def _camera_pan(self):
    e = self.pos
    r = PVector.sub(e,self.center).mag()

    # The change of the mouse determines how much the camera pans
    m_d_x = (pmouseX-mouseX) * self._HORI_PAN_SPEED
    m_d_y = (pmouseY-mouseY) * self._VERT_PAN_SPEED

    # Mouse must be dragged in order to look around
    # Any sudden snaps of the mouse will be ignored
    if mousePressed and PVector(m_d_x,m_d_y).mag() < 20:
      self.phi += m_d_x % 360
      self.theta = max(-89,min(89,self.theta+m_d_y))

      # Great Circle Distance
      t = radians(self.theta)
      p = radians(self.phi)

      x = r * cos(p) * cos(t)
      y = r * sin(t)
      z = r * sin(p) * cos(t)

      self.center.set(PVector(e.x+x,e.y+y,e.z+z))







