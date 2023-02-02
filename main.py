import sqlite3


if __name__ == '__main__':
    conn = sqlite3.connect('Chinook_Sqlite.sqlite')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Artist")
    results = cursor.fetchall()
    print(results)
    conn.close()



