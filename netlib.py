class IPv4:
  def __init__(self,iparg):
    if type(iparg) == int:
      self.value = iparg
      return(None)
    assert type(iparg) == str
    self.value = sum([int(i)<<(24-8*idx) for idx,i in enumerate(iparg.split('.'))])
  def __str__(self):
    return('.'.join(map(str, [ self.value.to_bytes(4,'big')[0], self.value.to_bytes(4,'big')[1], self.value.to_bytes(4,'big')[2], self.value.to_bytes(4,'big')[3] ])))
  def __int__(self):
    return(self.value)
  def __add__(self,other):
    if type(other) == type(self):
      return(  IPv4(self.value + other.value) )
    assert type(other) == int
    return(IPv4(self.value + other))
  def __sub__(self,other):
    if type(other) == type(self):
      return(IPv4(abs(self.value - other.value)))
    assert type(other) == int
    return(IPv4(abs(self.value - other)))
  def __and__(self,other):
    if type(other) == type(self):
      return(  IPv4(self.value & other.value) )
    assert type(other) == int
    return(IPv4(self.value & other))
