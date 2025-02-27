from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


class LoginWindow():

        def __init__(self,master):

                self.master= master
                self.master.title("Login System")
                self.master.geometry("900x500")
                self.master.resizable(False,False)
                img = Image.open('./images/login.jpg')
                img = img.resize((900, 500))
                self.photo = ImageTk.PhotoImage(img)
                self.credentials= {"Mohanad":"Cs312002"}
                self.success =FALSE
        # use to show photo (background)
                self.image_label = Label(self.master, image=self.photo)
                self.image_label.place(x=0, y=0)
        # create title before write username 
                self.title_label = Label(self.master,text="Employee Management System",font=("Fira Sans",30),fg="Blue")
                self.title_label.place(x=200,y=20)
        # create username 
                self.username_label = Label (self.master,text="UserName",bg="white",font=("Fira Sans",18),fg="blue")
                self.username_label.place(x=500,y=130)
                self.username_entry = Entry(self.master,bd=2,justify="left",font=("Arial",12))
                self.username_entry.place(x=500,y=170)
        # create pasword 
                self.password_label= Label(self.master,text="Password",bg="white",font=("Fira Sans",18),fg="blue")
                self.password_label.place(x=500,y=230)
                self.password_entry = Entry(self.master,bd=2,justify="left",font=("Arial",12),show="*")
                self.password_entry.place(x=500,y=270)
        #create button login 
                self.login_btn = Button(self.master,text="Login",bg="#5b73ec",fg="white",justify="center",font=("Fira Sans",14),command=self.check_login)
                self.login_btn.place(x=500,y=320)
        #closing window 
                self.master.protocol("WM_DELETE_WINDOW", self.closing)

        def check_login(self):
                userName = self.username_entry.get().strip()
                passWord = self.password_entry.get().strip()

                if not userName or not passWord:
                        messagebox.showerror("Error", "Please enter both username and password")
                        return

                if userName in self.credentials:
                        if self.credentials[userName] == passWord:
                                self.success=TRUE
                                messagebox.showinfo("Success", "Login Successful!")
                                self.master.destroy()
                        else:
                                messagebox.showerror("Error", "The password you entered is incorrect. Please try again.")
                else:
                        messagebox.showerror("Error", "The username does not exist. Please check and try again.")

        def closing(self):
                self.master.destroy()