import mariadb

yhteys = mariadb.connect(
        host='localhost',
        port= 3306,
        database= 'flight_game',
        user= 'flightuser',
        password= '1234',
        autocommit=True
)

def haku (iso_koodi):

    sql = (f"SELECT airport.type, COUNT(*) FROM airport WHERE airport.iso_country = '{iso_koodi}' GROUP BY airport.type")

    curs = yhteys.cursor()
    curs.execute(sql)
    tulos = curs.fetchall()

    for rivi in tulos :
        print(f"Suomessa on {rivi[0]} kenttätyyppiä, {rivi[1]} kappaletta")

    return

iso_koodi = input("= ").upper()

haku(iso_koodi)