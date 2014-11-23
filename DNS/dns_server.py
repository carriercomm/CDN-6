from optparse import OptionParser
import socket
from struct import *
from dns_header import DNSHeader
from dns_question import DNSQuestion
from dns_answer import DNSAnswer

hosts = ['ec2-54-174-6-90.compute-1.amazonaws.com']

def start_server(name, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind(('129.10.116.196', port))
  print socket.gethostname()
  print socket.gethostbyname(socket.gethostname())
  
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
    header = DNSHeader(data[0:12], parse=True)
    question = DNSQuestion(data[12:])
    new_header = DNSHeader(ancount=1, qdcount=1, id=header.id)
    answer = DNSAnswer('gsoeller.com', '129.10.116.197')
    print str(new_header)
    print str(answer)
    packet = new_header.construct() + question.construct() + answer.construct()
    print 'LENGHTH:\t', len(packet)
    s.sendto(packet, addr)


# parses the command line args
parser = OptionParser()

parser.add_option("-p", "--port", dest="port", 
  help="choose a port to connect to", default=44444)
parser.add_option("-n", "--name", dest="name", 
  help="choose a name", default="cs5700cdnproject.ccs.neu.edu")
(options, args) = parser.parse_args()

start_server(options.name, options.port)
