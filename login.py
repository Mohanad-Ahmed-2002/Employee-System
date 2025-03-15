from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from abc import ABC, abstractmethod

class AuthStartegy(ABC):
    @abstractmethod
    def authenticate(self,username,password)->bool:
        pass

class BasicAuth(AuthStartegy):
    
    def __init__(self):
        self.credentials= {"Mohanad":"Cs312002"}
    def authenticate(self,username,password)->bool:
        return self.credentials.get(username)== password  

class EmailAuth(AuthStartegy):

    def __init__(self):
        self.credentials= {"mohanadahmed092@gmail.com":"Cs312002"}
    
    def authenticate(self,username,password)->bool:
        return self.credentials.get(username)== password  

class LoginWindow():

        def __init__(self,master,auth_startegy:AuthStartegy):
            self.master= master
            self.success =False
            self.auth_strategy = auth_startegy
            self.master.protocol("WM_DELETE_WINDOW", self.closing)
            self.design_tk()
            self.show_background()
            self.title_background()
            self.create_username()
            self.create_password()
            self.button_login()

        def design_tk(self):
            self.master.title("Login System")
            self.master.geometry("900x500")
            self.master.resizable(False,False)

        def show_background(self):
            try:
                img = Image.open('./images/login.jpg')
                img = img.resize((900, 500))
                self.photo = ImageTk.PhotoImage(img)
                self.image_label = Label(self.master, image=self.photo)
                self.image_label.place(x=0, y=0)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load background image: {e}")

        def title_background(self):
            self.title_label = Label(self.master,text="Employee Management System",font=("Fira Sans",30),fg="Blue")
            self.title_label.place(x=200,y=20)

        def create_username(self):
            self.username_label = Label (self.master,text="UserName",bg="white",font=("Fira Sans",18),fg="blue")
            self.username_label.place(x=500,y=130)
            self.username_entry = Entry(self.master,bd=2,justify="left",font=("Arial",12))
            self.username_entry.place(x=500,y=170)

        def create_password(self):
            self.password_label= Label(self.master,text="Password",bg="white",font=("Fira Sans",18),fg="blue")
            self.password_label.place(x=500,y=230)
            self.password_entry = Entry(self.master,bd=2,justify="left",font=("Arial",12),show="*")
            self.password_entry.place(x=500,y=270)

        def button_login(self):
            self.login_btn = Button(self.master,text="Login",bg="#5b73ec",fg="white",justify="center",font=("Fira Sans",14),command=self.check_login)
            self.login_btn.place(x=500,y=320)

        def check_login(self):
            userName = self.username_entry.get().strip()
            passWord = self.password_entry.get().strip()

            if not userName or not passWord:
                messagebox.showerror("Error", "Please enter both username and password")
                return

            if self.auth_strategy.authenticate(userName, passWord):
                self.success = True
                messagebox.showinfo("Success", "Login Successful!")
                self.master.destroy()
            else:
                messagebox.showerror("Error", "Invalid username or password. Please try again.")

        def closing(self):
                self.master.destroy()