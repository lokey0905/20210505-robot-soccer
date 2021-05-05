import time
import paho.mqtt.client as paho     #MQTT Library
from botControl import run_ActionGroup
#MQTT的連線IP
broker = "broker.hivemq.com"#MQTT Broker
client = ''
NAME = 'unit1'              #MQTT客戶登入編號


#監聽頻道訊息
def on_message(client,userdata,message):
    time.sleep(1)
    mqttmsg = str(message.payload.decode("utf-8"))
    print("received message =",mqttmsg)
    #訊息接收控制
    if mqttmsg == 'w':
        run_ActionGroup('1',1)
    if mqttmsg == 's':
        run_ActionGroup('2',1)

client = paho.Client(NAME)
client.on_message=on_message
client.connect(broker)#connect
client.loop_start() #start loop to process received messages

#subscribe的頻道名稱
client.subscribe("playsub")
        
if __name__ == "__main__":
    print('press ctrl+c to stop......')
    while(1):
        time.sleep(2)
