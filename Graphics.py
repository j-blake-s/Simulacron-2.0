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


# TODO - draw_sphere()

