# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_scored1 = 'Ruud Gullit'
player_scored2 = 'Marco van Basten'

goal_min1 = '32'
goal_min2 = '54'

scorers = (f'{player_scored1} {goal_min1}, {player_scored2} {goal_min2}')
print(scorers)

report = (f'{player_scored1} scored in the {goal_min1}nd minute \n{player_scored2} scored in the {goal_min2}th minute')
print (report)

player = 'Hans van Breukelen'
first_name = player[:player.find(' ')]
print (first_name)
last_name = player[player.find(' ')+1:]
print (len(last_name))


name_short = (first_name[0] + '. ' +last_name[0:])
print (name_short)

chant = ((first_name +'! ') * 3) + (first_name +'!')
print(chant)
print (2 !=3)
print (2 !=2)


x= 2//3
print(x)
string + string
