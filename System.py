class System:
  def __init__(self):
    self.parts = []


  def get(self,index):
    return self.parts[index]

  def length(self):
    return len(self.parts)

  def add(self,particle_):
    self.parts.append(particle_)

  def clear(self):
    self.parts = []

  def remove(self,index):
    self.parts.remove(index)

  def apply_global_force(self,fv):
    for part in self.parts:
      part.apply_force(fv)
  

  def apply_force_function(self,f_f,*args):
    for part in self.parts:
      f_f(part,*args)

  def apply_single_force(self,index,fv):
    self.parts[index].apply_force(fv)

  def loop_all(self):
    for part in self.parts:
      part.loop()
      