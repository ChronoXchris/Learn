
original_string = "Hallo World"

print(original_string)
print(original_string.lower())
print(original_string.upper())

firstname ="Christopher"
lastname ="Laukart"

print("Hallo", firstname, lastname )

print(type(original_string))



#################################
#           Datentypen          #
#################################

n1=int(input('Gib mir ine zahl'))

n2=int(input('und noch eine'))

l1 = [1,2,3,4,5,6,7,8,9]

print('2 hoch 3 ist', n1**n2)
print('2 hoch 3 = ' + str(n1**n2))
print(-n1,+n1)
print('2 mal 3 ist', n1*n2)
print('2 mal b ist', n1*l1)
print('2 durch 3 ist', n1/n2)
print ('2 durch 3 hat einen rest von', n1%n2)
print('2 durch 3 die 2 past', n1//n2,'mal rein')
print('2 + 3 ist gleich', n1+n2)
print('2 - 3 ist gleich', n1-n2)

if n1 < n2:
    print('Die zahl',n1 ,' ist kleiner als',n2)
######################################################
if n1 <= n2:
    print('Die zahl', n1,' ist kleiner oder gleich',n2)
######################################################
if n1 > n2:
    print (n1,'Ist größer als',n2)
else:
    print(n1,'ist nicht größer als',n2)
######################################################
if n1 != n2:
    print('Die zahlen',n1 ,n2,'sind nicht gleich')
else:
    print('Die Zahlen',n1 ,n2,'sind gleich')
######################################################
if n1 == n2:
    print('Die Zahlen',n1 ,n2,'sind gleich')
else:
    print('Die Zahlen,',n1 ,n2,'sind nicht gleich')
######################################################
if n1 is n2:
    print('Die Zahlen',n1 ,n2,'sind identisch')
else:
    print('Die Zahlen,',n1 ,n2,'sind nicht identisch')
#####################################################    
if n1 is not n2:
    print('Die Zahlen',n1 ,n2,'sind nicht identisch')
else:
    print('Die Zahlen,',n1 ,n2,'sind identisch')
######################################################
if n1 in l1:
    print('Die zahl',n1,'ist in der liste')
else:
    print('Die zahl',n1,'ist nicht in der liste')
######################################################
print( not n1)
print(n1 and n2)
print(n1 or n2)