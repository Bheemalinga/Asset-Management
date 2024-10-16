from dao.AssetManagementServiceImpl import AssetManagementServiceImpl
from exception.AssetNotFoundException import AssetNotFoundException
from exception.AssetNotMaintainedException import AssetNotMaintainedException
from exception.AssetManagementException import AssetManagementException
from entity.assets import assets

class AssetManagementApp:
    def __init__(self):
        self.database_handshake = AssetManagementServiceImpl()

    def display_menu(self):
        while True:
            print("\n -----> Asset Management Menu <-----\n\t1. Add Asset\n\t2. Update Asset\n\t3. Delete Asset\n\t4. Allocate Asset\n\t5. Deallocate Asset\n\t6. Perform Maintenance\n\t7. Reserve Asset\n\t8. Exit Application")
            print("<---------------------------------->\n")
            choice = input("\tChoose an operation (1-8): ")

            try:
                if choice == '1':  # Add Asset
                    asset_id = input("\nEnter Asset ID: ")
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
                    asset_id = input("\nEnter Asset ID to update: ")
                    name = input("Enter Asset Name: ")
                    asset_type = input("Enter Asset Type: ")
                    serial_number = input("Enter Serial Number: ")
                    purchase_date = input("Enter Purchase Date (YYYY-MM-DD): ")
                    location = input("Enter Location: ")
                    status = input("Enter Status: ")
                    owner_id = input("Enter Owner ID: ")
                    # asset object and calling service.updateAsset(asset)
                    asset = assets(asset_id, name, asset_type, serial_number, purchase_date, location, status, owner_id)
                    self.database_handshake.updateAsset(asset)
                    print("Asset updated successfully.")


                elif choice == '3':  # Delete Asset
                    asset_id = input("\nEnter Asset ID to delete: ")
                    self.database_handshake.deleteAsset(asset_id)
                    print("Asset deleted successfully.")

                elif choice == '4':  # Allocate Asset
                    asset_id = input("\nEnter Asset ID to allocate: ")
                    employee_id = input("Enter Employee ID: ")
                    allocation_date = input("Enter Allocation Date (YYYY-MM-DD): ")
                    self.database_handshake.allocateAsset(asset_id, employee_id, allocation_date)
                    print("Asset allocated successfully.")

                elif choice == '5':  # Deallocate Asset
                    asset_id = input("\nEnter Asset ID to deallocate: ")
                    employee_id = input("Enter Employee ID: ")
                    return_date = input("Enter Return Date (YYYY-MM-DD): ")
                    self.database_handshake.deallocateAsset(asset_id, employee_id, return_date)
                    print("Asset deallocated successfully.")

                elif choice == '6':  # Perform Maintenance
                    asset_id = input("\nEnter Asset ID for maintenance: ")
                    maintenance_date = input("Enter Maintenance Date (YYYY-MM-DD): ")
                    description = input("Enter Maintenance Description: ")
                    cost = float(input("Enter Maintenance Cost: "))
                    self.database_handshake.performMaintenance(asset_id, maintenance_date, description, cost)
                    print("Maintenance recorded successfully.")

                elif choice == '7':  # Reserve Asset
                    asset_id = input("\nEnter Asset ID to reserve: ")
                    employee_id = input("Enter Employee ID: ")
                    reservation_date = input("Enter Reservation Date (YYYY-MM-DD): ")
                    start_date = input("Enter Start Date (YYYY-MM-DD): ")
                    end_date = input("Enter End Date (YYYY-MM-DD): ")
                    self.database_handshake.reserveAsset(asset_id, employee_id, reservation_date, start_date, end_date)
                    print("Asset reserved successfully.")

                elif choice == '8':
                    print("\nExiting application.")
                    break

                else:
                    print("\nInvalid choice. Please select a valid operation.")

            except AssetNotFoundException as e:
                print(f"Asset not found: {e}")
            except AssetNotMaintainedException as e:
                print(f"Maintenance issue: {e}")
            except AssetManagementException as e:
                print(f"General Asset Management Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

def main():
    asset_manager = AssetManagementApp()
    asset_manager.display_menu()


if __name__ == "__main__":
    main()
