messageuser= {}
messageadmin={}

def isFriend(X,Y):
def IsDirectSource(A,b):
def isSource(A,B):
def Anchor(A):
def DirectReport(A):
def Report(A):
def NicePrientU(X):
def NicePrintA(A):
def GetU(X):
def GetA(A):

def admin(): # admin function

def user(): #user function


def user_register():
    name = input("Please enter your username")
    while True:
        if name in messageuser:#
            temp = "This username has been taken, try another username："
            continue
        else: # 没有此人的信息
            break
    pw = input("Please enter your password：")
    messageuser[name] = pw
    print("Successfully register!")

def user_login():
    
    temp = "Please enter your username："
    while True:
        name = input(temp)
        if name not in messageuser:
            temp = "Username Wrong, try again："
            continue
        else:
            break
    pw = input("Please enter your password：")
    password = messageuser.get(name)
    if pw == password:
        print("Log in successfully")
        user() #转到用户功能
    else:
        print("Wrong Password")



def admin_register():
    name = input("Please enter your admin name")
    while True:
        if name in messageadmin:  #
            temp = "This username has been taken, try another username："
            continue
        else:  # 没有此人的信息
            break
    pw = input("Please enter your password：")
    messageadmin[name] = pw
    print("Successfully register!")


def admin_login():
    temp = "Please enter your admin name："
    while True:
        name = input(temp)
        if name not in messageadmin:
            temp = "Username Wrong, try again："
            continue
        else:
            break
    pw = input("Please enter your password：")
    password = messageuser.get(name)
    if pw == password:
        print("Log in successfully")
        admin() #转到管理功能
    else:
        print("Wrong Password")
    a1=input('Are you going to the admin? yes or no')

def main():
    print("""
    |---------Welcome to system------------|
    |--- Create a new user account：N/n ---|
    |---- Login user Account：S/s ---------|
    |--- Create a new admin account：W/w---|
    |----- Login admin Account：E/e -------|    
    |---------- Log out：Q/q --------------|
    """)
    while True:
        chose = 0
        while not chose:
            print('\n')
            order = input("Enter：")
            if order not in 'QqNnEe':
                print("Wrong input, please choose again!")
            else:
                chose = 1

        if order == 'N' or order == 'n':
            user_register()
        if order == 'S' or order == 's':
            user_login()
        if order == 'E' or order == 'e':
            admin_login()
        if order == 'W' or order == 'E':
            admin_register()
        if order == 'Q' or order == 'q':
            break

main()
