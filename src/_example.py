import ctypes

test = ctypes.cdll.LoadLibrary('C:\\Users\\Glist\\Downloads\\CheckSummTest\\c_module\\checksum.dll')

# Указываем, что функция возвращает char
test.calculateChecksum.restype = ctypes.c_char
# Указываем, что функция принимает аргумент char *
test.calculateChecksum.argtypes = [ctypes.POINTER(ctypes.c_char), ]

cmd = 'D,s,1,1,5430.1270,N,1920.2310,E,15.2,081121,38.000,48.000,*,$,\r,\n'

cs = ord(test.calculateChecksum(cmd.encode('utf-8')))
print(cs)
