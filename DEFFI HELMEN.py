p=23
g=5

#pnivate key
a=6
b=15

A=pow(g, a, p)
B=pow(g, b, p)

key_A=pow(B, a, p)
key_B=pow(A, b, p)
print("public prime(p)：",p)
print("primitive Root(g):",g)
print("Alice public key:", A)
print("Bob public key:", B)
print("Alice shared key:", key_A)
print("Bob shared key:", key_B)
if key_A==key_B:
    print("key Exchange successfull!")
else:
    print("key Exchange falied!")