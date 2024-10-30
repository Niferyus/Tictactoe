matris = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

print("\nGüncel Oyun Tablosu:")
for row in range(3):
    print(" | ".join([matris[row][col] if matris[row][col] != "" else " " for col in range(3)]))
    if row < 2:
        print("---------")

while(True):
    while True:
        x = input("X için satır giriniz: ")
        y = input("X için sütun giriniz: ")

        if(x.isnumeric() and y.isnumeric()):
            x = int(x)
            y = int(y)
            if(x < 3 and y < 3):
                if(matris[x][y] == ""):
                    matris[x][y] = "X"
                    break
                else:
                    print("Orası zaten dolu")
            else:
                print("0 ve 2 arasında değerler giriniz")
        else:
            print("Değerleri doğru giriniz")

    
    print("\nGüncel Oyun Tablosu:")
    for row in range(3):
        print(" | ".join([matris[row][col] if matris[row][col] != "" else " " for col in range(3)]))
        if row < 2:
            print("---------")

    
    if (
        (matris[1][y] == "X" and matris[0][y] == "X" and matris[2][y] == "X") or
        (matris[x][1] == "X" and matris[x][0] == "X" and matris[x][2] == "X") or
        (matris[0][0] == "X" and matris[1][1] == "X" and matris[2][2] == "X") or
        (matris[0][2] == "X" and matris[1][1] == "X" and matris[2][0] == "X")
    ):
        print("X kazandı")
        break

    
    while True:
        x = input("O için satır giriniz: ")
        y = input("O için sütun giriniz: ")

        if(x.isnumeric() and y.isnumeric()):
            x = int(x)
            y = int(y)
            if(x < 3 and y < 3):
                if(matris[x][y] == ""):
                    matris[x][y] = "O"
                    break
                else:
                    print("Orası zaten dolu")
            else:
                print("0 ve 2 arasında değerler giriniz")
        else:
            print("Değerleri doğru giriniz")

    
    print("\nGüncel Oyun Tablosu:")
    for row in range(3):
        print(" | ".join([matris[row][col] if matris[row][col] != "" else " " for col in range(3)]))
        if row < 2:
            print("---------")

    
    if (
        (matris[1][y] == "O" and matris[0][y] == "O" and matris[2][y] == "O") or
        (matris[x][1] == "O" and matris[x][0] == "O" and matris[x][2] == "O") or
        (matris[0][0] == "O" and matris[1][1] == "O" and matris[2][2] == "O") or
        (matris[0][2] == "O" and matris[1][1] == "O" and matris[2][0] == "O")
    ):
        print("O kazandı")
        break
