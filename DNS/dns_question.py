from struct import *

class DNSQuestion():
  def __init__(self, data, qtype=0, qclass=0):
    self.qname = self.parse_qname(data)
    self.qtype= qtype
    self.qclass = qclass
    print self.qname
    

  def parse_qname(self, data):
    get_size = True
    current_size = 0
    count = 0
    domain = ''
    for char in data:
      next_char = unpack('!c', char)[0]
      if get_size:
        current_size = ord(next_char)
        get_size = False
        if current_size == 0:
          return domain[1:]
        domain += '.'
      else:
        domain += next_char
        count += 1
        if count == current_size:
          get_size = True
          count = 0


