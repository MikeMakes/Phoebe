from tcp import mysocket

aSocket=mysocket()
aSocket.accept()
msg = aSocket.receive()
print "again ",msg
aSocket.closesocket()
