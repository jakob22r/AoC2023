import sys
import re
    
sum, powers_sum = 0, 0
input = open(sys.argv[1]).read().strip()
for line in input.split("\n"):
    game_num, game = line.split(":")
    game_num = ''.join(re.findall('[0-9]', game_num))
    gameok = True
    #Loop over draws
    #Minimum needed for that game
    min_red, min_green, min_blue = 0, 0, 0
    draws = game.split(";")
    for draw in draws:
        pairs = draw.split(',')
        red, green, blue = 0, 0, 0
        #Loop over (amount,col) for each draw), update both color and min_color variables
        for pair in pairs:
            amount, color = pair.split()
            if color == "red": 
                if int(amount) > min_red: min_red = int(amount)
                red += int(amount)
            elif color == "green": 
                if int(amount) > min_green: min_green = int(amount)
                green += int(amount)
            elif color == "blue": 
                if int(amount) > min_blue: min_blue = int(amount)
                blue += int(amount)
        #Check if game is not possible (part 1)
        if not(red <= 12 and green <= 13 and blue <= 14): 
            gameok = False
    if gameok:
        sum += int(game_num)
    powers_sum += (min_red * min_green * min_blue)
#Part 1 result
print(sum)
#Part 2 result
print(powers_sum)



