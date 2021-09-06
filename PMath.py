def great_circle_distance(t,p,r):
  
  # Convert to Radians
  t = radians(t)
  p = radians(p)

  x = r * cos(p) * cos(t)
  y = r * sin(t)
  z = r * sin(p) * cos(t)

  return x,y,z