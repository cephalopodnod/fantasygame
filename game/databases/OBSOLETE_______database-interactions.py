#this is one method.
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


#this is another method, haven't decided yet, currentyl commented out.
# from http.server import HTTPServer, BaseHTTPRequestHandler

# class Server(BaseHTTPRequestHandler):
#     def do_Get(self):
#         if self.path == '/':
#             self.path = '/index.html'
#         try:
#             file_to_open = open(self.path[1:]).read()
#             self.send_response(200)
#         except:
#             file_to_open = 'File not found!'
#             self.send_response(404)
#         self.end_headers
#         self.wfile.write(bytes(file_to_open, 'utf-8'))

# httpd = HTTPServer(('localhost',8080), Server)
# httpd.serve_forever()


# this is to pull spell data from the D&D 5e API
# import requests

# def display_spell(spell_data):
#     print(f"Name: {spell_data['name']}")
#     print(f"Level: {spell_data['level']}")
#     print(f"Index: {spell_data['index']}")
#     print(f"URL: {spell_data['url']}")
#     print()

# def main():
#     url = "https://www.dnd5eapi.co/api/spells"
#     headers = {'Accept': 'application/json'}

#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         spells_data = response.json()
#         spells = spells_data['results']

#         print("Welcome to the D&D 5e Spellbook!")
#         print(f"Total Spells: {spells_data['count']}\n")

#         while True:
#             print("Commands:")
#             print("1 - List all spells")
#             print("2 - Search for a spell by name")
#             print("3 - Exit")

#             choice = input("Enter your choice: ")

#             if choice == '1':
#                 print("\nList of Spells:")
#                 for spell in spells:
#                     display_spell(spell)
#             elif choice == '2':
#                 spell_name = input("Enter the spell name: ").lower()
#                 matching_spells = [spell for spell in spells if spell_name in spell['name'].lower()]
#                 print("\nMatching Spells:")
#                 for spell in matching_spells:
#                     display_spell(spell)
#             elif choice == '3':
#                 print("Goodbye!")
#                 break
#             else:
#                 print("Invalid choice. Please select a valid option.")

# if __name__ == "__main__":
#     main()