

vuoden_ajat = ("kevät", "kesä", "syksy", "talvi")

kuukauden_numero = int(input("Anna kuukaden numero kokonais lukuna = "))

if  3<= kuukauden_numero <=5 :
    print(vuoden_ajat[0])
elif 6<= kuukauden_numero <=8:
    print(vuoden_ajat[1])
elif 9<= kuukauden_numero <=11:
    print(vuoden_ajat[2])
elif kuukauden_numero == 12 or 1 or 2 :
    print(vuoden_ajat[3])
else :
    print("Luku on liian suuri tai pieni")