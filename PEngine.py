
def single_gravity(to,from_):
  G = 100 * from_.mass * to.mass
  f = PVector.sub(from_.pos,to.pos)  # Direction
  r = f.mag()
  f.normalize().mult(G / sq(r))
  to.apply_force(f)

def double_gravity(a,b):
  single_gravity(a,b)
  single_gravity(b,a)


def system_gravity(s):
  size_ = s.length()
  for i in range(size_):
    for j in range(i+1,size_):
      double_gravity(s.get(i),s.get(j))



# TODO - Make ~system_point_gravity~
# Takes in 2 systems  A and B, objects of which should inherit from particle
# Every particle in B will exert gravitational force on every particle in A
# But not vice versa, this is because B should be considered a system of 
# "dark" points which don't actually exist and thus are static/not moving
