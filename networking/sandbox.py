import socket
import fcntl
import struct
import netifaces

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('192.168.1.1', 0))
        IP = s.getsockname()[0]
    except Exception as e:
        print e
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
    except socket.error as e:
        print e
        return "127.0.0.1"
    return s.getsockname()[0]


print get_ip()
print get_ip_address()
print socket.gethostname()
print netifaces.interfaces()
addrs = netifaces.ifaddresses('en0')
print addrs[netifaces.AF_INET][0]['addr']
