from tkinter import *
import tkinter as tk
from tkinter import ttk
from database import DatabaseManager
from PIL import Image, ImageTk
from tkinter import messagebox





class AppWindow():

    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x600")
        self.root.resizable(False,False)
        self.root.title("Employee Management System ")
        image= Image.open('./images/ems.jpg')
        image = image.resize((1000, 150))
        self.photo = ImageTk.PhotoImage(image)
        self.root.configure(background=("#252d56"))
        self.db= DatabaseManager()



# use to show photo (background)
        self.image_label = Label(self.root, image=self.photo)
        self.image_label.place(x=0, y=0)
# use to create manage frame
        self.manage_frame = Frame(self.root,bg="#252d56")
        self.manage_frame.place(x=0,y=175,width=350,height=335)
    # use to create label id and entry 
        self.id_label = Label (self.manage_frame,text="ID",font=("Arial",18,"bold"),bg="#252d56",fg="white")
        self.id_label.place(x=30,y=10)
        self.id_entry= Entry(self.manage_frame,justify="center",relief="sunken",font=("Arial",12))
        self.id_entry.place(x=155,y=15,width=140)
    # use to create label Name and entry 
        self.name_label= Label(self.manage_frame,text="Name",font=("Arial",18,"bold"),bg="#252d56",fg="white")
        self.name_label.place(x=30,y=70)
        self.name_entry = Entry(self.manage_frame,relief="sunken",font=("Arial",12),justify="center")
        self.name_entry.place(x=155,y=75,width=140)
    # use to create label Position and entry 
        self.position_label= Label(self.manage_frame,text="Position",font=("Arial",18,"bold"),bg="#252d56",fg="white")
        self.position_label.place(x=30,y=130)
        self.combo_position = ttk.Combobox(self.manage_frame,justify="center")
        self.combo_position['value']=['GM','Secretariat','Marketing Manager','Marketing','Software Engineer','Sales','Customer Services','Quality Control','Lawyer']
        self.combo_position.place(x=155,y=135,width=140)
    # use to create label Gender and entry 
        self.gender_label = Label(self.manage_frame, text="Gender", font=("Arial", 18, "bold"), bg="#252d56", fg="white")
        self.gender_label.place(x=5, y=190,width=140)
        self.combo_gender = ttk.Combobox(self.manage_frame,justify="center")
        self.combo_gender['value'] = ['MALE', 'FEMALE']
        self.combo_gender.place(x=155, y=195)
    # use to create label Salary and entry 
        self.salary_label= Label(self.manage_frame,text="Salary",font=("Arial",18,"bold"),bg="#252d56",fg="white")
        self.salary_label.place(x=30,y=250)
        self.salary_entry = Entry(self.manage_frame,relief="sunken",font=("Arial",12),justify="center")
        self.salary_entry.place(x=155,y=255,width=140)
#----------------------------------------------------------------------------------------------------------------------------------------
# use to button frame
        self.button_frame = Frame(self.root,bg="#252d56")
        self.button_frame.place(x=0,y=485,width=1000,height=115)
        # use to create button New employee 
        self.new_emp_btn = Button(self.button_frame,bg="#5dade2",text="New Employee",font=("Arial",12,"bold"),justify="center",fg="white",command=self.new_employee)
        self.new_emp_btn.place(x=10,y=55,width=180)
        # use to create button Add Employee 
        self.add_emp_btn = Button(self.button_frame,bg="#5dade2",text="Add Employee",font=("Arial",12,"bold"),justify="center",fg="white",command=self.add_employee)
        self.add_emp_btn.place(x=200,y=55,width=180)
        # #use to create button Update employee 
        self.upd_emp_btn = Button(self.button_frame,bg="#5dade2",text="Update Employee",font=("Arial",12,"bold"),justify="center",fg="white",command=self.update_employee)
        self.upd_emp_btn.place(x=400,y=55,width=180)
        # # use to create button Delete employee 
        self.del_emp_btn = Button(self.button_frame,bg="#5dade2",text="Delete Employee",font=("Arial",12,"bold"),justify="center",fg="white",command=self.delete_employee)
        self.del_emp_btn.place(x=600,y=55,width=180)
        # # use to create button Delete 
        self.del_all_btn = Button(self.button_frame,bg="#5dade2",text="Delete ALL",font=("Arial",12,"bold"),justify="center",fg="white",command=self.delete_all_employees)
        self.del_all_btn.place(x=800,y=55,width=180)
#--------------------------------------------------------------------------------------------------------------------------------------------
# use to create serach-frame 
        self.search_frame = Frame(self.root,bg="#d8d8cb")
        self.search_frame.place(x=350,y=165,width=640,height=60)
        # use to create label search and combobox
        self.combo_search = ttk.Combobox(self.search_frame,background="white",justify="left")
        self.combo_search['value']=['Id','Name','Position']
        self.combo_search.place(x=5,y=20,width=120)
        # use to create entry search
        self.search_entry = Entry(self.search_frame,justify="center",font=("Arial",12),relief="sunken")
        self.search_entry.place(x=150,y=20,width=150)
        # use to create button search
        self.search_btn = Button(self.search_frame,bg="#0b1450",text="search",font=("Arial",12,"bold"),justify="center",fg="white",command=self.search_employee)
        self.search_btn.place(x=330,y=15,width=100,height=30)
        # use to create button show all
        self.show_btn = Button(self.search_frame,bg="#0b1450",text="Show All",font=("Arial",12,"bold"),justify="center",fg="white",command=self.show_all)
        self.show_btn.place(x=450,y=15,width=100,height=30)


#----------------------------------------------------------------------------------------------------------------------------------------------
# use to create Details Frame 
        self.details_frame = Frame(self.root, background="#34495e")
        self.details_frame.place(x=350, y=225, width=640, height=265)

        # إعداد النمط للـ Treeview ورؤوس الأعمدة باستخدام ثيم "clam"
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")
        self.style.configure("Treeview",
                            background="#1a5276",        # خلفية بيانات الصفوف
                            fieldbackground="white",   # خلفية منطقة الخلايا
                            foreground="white",
                            font=("Helvetica", 10,"bold"))
        self.style.configure("Treeview.Heading",
                            background="Silver",       # خلفية رؤوس الأعمدة
                            foreground="black",
                            font=("Helvetica", 12, "bold"))

        # إنشاء Scrollbars وربطها بالـ Treeview
        scroll_x = Scrollbar(self.details_frame, orient="horizontal")
        scroll_y = Scrollbar(self.details_frame, orient="vertical")

        # إنشاء الـ Treeview وربطه مع الـ Scrollbars
        self.employee_table = ttk.Treeview(self.details_frame,
                                        columns=('id', 'name', 'position', 'gender', 'salary'),
                                        xscrollcommand=scroll_x.set,
                                        yscrollcommand=scroll_y.set,
                                        show='headings')
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        # استخدام pack داخل details_frame لملء المساحة المتاحة
        self.employee_table.pack(side=LEFT, fill=BOTH, expand=True)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)

        # إعداد رؤوس الأعمدة وضبط عرضها
        self.employee_table.heading('id', text="ID")
        self.employee_table.heading('name', text="Name")
        self.employee_table.heading('position', text="Position")
        self.employee_table.heading('gender', text="Gender")
        self.employee_table.heading('salary', text="Salary")

        self.employee_table.column("id", width=60)
        self.employee_table.column("name", width=200)
        self.employee_table.column("position", width=200)
        self.employee_table.column("gender", width=100)
        self.employee_table.column("salary", width=80)

        self.employee_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

#-----------------------------------------------------------------------------------------------------------------
    def new_employee(self):#use this function to remove fields to add new employee 

        self.id_entry.delete(0,END)
        self.name_entry.delete(0,END)
        self.combo_position.set("")
        self.combo_gender.set("")
        self.salary_entry.delete(0,END)
        
#---------------------------------------------------------------------------------------------------------------------
    def add_employee(self): #use to add new employee this function 
        
        id=self.id_entry.get().strip()
        name= self.name_entry.get().strip()
        position = self.combo_position.get().strip()
        gender= self.combo_gender.get().strip()
        salary = self.salary_entry.get().strip()

        try:
            self.db.add_employee(id,name,position,gender,salary)
            messagebox.showinfo("Success","Employee added successfully")
            self.fetch_data()
        except Exception as e:
            messagebox.showerror("Error",f"While adding employee {e}")
#-------------------------------------------------------------------------------------------------------------------------
    def fetch_data(self):

        self.employee_table.delete(*self.employee_table.get_children())
        rows= self.db.get_employees()

        for row in rows:
            self.employee_table.insert("","end",values=row)
#--------------------------------------------------------------------------------------------------------------------------
    def get_cursor(self,event): # use to focus in row 

        cursor_row = self.employee_table.focus()
        contents= self.employee_table.item(cursor_row)
        row = contents["values"]

        if row:
            self.id_entry.delete(0,END)
            self.id_entry.insert(END,row[0])
            self.name_entry.delete(0,END)
            self.name_entry.insert(END,row[1])
            self.combo_position.set(row[2])
            self.combo_gender.set(row[3])
            self.salary_entry.delete(0,END)
            self.salary_entry.insert(END,row[4])
#-------------------------------------------------------------------------------------------------------------------------------
    def update_employee(self):
        
        if not self.id_entry.get():
            messagebox.showerror("Warining", "please select employee to update ")
            return
        
        id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        position = self.combo_position.get().strip()
        gender = self.combo_gender.get().strip()
        salary = self.salary_entry.get().strip()

        if not (id and name and position and gender and salary ):
            messagebox.showerror("Error", "Please Fill All Fields")
            return
        
        try:
            self.db.update_employee(id,name,position,gender,salary)
            messagebox.showinfo("Success", "Employee updated successfully")
            self.fetch_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error while updating employee: {e}")
#-----------------------------------------------------------------------------------------------------------------------------------
    def delete_employee(self):

        id= self.id_entry.get().strip()
        if not id:
            messagebox.showerror("Warning","Please Select Employee to delete")
            return
        
        confirm = messagebox.askyesno ("Confirm","Are You Sure Want To Delete This Employee ?")

        if confirm:
            try:
                self.db.delete_employee(id)
                messagebox.showinfo("Error","Employee deleted successfully")
                self.fetch_data()
            except Exception as e:
                messagebox.showerror("Error", f"Error while deleting employee: {e}")
#----------------------------------------------------------------------------------------------------------------------------------------
    def delete_all_employees (self):
        
        confirm = messagebox.askyesno("Confrim","Are You Sure Want To Delete All Employees ?")
        
        if confirm:
            rows=self.db.get_employees()
            for row in rows :
                id = row[0]
                self.db.delete_employee(id)
            messagebox.showinfo("Success", "All employees deleted successfully")
            self.fetch_data()
#------------------------------------------------------------------------------------------------------------------------------------------
    def search_employee(self):

        category =self.combo_search.get().strip()
        keyword = self.search_entry.get().strip()

        if not (category and keyword):
            messagebox.showwarning("Warning", "Please select a category and enter a search keyword.")
            return
        
        query = "SELECT * FROM employees WHERE "

        if category.lower() == 'id':
            query += "id LIKE %s"
        elif category.lower() == 'name':
            query += "name LIKE %s"
        elif category.lower() == 'position':
            query += "position LIKE %s"
        else:
            messagebox.showwarning("Warning", "Invalid search category.")
            return
        
        try:
            self.employee_table.delete(*self.employee_table.get_children())
            self.db.cursor.execute(query, (f"%{keyword}%",))
            results = self.db.cursor.fetchall()
            for row in results:
                self.employee_table.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error while searching: {e}")
#---------------------------------------------------------------------------------------------------------------------------------------
    def show_all (self):

        self.fetch_data()
        self.combo_search.set("")
        self.search_entry.delete(0,END)
        