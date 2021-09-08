
from Graphics import draw_line


DEF_PATH_RATE = 10
DEF_PATH_SIZE = 100
class Path:
  def __init__(self,obj,path_size=DEF_PATH_SIZE,rate=DEF_PATH_RATE):
    self.prey = obj
    self.idx = 0
    self.path = [None] * path_size
    self.clock = 0
    self.trate = rate
      

  def size(self):
    return len(self.path)

  def loop(self):
    self.record()
    self.trace()
    self.clock += 1

  def record(self):

    if self.clock % self.trate == 0:
      self.path[self.idx] = self.prey.pos.copy()
      self.idx = (self.idx + 1) % (self.size())
    

  def trace(self):
    stroke(0,255,0)
    prev = None
    for i in range(self.idx,self.idx + self.size()-1):
      curr = self.path[i % self.size()]
      if curr is None: continue
      if prev is not None: draw_line(prev,curr)
      prev = curr


    



    