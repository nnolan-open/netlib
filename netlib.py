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

  class IPv4Network(IPv4):
   def __init__(self,network=0,shortmask=0,):
      IPv4.__init__(self,network)
      self.setmask(shortmask)
   def setmask(self,shortmask=None):
      if type(shortmask) == int and 0 <= shortmask <= 32:
         self.shortmask = shortmask
      self.mask = IPv4(sum(map(lambda b: 2**(31-b),list(range(0,self.shortmask)))))
      self.nhosts = 2**(32 - self.shortmask) - 2 if self.shortmask < 31 else 2**(32 - self.shortmask)
      self.baseaddr = IPv4(self.value & self.mask.value)
      self.broadcast = IPv4(int(self.baseaddr) + (((2**32)-1) ^ int(self.mask)))
   def contains(self,address):
      if self.mask.value & self.value == self.mask.value & int(IPv4(address)):
         return True
      else:
         return False
