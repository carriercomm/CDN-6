from optparse import OptionParser
import socket
from struct import *
from dns_header import DNSHeader
from dns_question import DNSQuestion


def start_server(name, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind(('127.0.0.1', port))
  
  '''
  qname = pack('!cscscs', ord('3'), 'www', ord('6'), 'google', ord('3'), 'com')
  question = DNSQuestion(qname)

  header = DNSHeader()
  print len(header.pack())
  s.connect(('127.0.0.1', port))
  s.send(header.pack())
  '''
  while 1:
    data, addr = s.recvfrom(1024)
    #print data, len(data)
    header = DNSHeader(data[0:12], parse=True)
    print str(header)
    question = DNSQuestion(data[12:])


# parses the command line args
parser = OptionParser()

parser.add_option("-p", "--port", dest="port", 
  help="choose a port to connect to", default=44444)
parser.add_option("-n", "--name", dest="name", 
  help="choose a name", default="cs5700cdnproject.ccs.neu.edu")
(options, args) = parser.parse_args()

start_server(options.name, options.port)