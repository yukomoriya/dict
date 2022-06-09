import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="database",
   user="user",
   password="abc123"
)

print("You can choose different commands so as list, add, delete and quit")
## read_dict: returns the list of all dictionary entries:
# argument: conn - the database connection.
# Adding more comments about read_dic like reading means listing all the words from dictionary
    
def read_dict(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
# add_word: adds word and translation into dictionary
def add_word(conn, word, translation):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
# delete_word: delets word with id
def delete_word(conn, ID):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
#save_dict: save dictionary and commit
def save_dict(conn):
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close()


def main():
    while True: ## REPL - Read Execute Program Loop
        cmd = input("Command: ")
        if cmd == "list":
            print(read_dict(conn))
        elif cmd == "add":
            name = input("  Word: ")
            phone = input("  Translation: ")
            add_word(conn, name, phone)
            print(f"Added word {word}")
        elif cmd == "delete":
            ID = input("  ID: ")
            delete_word(conn, ID)
            print(f"Deleted word {ID}")
        elif cmd == "quit":
            save_dict(conn)
            print("Program quits")
            break

main()
