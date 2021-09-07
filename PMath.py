# Given 2 angles (t)heta and (p)hi, and a (r)adius for a sphere,
# calculates the corresponding position on said sphere.
def great_circle_distance(t,p,r):
  t = radians(t)
  p = radians(p)

  x = r * cos(p) * cos(t)
  y = r * sin(t)
  z = r * sin(p) * cos(t)

  return x,y,z


def rand_vector(range_):
  x = random(-range_,range_)
  y = random(-range_,range_)
  z = random(-range_,range_)
  return PVector(x,y,z)