'''
Latihan membuat Game Tamagochi
'''
print("========== Ayo bermain Tamagochi ==========")

name = input("Nama monster kamu siapa ? ")
monster = {"name": name, "power":100, "strenght": 50}


def startGame():
    choice = input(f"Mau apa monster {monster['name']} ? \n 1. Makan \n 2. Lihat Status \n 3. Latihan \n 4. Latihan Extra \n 5. Bertarung  \n 6. Keluar \n Pilih (1/2/3/4/5) : ")

    if choice == "1":
        goEat()
    elif choice =="2":
        goLihatStatus()
    elif choice == "3":
        goTraining()
    elif choice == "4":
        goExtraTraining()
    elif choice == "5":
        goFight()
    else:
        goExit()

def goEat():
    print("Monster lagi makan , Nyam ... Nyam ....")
    monster['power'] += 100
    startGame()

def goLihatStatus():
    print('Lihat status monster ...')
    print(monster)
    startGame()

def goTraining():
    monster["power"] -= 10
    monster["strenght"] += 10
    startGame()

def goExtraTraining():
    monster["power"] += 50
    monster["strenght"] += 500
    print(f"Sekarang stautus kamu : {monster}")
    startGame()

def mainLagi(main):
    if main.lower() == "y":
        startGame()
    else:
        goExit()

def goFight():
    # nama_lawan = input("Siapa nama monster lawanmu ? ")
    monster_lawan = {"name": "", "power":1000, "strenght": 500}

    if monster_lawan['name'] in (None, '', []):
        nama_lawan = input("Siapa nama monster lawanmu ? ")
        monster_lawan.update({"name": nama_lawan})
    else:
        pass

    print(f"Sekarang pertarungan antara {monster['name']} Vs {monster_lawan['name']}")

    if monster['strenght'] > monster_lawan['strenght']:
        print(f"Berhasil monster {monster['name']} Menang ... !! ")
        main_Lagi = input("Ayo main lagi ... (Y/T) ")
        monster.update(
          {
            "power" : 10,
            "strenght" : 50
          }
        )
        mainLagi(main_Lagi)
    elif monster['strenght'] == monster_lawan['strenght']:
        print(f"Kita masih imbang ... !! ")
        main_Lagi = input("Ayo main lagi ... (Y/T) ")
        mainLagi(main_Lagi)
    else:
        print(f"Yah monster {monster['name']} kamu masih kalah ...")
        main_Lagi = input("Ayo main lagi ... (Y/T) ")
        mainLagi(main_Lagi)

def goExit():
    print("Bye ... Bye ....")

startGame()