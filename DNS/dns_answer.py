from struct import *

class DNSAnswer():
  def __init__(self, domain, ip, dns_type=1, dns_class=1, ttl=250, rdlength=4):
    self.domain = domain
    self.ip = int(ip.replace('.', ''))
    self.dns_type = dns_type
    self.dns_class = dns_class
    self.ttl = ttl
    self.rdlength = rdlength

  def construct(self):
    name = self.construct_name()
    return pack('!pHHIHI', name, self.dns_type, self.dns_class, self.ttl, self.rdlength, self.ip)

  def construct_name(self):
    name = ''
    for part in self.domain.split('.'):
      name += str(len(part)) + part
    return name