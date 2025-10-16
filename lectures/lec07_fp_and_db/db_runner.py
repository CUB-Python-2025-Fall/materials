from pathlib import Path
import sqlite3

class DB:
    """Tiny helper to execute SQL files; reuses a single DB path."""
    def __init__(self, db_path="mini.db"):
        self.db_path = db_path

    def _connect(self):
        con = sqlite3.connect(self.db_path)
        con.execute("PRAGMA foreign_keys=ON")  # enable FK enforcement
        return con

    def run_file(self, path: str):
        """Executes the SQL script (may contain multiple statements)."""
        sql = Path(path).read_text(encoding="utf-8")
        with self._connect() as con:
            con.executescript(sql)

    def query_file(self, path: str):
        """Runs the script but returns rows from the LAST statement if it's a SELECT.
        Safe for scripts with multiple statements.        """
        sql = Path(path).read_text(encoding="utf-8")
        # Split into statements; execute all but last via executescript, then run last with execute
        statements = [s.strip() for s in sql.split(';') if s.strip()]
        if not statements:
            return []
        head = ';'.join(statements[:-1])
        last = statements[-1]
        with self._connect() as con:
            if head:
                con.executescript(head + ';')
            try:
                cur = con.execute(last)
                rows = cur.fetchall()
            except sqlite3.Error:
                # If last isn't a SELECT, just execute it and return empty list
                con.executescript(last + ';')
                rows = []
        return rows
