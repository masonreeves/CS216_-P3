
from p3 import *

# p3_test.py
# Mason Reeves
# spring 2026
# test cases for p3 Chutes and Ladders functions


# helper function
# header function for output
def header( functionName ):
    print()
    print()    
    print("+---------------------------+")
    print("+  testing: ", functionName)
    print("+---------------------------+")
    print()
    


# --------------------------------------------
# --- getSpin()
# --------------------------------------------

header( "getSpin()" )

spin = getSpin()

if spin >= 1 and spin <= 6:
    print("Passed: getSpin returned a value between 1 and 6")
else:
    print("Failed: getSpin returned an invalid value")



# --------------------------------------------
# --- offBoard( N )
# --------------------------------------------

header( "offBoard( N )" )

# Test 1: Below board (too small)
if offBoard(0) == True:
    print("Passed: offBoard(0) returned True")
else:
    print("Failed: offBoard(0) should return True")

# Test 2: Above board (too large)
if offBoard(101) == True:
    print("Passed: offBoard(101) returned True")
else:
    print("Failed: offBoard(101) should return True")

# Test 3: Lower boundary
if offBoard(1) == False:
    print("Passed: offBoard(1) returned False")
else:
    print("Failed: offBoard(1) should return False")

# Test 4: Upper boundary
if offBoard(100) == False:
    print("Passed: offBoard(100) returned False")
else:
    print("Failed: offBoard(100) should return False")

# Test 5: Middle of board
if offBoard(50) == False:
    print("Passed: offBoard(50) returned False")
else:
    print("Failed: offBoard(50) should return False")


# --------------------------------------------
# --- gameWon( N )
# --------------------------------------------

header( "gameWon( N )" )

# Test 1: Winning position
if gameWon(100) == True:
    print("Passed: gameWon(100) returned True")
else:
    print("Failed: gameWon(100) should return True")

# Test 2: Below winning position
if gameWon(99) == False:
    print("Passed: gameWon(99) returned False")
else:
    print("Failed: gameWon(99) should return False")

# Test 3: Starting position
if gameWon(1) == False:
    print("Passed: gameWon(1) returned False")
else:
    print("Failed: gameWon(1) should return False")

# Test 4: Above winning position
if gameWon(101) == False:
    print("Passed: gameWon(101) returned False")
else:
    print("Failed: gameWon(101) should return False")



# --------------------------------------------
# --- isLadder( N )
# --------------------------------------------

header( "isLadder( N )" )

# Ladder at 1
if isLadder(1) == True:
    print("Passed: 1 is a ladder")
else:
    print("Failed: 1 should be a ladder")

# Ladder at 4
if isLadder(4) == True:
    print("Passed: 4 is a ladder")
else:
    print("Failed: 4 should be a ladder")

# Ladder at 9
if isLadder(9) == True:
    print("Passed: 9 is a ladder")
else:
    print("Failed: 9 should be a ladder")

# Ladder at 21
if isLadder(21) == True:
    print("Passed: 21 is a ladder")
else:
    print("Failed: 21 should be a ladder")

# Ladder at 28
if isLadder(28) == True:
    print("Passed: 28 is a ladder")
else:
    print("Failed: 28 should be a ladder")

# Ladder at 36
if isLadder(36) == True:
    print("Passed: 36 is a ladder")
else:
    print("Failed: 36 should be a ladder")

# Ladder at 51
if isLadder(51) == True:
    print("Passed: 51 is a ladder")
else:
    print("Failed: 51 should be a ladder")

# Ladder at 71
if isLadder(71) == True:
    print("Passed: 71 is a ladder")
else:
    print("Failed: 71 should be a ladder")

# Ladder at 80
if isLadder(80) == True:
    print("Passed: 80 is a ladder")
else:
    print("Failed: 80 should be a ladder")


# Not a ladder
if isLadder(2) == False:
    print("Passed: 2 is not a ladder")
else:
    print("Failed: 2 should not be a ladder")

# Not a ladder
if isLadder(50) == False:
    print("Passed: 50 is not a ladder")
else:
    print("Failed: 50 should not be a ladder")
    
    

# --------------------------------------------
# --- isChute( N )
# --------------------------------------------

header("isChute( N )")

# Chute at 16
if isChute(16) == True:
    print("Passed: 16 is a chute")
else:
    print("Failed: 16 should be a chute")

# Chute at 47
if isChute(47) == True:
    print("Passed: 47 is a chute")
else:
    print("Failed: 47 should be a chute")

# Chute at 49
if isChute(49) == True:
    print("Passed: 49 is a chute")
else:
    print("Failed: 49 should be a chute")

# Chute at 56
if isChute(56) == True:
    print("Passed: 56 is a chute")
else:
    print("Failed: 56 should be a chute")

# Chute at 62
if isChute(62) == True:
    print("Passed: 62 is a chute")
else:
    print("Failed: 62 should be a chute")

# Chute at 64
if isChute(64) == True:
    print("Passed: 64 is a chute")
else:
    print("Failed: 64 should be a chute")

# Chute at 87
if isChute(87) == True:
    print("Passed: 87 is a chute")
else:
    print("Failed: 87 should be a chute")

# Chute at 93
if isChute(93) == True:
    print("Passed: 93 is a chute")
else:
    print("Failed: 93 should be a chute")

# Chute at 95
if isChute(95) == True:
    print("Passed: 95 is a chute")
else:
    print("Failed: 95 should be a chute")

# Chute at 98
if isChute(98) == True:
    print("Passed: 98 is a chute")
else:
    print("Failed: 98 should be a chute")

# Not a chute
if isChute(10) == False:
    print("Passed: 10 is not a chute")
else:
    print("Failed: 10 should not be a chute")

# Not a chute
if isChute(50) == False:
    print("Passed: 50 is not a chute")
else:
    print("Failed: 50 should not be a chute")
    


# --------------------------------------------
# --- upLadder( N )
# --------------------------------------------

header("upLadder( N )")

# Ladder at 1 -> 38
if upLadder(1) == 38:
    print("Passed: upLadder(1) returns 38")
else:
    print("Failed: upLadder(1) should return 38")

# Ladder at 4 -> 14
if upLadder(4) == 14:
    print("Passed: upLadder(4) returns 14")
else:
    print("Failed: upLadder(4) should return 14")

# Ladder at 9 -> 31
if upLadder(9) == 31:
    print("Passed: upLadder(9) returns 31")
else:
    print("Failed: upLadder(9) should return 31")

# Ladder at 21 -> 42
if upLadder(21) == 42:
    print("Passed: upLadder(21) returns 42")
else:
    print("Failed: upLadder(21) should return 42")

# Ladder at 28 -> 84
if upLadder(28) == 84:
    print("Passed: upLadder(28) returns 84")
else:
    print("Failed: upLadder(28) should return 84")

# Ladder at 36 -> 44
if upLadder(36) == 44:
    print("Passed: upLadder(36) returns 44")
else:
    print("Failed: upLadder(36) should return 44")

# Ladder at 51 -> 67
if upLadder(51) == 67:
    print("Passed: upLadder(51) returns 67")
else:
    print("Failed: upLadder(51) should return 67")

# Ladder at 71 -> 91
if upLadder(71) == 91:
    print("Passed: upLadder(71) returns 91")
else:
    print("Failed: upLadder(71) should return 91")

# Ladder at 80 -> 100
if upLadder(80) == 100:
    print("Passed: upLadder(80) returns 100")
else:
    print("Failed: upLadder(80) should return 100")


# Not a ladder start
if upLadder(2) == 2:
    print("Passed: upLadder(2) returns 2 (no ladder)")
else:
    print("Failed: upLadder(2) should return 2")

# Not a ladder start
if upLadder(50) == 50:
    print("Passed: upLadder(50) returns 50 (no ladder)")
else:
    print("Failed: upLadder(50) should return 50")



# --------------------------------------------
# --- downChute( N )
# --------------------------------------------

header("downChute( N )")

# *** add test cases for downChute( N ) here ***


if downChute(16) == 6:
    print("Passed: downChute(16) returns 6")
else:
    print("Failed: downChute(16) should return 6")

if downChute(47) == 26:
    print("Passed: downChute(47) returns 26")
else:
    print("Failed: downChute(47) should return 26")

if downChute(49) == 11:
    print("Passed: downChute(49) returns 11")
else:
    print("Failed: downChute(49) should return 11")

if downChute(56) == 53:
    print("Passed: downChute(56) returns 53")
else:
    print("Failed: downChute(56) should return 53")

if downChute(62) == 19:
    print("Passed: downChute(62) returns 19")
else:
    print("Failed: downChute(62) should return 19")

if downChute(64) == 60:
    print("Passed: downChute(64) returns 60")
else:
    print("Failed: downChute(64) should return 60")

if downChute(87) == 24:
    print("Passed: downChute(87) returns 24")
else:
    print("Failed: downChute(87) should return 24")

if downChute(93) == 73:
    print("Passed: downChute(93) returns 73")
else:
    print("Failed: downChute(93) should return 73")


if downChute(95) == 75:
    print("Passed: downChute(95) returns 75")
else:
    print("Failed: downChute(95) should return 75")
    

if downChute(98) == 78:
    print("Passed: downChute(98) returns 78")
else:
    print("Failed: downChute(98) should return 78")

