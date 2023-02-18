import time
from paho.mqtt import client as mqtt_client
import paho.mqtt.client as mqtt
import uuid
# Bibliotecas PostgreSql
import json
import psycopg2
  
HOST = "192.168.1.164"
PORT = 1883
TOPIC_FRONIUS = ["N/102c6b9d30f3/pvinverter/20/Ac/L1/Power", 
                "N/102c6b9d30f3/pvinverter/20/Ac/L1/Energy/Forward",
                "N/102c6b9d30f3/pvinverter/20/Ac/L1/Voltage",
                "N/102c6b9d30f3/pvinverter/20/Ac/L1/Current"] 
CLIENT_ID = str(uuid.uuid1())
DATABASE = 'mqtt'
USERDB = 'postgres'
PASSDB = 'postgres'
HOSTDB = 'localhost'

print("Iniciando")
print("Connecting to broker with client ID '{}'...".format(CLIENT_ID))

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect!\n")
    client = mqtt_client.Client(CLIENT_ID, clean_session=False)
    #client.username_pw_set(USER, PASSWD)
    client.on_connect = on_connect
    client.connect(HOST, PORT)
    return client

def subscribe(client: mqtt_client):
    values = {topic: None for topic in TOPIC_FRONIUS}

    def on_message(client, userdata, msg):
        topic = msg.topic
        value = json.loads(msg.payload.decode())['value']
        values[topic] = value
        if all(values.values()):
            try:
                connection = psycopg2.connect(host=HOSTDB, database=DATABASE, user=USERDB, password=PASSDB)
                postgresql_insert_query = f"INSERT INTO fase01_fronius (potencia_ac_l1, energia_ac_l1, tensao_ac_l1, corrente_ac_l1) VALUES ({values[TOPIC_FRONIUS[0]]}, {values[TOPIC_FRONIUS[1]]}, {values[TOPIC_FRONIUS[2]]}, {values[TOPIC_FRONIUS[3]]})"
                cursor = connection.cursor()
                cursor.execute(postgresql_insert_query)
                connection.commit()
                print(cursor.rowcount, "Data entered successfully")
                cursor.close()
                connection.close()
                print("Closed connection")
            except (Exception, psycopg2.DatabaseError) as error:
                print("Database failure".format(error))
            
        
    print('teste')
    for topic in TOPIC_FRONIUS:
        client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()



  