import json
import os
import psycopg2
import paho.mqtt.client as mqtt
import uuid
from os.path import join
import datetime

json_path = join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
with open(json_path, 'r') as config_file:
    config = json.load(config_file)

HOST = config['mqtt']['host']
PORT = config['mqtt']['port']
TOPIC_FRONIUS = config['mqtt']['topics']
CLIENT_ID = str(uuid.uuid1())
DATABASE = config['database']['name']
USERDB = config['database']['user']
PASSDB = config['database']['password']
HOSTDB = config['database']['host']
last_value_time = datetime.datetime.now()

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
    values = {topic: None for topic in TOPIC_FRONIUS}

    def on_message(client, userdata, msg):
        connection = psycopg2.connect(host=HOSTDB, database=DATABASE, user=USERDB, password=PASSDB)
        cursor = connection.cursor()
        cursor.execute("SELECT set_zero_if_idle()")
        connection.commit()
        cursor.close()
        connection.close()
        
        topic = msg.topic
        value = json.loads(msg.payload.decode())['value']
        values[topic] = value
        global last_value_time
        if (datetime.datetime.now() - last_value_time).total_seconds() >= 120:
            if all(values.values()):
                try:
                    connection = psycopg2.connect(host=HOSTDB, database=DATABASE, user=USERDB, password=PASSDB)
                    postgresql_insert_query = f"INSERT INTO fronius (potencia_total_ac, energia_total_ac, potencia_ac_l1, energia_ac_l1, tensao_ac_l1, corrente_ac_l1, potencia_ac_l2, energia_ac_l2, tensao_ac_l2, corrente_ac_l2, potencia_ac_l3, energia_ac_l3, tensao_ac_l3, corrente_ac_l3, potencia_injetadas_na_rede_l1, potencia_injetadas_na_rede_l2, potencia_injetadas_na_rede_l3 ) VALUES ({values[TOPIC_FRONIUS[0]]}, {values[TOPIC_FRONIUS[1]]}, {values[TOPIC_FRONIUS[2]]}, {values[TOPIC_FRONIUS[3]]}, {values[TOPIC_FRONIUS[4]]}, {values[TOPIC_FRONIUS[5]]}, {values[TOPIC_FRONIUS[6]]}, {values[TOPIC_FRONIUS[7]]}, {values[TOPIC_FRONIUS[8]]}, {values[TOPIC_FRONIUS[9]]}, {values[TOPIC_FRONIUS[10]]}, {values[TOPIC_FRONIUS[11]]}, {values[TOPIC_FRONIUS[12]]}, {values[TOPIC_FRONIUS[13]]}, {values[TOPIC_FRONIUS[14]]}, {values[TOPIC_FRONIUS[15]]}, {values[TOPIC_FRONIUS[16]]})"
                    cursor = connection.cursor()
                    cursor.execute(postgresql_insert_query)
                    connection.commit()
                    print(cursor.rowcount, "Data entered successfully")
                    cursor.close()
                    connection.close()
                    print("Closed connection")
                    print( {values[TOPIC_FRONIUS[4]]})
                    last_value_time = datetime.datetime.now()
                except (Exception, psycopg2.DatabaseError) as error:
                    print("Database failure".format(error))
        
    print('Fronius')
    for topic in TOPIC_FRONIUS:
        client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()  
    subscribe(client)
    client.loop_forever()
    


if __name__ == '__main__':
    while True:
        run()