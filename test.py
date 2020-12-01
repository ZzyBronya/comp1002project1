paper_direct={'A':['C','D'],'B':0,'C':0,'D':['B']}# 论文与其他论文的直接引用关系
paper_all={}
messageuser = {
    'Tsai-ing': {'password':'12345', 'first_name': 'Tsai', 'last_name': 'Ingwen', 'Phone_number': '886-22311-3731',
                 'relationship': {'Winnie': 0, 'Trump': 1},'paper':{}},
    'Trump': {'password':'12345', 'first_name': 'Donald', 'last_name': 'Trump', 'Phone_number': '1234567',
              'relationship': {'Winnie': 1, 'Tsai-ing': 1},'paper':{}},
    'Winnie': {'password':'12345', 'first_name': 'abc', 'last_name': 'def', 'Phone_number': '1234567890',
               'relationship': {'Winnie': 1, 'Tsai-ing': 0},'paper':{}}}
# username:{'password':'12345','first_name':'Tsai','last_name':'Ingwen'...与别人的关系：{}}三重列表！！最外层列表是用户名，第二层列表是用户个人信息，第三重是与别人关系
messageadmin = {'dennis LIU': {'password': '123456'}}


'''
def isFriend(X, Y):


def IsDirectSource(A, b):

def isSource(A, B):

def Anchor(A):

def DirectReport(A):

def Report(A):

def NicePrientU(X):

def NicePrintA(A):

def GetU(X):

def GetA(A):

'''
def admin(name):  # admin function
    print('Hello',name)
    print("""
    |---------Welcome to admin interface-----|
    |--- ：N/n ---|
    |---- Login user Account：S/s ---------|
    |--- Create a new admin account：W/w---|
    |----- Login admin Account：E/e -------|    
    |---------- Log out：Q/q --------------|
    """)

def user(name):  # user function
    print('Hello',name)
    while True:
        print("""
        |--- Welcome to admin interfac------|
        |--- Submit Paper：N/n -------------|
        |--- Make friends: S/s--------------|
        |--- Back to main interface: Q/q----|
        """)
        while True: #上传paper
            chose = 0
            while not chose:
                print('\n')
                order = input("Enter：")
                if order not in 'NnSsWw':
                    print("Wrong input, please choose again!")
                else:
                    chose = 1
            if order=='N' or order=='n':# Submit paper
                paper_index=input('Please enter your paper index:')
                while True:
                    if paper_index in paper_direct:
                        print('This index has been taken, try a new index.')
                    else:
                        break
                aa=input('Please submit your paper content (Just paste here):')
                messageuser[name]['paper'][paper_index]=aa
                print('')
                
            if order=='S' or order=='s': # Make friends
                for i in messageuser:
                    print(i,end='')
                    print('')
                    print("Enter your friend's username one by one:")
                    while True:
                        a1=input("Enter your friend's username(If no more, enter 'No' exit):")
                        if a1=='No':
                            break
                        elif a1 in messageuser:
                            messageuser[name]['relationship'][a1]=1
                            messageuser[a1]['relationship'][name]=1
                        else:
                            print()
            if order=='Q' or order=='q': 
                main()
    

def user_register():
    print('User register interface')
    name = input("Please enter your username:")
    while True:
        if name in messageuser:  #
            temp = "This username has been taken, try another username:"
            continue
        else:  # 没有此人的信息
            break

    pw = input("Please enter your password:")
    messageuser[name]={}
    messageuser[name]['relationship']={}
    messageuser[name]['paper']={}
    messageuser[name]['password'] = pw
    p1 = input('Please enter your first name:')
    messageuser[name]['first_name']=p1
    p2 = input('Please enter your last name:')
    messageuser[name]['last_name']=p2
    print("""
    |------Add auxiliary information one by one-----|
    |--- Date-of-birth：N/n ---|
    |---- Phone number：S/s ---------|
    """)
    while True:
        pp=input('How many type of information are you going to add:')
        if pp.isdigit():
            break
        else:
            print('Are you serious?')

   
    chose = 0
    while  chose <int(pp):
        print('\n')
        order = input("Enter the type of information you would like to enter：")
        if order not in 'NnSs':
            print("Wrong input, please choose again!")
        else:
            chose +=1

            if order=='N' or order=='n':
                k1=input('Please enter your data of birth:')
                messageuser[name]['Date-of-birth']=k1

            if order=='S' or order=='s':
                k2 = input('Please enter your phone number:')
                messageuser[name]['Phone_number']=k2
    print("Successfully register!")
    main()

def user_login():
    print('User login interface')
    temp = "Please enter your username:"
    while True:
        name = input(temp)
        if name not in messageuser:
            temp = "Username Wrong, try again："
            continue
        else:
            break
    pw = str(input("Please enter your password："))
    password = messageuser[name]['password']
    if pw == password:
        print("Log in successfully")
        user(name)  # 转到用户功能
    else:
        print("Wrong Password")

def admin_register():
    print('Admin register interface')
    name = input("Please enter your admin name")
    while True:
        if name in messageadmin:  #
            temp = "This username has been taken, try another username"
            continue
        else:  # 没有此人的信息
            break
    pw = input("Please enter your password")
    messageadmin[name] = pw
    print("Successfully register!")
    main()


def admin_login():
    print('Admin login interface')
    temp = "Please enter your admin name："
    while True:
        name = input(temp)
        if name not in messageadmin:
            temp = "Username Wrong, try again："
            continue
        else:
            break
    pw = input("Please enter your password：")
    password = messageadmin[name]['password']
    if pw == password:
        print("Log in successfully")
        admin(name)  # 转到管理功能
    else:
        print("Wrong Password")

def main():
    while True:
            print('*'*20)
            print("""
            |---------Welcome to system------------|
            |--- Create a new user account：N/n ---|
            |---- Login user Account：S/s ---------|
            |--- Create a new admin account：W/w---|
            |----- Login admin Account：E/e -------| 
            """)
            print('*'*20)
            while True:
                chose = 0
                while not chose:
                    print('\n')
                    order = input("Enter:")
                    if order not in 'QqNnSsWwEe':
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



main()
