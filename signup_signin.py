import re

user_dict= {
    'gaurav':'qwe123',
    'sonali':'son45',
    'ajay':'aj007',
}

def add_user(user_dict,temp_dict):
    user_dict.update(temp_dict)

def signup(user_dict):
    usernames=list(user_dict.keys())
    i=1
    while i>0:
        new_username=input("choose your username: ")
        new_username=new_username.lower()
        if new_username in usernames: 
            print("username is already taken.")
            continue
        else:
            print(f"your username is {new_username}.")
            break
    usernames.append(new_username)
    
    print("Let's set up password.")
    
    i=1
    while i>0:
        user= input("enter your username to set password: ")
        if user.lower() in usernames:
            print(f"welcome {user}!")
            i=1
            while i>0:
                password=input("choose the password: ")
                pat=re.search("\W",password)
                if pat:
                    print("password must contain only letters and numbers.")
                    continue
                else:
                    print(f"password set for {user} is {password}.")
                    break
            break        
        else:
            print("username not found. Enter correct username.")
            continue

    return new_username,password

def signin(user_dict):
    usernames=list(user_dict.keys())
    i=1
    while i>0:
        name=input("enter username: ")
        name=name.lower()
        if name in usernames:
            for i in range(0,3):
                passwd=input("enter your password: ")
                if passwd==user_dict.get(name):
                    a=True
                    break
                else:
                    print("password is incorrect.")
                    a=False
                    continue
            if a==False:
                print("forgot your password.")
                b=input("enter your username: ")
                b=b.lower()
                if b in usernames:
                    print(f"your password is: {user_dict.get(b)}")
                else:
                    print("you are not a user.")
            elif a==True:
                print("WELCOME!")
        else:
            print("not a user.")

print("welcome! \n if already a user signin(in). if not signup(up).")
x=input("in or up: ")
if x=="in":
    signin(user_dict)
elif x=="up":
    newuser=list(signup(user_dict))
    temp_dict={newuser[0]:newuser[1]}
    add_user(user_dict,temp_dict)





        
        




    
    



