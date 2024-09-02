from tools import game
import random
from tools.game import guess_num
from tools import week

the_Day="wednesday"
the_day="星期三"
print("Today is {1:<10s} 今天是{0:>10s}".format(the_Day,the_day))
print(week.get_week())
while (True):
    game.guess_num()
    playagain=input("Do you want to continue playing (y,n): ")
    if(playagain=='n'):
        print("Game Over!")
        break
    
