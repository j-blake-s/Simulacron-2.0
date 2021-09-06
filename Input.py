############################################## MOUSE ##############################################
_mouse_is_dragged = False
_mouse_wrap_buffer = 100

def mouseDragged():
  global _mouse_is_dragged
  _mouse_is_dragged = True

def mouseReleased():
  global _mouse_is_dragged
  _mouse_is_dragged = False

def is_mouse_dragged():
  return _mouse_is_dragged

############################################## KEYS ###############################################
_key_dict = {}

def keyPressed():
  log_key(keyCode,True)

def keyReleased():
  log_key(keyCode,False)

def log_key(key_code,pressed):
  global _key_dict
  _key_dict[key_code] = pressed

def key_log(*args):
  global _key_dict
  num_args = len(args)

  if num_args is 0:
    return _key_dict

  else:
    keys = []
    for arg in args:
      keys.append(False if _key_dict.get(arg) is None else _key_dict[arg])
    return keys

def arrows():
  vals = key_log(38,40,37,39)
  names = ("UP","DOWN","LEFT","RIGHT")
  res = {}
  for i in range(len(vals)):
    res[names[i]] = vals[i]
  return res

def wasd():
  vals = key_log(87,65,83,68)
  names = ("W","A","S","D")
  res = {}
  for i in range(len(vals)):
    res[names[i]] = vals[i]
  return res

def numbers():
  vals = key_log(48,49,50,51,52,53,54,55,56)
  res = {}
  for i in range(9):
    res[str(i)] = vals[i]
  return res



