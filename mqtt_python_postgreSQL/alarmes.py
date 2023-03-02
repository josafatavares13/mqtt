import json
import os
import psycopg2
import paho.mqtt.client as mqtt
import uuid
from os.path import join


json_path = join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
with open(json_path, 'r') as config_file:
    config = json.load(config_file)

HOST = config['mqtt']['host']
PORT = config['mqtt']['port']
TOPIC_ALARMES = config['mqtt']['topics4']
CLIENT_ID = str(uuid.uuid1())
DATABASE = config['database']['name']
USERDB = config['database']['user']
PASSDB = config['database']['password']
HOSTDB = config['database']['host']


print("Iniciando")
print("Connecting to broker with client ID '{}'...".format(CLIENT_ID))


def connect_mqtt() -> mqtt.Client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect!\n")
            
    client = mqtt.Client(CLIENT_ID, clean_session=False)
    #client.username_pw_set(USER, PASSWD)
    client.on_connect = on_connect
    client.connect(HOST, PORT)
    return client


def subscribe(client: mqtt.Client):
    values = {topic: None for topic in TOPIC_ALARMES}

    def on_message(client, userdata, msg):
        topic = msg.topic
        value = json.loads(msg.payload.decode())['value']
        if topic == TOPIC_ALARMES[0]:
            try:
                connection = psycopg2.connect(host=HOSTDB, database=DATABASE, user=USERDB, password=PASSDB)
                postgresql_insert_query = f"INSERT INTO alarme01_bateria (temperatura_alta_na_carga) VALUES ({value})"
                cursor = connection.cursor()
                cursor.execute(postgresql_insert_query)
                connection.commit()
                print(cursor.rowcount, "Data entered successfully")
                cursor.close()
                connection.close()
                print("Closed connection")
            except (Exception, psycopg2.DatabaseError) as error:
                print("Database failure".format(error))
        elif topic == TOPIC_ALARMES[1]:
            try:
                connection = psycopg2.connect(host=HOSTDB, database=DATABASE, user=USERDB, password=PASSDB)
                postgresql_insert_query = f"INSERT INTO alarme02_bateria (temperatura_baixa_na_carga) VALUES ({value})"
                cursor = connection.cursor()
                cursor.execute(postgresql_insert_query)
                connection.commit()
                print(cursor.rowcount, "Data entered successfully")
                cursor.close()
                connection.close()
                print("Closed connection")
            except (Exception, psycopg2.DatabaseError) as error:
                print("Database failure".format(error))
        elif topic == TOPIC_ALARMES[2]:
            try:
                connection = psycopg2.connect(host=HOSTDB, database=DATABASE, user=USERDB, password=PASSDB)
                postgresql_insert_query = f"INSERT INTO alarme03_bateria (temperatura_alta) VALUES ({value})"
                cursor = connection.cursor()
                cursor.execute(postgresql_insert_query)
                connection.commit()
                print(cursor.rowcount, "Data entered successfully")
                cursor.close()
                connection.close()
                print("Closed connection")
            except (Exception, psycopg2.DatabaseError) as error:
                print("Database failure".format(error))
        elif topic == TOPIC_ALARMES[3]:
            try:
                connection = psycopg2.connect(host=HOSTDB, database=DATABASE, user=USERDB, password=PASSDB)
                postgresql_insert_query = f"INSERT INTO alarme04_bateria (temperatura_baixa) VALUES ({value})"
                cursor = connection.cursor()
                cursor.execute(postgresql_insert_query)
                connection.commit()
                print(cursor.rowcount, "Data entered successfully")
                cursor.close()
                connection.close()
                print("Closed connection")
            except (Exception, psycopg2.DatabaseError) as error:
                print("Database failure".format(error))

    print('Alarmes')
    
    for topic in TOPIC_ALARMES:
        client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
