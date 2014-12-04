import SocketServer
import socket

class DNSServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
  def update_rtt(self, client_ip, replica_ip, rtt):
    if replica_ip not in self.ip_rtt:
      self.ip_rtt[replica_ip] = {}
    if client_ip not in self.ip_rtt[replica_ip]:
      self.ip_rtt[replica_ip][client_ip] = rtt 
    self.ip_rtt[replica_ip][client_ip] = rtt

  def send_ip(self, client_ip):
    for host in self.host_list:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((host[1], 44446))
      data = json.dumps({'ip': client})
      s.send(data)
