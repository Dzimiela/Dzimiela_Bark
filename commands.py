import sys
import sqlite3
from datetime import datetime

from database import DatabaseManager

db = DatabaseManager('bookmarks.db')  # <1>


class CreateBookmarksTableCommand:
    def execute(self):  # <2>
        # Create cursor object
        cur = con.cursor()
 
        cur._execute("""SELECT title
                          ,id
                   FROM * bookmarks
                   WHERE title = self""",
                (self))
                

    # Fetch one result from the query because it
    # doesn't matter how many records are returned.
    # If it returns just one result, then you know
    # that a record already exists in the table.
    # If no results are pulled from the query, then
    # fetchone will return None.
        result = cur.fetchone()

        if result: # Do something that tells the user that email/user handle already exists
            return 'Record already exists!'
        
        else:
            db.create_table('bookmarks', {  # <3>
            'id': 'integer primary key autoincrement',
            'title': 'text not null',
            'url': 'text not null',
            'notes': 'text',
            'date_added': 'text not null',
            })


class AddBookmarkCommand:
    def execute(self, data):
        data['date_added'] = datetime.utcnow().isoformat()  # <1>
        db.add('bookmarks', data)  # <2>
        return 'Bookmark added!'  # <3>


class ListBookmarksCommand:
    def __init__(self, order_by='date_added'):  # <1>
        self.order_by = order_by

    def execute(self):
        return db.select('bookmarks', order_by=self.order_by).fetchall()  # <2>


class DeleteBookmarkCommand:
    def execute(self, data):
        db.delete('bookmarks', {'id': data})  # <1>
        return 'Bookmark deleted!'


class QuitCommand:
    def execute(self):
        sys.exit()  # <1>