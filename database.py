import mysql.connector
from mysql.connector import Error

class DatabaseManager():

    def __init__(self,host='localhost',user='root',password='',database='ems_db'):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.conn=None
        self.cursor=None
        self.connect()
        self.create_table()
#function use to connect with database
    def connect(self):
        try:
                self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=3307
            )
                self.cursor = self.conn.cursor()
                print("Connected to MySQL database")
        except Error as e:
            print("Error while connecting to MySQL", e)
            raise
# function use to create table 
    def create_table(self):
        
        if self.cursor is None:
            print("المؤشر (cursor) غير معرف. لا يمكن إنشاء الجدول.")
            
        query = """ CREATE TABLE IF NOT EXISTS employees (
                    id INT  PRIMARY KEY,
                    name VARCHAR(255) NOT NULL ,
                    position VARCHAR (255),
                    gender VARCHAR(100),
                    salary DECIMAL(10,2)
                    )
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print("Employees table is ready")
        except Error as e:
            print("Error while creating table", e)
#function use to add employee 
    def add_employee(self,id,name,position,gender,salary): 
    
        query= " INSERT INTO employees (id,name,position,gender,salary) VALUES (%s,%s,%s,%s,%s)"
        value = (id,name,position,gender,salary)

        try:
            self.cursor.execute(query,value)
            self.conn.commit()
            print("Employee added successfully")
        except Error as e:
            print("Error while adding employee", e)
#function use to update employee 
    def update_employee (self,employee_id,name,position,gender,salary):

        query= "UPDATE employees SET name=%s, position=%s,gender=%s, salary=%s WHERE id=%s"
        value= (name,position,gender,salary,employee_id)

        try:
            self.cursor.execute(query,value)
            self.conn.commit()
            print("Update Employee Successfully")
        except Error as e:
            print("Error While Updating Employee",e)
#function use to delete employee
    def delete_employee(self,employee_id):
        query= "DELETE FROM employees WHERE id=%s"
        value=(employee_id,)

        try:
            self.cursor.execute(query,value)
            self.conn.commit()
            print("Delete Employee Successfully")
        except Error as e:
            print("Error While Delete Employee",e)
#function use to get all emoloyees
    def get_employees(self):

        query= "SELECT * FROM employees"

        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
        except Error as e:
            print("Error while fetching employees", e)
            return []
#function use to close connect with database
    def __del__(self):
        
        if self.conn:
            self.conn.close()
            print("MySQL connection is closed")