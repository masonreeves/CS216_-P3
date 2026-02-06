import random

# p3.py
# spring 2026
# Mason Reeves
# 
# Chutes and Ladders
# 1. Begin by updating the functions to play a two person game
#    Do not modify the processTurn function
#
# 2. Update the main logic to create a four player game
#    Do not modify your functions to make this change

def getSpin():
    """ return random int 1 to 6 """
    return random.randint(1,3)

def offBoard( N ):
    """ use an IF statement approach to return True if N is not between 1 and 100 """
    
    if N < 1 or N > 100:
        
        result = True
    
    else:
      
        result = False
   
   
    return result

def gameWon( N ):
    """ use if statements to return True of N is 100 """
    if N == 100:
        result = True
    else:
        result = False
    return result

def isLadder( N ):
    """ use individual if approach (ie. no else or elif) to return True if N is bottom ladder position """
    result = False
    
    if N == 1:
       result = True
    
    if N == 4:
       result = True
       
    if N == 9:
       result = True
       
    if N == 21:
       result = True
      
    if N == 28:
       result = True
      
    if N == 36:
       result = True
      
    if N == 51:
       result = True
   
    if N == 71:
       result = True
       
    if N == 80:
       result = True
       
    return result
        

def isChute( N ):
    """ use individual if approach (ie. no else or elif) to return True if N is top of chute position """
    result = False
    
    if N == 16:
       result = True
    
    if N == 47:
       result = True
       
    if N == 49:
       result = True
           
    if N == 56:
       result = True
       
    if N == 62:
       result = True
       
    if N == 64:
       result = True
       
    if N == 87:
       result = True
       
    if N == 93:
       result = True
       
    if N == 95:
       result = True
       
    if N == 98:
       result = True
       
    return result


  
def upLadder( N ):
    """ use nested elif approach to return top of ladder position from bottom position N """

    result = -1
       
       
    if N == 1:
           result = 38
           
    if N == 2:
           result = 2
            
    if N == 4:
           result = 14
            
    if N == 9:
           result = 31
            
    if N == 21:
           result = 42
            
    if N == 28:
           result = 84
            
    if N == 36:
           result = 44
           
    if N == 50:
           result = 50
            
    if N == 51:
           result = 67
            
    if N == 71:
           result = 91
            
    if N == 80:
           result = 100
                

    return result
 
       
                
        
    
def downChute( N ):
    """ use nested elif approch to return bottom of chute position from top position N """
    result = -1
    if N == 16:
        result = 6
        
    if N == 47:
        result = 26
    
    if N == 49:
        result = 11
        
    if N == 56:
        result = 53
        
    if N == 62:
        result = 19
        
    if N == 64:
        result = 60
        
    if N == 87:
        result = 24
        
    if N == 93:
        result = 73
        
    if N == 95:
        result = 75
        
    if N == 98:
        result = 78
        
    
    return result



# *** do not modify processTurn **
def processTurn( player, position ):
    
    spin = getSpin()
    
    print(f"{player} Spin = {spin}".format(player, spin))
    
    nextPosition = position + spin
    
    if isLadder( nextPosition ) == True:
        endingPosition = upLadder( nextPosition )
        print( f"{player} Up ladder at {nextPosition} to {endingPosition}".format( player, nextPosition, endingPosition ) )            
        position = endingPosition

    elif isChute( nextPosition ) == True:
        endingPosition = downChute( nextPosition )
        print( f"{player} Down chute at {nextPosition} to {endingPosition}" )            
        position = endingPosition
    
    elif offBoard( nextPosition ) == True:
        print( " Off board, try again ..." )
               
    else:
        print( f"{player} Move to {nextPosition}" )
        position = nextPosition
    
    if gameWon(position):
        print()
        print( f"Game Over ... {player} Wins!!!" )

    return position


# *** main game logic ***
if __name__ == "__main__":

    #random.seed( -1 () #can set number to get same random numbers
        
    print( "Enter player 1 name: " )
    player1 = input() #comment out when debugging
    #player1 = "Alice"  #comment out when submitting
    
    print( "Enter player 2 name: " )
    player2 = input() #comment out when debugging
    #player2 = "Bob"  #comment out when submitting

    print( "Enter player 3 name: " )
    player3 = input() #comment out when debugging
   # player3 = "John"  #comment out when submitting

    print( "Enter player 4 name: " )
    player4 = input() #comment out when debugging
   # player4 = "Hannah"  #comment out when submitting
    
    print()
    
    player1Position = 0
    player2Position = 0
    player3Position = 0
    player4Position = 0
    
    gameOver = False
    while gameOver != True:
        
        player1Position = processTurn( player1, player1Position )
        gameOver = gameWon( player1Position )
        
        if gameOver != True:
            player2Position = processTurn( player2, player2Position )
            gameOver = gameWon( player2Position )
     
        #while loop

            
               
