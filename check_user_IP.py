# This script checks user IP and its host name.

import socket
host = socket.gethostname()
host2 = socket.gethostbyname(host)
print(host)
print(host2)
