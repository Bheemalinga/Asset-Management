import pyodbc
from util.PropertyUtil import PropertyUtil

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            try:
                Credentials = PropertyUtil.getPropertyString()
                DBConnection.connection = pyodbc.connect(Credentials)
                print("\n\tPython and DB handshake Successful.")
            except Exception as e:
                print("Python - DB handshake failure : ",e)
        return DBConnection.connection