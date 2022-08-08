import sqlite3

class databaseUtilities:
    def createDatabase(self, fileDir):
        self.connection = sqlite3.connect(fileDir)
        self.cursor = self.connection.cursor()
        print(f"Database...Done")
        return self.connection, self.cursor

    def drawTable(self, table_name, query):
        try:
            doesTableExist = self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'").fetchall()
            if doesTableExist == []:
                self.cursor.execute(f"CREATE TABLE {table_name} {query}")
        except OSError as error:
            print(f"Error: '{error}'")

    def insertIntoTable(self, table_name, query, values):
        try:
            self.cursor.execute(f"INSERT or REPLACE INTO {table_name} {query}", values)
            self.connection.commit()
        except OSError as error:
            print(f"Error: '{error}'")

    def getData(self, query):
        try:
            self.cursor.execute(query)
            return [list(row) for row in self.cursor.fetchall()]
        except OSError as error:
            print(f"Error: '{error}'")
