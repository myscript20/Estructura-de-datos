import re, json
def extraer_expresion_regular(regex, data):
    if data:
        return re.findall(regex, data)  
    else:
        return None

regex = r"\"([^\"]*)\"$" 

navegador = {
    "Chrome": 0,
    "Firefox": 0,
    "Safari": 0,
    "Edge": 0,
    "Opera": 0,
    "Internet Explorer": 0,
    "Otro": 0
}
with open("access.log", "r") as data:
    for line in data:
        resultado = extraer_expresion_regular(regex, line)
        for user in resultado:
            user = user.lower()
            if "chrome" in user: 
                navegador["Chrome"] += 1
            elif "firefox" in user:
               navegador["Firefox"] += 1
            elif "safari" in user:
                navegador["Safari"] += 1
            elif "edge" in user:
                navegador["Edge"] += 1
            elif "opera" in user:
                navegador["Opera"] += 1
            elif "msie" in user:
                navegador["Internet Explorer"] += 1
            else:
                navegador["Otro"] += 1
for nav, cantidad in navegador.items():
    print(f"{nav}: {cantidad}")

            

