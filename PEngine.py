def converge(part,**kwargs):
  p = PVector(0,1000,0)

  diff = PVector.sub(p,part.pos)
  diff.div(5000)
  base_ = 1.001
  
  x = pow(base_,diff.x)
  y = pow(base_,diff.y)
  z = pow(base_,diff.z)

  force_ = PVector(diff.x*x,diff.y*y,diff.z*z)

  part.apply_force(force_)
