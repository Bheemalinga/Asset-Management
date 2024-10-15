class AssetNotFoundException(Exception):
    def __init__(self, message="Asset not found in the database."):
        super().__init__(message)