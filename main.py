import sqlite3


class Album:
    def __init__(self, album_id, title, artist_id):
        self.artist_id = artist_id
        self.title = title
        self.album_id = album_id

    def __str__(self) -> str:
        return f'{self.album_id}, {self.title}, {self.artist_id}'

    def __repr__(self) -> str:
        return self.__str__()


class AlbumDAO:
    def __init__(self):
        self.conn = sqlite3.connect('Chinook_Sqlite.sqlite')
        self.cursor = self.conn.cursor()

    def find_all(self):
        self.album_list = []
        self.cursor.execute("SELECT * FROM Album")
        results = self.cursor.fetchall()
        for row in results:
            self.album_list.append(Album(row[0], row[1], row[2]))
        return self.album_list

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    album_db = AlbumDAO()
    print(album_db.find_all())
    album_db.close()









