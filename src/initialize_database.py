from database_connection import get_database_connection


def _drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS highscores;")
    connection.commit()


def _create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE highscores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL
        );
    """)
    connection.commit()


def initialize_database():
    """
    Initializes the database by dropping existing tables and creating new ones.

    Specifically, drops the 'highscores' table if it exists and then creates
    a new 'highscores' table.
    """
    connection = get_database_connection()
    _drop_tables(connection)
    _create_tables(connection)


if __name__ == "__main__":
    initialize_database()
