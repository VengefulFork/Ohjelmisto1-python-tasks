import mariadb
import sys





def sqlkomento (icao):
    sql = f"SELECT name, municipality FROM airport where ident = '{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"ICAO koodia vastaava kenttä on {rivi[0]} ja sijantikunta {rivi[1]}")
    return

yhteys = mariadb.connect(
        host='localhost',
        port= 3306,
        database= 'flight_game',
        user= 'flightuser',
        password= '1234',
        autocommit=True
)


icao = input("anna icao koodi = ").upper()

sqlkomento(icao)


