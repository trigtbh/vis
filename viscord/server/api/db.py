
import psycopg2

# conn_uri = "postgres://avnadmin:AVNS_DyzcoS4HYJRuXlJCxuw@postgresql-terminal-suite-discord-terminal-suite-discord.a.aivencloud.com:15025/Discord?sslmode=require"


import os
base = os.path.dirname(os.path.realpath(__file__))

conn_uri = "host='localhost' dbname='Discord' user='root' password='root'"

try:
    conn = psycopg2.connect(conn_uri)
    conn.set_session(autocommit=True)
    conn.cursor()
except:
    creation_uri = "host='localhost' dbname='postgres' user='root' password='root'"
    conn = psycopg2.connect(creation_uri)
    conn.set_session(autocommit=True)
    with open(os.path.join(base, "CreateDiscordDB.sql")) as f:
        conn.cursor().execute(f.read())

def connect_to_db():
    conn = psycopg2.connect(conn_uri)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    return cur

cur = connect_to_db()

