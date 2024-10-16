class assetAllocation:
    def __init__(self, allocation_id = None,asset_id = None,employee_id = None,allocation_date = None,return_date = None):
        # Private attributes
        self.__allocation_id = allocation_id
        self.__asset_id = asset_id
        self.__employee_id = employee_id
        self.__allocation_date = allocation_date
        self.__return_date = return_date

    # Getter methods
    def get_allocation_id(self):
        return self.__allocation_id

    def get_asset_id(self):
        return self.__asset_id

    def get_employee_id(self):
        return self.__employee_id

    def get_allocation_date(self):
        return self.__allocation_date

    def get_return_date(self):
        return self.__return_date

    # Setter methods
    def set_allocation_id(self, allocation_id):
        self.__allocation_id = allocation_id

    def set_asset_id(self, asset_id):
        self.__asset_id = asset_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_allocation_date(self, allocation_date):
        self.__allocation_date = allocation_date

    def set_return_date(self, return_date):
        self.__return_date = return_date

    # Method to return the object as a dictionary
    def __str__(self):
        return (f"Allocation ID: {self.__allocation_id}|| Asset ID: {self.__asset_id}|| Employee ID: {self.__employee_id}|| Allocation Date: {self.__allocation_date}|| Return Date: {self.__return_date}")