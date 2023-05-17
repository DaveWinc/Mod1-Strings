# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player1 = 'Ruud Gullit'
player2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = player1 + ' ' + str(goal_0) + ',' + ' ' + player2 + ' ' + str(goal_1)
print(scorers)
report = f'{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute'

player = 'Ronald Koeman'
first_name = player[:6]
last_name = player[7:] 
last_name_len = len(last_name)
name_short = 'R. Koeman'
chanttest = (' ' + first_name + '!') * len(first_name)
chant = chanttest[1:]
good_chant = (chant[-1]!=' ')
print(chant[-1] != ' ')
print(chant)
print(report)
print(good_chant)