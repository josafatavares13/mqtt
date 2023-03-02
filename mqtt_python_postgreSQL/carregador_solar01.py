import json
import os
import psycopg2
import paho.mqtt.client as mqtt
import uuid
from os.path import join
import time

json_path = join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
with open(json_path, 'r') as config_file:
    config = json.load(config_file)

HOST = config['mqtt']['host']
PORT = config['mqtt']['port']
TOPIC_CARREGADOR_SOLAR01 = config['mqtt']['topics6']
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
    values = {topic: None for topic in TOPIC_CARREGADOR_SOLAR01}

    def on_message(client, userdata, msg):
        topic = msg.topic
        value = json.loads(msg.payload.decode())['value']
        values[topic] = value
        if all(values.values()):
            try:
                connection = psycopg2.connect(host=HOSTDB, database=DATABASE, user=USERDB, password=PASSDB)
                corrente_pv_solarcharger1 = values[TOPIC_CARREGADOR_SOLAR01[0]] / values[TOPIC_CARREGADOR_SOLAR01[1]]
                postgresql_insert_query = f"INSERT INTO carregador_solar01 (potencia_pv_solarcharger1, tensao_pv_solarcharger1, corrente_pv_solarcharger1) VALUES ({values[TOPIC_CARREGADOR_SOLAR01[0]]}, {values[TOPIC_CARREGADOR_SOLAR01[1]]}, {corrente_pv_solarcharger1})"
                cursor = connection.cursor()
                cursor.execute(postgresql_insert_query)
                connection.commit()
                print(cursor.rowcount, "Data entered successfully")
                cursor.close()
                connection.close()
                print("Closed connection")
            except (Exception, psycopg2.DatabaseError) as error:
                print("Database failure".format(error))
        
    print('Carregador solar 01')
    for topic in TOPIC_CARREGADOR_SOLAR01:
        client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()