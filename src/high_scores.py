from database_connection import get_database_connection


class HighScores:
    """
    Handles interactions with the high scores database.

    Provides methods to add new scores and retrieve top scores.
    """
    def __init__(self):
        self._connection = get_database_connection()

    def add_score(self, name: str, score: int):
        """
        Adds a new high score to the database.

        Args:
            name (str): The name of the player.
            score (int): The score achieved by the player.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO highscores (name, score) VALUES (?, ?)",
            (name, score)
        )
        self._connection.commit()

    def get_top_scores(self, limit: int = 10):
        """
        Retrieves the top high scores from the database.

        Args:
            limit (int): The maximum number of top scores to retrieve (default is 10).

        Returns:
            list: A list of tuples, where each tuple contains (name, score)
                  for the top scores, ordered from highest to lowest score.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT name, score FROM highscores ORDER BY score DESC LIMIT ?",
            (limit,)
        )
        rows = cursor.fetchall()
        return [(row["name"], row["score"]) for row in rows]
