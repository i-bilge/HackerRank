# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
# ----------------------------------------------------------------
# Function Description

# Complete the minion_game in the editor below.

# minion_game has the following parameters:

# string string: the string to analyze
# Prints

# string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
# Input Format

# A single line of input containing the string S.
# Note: The string S will contain only uppercase letters: [A-Z].

#---------------------------SOLUTION--------------------------------
def minion_game(string):
    player1 = 0
    player2 = 0
    str_len = len(string)
    for i in range(str_len):
        if s[i] in "AEIOU":
            player1 += (str_len)-i
        else :
            player2 += (str_len)-i
    
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    elif player1 == player2:
        print("Draw")
    else :
        print("Draw")

s = input("the string please :")
minion_game(s)