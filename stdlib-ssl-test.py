import ssl, socket

ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS) # Noncompliant
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS) # Noncompliant
ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23) # Noncompliant
ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv2) # Noncompliant; removed
ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv3) # Noncompliant; removed
ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1) # Noncompliant
ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_1) # Noncompliant

args = [ssl.PROTOCOL_TLS]  # Noncompliant
ctx = ssl.SSLContext(*args)
kargs = {'protocol': ssl.PROTOCOL_TLS}  # Noncompliant
ctx = ssl.SSLContext(**kargs)

def get_ctx(version=ssl.PROTOCOL_SSLv2): # Noncompliant
    return ssl.SSLContext(version)

version = ssl.PROTOCOL_SSLv2 # Noncompliant

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl.wrap_socket(s) # Noncompliant; Default value is ssl.PROTOCOL_TLS
ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLS) # Noncompliant
ssl.wrap_socket(ssl_version=ssl.PROTOCOL_TLS, sock=s) # Noncompliant
ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv2) # Noncompliant
ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv3) # Noncompliant
ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv23) # Noncompliant
ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1) # Noncompliant
ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1_1) # Noncompliant

kargs = {'ssl_version': ssl.PROTOCOL_TLS} # Noncompliant
ssl.wrap_socket(s, **kargs) 
kargs = {'sock': s, 'ssl_version': ssl.PROTOCOL_TLS}  # Noncompliant
ssl.wrap_socket(**kargs)

ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2) # Compliant
ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2) # Compliant

args = [ssl.PROTOCOL_TLSv1_2] # Compliant
ctx = ssl.SSLContext(*args)
kargs = {'protocol': ssl.PROTOCOL_TLSv1_2}  # Compliant
ctx = ssl.SSLContext(**kargs)

ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1_2) # Compliant
ssl.wrap_socket(ssl_version=ssl.PROTOCOL_TLSv1_2, sock=s) # Compliant

kargs = {'ssl_version': ssl.PROTOCOL_TLSv1_2} # Noncompliant
ssl.wrap_socket(s, **kargs) 
kargs = {'sock': s, 'ssl_version': ssl.PROTOCOL_TLSv1_2}  # Noncompliant
ssl.wrap_socket(**kargs)

def get_ctx(version=ssl.PROTOCOL_TLSv1_2): # Compliant
    return ssl.SSLContext(version)

version = ssl.PROTOCOL_TLSv1_2 # Compliant