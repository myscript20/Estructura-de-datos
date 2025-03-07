import re, json


def ExtraerExpresionRegular(regex,data):
    if data:
        return re.findall(regex,data)
    else:
        return None

data = open("accessparcial.log","r")
regex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s\-\s\-\s\[(\d{2}\/\b[a-zA-Z]{3}\b\/\d{4})\:(\d{2}\:\d{2}\:\d{2})\s\+\d{4,6}\]\s\"(\b[A-Z]{3,7}\b)\s(\/\S+)\sHTTP\/\d{1}\.\d{1}\"\s(\d{3})"

resultado = ExtraerExpresionRegular(regex,data.read())

ips = []
for ip,fecha,hora, metodo, ruta, error in resultado:
    if ip not in ips:
         ips.append(f"{ip}")
print(f"ip:{ips}")

error100 = 0
error200 = 0
error300 = 0
error400 = 0
error500 = 0

for ip,fecha,hora, metodo, ruta, error in resultado:
    if error == "100":
        error100 += 1
    elif error == "200":
        error200 += 1
    elif error == "300":
        error300 += 1
    elif error == "400":
        error400 += 1
    elif error == "500":
        error500 += 1
print(f"La cantidad de errores 100: {error100},La cantidad de errores 200: {error200}, La cantidad de errores 300: {error300}, La cantidad de errores 400: {error400} y La cantidad de errores 500: {error500}")