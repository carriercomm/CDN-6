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
    return pack('!pHHIHBBBB', name, self.dns_type, self.dns_class, self.ttl, self.rdlength, int(self.split[0]), int(self.split[1]), int(self.split[2]), int(self.split[3]))

  def construct_name(self):
    name = ''
    for part in self.split:
      name += str(len(part)) + part
    return name

  def __str__(self):
    return 'DNS Answer\n' +\
      '\nIP:\t' + str(self.ip) +\
      '\nDNS Type:\t' + str(self.dns_type) +\
      '\nDNS Class:\t' + str(self.dns_class) +\
      '\nTTL:\t' + str(self.dns_class) +\
      '\nRDLength:\t' + str(self.rdlength)