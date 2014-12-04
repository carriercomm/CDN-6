import SocketServer
from GeoLocator import Locator
from dns_header import DNSHeader
from dns_question import DNSQuestion
from dns_answer import DNSAnswer

class DNSRequestHandler(SocketServer.BaseRequestHandler):
  def handle(self):
    self.data = self.request[0].strip()
    closest_ip = self.find_closest_location(self.client_address[0])
    header = DNSHeader(self.data[0:12], parse=True)
    question = DNSQuestion(self.data[12:])
    domain = question.domain
    if domain == self.server.dns_server:
      new_header = DNSHeader(ancount=1, qdcount=1, id=header.id)
      answer = DNSAnswer(domain, closest_ip)
      packet = new_header.construct() + question.construct() + answer.construct()
      self.request[1].sendto(packet, self.client_address)

  def find_closest_location(self, ip_address):
    locator = Locator()
    coord = locator.find_coordinates(ip_address)
    try:
      if coord['status'] == 'fail':
        return self.server.host_list[0][1]
    except Exception:
      pass
    closest_distance = None
    closest_ip = None
    for host in self.server.hosts:
      distance = self.find_distance(self.server.hosts[host]['lat'], self.server.hosts[host]['lon'], coord['lat'], coord['lon'])
      if closest_distance == None:
        closest_distance = distance
        closest_ip = self.server.hosts[host]['ip']
      elif closest_distance < distance:
        closest_distance = distance
        closest_ip = self.server.hosts[host]['ip']
    return closest_ip

  def find_distance(self, lat1, lon1, lat2, lon2):
    radius = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    lon_distance = lon2 - lon1
    lat_distance = lat2 - lat1
    a = (sin(lat_distance/2))**2 + cos(lat1) * cos(lat2) * (sin(lon_distance/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return radius * c