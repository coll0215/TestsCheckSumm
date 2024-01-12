import ctypes

test = ctypes.cdll.LoadLibrary('C:\\Users\\Glist\\Downloads\\Testing\\Testing\\c_module\\checksum.dll')

# Указываем, что функция возвращает char
test.calculateChecksum.restype = ctypes.c_char
# Указываем, что функция принимает аргумент char *
test.calculateChecksum.argtypes = [ctypes.POINTER(ctypes.c_char), ]

cmd = 'D,s,1,2,31085,6233,19167,3377,333,24855,17178,20629,26180,277.200,*,$,\r,\n'

cs = ord(test.calculateChecksum(cmd.encode('utf-8')))
print(cs)
