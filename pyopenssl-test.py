
from OpenSSL import SSL
#import OpenSSL.SSL
import sys, os, select, socket

# Initialize context
ctx = SSL.Context(SSL.SSLv2_METHOD)  # Noncompliant
ctx = OpenSSL.SSL.Context(OpenSSL.SSL.SSLv2_METHOD)  # Noncompliant
ctx = SSL.Context(SSL.SSLv3_METHOD)  # Noncompliant
ctx = OpenSSL.SSL.Context(OpenSSL.SSL.SSLv3_METHOD)  # Noncompliant
ctx = SSL.Context(SSL.SSLv23_METHOD)  # Noncompliant
ctx = OpenSSL.SSL.Context(OpenSSL.SSL.SSLv23_METHOD)  # Noncompliant
ctx = SSL.Context(SSL.TLSv1_METHOD)  # Noncompliant
ctx = OpenSSL.SSL.Context(OpenSSL.SSL.TLSv1_METHOD)  # Noncompliant
ctx = SSL.Context(SSL.TLSv1_1_METHOD)  # Noncompliant
ctx = OpenSSL.SSL.Context(OpenSSL.SSL.TLSv1_1_METHOD)  # Noncompliant

ctx = SSL.Context(method=SSL.SSLv2_METHOD)  # Noncompliant
ctx = OpenSSL.SSL.Context(method=OpenSSL.SSL.SSLv2_METHOD)  # Noncompliant

args = (SSL.SSLv2_METHOD) # Noncompliant
SSL.Context(*args ) 
kargs = {'method': SSL.SSLv2_METHOD} # Noncompliant
SSL.Context(**kargs )

def get_ctx(version=ssl.PROTOCOL_SSLv2): # Noncompliant
    return SSL.Context(version)

version=ssl.PROTOCOL_SSLv2 # Noncompliant

ctx = SSL.Context(SSL.TLSv1_2_METHOD)  # Compliant
ctx = SSL.Context(method=SSL.TLSv1_2_METHOD)  # Compliant
ctx = OpenSSL.SSL.Context(OpenSSL.SSL.TLSv1_2_METHOD)  # Compliant

args = [SSL.TLSv1_2_METHOD] # Compliant
SSL.Context(*args) 
kargs = {'method': SSL.TLSv1_2_METHOD} # Compliant
ctx = SSL.Context(**kargs )  

# Set up client
sock = SSL.Connection(ctx, socket.socket())
sock.connect(("127.0.0.1", 8443))
sock.do_handshake()

data="""GET / HTTP/1.1
Host: 127.0.0.1

""".replace("\n","\r\n")
sock.send(data)

while 1:
    try:
        buf = sock.recv(4096)
        print(buf)
    except SSL.Error:
        print('Connection died unexpectedly')
        break


sock.shutdown()
sock.close()