class login:
    user=[{'Name': 'Kowsalya', 'Email': 'kowsi@gmail.com', 'Password': 'Kowsi'},
            {'Name': 'Reshma', 'Email': 'reshma@gmail.com', 'Password': 'Reshma138'}]
    
    
    def __init__(self,Name,Email,Password):
        self.Name = Name
        self.Email = Email
        self.Password = Password

    def sign_in(self):
        user_detail = {'Name': self.Name, 'Email': self.Email, 'Password': self.Password}

        if user_detail in login.user:
            print('Username is invalid or already taken')
        
        else:
            (login.user).append(user_detail)
            print('Login Successfully')
            
def show():
    Name = input("Enter your name : ")
    Email = input("Enter your mail id : ")
    Password = input("Enter the password : ")
    user1 = login(Name,Email,Password)
    user1.sign_in()
    
show() 

Output:

Enter your name : Praba
Enter your mail id : praba23@gmail.com
Enter the password : praba831
Login Successfully
