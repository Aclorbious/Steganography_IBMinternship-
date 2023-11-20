import cv2
import os
import string

img = cv2.imread("CyberF_LM_CyberKillChain_Eng.png")

msg = input("ENTER YOUR MESSAGE : ")

password = input("CREATE A PASSWORD : ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)
    
m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n,m,z] = d[msg[i]]
    n = n+1
    m = m+1
    z = (z+1)%3
cv2.imwrite("nweimager.jpg",img)
os.system("start nweimager.jpg")
    
message =" "
m = 0
n = 0
z = 0

pas=input("ENTER THE PASSWORD")

if password == pas:
    for i in range(len(msg)):
        message = message+c[img[n,m,z]]
        n =n+1
        m = m+1
        z = (z+1)%3
    print("THE MESSAGE IS",message)
else:
    print("THE PASSWORD IS WRONG")
