import re, json, collections

def extraer_expresion_regular(regex, data):
    if data:
        return re.findall(regex, data)  
    else:
        return None

regex = (r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(\d{2}/\b[a-zA-Z]{3}\b/\d{4}):(\d{2}:\d{2}:\d{2})\s\+\d{4,6}\]\s\"(\b[A-Z]{3,7}\b)\s(/\S+)\sHTTP/\d\.\d\"\s(\d{3})")

ips = set()
error100 = 0
error200 = 0
error300 = 0
error400 = 0
error500 = 0
with open("accessparcial.log", "r") as data:
    for line in data:
        resultado = extraer_expresion_regular(regex, line)
        for ip, fecha, hora, metodo, ruta, error in resultado:
            ips.add(ip)
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



# Impresión de resultados
print(f"IPS:")
print(json.dumps(sorted(ips), indent=2))
print(f"Catidad de IPS sin repetir: {len(ips)}")
print(f"Cantidad de errores:")
print(f"100: {error100}\n200: {error200}\n300: {error300}\n400: {error400}\n500: {error500}")

