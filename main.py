# write your code here
def padel_court_cost(court_type):

    if court_type == 'indoor':
        return 30
    elif court_type == 'outdoor':
        return 20
def rackets_cost(racket_brand):
    if racket_brand == 'bullpadel':
        return 20
    elif racket_brand == 'Nox':
        return 140
    elif racket_brand == 'siux' :
        return 200
def  padel_balls_cost(ball_boxes):
    if ball_boxes == '1':
        return 2
    elif ball_boxes == '2':
        return 3.5 
    elif ball_boxes == '3':
        return 5
def padel_game_cost():
    curtType = input('enter your type')
    racketBrand=input('enter your brand')
    ballBoxes=input('how many box')
    cost=padel_court_cost(curtType)
    brand=rackets_cost(racketBrand)
    box=padel_balls_cost(ballBoxes)
    price = cost + brand + box 
    print(price) 

padel_game_cost()    


           
    



