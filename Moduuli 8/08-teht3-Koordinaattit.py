# Tämä ohjelma toimisi jos saisin geopy:n toimimaan tässä projekti ympäristössä jostain syystä ei toimi

import mariadb
from geopy import distance

yhteys = mariadb.connect(
        host='localhost',
        port= 3306,
        database= 'flight_game',
        user= 'flightuser',
        password= '1234',
        autocommit=True
)

def koordinaatit (icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'"
    curs = yhteys.cursor()
    curs.execute(sql)
    tulos = curs.fetchall()

    return tulos

icao = input("Syötä kentän yksi icao koodi = ").upper()

kenttä1 = koordinaatit(icao)

icao = input("Syötä kentän kaksi icao koodi = ").upper()

kenttä2 = koordinaatit(icao)

print(distance.distance(kenttä1, kenttä2).km)

