class InputManager:
  
  def __init__(self):

    self._code_to_press_dict = {}
    # Pre-init the values to false
    for i in range(256):
      self._code_to_press_dict[i] = False


    # Init Special Keys
    self._name_to_code_dict = {
      "BACKSPCE" : 8,
      "TAB" : 9,
      "ENTER" : 13,
      "SHIFT" : 16,
      "CTRL" : 17,
      "ALT" : 18,
      "ESCAPE" : 27,
      "SPACE" : 32,
      "LEFT" : 37,
      "UP" : 38,
      "RIGHT" : 39,
      "DOWN" : 40
    }

    # Init Numbers
    for i in range(10):
      print(i)
      self._name_to_code_dict[str(i)] = i+48


    # Init Letters
    alpha = [ "A","B","C","D","E","F","G","H","I","J","K","L","M",
              "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(65,91):
      self._name_to_code_dict[alpha[i-65]] = i
      

  def press_key(self,key_code):
    self._code_to_press_dict[key_code] = True

  def release_key(self,key_code):
    self._code_to_press_dict[key_code] = False

  def check(self,*args):
    name_to_press_dict = {}

    for name in args:

      code = self._name_to_code_dict.get(name)
      code = name if code is None else code  # If name is None, then either arg is key code or missing key name

      is_pressed = self._code_to_press_dict.get(code)
      is_pressed = False if is_pressed is None else is_pressed # If still None, then key does not exist

      name_to_press_dict[name] = is_pressed

    return name_to_press_dict

 



