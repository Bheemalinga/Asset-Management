from dao.AssetManagementServiceImpl import AssetManagementServiceImpl
from exception.AssetNotFoundException import AssetNotFoundException
from exception.AssetNotMaintainedException import AssetNotMaintainedException
from exception.AssetManagementException import AssetManagementException
from entity.assets import assets

class AssetManagement:
    def __init__(self):
        self.database_handshake = AssetManagementServiceImpl()

    def display_menu(self):
        while True:
            print("\n--- Asset Management Menu ---")
            print("1. Add Asset")
            print("2. Update Asset")
            print("3. Delete Asset")
            print("4. Allocate Asset")
            print("5. Deallocate Asset")
            print("6. Perform Maintenance")
            print("7. Reserve Asset")
            print("8. Exit Application")

            choice = input("Choose an operation (1-8): ")

            try:
                if choice == '1':  # Add Asset
                    asset_id = input("Enter Asset ID: ")
                    name = input("Enter Asset Name: ")
                    asset_type = input("Enter Asset Type: ")
                    serial_number = input("Enter Serial Number: ")
                    purchase_date = input("Enter Purchase Date (YYYY-MM-DD): ")
                    location = input("Enter Location: ")
                    status = input("Enter Status: ")
                    owner_id = input("Enter Owner ID: ")

                    asset = assets(asset_id, name, asset_type, serial_number, purchase_date, location, status, owner_id)
                    self.database_handshake.addAsset(asset)
                    print("Asset added successfully.")

                elif choice == '2':  # Update Asset
                    asset_id = input("Enter Asset ID to update: ")
                    # Repeat input for other asset fields similar to Add Asset...
                    name = input("Enter Asset Name: ")
                    asset_type = input("Enter Asset Type: ")
                    serial_number = input("Enter Serial Number: ")
                    purchase_date = input("Enter Purchase Date (YYYY-MM-DD): ")
                    location = input("Enter Location: ")
                    status = input("Enter Status: ")
                    owner_id = input("Enter Owner ID: ")
                    # Create asset object and call service.updateAsset(asset)
                    asset = assets(asset_id, name, asset_type, serial_number, purchase_date, location, status, owner_id)
                    self.database_handshake.updateAsset(asset)
                    print("Asset updated successfully.")


                elif choice == '3':  # Delete Asset
                    asset_id = int(input("Enter Asset ID to delete: "))
                    self.database_handshake.deleteAsset(asset_id)
                    print("Asset deleted successfully.")

                elif choice == '4':  # Allocate Asset
                    asset_id = int(input("Enter Asset ID to allocate: "))
                    employee_id = int(input("Enter Employee ID: "))
                    allocation_date = input("Enter Allocation Date (YYYY-MM-DD): ")
                    self.database_handshake.allocateAsset(asset_id, employee_id, allocation_date)
                    print("Asset allocated successfully.")

                elif choice == '5':  # Deallocate Asset
                    asset_id = int(input("Enter Asset ID to deallocate: "))
                    employee_id = int(input("Enter Employee ID: "))
                    return_date = input("Enter Return Date (YYYY-MM-DD): ")
                    self.database_handshake.deallocateAsset(asset_id, employee_id, return_date)
                    print("Asset deallocated successfully.")

                elif choice == '6':  # Perform Maintenance
                    asset_id = int(input("Enter Asset ID for maintenance: "))
                    maintenance_date = input("Enter Maintenance Date (YYYY-MM-DD): ")
                    description = input("Enter Maintenance Description: ")
                    cost = float(input("Enter Maintenance Cost: "))
                    self.database_handshake.performMaintenance(asset_id, maintenance_date, description, cost)
                    print("Maintenance recorded successfully.")

                elif choice == '7':  # Reserve Asset
                    asset_id = int(input("Enter Asset ID to reserve: "))
                    employee_id = int(input("Enter Employee ID: "))
                    reservation_date = input("Enter Reservation Date (YYYY-MM-DD): ")
                    start_date = input("Enter Start Date (YYYY-MM-DD): ")
                    end_date = input("Enter End Date (YYYY-MM-DD): ")
                    self.database_handshake.reserveAsset(asset_id, employee_id, reservation_date, start_date, end_date)
                    print("Asset reserved successfully.")

                elif choice == '8':  # Exit Application
                    print("Exiting application.")
                    break

                else:
                    print("Invalid choice. Please select a valid operation.")

            except AssetNotFoundException as e:
                print(f"Asset not found: {e}")
            except AssetNotMaintainedException as e:
                print(f"Maintenance issue: {e}")
            except AssetManagementException as e:
                print(f"General Asset Management Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

def main():
    asset_manager = AssetManagement()
    asset_manager.display_menu()


if __name__ == "__main__":
    main()
