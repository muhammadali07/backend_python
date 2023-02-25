''''
latihan

'''

player1 = {"name": "", "powers": 0}
player2 = {"name": "", "powers": 0}

'''
====================================== 
'''

nama_player_1 = input("Masukkan nama untuk player 1: ")
power_1 = input(f"Masukkin power untuk {nama_player_1} : ")
nama_player_2 = input("Masukkan nama untuk player 2: ")
power_2 = input(f"Masukkin power untuk {nama_player_2} : ")


def update_player(player,name, powers):
    player.update(
        {
            "name": name,
            "powers": powers
        }
    )

def train(player):
    player['powers'] += 100

def attack(attacker, defender):
    if(attacker['powers'] > defender['powers']):
        print(f"serangan berhasil! selamat untuk {attacker['name']}") 
    else:
        print(f"serangan gagal!, kamu lemah {attacker['name']}")

    

if nama_player_1 in (None, '') and nama_player_2 in (None, ''):
    print("Player 1 dan Player 2 belum di set")
else:
    update_player(
        player=player1,
        name=nama_player_1,
        powers=int(power_1)
    )

    update_player(
        player=player2,
        name=nama_player_2,
        powers=int(power_2)
    )

def bermain():
    trainee = input("Player mana nih yang mau di training (1/2): ")

    if trainee == 1:
        train(player1)
    elif trainee == 2:
        train(player2)
    else:
        print("Player yang anda masukkan tidak terdaftar")

    print("Siapa nih yang mau jadi attacker dan defender ? \n 1. player 1 \n 2. player 2")
    _attack = input("Masukkan nomor player untuk jadi penyerang (1/2) : ")
    _defence = input("Masukkan nomor player untuk jadi bertahan (1/2) : ")
    
    _attack = player1 if int(_attack) == 1 else player2
    _defence = player1 if int(_defence) == 1 else player2
    attack(_attack, _defence)   

while(True):
    bermain()
    main = input("Mau main lagi ? (Ya/Tidak): ")
    if main == "Tidak":
        break

       