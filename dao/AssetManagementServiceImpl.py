from dao.AssetManagementService import AssetManagementService
from util.DBConnection import DBConnection
from entity.assets import assets
from entity.assetAllocation import assetAllocation
from entity.maintenanceRecords import maintenanceRecords
from entity.reservations import reservations
from exception.AssetManagementException import AssetManagementException

class AssetManagementServiceImpl(AssetManagementService):
    def __init__(self):
        self.connection = DBConnection.getConnection()

    def addAsset(self, asset: assets) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''INSERT INTO assets (asset_id, name, type, serial_number, purchase_date, location, status, owner_id)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            cursor.execute(query, asset.get_asset_id(), asset.get_name(), asset.get_type(), asset.get_serial_number(), 
                           asset.get_purchase_date(), asset.get_location(), asset.get_status(), asset.get_owner_id())
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Failed to add asset: {e}")

    def updateAsset(self, asset: assets) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''UPDATE assets SET name = ?, type = ?, serial_number = ?, purchase_date = ?, 
                       location = ?, status = ?, owner_id = ? WHERE asset_id = ?'''
            cursor.execute(query, asset.get_name(), asset.get_type(), asset.get_serial_number(), 
                           asset.get_purchase_date(), asset.get_location(), asset.get_status(), asset.get_owner_id(), 
                           asset.get_asset_id())
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Failed to update asset: {e}")

    def deleteAsset(self, assetId: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''DELETE FROM assets WHERE asset_id = ?'''
            cursor.execute(query, assetId)
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Failed to delete asset: {e}")

    def allocateAsset(self, assetId: int, employeeId: int, allocationDate: str) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''INSERT INTO assetAllocation (asset_id, employee_id, allocation_date) VALUES (?, ?, ?)'''
            cursor.execute(query, assetId, employeeId, allocationDate)
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Failed to allocate asset: {e}")

    def deallocateAsset(self, assetId: int, employeeId: int, returnDate: str) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''UPDATE assetAllocation SET return_date = ? WHERE asset_id = ? AND employee_id = ?'''
            cursor.execute(query, returnDate, assetId, employeeId)
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Failed to deallocate asset: {e}")

    def performMaintenance(self, assetId: int, maintenanceDate: str, description: str, cost: float) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''INSERT INTO maintenanceRecords (asset_id, maintenance_date, description, cost) 
                       VALUES (?, ?, ?, ?)'''
            cursor.execute(query, assetId, maintenanceDate, description, cost)
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Failed to perform maintenance: {e}")

    def reserveAsset(self, assetId: int, employeeId: int, reservationDate: str, startDate: str, endDate: str) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''INSERT INTO reservations (asset_id, employee_id, reservation_date, start_date, end_date, status) 
                       VALUES (?, ?, ?, ?, ?, ?)'''
            cursor.execute(query, assetId, employeeId, reservationDate, startDate, endDate, "Reserved")
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Failed to reserve asset: {e}")

    def withdrawReservation(self, reservationId: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''DELETE FROM reservations WHERE reservation_id = ?'''
            cursor.execute(query, reservationId)
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Failed to withdraw reservation: {e}")
