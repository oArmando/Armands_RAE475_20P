import socket, time #importejam socket un time modulus

host = socket.gethostbyname(socket.gethostname()) #mainigais host lai automatiski uzliekas IP
port = 9090 #porta mainigais, nemam no liela diapazona/nevajag admin tiesibas un brivs

clients = [] #mainigais klients, kur ir pieslegtie klienti//nevar username,lai pie vienadiem usrname dazadi klienti

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#UDP
s.bind((host,port))#

quit = False
(host):print("[ Server Started IP: "+host+" ]")#pieliekam lai izvada IP savādāk pusgadu jāmeklē

while not quit:
	try:
		data, addr = s.recvfrom(1024)

		if addr not in clients:
			clients.append(addr)

		itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

		print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/",end="")
		print(data.decode("utf-8"))

		for client in clients:
			if addr != client:
				s.sendto(data,client)
	except:	
		print("\n[ Server Stopped ]")
		quit = True
		
s.close()