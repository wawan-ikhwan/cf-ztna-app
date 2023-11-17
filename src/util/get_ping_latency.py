import platform    # For getting the operating system name
import subprocess  # For executing a shell command
from .cache import FunctionCacher

def uncached_get_ping_latency(host):
  """
  Returns the round-trip latency in milliseconds if the host (str) responds to a ping request.
  Returns None if the host is unreachable.
  """

  # Option for the number of packets as a function of
  param = '-n' if platform.system().lower() == 'windows' else '-c'

  # Building the command. Ex: "ping -c 1 google.com"
  command = ['ping', param, '1', host]

  try:
    # Run the ping command and capture the output
    output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)

    # Extracting the round-trip time from the output
    start_index = output.find("time=")
    if start_index != -1:
      end_index = output.find("ms", start_index)
      latency_str = output[start_index + 5:end_index].strip()
      return int(latency_str)

  except subprocess.CalledProcessError:
    # Host is unreachable
    return None

get_ping_latency = FunctionCacher(uncached_get_ping_latency, ttl_seconds=60)
