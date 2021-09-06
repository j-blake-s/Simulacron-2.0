from Input import wasd,key_log,is_mouse_dragged
from PMath import great_circle_distance
class Cam():



  def __init__( self, eye=None, center=None, up=None):

    self.pos = eye if eye is not None else PVector(0,300,-200)
    self.center = center if center is not None else PVector(0,0,0)
    self.up = up if center is not None else PVector(0,-1,0)

    self.manual()
    
    self._CAM_FORWARD_SPEED = 5
    self._CAM_HORIZONTAL_SPEED = 5
    self._CAM_VERTICAL_SPEED = 5
    
    self._VERT_PAN_SPEED = 0.1 # Up and Down
    self._HORI_PAN_SPEED = 0.1 # Left and Right

    self._SPRINT_SPEED = 2

    self._UP_KEY = 32 # SPACE
    self._DOWN_KEY = 16 # LEFT SHIFT
    self._SPRINT_KEY = 17 # LEFT CTRL

    


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
    self.theta = -45
    self.phi = 90
    return self
  
################################# Camera Movement ######################################

  def _static(self):
    pass

  def _manual(self):
    # Helper Methods
    self._camera_move()
    self._camera_pan()
    
###################################### Helper Methods ###################################################

  def _camera_move(self):

    # Get user input
    WASD = wasd()
    UD = key_log(self._UP_KEY,self._DOWN_KEY)
    sprint = key_log(self._SPRINT_KEY)[0] * (self._SPRINT_SPEED - 1) + 1

    # Pre-Calc useful things
    forward = PVector.sub(self.pos,self.center)
    horizontal = PVector.cross(forward,self.up)
    vertical = PVector.cross(forward,horizontal)

    # Calculate Forward-Back Movement
    for_back = PVector.mult(forward.normalize(),self._CAM_FORWARD_SPEED*(WASD["S"] - WASD["W"])*sprint)

    # Calculate Side-to-Side Movement
    side_side = PVector.mult(horizontal.normalize(),self._CAM_HORIZONTAL_SPEED*(WASD["A"] - WASD["D"])*sprint)

    # Calculate Up-Down Movement
    u_d = UD[0] - UD[1]
    up_down = PVector.mult(vertical.normalize(),self._CAM_VERTICAL_SPEED*u_d)

    # Add changes to Cam
    final_ = PVector.add(PVector.add(for_back,side_side),up_down)
    self.pos.add(final_)
    self.center.add(final_)

  def _camera_pan(self):
    e = self.pos
    r = PVector.sub(e,self.center).mag()

    # Farther Drag Equals More Pan
    m_d_x = (pmouseX-mouseX) * self._HORI_PAN_SPEED
    m_d_y = (pmouseY-mouseY) * self._VERT_PAN_SPEED

    if is_mouse_dragged() and PVector(m_d_x,m_d_y).mag() < 20:
      self.phi += m_d_x % 360
      self.theta = max(-89,min(89,self.theta+m_d_y))

      # ANGLES
      x,y,z = great_circle_distance(self.theta,self.phi,r)

      self.center.set(PVector(e.x+x,e.y+y,e.z+z))







