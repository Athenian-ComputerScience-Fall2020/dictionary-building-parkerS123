# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

sports_players = {}
position = 'start'

while position != 'break':
    position = input("Enter a football positon or enter break to stop: ")
    if position == 'break':
        break
    player = input("Enter a player that plays that position: ")
    sports_players[position] = player

for x, y in sports_players.items():
    print(x, y)
        #sports_players[x] = y
        #print({x: y})

print(sports_players)
