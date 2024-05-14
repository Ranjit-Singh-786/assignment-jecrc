import socket
my_ip = "192.168.1.11"
port_no = 9999
my_address = (my_ip,port_no)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(my_address)
while True:
    print("I am recieving ...")
    complt_data = s.recvfrom(120)
    # print(complt_data)
    encrypted_message = complt_data[0]
    print(encrypted_message.decode('ascii'))
    address = complt_data[1]
    reply_message = "Thank you"
    reply_message = reply_message.encode('ascii')
    s.sendto(reply_message,address)
