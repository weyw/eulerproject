#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=54

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand        Player 1        Player 2        Winner
1       5H 5C 6S 7S KD
Pair of Fives
    2C 3S 8S 8D TD
Pair of Eights
    Player 2
2       5D 8C 9S JS AC
Highest card Ace
    2C 5C 7D 8S QH
Highest card Queen
    Player 1
3       2D 9C AS AH AC
Three Aces
    3D 6D 7D TD QD
Flush with Diamonds
    Player 2
4       4D 6S 9H QH QC
Pair of Queens
Highest card Nine
    3D 6D 7H QD QS
Pair of Queens
Highest card Seven
    Player 1
5       2H 2D 4C 4D 4S
Full House
With Three Fours
    3C 3D 3S 9S 9D
Full House
with Three Threes
    Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

= 376
'''

import time
import math
import sys
import string
from euler import *

start_time = time.clock()
''' '''
from collections import Counter

def hand_rank(hand):
    score = zip(*sorted(((v, values[k]) for
        k,v in Counter(x[0] for x in hand).items()), reverse=True))
    score[0] = ranks.index(score[0])
    if len(set(card[1] for card in hand)) == 1: score[0] = 5  # flush
    if score[1] in straights: score[0] = 8 if score[0] == 5 else 4  # str./str. flush
    return score

file_name = "p54_poker.txt"
hands = (line.split() for line in open(file_name))

values = {r:i for i,r in enumerate('23456789TJQKA', start=2)}
straights = [(v, v-1, v-2, v-3, v-4) for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]

print "Project Euler 54 Solution =", sum(hand_rank(hand[:5]) > hand_rank(hand[5:]) for hand in hands)

# '''
print time.clock() - start_time


