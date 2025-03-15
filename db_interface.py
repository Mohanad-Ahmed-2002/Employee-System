from abc import ABC, abstractmethod

class IDatabase(ABC):

    @abstractmethod
    def connect(self):
        pass 

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def add_employee(self,id,name,position,gender,salary):
        pass

    @abstractmethod
    def update_employee(self,id,name,position,gender,salary):
        pass

    @abstractmethod
    def delete_employee(self,employee_id):
        pass

    @abstractmethod
    def get_employees(self):
        pass

    