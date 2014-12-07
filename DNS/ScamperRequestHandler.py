import SocketServer
import json

class ScamperRequestHandler(SocketServer.BaseRequestHandler):
  def handle(self):
    self.data = self.request.recv(1024)
    data = json.loads(self.data)
    ip = str(data['ip'])
    rtt = int(data['rtt'])
    print "%s : %dms" % (ip, rtt)
    if rtt >= 0:
      self.server.update_rtt(self.client_address[0], ip, rtt)