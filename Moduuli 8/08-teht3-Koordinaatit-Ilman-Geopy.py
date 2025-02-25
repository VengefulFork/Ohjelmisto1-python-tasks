import mariadb
from math import sin, cos, sqrt, atan2, radians

yhteys = mariadb.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='flightuser',
    password='1234',
    autocommit=True
)

def koordinaatit(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'"
    curs = yhteys.cursor()
    curs.execute(sql)
    tulos = curs.fetchall()

    for rivi in tulos:
        lat = rivi[0]
        long = rivi[1]

    return lat, long

icao = input("Syotä kentän yksi ICAO koodi = ").upper()

lat1 = radians(koordinaatit(icao)[0])
long1 = radians(koordinaatit(icao)[1])

icao = input("Syotä kentän kaksi ICAO koodi = ").upper()

lat2 = radians(koordinaatit(icao)[0])
long2 = radians(koordinaatit(icao)[1])

# print(lat1, long1)
# print(lat2, long2)


# Alempana oleva matematiikka on seuraavasta vastauksesta https://stackoverflow.com/a/19412565
# Maan säde
r = 6378.1

lat_laskuun = lat2 - lat1
long_laskuun = long2 - long1

a = (sin(lat_laskuun/2))**2 + cos(lat1) * cos(lat2) * (sin(long_laskuun/2)) ** 2
c = 2 * atan2(sqrt(a), sqrt(1-a))

etäisyys = r * c

print(f"Kentien välinen etäisyys on {round(etäisyys, 3)} kilometriä")