
from dao.AssetManagementServiceImpl import AssetManagementServiceImpl
from myexceptions.AssetNotFoundException import AssetNotFoundException
from myexceptions.AssetNotMaintainException import AssetNotMaintainException
from exception.AssetManagementException import AssetManagementException

def main():
    service = AssetManagementServiceImpl()

    try:
        # Example usage
        asset = service.getAssetById("some_invalid_id")
        print(asset)

        # Example maintenance operation
        service.performMaintenance("some_asset_id", "2024-10-15", "Routine check", 100.00)
        
    except AssetNotFoundException as e:
        print(e)
    except AssetNotMaintainException as e:
        print(e)
    except AssetManagementException as e:
        print(f"General Asset Management Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
