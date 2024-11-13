card_value = {"A": 11,
              "2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
              "10": 10,
              "J": 10,
              "Q": 10,
              "K": 10}

a = ["A", "2", "A", "9", "A"]
player_score = 0
player_A_number = 0
for i in a:
    player_score += card_value[i]
    if i == "A":
        player_A_number+= 1
    if player_score > 21 and player_A_number > 0:
        player_score-= 10
        player_A_number-= 1
