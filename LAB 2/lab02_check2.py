'''
function
'''

def Points_Cal(a,num_wins,num_losses,num_draw,goals_for,goals_againts):
    goals_against = 2
    points = num_wins * 3+num_draw
    goal_adv = goals_for - goals_against
    print a
    print "Win:", num_wins, "Lose:", num_losses, "Draw:", num_draw
    print "Total number of points:", points, "Goal advantage:", goal_adv
## Process results for Germany

Points_Cal("Germany",2,1,0,7,2)

## Process results for USA

Points_Cal("USA",1,1,1,4,4)

## Process results for Argentina

Points_Cal("Argentina",3,0,0,0,6)

## Process results for England

Points_Cal("England",0,1,2,2,4)
