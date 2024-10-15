class employees:
    def __init__(self, employee_id = None, name = None, department = None, email = None, password = None):
        # Private attributes
        self.__employee_id = employee_id
        self.__name = name
        self.__department = department
        self.__email = email
        self.__password = password

    # Getter methods
    def get_employee_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password


    # Setter methods
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_name(self, name):
        self.__name = name

    def set_department(self, department):
        self.__department = department

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    # Method to return the object as a dictionary
    def __str__(self):
        return (f"Employee ID: {self.__employee_id}|| Name: {self.__name}|| Department: {self.__department}|| Email: {self.__email}|| Password: {self.__password}")