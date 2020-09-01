import network
station = network.WLAN(network.STA_IF)
station.active(True)
#station.scan()

station.connect("SSID_WIFI", "SENHA_WIFI")
station.isconnected()
#station.ifconfig()

import urequests
response = urequests.get("http://teste.afonsomiguel.com")
print(response.text)

#--------------------------------------------------------

def conecta(ssid, senha):
    import network
    import time
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, senha)
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station

import urequests
print("Conectando...")
station = conecta("teste_wifi", "senha_teste_wifi")
if not station.isconnected():
    print("N‹o conectado!...")
else:
    print("Conectado!...")
    print("Acessando o site...")
    response = urequests.get("http://teste.afonsomiguel.com")
    print("P‡gina acessada:")
    print(response.text)
    station.disconnect()



















#---------------------------------------------------------













from wifi_lib import conecta
import urequests
import time

print("Conectando...")
station = conecta("teste_wifi", "senha_teste_wifi")
if not station.isconnected():
    print("N‹o conectado!")
else:
    for v in range (0, 10):
        print(v)
        try:
            resposta = urequests.get("https://api.thingspeak.com/update?api_key=2CR04ZPOULLJARBX&field1={}".format(v))
            print(resposta.text)
        except:
            print("Falha!")
        time.sleep(15)
    





