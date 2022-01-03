dict = {"Pokemon": "Pikachu", "Digimon": "Agumon", "Yugioh": "Black Magician"}

s = input().strip()
if s in dict:
    print(dict[s])
else:
    print("I don\'t know")
