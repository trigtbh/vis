import psycopg2
import datetime
import random
from uuid import uuid4
from typing import Optional, Dict

conn_uri="postgres://avnadmin:AVNS_DyzcoS4HYJRuXlJCxuw@postgresql-terminal-suite-discord-terminal-suite-discord.a.aivencloud.com:15025/Discord?sslmode=require"

def connect_to_db():
    conn = psycopg2.connect(conn_uri)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    return cur

cur = connect_to_db()

def get_server_perms(user_id:str, server_id: str):
    member_query="""select roles_list from "Discord"."MemberInfo" where user_id = %s and server_id= %s"""
    cur.execute(member_query, (user_id, server_id))
    roles_list= cur.fetchall()[0][0]

    perms={"manage_server":False, "manage_chats":False, "manage_members":False, "manage_roles":False, "manage_voice":False,  
           "manage_messages":False, "is_admin":False}
    list_perms=list(perms.items())

    # Getting all the perms based on the list of roles and updating the dict (which combines all the perms of all the roles the user has)

    for role_id in roles_list:
        perm_query="""select manage_server, manage_chats, manage_members, manage_roles, manage_voice, manage_messages, is_admin from "Discord"."RolesInfo" where role_id = %s"""
        cur.execute(perm_query, (role_id,))
        perm_arr=cur.fetchall()[0]
        
        # Checking to see if a role has a permission that isn't already true in the dict

        for i in range(0,len(perm_arr)):
            if not perms[list_perms[i][0]] and perm_arr[i]:
                perms[list_perms[i][0]]=True
    
    # If the user is an admin, all perms should be true

    if perms["is_admin"]:
        for key in perms:
            perms[key]=True
    
    return perms

#test method to create server - just so I can test building a chat out of that server
def test_server_creation(data):
    server_id = str(uuid4())
    print("Server ID: " + server_id)
    server_timestamp = str(datetime.datetime.now())
    server_name = None
    server_icon = None
    server_color = None
    if data is None:
        server_id = server_id
        server_name = "test_server"
        server_icon = random.choice("☀☁★☾♥♠♦♣♫☘☉☠")
        server_color = "#ffffff"
    else:
        server_name = data["server_name"]
        server_icon = data["server_symbol"]
        server_color = data["server_color"]

    send_query='''
        INSERT into "Discord"."ServerInfo" (server_id, server__name, color, server_icon, server_creation_timestamp) values (%s, %s, %s, %s, %s)
    '''
    cur.execute(send_query, (server_id, server_name, server_color, server_icon, server_timestamp))

#creates chat given the chat data - if data is null will create a test chat with preset information
def handle_chat_creation(data: Optional[Dict[str, str]]):
    chat_id = str(uuid4())
    if data is None:
        server_id = input("Enter server id: ")
        chat_name = "test_chat"
        chat_type = "public" 
        chat_topic = "chat description"
        chat_order = 0  
        read_perm_level = 1  
        write_perm_level = 1
        is_dm = False
    else:
        server_id = data["server_id"]
        chat_name = data["chat_name"]
        chat_type = data["chat_type"]
        chat_topic = data["chat_topic"]
        chat_order = data["chat_order"]
        read_perm_level = data["read_perm_level"]
        write_perm_level = data["write_perm_level"]
        is_dm = data["is_dm"]

    print("Chat ID: " + chat_id)
    send_query='''
        INSERT INTO "Discord"."ChatInfo" 
        (chat_id, server_id, chat_name, chat_type, chat_topic, chat_order, read_perm_level, write_perm_level, is_dm)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    cur.execute(send_query, (chat_id, server_id, chat_name, chat_type, chat_topic, chat_order, read_perm_level, write_perm_level, is_dm))

def handle_chat_name_update(user_id: str, server_id: str, chat_id: str, new_chat_name: str) -> None:
    """
    Update the name of a chat in the database given the chat's id. It first checks whether
    the user making the request has the necessary permissions to manage the chat. If the user does not have
    permission, it prints a message indicating so and returns without updating the database.

    Parameters:
        user_id (str): The id of the user making the request.
        server_id (str): The id of the server the chat is in.
        chat_id (str): The id of the chat whose name is to be updated.
        new_chat_name (str): The new name for the chat.

    Returns:
        None
    """

    perms = get_server_perms(user_id, server_id)

    if not perms["manage_chats"]:
        print("You do not have permission to change the chat name")
        return
    
    send_query = '''
        UPDATE "Discord"."ChatInfo"
        SET chat_name = %s
        WHERE chat_id = %s
    '''    
    cur.execute(send_query, (new_chat_name, chat_id))

def handle_chat_topic_update(user_id: str, server_id: str, chat_id: str, new_chat_topic: str) -> None:
    """
    Update the topic of a chat in the database given the chat's id. It first checks whether
    the user making the request has the necessary permissions to manage the chat. If the user does not have
    permission, it prints a message indicating so and returns without updating the database.

    Parameters:
        user_id (str): The id of the user making the request.
        server_id (str): The id of the server the chat is in.
        chat_id (str): The id of the chat whose topic is to be updated.
        new_chat_topic (str): The new topic for the chat.

    Returns:
        None
    """

    perms = get_server_perms(user_id, server_id)

    if not perms["manage_chats"]:
        print("You do not have permission to change the chat topic")
        return

    send_query = '''
        UPDATE "Discord"."ChatInfo"
        SET chat_topic = %s
        WHERE chat_id = %s
    '''    
    cur.execute(send_query, (new_chat_topic, chat_id))

def handle_chat_order_update(user_id: str, server_id: str, chat_id: str, new_chat_order: int) -> None:
    """
    Update the order of a chat in the database given the chat's id. It first checks whether
    the user making the request has the necessary permissions to manage the chat. If the user does not have
    permission, it prints a message indicating so and returns without updating the database.

    Parameters:
        user_id (str): The id of the user making the request.
        server_id (str): The id of the server the chat is in.
        chat_id (str): The id of the chat whose order is to be updated.
        new_chat_order (int): The new order placement for the chat.

    Returns:
        None
    """

    perms = get_server_perms(user_id, server_id)

    if not perms["manage_chats"]:
        print("You do not have permission to change the chat prder")
        return

    send_query = '''
        UPDATE "Discord"."ChatInfo"
        SET chat_order = %s
        WHERE chat_id = %s
    '''    
    cur.execute(send_query, (new_chat_order, chat_id))

def handle_chat_deletion(user_id: str, server_id: str, chat_id: str):
    """
    Deletes the chat in the database given the chat's id. It first checks whether
    the user making the request has the necessary permissions to manage the chat. If the user does not have
    permission, it prints a message indicating so and returns without updating the database.

    Parameters:
        user_id (str): The id of the user making the request.
        server_id (str): The id of the server the chat is in.
        chat_id (str): The id of the chat whose order is to be updated.

    Returns:
        None
    """

    perms = get_server_perms(user_id, server_id)

    if not perms["manage_chats"]:
        print("You do not have permission to delete the chat")
        return
    
    send_query = '''
        DELETE FROM "Discord"."ChatInfo"
        WHERE chat_id = %s AND server_id = %s
    '''    

    cur.execute(send_query, (chat_id, server_id))

def test_retrieve_chat_information(chat_id: str) -> None:
    """
    Retrieve information about a chat from the database given the chat's id.

    Parameters:
        chat_id (str): The id of the chat to retrieve information for.

    Returns:
        None
    """
    send_query = '''
        SELECT * FROM "Discord"."ChatInfo"
        WHERE chat_id = %s
    '''
    cur.execute(send_query, (chat_id,))
    records = cur.fetchall()
    if records:
        print("Chat Information:")
        for result in records:
            print("Chat ID:", result[0])
            print("Server ID:", result[1])
            print("Chat Name:", result[2])
            print("Chat Type:", result[3])
            print("Chat Topic:", result[4])
            print("Chat Order:", result[5])
            print("Read Permission Level:", result[6])
            print("Write Permission Level:", result[7])
            print("Is DM:", result[8])
            print("--------------------------------")
    else:
        print("Chat not found")

test_server_creation(None)
handle_chat_creation(None)
chat_id = input("Enter chat id: ")
test_retrieve_chat_information(chat_id)
print()
print("Updating chat name...")
print()
handle_chat_name_update(chat_id, "NEWNAME")
print()
print("Updating chat topic...")
print()
handle_chat_topic_update(chat_id, "NEW TOPIC")
print()
print("Updating chat order...")
print()
handle_chat_order_update(chat_id, 3)
test_retrieve_chat_information(chat_id)
