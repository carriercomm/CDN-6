import SocketServer
from DNSRequestHandler import DNSRequestHandler
from DNSServer import DNSServer
import threading
import time

class ScamperServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
  def send_ip(self, ip):
    data = json.dunps({'ip': ip})
    print 'Sending'
    for host in host_list:
      self.socket.sendto(data, (host[1], SCAMPER_PORT))

  def update_rtt(self, client_ip, replica_ip, rtt):
    self.dnsserver.update_rtt(client_ip, replica_ip, rtt)

  def start_dns(self, ip, port, dns_server, hosts, host_list):
    self.dnsserver = DNSServer((ip, port), DNSRequestHandler)
    self.dnsserver.dns_server = dns_server
    self.dnsserver.ip_rtt = {}
    self.dnsserver.hosts = hosts
    self.dnsserver.host_list = host_list
    self.dns_server_thread = threading.Thread(target=self.dnsserver.serve_forever)
    self.dns_server_thread.setDaemon(True)
    self.dns_server_thread.start()
