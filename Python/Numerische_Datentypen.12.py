##################################
#           12.1                 #
##################################

n1 = int(input('Gib mir eine Zahl'))
n2 = int(input('Gib mir noch eine Zahl'))
n3 = int(input('Gib mir eine komma Zahl'))

print(n1, 'plus', n2, 'ist gleich', n1 + n2)
print(n1, 'minus', n2, 'ist gleich',n1 - n2)
print(n1, 'mal', n2, 'ist gleich', n1*n2)
print(n1, 'geteilt durch', n2, 'ist gleich',n1/n2)
print(n1,'geteilt durch', n2, 'hat einen rest von' ,n1%n2)
print(+n1, +n2)
print(-n1, -n2)
print(n1, 'hoch', n2, 'ist gleich')
print(n1, 'past', n1//n2, 'in ', n2, 'rein')

############################
#          12.3            #
############################

float(n1, n2, n3)
int(n1, n2 , n3)
bool(n1, n2, n3)
complex(True)

################################################################################

1_000_000
1_0_0

################################################################################

v_dez = 1337   #Dezimalsystem (Basis 10)
v_okt = 0o2471 #Oktalsystem (Basis 8)
v_hex = 0x5A3F #Hexadezimalsystem (Basis 16)
v_bin = 0b1101 #Binärsystem (Basis 2)

v6= int('44325', 6)
-1234
-0o777
-0xFF
-0b1010101

#################################################################################

v1 = 0xFF
v2 = 0o777
print(v1)
print(v2)

#################################################################################

print(107 & 25) #Bitweise UND
print(107 | 25) #Bitweise nich ausschließend ODER
print(107 ^ 25) #Bitweise ausschließend ODER
print(~107)     #Bitweise Komplement von 107
print(107 << 2) #Bit-Verschiebung um 2 stellen nach links
print(107 >> 2) #BIt-Verschiebung um2 Stellen nach rechts

#################################################################################

print((36).bit_length())
print((4345).bit_length())

#################################################################################

print(-3.)
print(.001)
print(3e2)

#################################################################################

print(3.000_000_000_1)
print(1.1 + 2.2)

#################################################################################

v3 = True
v4 = False
n4 = 2
n5 = 3

if not v4:
    print('x ist False')
else:
    print('x ist True')

if 2 and 3:
    print( '2 und 3 sind True')

