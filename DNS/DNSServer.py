import SocketServer

class DNSServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
  def update_rtt(self, client_ip, replica_ip, rtt):
    if replica_ip not in self.ip_rtt:
      self.ip_rtt[replica_ip] = {}
    if client_ip not in self.ip_rtt[replica_ip]:
      self.ip_rtt[replica_ip][client_ip] = rtt 
    self.ip_rtt[replica_ip][client_ip] = rtt
