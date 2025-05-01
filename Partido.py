import json

# Abrir el archivo JSON
with open('cuartos_champions_2019.json', 'r') as archivo:
    datos = json.load(archivo)

fase = datos.get("fase")
for i in datos["Resultados"]:
    local = i["local"]
    visitante = i["visitante"]
    resultado = i["resultado"]

    tarjetas_rojas = 0
    tarjetas_amarillas = 0

    if "tarjetas" in i:
        tarjetas_rojas = i["tarjetas"].get("rojas", 0)
        tarjetas_amarillas = i["tarjetas"].get("amarillas", 0)

    print(f"La fase del torneo es: {fase}")
    print(f"Partido: {local} vs {visitante}")
    print(f"Tarjetas rojas: {tarjetas_rojas}")
    print(f"Tarjetas amarillas: {tarjetas_amarillas}")
    print(f"Resultado: {resultado}")
    print("-" * 30)

# Acumular goles por llave
marcadores = {}

for partido in datos["Resultados"]:
    local = partido["local"]
    visitante = partido["visitante"]

    goles_local, goles_visitante = map(int, resultado.split("-"))
    llave = tuple(sorted([local, visitante]))

    if llave not in marcadores:
        marcadores[llave] = {local: 0, visitante: 0}

    marcadores[llave][local] += goles_local
    marcadores[llave][visitante] += goles_visitante

# Clasificados a semifinales (ganadores de cuartos)
semifinalistas = []
for equipos, goles in marcadores.items():
    equipo1, equipo2 = equipos
    if goles[equipo1] > goles[equipo2]:
        semifinalistas.append(equipo1)
    else:
        semifinalistas.append(equipo2)



print("\nEquipos clasificados a semifinales:")
for equipo in semifinalistas:
    print("-", equipo)