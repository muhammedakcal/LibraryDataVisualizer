# main.py

from utils.query_executor import QueryExecutor

def main():
    query_executor = QueryExecutor()
    test_query = "SELECT * FROM your_table LIMIT 5"  # Replace with your actual query

    # Execute the query and handle results within the execute_query method
    query_executor.execute_query(test_query)

if __name__ == '__main__':
    main()
