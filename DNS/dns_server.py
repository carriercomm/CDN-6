from optparse import OptionParser
import socket
from struct import *
from dns_header import DNSHeader
from dns_question import DNSQuestion
from dns_answer import DNSAnswer

hosts = ['ec2-54-174-6-90.compute-1.amazonaws.com']

def start_server(dns_server, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind(('129.10.116.196', port))

  while 1:
    data, addr = s.recvfrom(1024)
    header = DNSHeader(data[0:12], parse=True)
    question = DNSQuestion(data[12:])
    domain = question.domain
    if domain == dns_server:
      new_header = DNSHeader(ancount=2, qdcount=1, id=header.id)
      answer = DNSAnswer(domain, '129.10.116.197')
      answer2 = DNSAnswer(domain, '129.10.116.196')
      packet = new_header.construct() + question.construct() + answer.construct() + answer2.construct()
      s.sendto(packet, addr)


# parses the command line args
parser = OptionParser()

parser.add_option("-p", "--port", dest="port", 
  help="choose a port to connect to", default=44444)
parser.add_option("-n", "--name", dest="name", 
  help="choose a name", default="cs5700cdnproject.ccs.neu.edu")
(options, args) = parser.parse_args()

start_server(options.name, options.port)
