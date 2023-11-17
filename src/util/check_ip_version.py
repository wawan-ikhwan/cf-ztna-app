import ipaddress

def check_ip_version(ip_address):
  try:
    ip = ipaddress.ip_address(ip_address)
    if ip.version == 4:
      return "IPv4"
    elif ip.version == 6:
      return "IPv6"
    else:
      return "Unknown IP version"
  except ValueError:
    return "Invalid IP address"