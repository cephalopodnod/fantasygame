import pymysql

def run_query(database, query, parameters=None, fetch=True):
    """
    Execute a MySQL query and return results as a list of dictionaries.

    Args:
        database: An open PyMySQL connection object (configured with DictCursor).
        query (str): The SQL query to execute.
        parameters (tuple or dict, optional): Query parameters to prevent SQL injection.
        fetch (bool): If True, return fetched results; if False, return None (for INSERT/UPDATE).

    Returns:
        list: List of dictionaries (rows) if fetch=True, else None.
        None: On error or if fetch=False and query executes successfully.

    Raises:
        pymysql.Error: If the query fails and the error needs to be handled upstream.
    """
    try:
        # Ensure cursor uses DictCursor for dictionary output
        with database.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query, parameters)
            
            if fetch:
                result = cursor.fetchall()  # Returns list of dicts with DictCursor
                return result if result else []  # Return empty list if no rows
            else:
                database.commit()  # Commit changes for non-fetch queries (e.g., INSERT)
                return None

    except pymysql.Error as e:
        print(f"Error executing query: {e}")
        raise  # Re-raise the exception for caller to handle if needed

    finally:
        connection.close()
        print("Connection closed.")