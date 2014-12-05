from optparse import OptionParser
import socket
from struct import *
import json
import threading
import time
import SocketServer
from DNSRequestHandler import DNSRequestHandler
from DNSServer import DNSServer
from ScamperRequestHandler import ScamperRequestHandler
from ScamperServer import ScamperServer
from GeoLocator import Locator

host_list = [('localhost', '127.0.0.1')]
hosts = {}
IP = '129.10.117.186'
IP = '127.0.0.1'
SCAMPER_PORT = 44445

def start_server(dns_server, port):
  scamper_server = ScamperServer((IP, 44446), ScamperRequestHandler)
  scamper_server.start_dns(IP, port, dns_server, hosts, host_list)
  scamper_server.serve_forever()
 
def load_locations():
  locator = Locator()
  for host in host_list:
    data = locator.find_coordinates(host[1])
    #hosts[host[0]] = {'ip':host[1], 'lat': data['lat'], 'lon': data['lon']}

# parses the command line args
parser = OptionParser()

parser.add_option("-p", "--port", dest="port", 
  help="choose a port to connect to", default="44444")
parser.add_option("-n", "--name", dest="name", 
  help="choose a name", default="cs5700cdnproject.ccs.neu.edu")
(options, args) = parser.parse_args()

load_locations()
start_server(options.name, int(options.port))
