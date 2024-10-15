class assets:
    def __init__(self, asset_id = None, name = None, type = None, serial_number = None, purchase_date = None, location = None, status = None, owner_id = None):
        # Private attributes
        self.__asset_id = asset_id
        self.__name = name
        self.__type = type
        self.__serial_number = serial_number
        self.__purchase_date = purchase_date
        self.__location = location
        self.__status = status
        self.__owner_id = owner_id

    # Getter methods
    def get_asset_id(self):
        return self.__asset_id

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_serial_number(self):
        return self.__serial_number

    def get_purchase_date(self):
        return self.__purchase_date

    def get_location(self):
        return self.__location

    def get_status(self):
        return self.__status

    def get_owner_id(self):
        return self.__owner_id

    # Setter methods
    def set_asset_id(self, asset_id):
        self.__asset_id = asset_id

    def set_name(self, name):
        self.__name = name

    def set_type(self, type):
        self.__type = type

    def set_serial_number(self, serial_number):
        self.__serial_number = serial_number

    def set_purchase_date(self, purchase_date):
        self.__purchase_date = purchase_date

    def set_location(self, location):
        self.__location = location

    def set_status(self, status):
        self.__status = status

    def set_owner_id(self, owner_id):
        self.__owner_id = owner_id

    # Method to return the object as a dictionary
    def __str__(self):
        return (f"Asset ID: {self.__asset_id}|| Name: {self.__name}|| Type: {self.__type}|| Serial Number: {self.__serial_number}|| Purchase Date: {self.__purchase_date}|| Location: {self.__location}|| Status: {self.__status}|| Owner ID: {self.__owner_id}")