from abc import ABC
from dao.AssetManagementService import AssetManagementService
from util.DBConnection import DBConnection
from entity.assets import assets
from entity.assetAllocation import assetAllocation
from entity.maintenanceRecords import maintenanceRecords
from entity.reservations import reservations
from myexceptions.AssetNotFoundException import AssetNotFoundException
from myexceptions.AssetNotMaintainException import AssetNotMaintainException
from exception.AssetManagementException import AssetManagementException
import datetime

class AssetManagementServiceImpl(AssetManagementService, ABC):
    def __init__(self):
        self.connection = DBConnection.getConnection()

    def addAsset(self, asset: assets) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''INSERT INTO assets (asset_id, name, type, serial_number, purchase_date, location, status, owner_id) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            cursor.execute(query, asset.get_asset_id(), asset.get_name(), asset.get_type(),
                           asset.get_serial_number(), asset.get_purchase_date(), asset.get_location(),
                           asset.get_status(), asset.get_owner_id())
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Error adding asset: {e}")

    def updateAsset(self, asset: assets) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''UPDATE assets SET name=?, type=?, serial_number=?, purchase_date=?, 
                       location=?, status=?, owner_id=? WHERE asset_id=?'''
            cursor.execute(query, asset.get_name(), asset.get_type(), asset.get_serial_number(),
                           asset.get_purchase_date(), asset.get_location(), asset.get_status(),
                           asset.get_owner_id(), asset.get_asset_id())
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Error updating asset: {e}")

    def deleteAsset(self, assetId: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''DELETE FROM assets WHERE asset_id=?'''
            cursor.execute(query, assetId)
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Error deleting asset: {e}")

    def allocateAsset(self, assetId: int, employeeId: int, allocationDate: str) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''INSERT INTO assetAllocation (allocation_id, asset_id, employee_id, allocation_date) 
                       VALUES (?, ?, ?, ?)'''
            allocation_id = f"AL-{allocationDate}-{assetId}"
            cursor.execute(query, allocation_id, assetId, employeeId, allocationDate)
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Error allocating asset: {e}")

    def deallocateAsset(self, assetId: int, employeeId: int, returnDate: str) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''UPDATE assetAllocation SET return_date=? WHERE asset_id=? AND employee_id=? AND return_date IS NULL'''
            cursor.execute(query, returnDate, assetId, employeeId)
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Error deallocating asset: {e}")

    def performMaintenance(self, assetId: int, maintenanceDate: str, description: str, cost: float) -> bool:
        try:
            cursor = self.connection.cursor()
            # Check if the asset has been maintained for more than 2 years
            query = '''SELECT maintenance_date FROM maintenanceRecords WHERE asset_id = ? ORDER BY maintenance_date DESC'''
            cursor.execute(query, assetId)
            last_maintenance_date = cursor.fetchone()
            
            if last_maintenance_date:
                # Assuming last_maintenance_date is a date object
                if (datetime.datetime.now().date() - last_maintenance_date[0]).days < 730:  # 2 years
                    raise AssetNotMaintainException(f"Asset ID {assetId} has not been maintained for more than 2 years.")

            # If passed, perform maintenance
            query = '''INSERT INTO maintenanceRecords (asset_id, maintenance_date, description, cost) 
                       VALUES (?, ?, ?, ?)'''
            cursor.execute(query, assetId, maintenanceDate, description, cost)
            self.connection.commit()
            return True
        except AssetNotMaintainException:
            raise
        except Exception as e:
            raise AssetManagementException(f"Failed to perform maintenance: {e}")

    def reserveAsset(self, assetId: int, employeeId: int, reservationDate: str, startDate: str, endDate: str) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''INSERT INTO reservations (reservation_id, asset_id, employee_id, reservation_date, start_date, end_date, status) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)'''
            reservation_id = f"RES-{reservationDate}-{assetId}"
            cursor.execute(query, reservation_id, assetId, employeeId, reservationDate, startDate, endDate, 'Reserved')
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Error reserving asset: {e}")

    def withdrawReservation(self, reservationId: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = '''DELETE FROM reservations WHERE reservation_id=?'''
            cursor.execute(query, reservationId)
            self.connection.commit()
            return True
        except Exception as e:
            raise AssetManagementException(f"Error withdrawing reservation: {e}")