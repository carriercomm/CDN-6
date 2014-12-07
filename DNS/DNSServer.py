import SocketServer
import socket
import json

SCAMPER_PORT = 44447

class DNSServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
  def update_rtt(self, client_ip, replica_ip, rtt):
    if replica_ip not in self.ip_rtt:
      self.ip_rtt[replica_ip] = {}
    if client_ip not in self.ip_rtt[replica_ip]:
      self.ip_rtt[replica_ip][client_ip] = rtt 
    self.ip_rtt[replica_ip][client_ip] = rtt

  def send_ip(self, client_ip):
    '''
    Remove comments when http scamper client is ready and this will 
    send the data from DNS to HTTP
    '''
    for host in self.host_list:
      print "%s : %d" % (host[1], SCAMPER_PORT)
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((host[1], SCAMPER_PORT))
      data = json.dumps({'ip': client_ip})
      s.send(data)
