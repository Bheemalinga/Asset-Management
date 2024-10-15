"""
create table maintenanceRecords(
    maintenance_id varchar(10) primary key not null,
    asset_id varchar(10),
    maintenance_date date,
    description varchar(150),
    cost decimal(6, 2),
    foreign key (asset_id) references assets(asset_id)
);
"""
class maintenanceRecords:
    def __init__(self, maintenance_id = None, asset_id = None, maintenance_date = None, description = None, cost = None):
        # Private attributes
        self.__maintenance_id = maintenance_id
        self.__asset_id = asset_id
        self.__maintenance_date = maintenance_date
        self.__description = description
        self.__cost = cost

    # Getter methods
    def get_maintenance_id(self):
        return self.__maintenance_id

    def get_asset_id(self):
        return self.__asset_id

    def get_maintenance_date(self):
        return self.__maintenance_date

    def get_description(self):
        return self.__description

    def get_cost(self):
        return self.__cost

    # Setter methods
    def set_maintenance_id(self, maintenance_id):
        self.__maintenance_id = maintenance_id

    def set_asset_id(self, asset_id):
        self.__asset_id = asset_id

    def set_maintenance_date(self, maintenance_date):
        self.__maintenance_date = maintenance_date

    def set_description(self, description):
        self.__description = description

    def set_cost(self, cost):
        self.__cost = cost

    # Method to return the object as a dictionary
    def __str__(self):
        return (f"Maintenance ID: {self.__maintenance_id}|| Asset ID: {self.__asset_id}|| Maintenance Date: {self.__maintenance_date}|| Description: {self.__description}|| Cost: {self.__cost}")