import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="database",
   user="user",
   password="abc123"
)


## read_dict: returns the list of all dictionary entries:
# argument: C - the database connection.
# Adding more comments about read_dic like reading means listing all the words from dictionary

def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
# add_word: adds word and translation into dictionary
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
# delete_word: delets word with id
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
#save_dict: save dictionary and commit
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()

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
        exit()
