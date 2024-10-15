from abc import ABC, abstractmethod
from entity.assets import assets
from entity.assetAllocation import assetAllocation
from entity.employees import employees
from entity.maintenanceRecords import maintenanceRecords
from entity.reservations import reservations

class AssetManagementService(ABC):
    
    @abstractmethod
    def addAsset(self, asset: assets):
        """
        Adds a new asset to the system.
        :param asset: An instance of the 'assets' class.
        :return: True if asset is added successfully, False otherwise.
        """
        pass
    
    @abstractmethod
    def updateAsset(self, asset: assets):
        """
        Updates information about an existing asset.
        :param asset: An instance of the 'assets' class.
        :return: True if asset is updated successfully, False otherwise.
        """
        pass
    
    @abstractmethod
    def deleteAsset(self, assetId: int):
        """
        Deletes an asset from the system based on its ID.
        :param assetId: ID of the asset to be deleted.
        :return: True if asset is deleted successfully, False otherwise.
        """
        pass
    
    @abstractmethod
    def allocateAsset(self, assetId: int, employeeId: int, allocationDate: str):
        """
        Allocates an asset to an employee on a specified allocation date.
        :param assetId: ID of the asset to allocate.
        :param employeeId: ID of the employee to whom the asset will be allocated.
        :param allocationDate: The date on which the allocation is made.
        :return: True if the asset is allocated successfully, False otherwise.
        """
        pass
    
    @abstractmethod
    def deallocateAsset(self, assetId: int, employeeId: int, returnDate: str):
        """
        Deallocates an asset from an employee on a specified return date.
        :param assetId: ID of the asset to deallocate.
        :param employeeId: ID of the employee from whom the asset will be deallocated.
        :param returnDate: The date on which the asset is returned.
        :return: True if the asset is deallocated successfully, False otherwise.
        """
        pass
    
    @abstractmethod
    def performMaintenance(self, assetId: int, maintenanceDate: str, description: str, cost: float):
        """
        Records maintenance activity for an asset, including the date, description, and cost.
        :param assetId: ID of the asset to maintain.
        :param maintenanceDate: The date on which maintenance is performed.
        :param description: Description of the maintenance.
        :param cost: Cost of the maintenance.
        :return: True if maintenance is recorded successfully, False otherwise.
        """
        pass
    
    @abstractmethod
    def reserveAsset(self, assetId: int, employeeId: int, reservationDate: str, startDate: str, endDate: str):
        """
        Reserves an asset for a specified employee for a specific period.
        :param assetId: ID of the asset to reserve.
        :param employeeId: ID of the employee reserving the asset.
        :param reservationDate: The date on which the reservation is made.
        :param startDate: The start date of the reservation period.
        :param endDate: The end date of the reservation period.
        :return: True if the asset is reserved successfully, False otherwise.
        """
        pass
    
    @abstractmethod
    def withdrawReservation(self, reservationId: int):
        """
        Withdraws a reservation for an asset identified by the reservation ID.
        :param reservationId: ID of the reservation to withdraw.
        :return: True if the reservation is withdrawn successfully, False otherwise.
        """
        pass
