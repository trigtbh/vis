
# import psycopg2

# conn_uri = "postgres://avnadmin:AVNS_DyzcoS4HYJRuXlJCxuw@postgresql-terminal-suite-discord-terminal-suite-discord.a.aivencloud.com:15025/Discord?sslmode=require"


# def connect_to_db():
#     conn = psycopg2.connect(conn_uri)
#     conn.set_session(autocommit=True)
#     cur = conn.cursor()
#     return cur

# cur = connect_to_db()



import sqlite3, os

base = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(os.path.join(base, "viscord.db")):
    conn = sqlite3.connect("viscord.db")
    with open(os.path.join(base, "CreateDiscordDB.sql")) as f:
        conn.executescript(f.read())

def connect_to_db():
    conn = sqlite3.connect("viscord.db")
    cur = conn.cursor()
    return cur

cur = connect_to_db()