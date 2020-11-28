messageuser= {'Tsai-ing':{'password':'12345','first_name':'Tsai','last_name':'Ingwen','Phone_number':'886-22311-3731','relationship':{'Winnie':0,'Trump':1}},
              'Trump':{'password':'12345','first_name':'Donald','last_name':'Trump','Phone_number':'1234567','relationship':{'Winnie':1,'Tsai-ing':1}},
             'Winnie':{'password':'12345','first_name':'abc','last_name':'def','Phone_number':'1234567890','relationship':{'Winnie':1,'Tsai-ing':0}}}
        #username:{'password':'12345','first_name':'Tsai','last_name':'Ingwen'...与别人的关系：{}}三重列表！！最外层列表是用户名，第二层列表是用户个人信息，第三重是与别人关系
messageadmin={'dennis LIU':{'password':'123456'}}

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
