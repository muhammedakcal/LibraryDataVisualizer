# utils/query_executor.py

from db.database_manager import DatabaseManager


class QueryExecutor:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def execute_query(self, query, is_select=True):

        try:
            self.db_manager.connect()
            results = None

            # Execute the query
            with self.db_manager.connection.cursor() as cursor:
                cursor.execute(query)

                # Fetch results for SELECT queries
                if is_select:
                    results = cursor.fetchall()
                    if results:
                        for row in results:
                            print(row)
                    else:
                        print("No data returned from the database.")
                else:
                    # Commit changes for non-SELECT queries
                    self.db_manager.connection.commit()

            return results

        except Exception as e:
            print(f"An error occurred while executing the query: {e}")
            return None

        finally:
            # Ensure the database connection is closed
            self.db_manager.close_connection()
