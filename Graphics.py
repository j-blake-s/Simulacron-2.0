def floor(size=500,ypos=0,grid=False):
  fill(255)
  noStroke()
  beginShape()
  for (i,j) in [(1,1),(1,-1),(-1,-1),(-1,1)]:
    vertex(i*size,ypos,j*size)
  endShape(CLOSE)

  # TODO - Draw a grid on the floor
  if grid:
    pass


def draw_line(p1,p2,offset=False):
  if offset:
    p2.add(p1)
  line(p1.x,p1.y,p1.z,p2.x,p2.y,p2.z)

def draw_box(size_,x=0,y=0,z=0):
  pushMatrix()
  translate(x,y,z)
  box(size_)
  popMatrix()

def draw_sphere(radius,pos=PVector(0,0,0)):
  pushMatrix()
  translate(pos.x,pos.y,pos.z)
  sphere(radius)
  popMatrix()

