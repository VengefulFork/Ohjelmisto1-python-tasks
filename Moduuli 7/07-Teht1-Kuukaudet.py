

vuoden_ajat = ("kevät", "kesä", "syksy", "talvi")

kuukauden_numero = int(input("Anna kuukaden numero kokonais lukuna = "))

if  kuukauden_numero == 3 or 4 or 5 :
    print(vuoden_ajat[0])
if kuukauden_numero == 6 or 7 or 8:
    print(vuoden_ajat[1])
if kuukauden_numero == 9 or 10 or 11:
    print(vuoden_ajat[2])
if kuukauden_numero == 12 or 1 or 2 :
    print(vuoden_ajat[3])
else :
    print("Luku on liian suuri tai pieni")