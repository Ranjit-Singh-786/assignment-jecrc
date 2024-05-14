import socket 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
target_ip = "192.168.1.11"
target_port = 9999
target_address = (target_ip,target_port)

message = input("plz enter your message : ")
encrypted_message = message.encode('ascii')
s.sendto(encrypted_message,target_address)
Data = s.recvfrom(100)
print("i got something : ",Data)