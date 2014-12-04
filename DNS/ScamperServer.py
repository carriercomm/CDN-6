import SocketServer

class ScamperServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
  def send_ip(self, ip):
    data = json.dunps({'ip': ip})
    print 'Sending'
    for host in host_list:
      self.socket.sendto(data, (host[1], SCAMPER_PORT))
