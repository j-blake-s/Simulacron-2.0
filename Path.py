
from Graphics import draw_line
class Path:
  def __init__(self,tracking=None,path_size=100):
    self._tracker = tracking
    self._counter = 0
    self._path_size = path_size
    self._empty_path()

  def _empty_path(self):
    self._path = []
    for i in range(self._path_size):
      self._path.append(None)
      
  def loop(self):
    self._record()
    self.trace()

  def track(self,obj):
    self._tracker = obj
    self._empty_path()

  def _record(self):
    if self._tracker is not None:
      self._path[self._counter] = self._tracker.pos
      self._itr_counter()

  def trace(self):
    for i in range(self._path_size-1):
      ind = (i + self._counter) % self._path_size-1
      prev = self._path[ind]
      ind = (ind + 1) % self._path_size-1
      next_ = self._path[ind] 

      if prev is not None and next_ is not None:
        stroke(0,255,0)
        fill(0,255,0)
        draw_line(prev,next_)


  def _itr_counter(self):
    self._counter = (self._counter + 1) % self._path_size - 1



    