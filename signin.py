import os
found=False
def sigin():
    z=int(0)
    k=int(input())
    if(k==1):
        name = input()
        password = input()
        t=open("doc.txt","r")
        for line in t:
            if name in line:
                if password in line:
                    print("got it")
                    os.system("afterlogin.py")
                    found = True
                    z=1
                    break
        if(z==0):
            print("not found")




    else:
        name = input()
        password = input()
        t = open("pat.txt", "r")
        for line in t:
            if name in line:
                if password in line:
                    print("got it")
                    os.system("afterlogin.py")
                    found = True
                    z=1
                    break
        if (z == 0):
            print("not found")



sigin()