from optparse import OptionParser
import socket
from struct import *
from dns_header import DNSHeader
from dns_question import DNSQuestion
from dns_answer import DNSAnswer
import urllib2
import json
from math import sin, cos, sqrt, atan2, radians

host_list = [('ec2-54-174-6-90.compute-1.amazonaws.com', '205.251.192.27')]
hosts = {}
radius = 6373.0
IP = '129.10.117.186'

def start_server(dns_server, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind((IP, int(port)))

  while 1:
    data, addr = s.recvfrom(1024)
    closest_ip = find_closest_location(addr[0])
    header = DNSHeader(data[0:12], parse=True)
    question = DNSQuestion(data[12:])
    domain = question.domain
    if domain == dns_server:
      new_header = DNSHeader(ancount=1, qdcount=1, id=header.id)
      answer = DNSAnswer(domain, closest_ip)
      packet = new_header.construct() + question.construct() + answer.construct()
      s.sendto(packet, addr)

def find_closest_location(ip_address):
  coord = find_coordinates(ip_address)
  closest_distance = None
  closest_ip = None
  for host in hosts:
    distance = find_distance(hosts[host]['lat'], hosts[host]['lon'], coord['lat'], coord['lon'])
    if closest_distance == None:
      closest_distance = distance
      closest_ip = hosts[host]['ip']
    elif closest_distance < distance:
      closest_distance = distance
      closest_ip = hosts[host]['ip']
  return closest_ip


def find_distance(lat1, lon1, lat2, lon2):
  lat1 = radians(lat1)
  lon1 = radians(lon1)
  lat2 = radians(lat2)
  lon2 = radians(lon2)
  lon_distance = lon2 - lon1
  lat_distance = lat2 - lat1
  a = (sin(lat_distance/2))**2 + cos(lat1) * cos(lat2) * (sin(lon_distance/2))**2
  c = 2 * atan2(sqrt(a), sqrt(1-a))
  return radius * c

def find_coordinates(ip):
  response = urllib2.urlopen('http://ip-api.com/json/' + ip)
  return json.load(response)

def load_locations():
  for host in host_list:
    data = find_coordinates(host[1])
    hosts[host[0]] = {'ip':host[1], 'lat': data['lat'], 'lon': data['lon']}

# parses the command line args
parser = OptionParser()

parser.add_option("-p", "--port", dest="port", 
  help="choose a port to connect to", default=44444)
parser.add_option("-n", "--name", dest="name", 
  help="choose a name", default="cs5700cdnproject.ccs.neu.edu")
(options, args) = parser.parse_args()

load_locations()
start_server(options.name, options.port)
