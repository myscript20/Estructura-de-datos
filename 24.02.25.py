import requests, re, json


def extractFromRegularExpresion(regex, data):
    if data:
        return re.findall(regex, data)
    return None
data = requests.get("https://raw.githubusercontent.com/elastic/examples/refs/heads/master/Common%20Data%20Formats/apache_logs/apache_logs").text
regex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(\d{2}\/\b[a-zA-Z]{3}\b\/\d{4})\:(\d{2}\:\d{2}\:\d{2})"

resultado = extractFromRegularExpresion(regex, data)
for i in range(len(resultado)):
    print(f"La ip: {resultado[i][0]}, la fecha es: {resultado[i][1]} y la hora: {resultado[i][2]}")