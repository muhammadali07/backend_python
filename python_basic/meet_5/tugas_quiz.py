''''
latihan

'''

player1 = {"name": "", "powers": ""}
player2 = {"name": "", "powers": ""}

'''
====================================== 
'''

nama_player_1 = input("Masukkan nama untuk player 1: ")
nama_player_2 = input("Masukkan nama untuk player21: ")


def update_player(player,name, power):
    player.update(
        {
            "name": name,
            "power": power
        }
    )
    

if nama_player_1 in (None, '') and nama_player_2 in (None, ''):
    print("Player 1 dan Player 2 belum di set")
else:
    update_player()



def train(player):
    player['power'] += 100

def attack(attacker, defender):
    if(attack['power'] > defender['power']):
        print(f"serangan berhasil! selamat untuk {attacker['name']}") 
    else:
        print(f"serangan gagal!, kamu lemah {attacker['name']}")

train(player1)
attack(player1, player2)