from struct import *

class DNSAnswer():
  def __init__(self, domain, ip, dns_type=1, dns_class=1, ttl=250, rdlength=4):
    self.domain = domain
    self.ip = int(ip.replace('.', ''))
    self.dns_type = dns_type
    self.dns_class = dns_class
    self.ttl = ttl
    self.rdlength = rdlength
    self.split = ip.split('.')

  def construct(self):
    name = self.construct_name()
    p = pack('!HHIHBBBB', self.dns_type, self.dns_class, self.ttl, self.rdlength, int(self.split[0]), int(self.split[1]), int(self.split[2]), int(self.split[3]))
    name = self.construct_name()
    return name + p

  def construct_name(self):
    name = None
    for part in self.domain.split('.'):
      if name == None:
        name = pack('!B', len(str(part)))
        name += self.pack_string(part)
      else:
        name += pack('!B', len(str(part)))
        name += self.pack_string(part)
    name += pack('!B', 0)
    return name 

  def pack_string(self, part):
    packed = None
    for char in part:
      if packed == None:
        packed = pack('!c', char)
      else:
        packed += pack('!c', char)
    return packed

  def __str__(self):
    return 'DNS Answer\n' +\
      'Name:\t' + str(self.domain) +\
      '\nIP:\t' + str(self.ip) +\
      '\nDNS Type:\t' + str(self.dns_type) +\
      '\nDNS Class:\t' + str(self.dns_class) +\
      '\nTTL:\t' + str(self.dns_class) +\
      '\nRDLength:\t' + str(self.rdlength)