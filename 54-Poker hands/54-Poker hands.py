# https://projecteuler.net/problem=54

from collections import Counter

class Hand():
	
	# Ranks in order from highest value to lowest.
	ranks = ["royal_flush", "straight_flush", "four_of_a_kind", "full_house", 
	"flush", "straight", "three_of_a_kind", "two_pairs", "one_pair", "high_card"]
	
	def __init__(self, cards):
		"""Initializes Hand obj."""
		self.cards = cards
		
		values_table = {ord("T"): "10", ord("J"): "11", ord("Q"): "12", ord("K"): "13", ord("A"): "14"}
		self.values = [int(card[0].translate(values_table)) for card in cards]
		self.values_count = Counter(self.values)
				
		self.suits = [card[1] for card in cards]
		
	def __str__(self):
		return "Hand(cards: {}, highest_rank: {})".format(self.cards, self.highest_rank())
				
	def is_one_pair(self):
		"""Checks if hand has a one pair."""
		if 2 in self.values_count.values():
			return True
		else:
			return False
	
	def is_two_pairs(self):
		"""Checks if hand has a two pairs."""
		num = 0
		for value in self.values_count.values():
			if value == 2:
				num += 1
		if num == 2:
			return True
		else:
			return False
	
	def is_three_of_a_kind(self):
		"""Checks if hand has a three of a kind."""
		if 3 in self.values_count.values():
			return True
		else:
			return False
			
	def is_straight(self):
		"""Checks if hand is a straight."""
		values = sorted(self.values)
		v1 = values[0]
		# Consecutive numbers have a difference of 1 between each.
		for v2 in values[1:]:
			diff = v2 - v1
			if diff != 1:
				return False
			v1 = v2
		else:
			return True
		
	def is_flush(self):
		"""Checks if hand is a flush."""
		count = Counter(self.suits)
		# Only one type of suit in hand if it is a flush.
		if len(count) == 1:
			return True
		else:
			return False
			
	def is_full_house(self):
		"""Checks if hand has a full house."""
		return self.is_three_of_a_kind() and self.is_one_pair()
		
	def is_four_of_a_kind(self):
		"""Checks if hand has a four of a kind."""
		if 4 in self.values_count.values():
			return True
		else:
			return False
	
	def is_straight_flush(self):
		"""Checks if hand is a straight flush."""
		return self.is_straight() and self.is_flush()
	
	def is_royal_flush(self):
		"""Checks if hand is a royal flush."""
		if self.is_flush() and sorted(self.values) == [10,11,12,13,14]:
			return True
		else:
			return False
			
	def highest_rank(self):
		"""Identifies highest rank of hand."""
		# Skip high card in ranks as that rank exists for all hands.
		for rank in Hand.ranks[:-1]:
			if eval("self.is_" + rank + "()"):
				return rank
		else:
			return "high_card"
	
	def rank_number(self):
		"""Returns number of Hand's highest rank according to their value.
		9 is royal flush and 0 is high card."""
		return 9 - Hand.ranks.index(self.highest_rank())
	
	def one_pair_value(self):
		"""Returns value of one pair cards if it exists."""
		if self.is_one_pair():
			for value, freq in self.values_count.items():
				if freq == 2:
					return value
		else:
			return None

def draw_breaker(hand_obj_1, hand_obj_2):
	"""Determines winner if both hands have the same highest rank."""
	highest_rank = hand_obj_1.highest_rank()
	
	if highest_rank == "high_card" or highest_rank == "flush":
		if sorted(hand_obj_1.values, reverse=True) > sorted(hand_obj_2.values, reverse=True):
			winner = 1
		else:
			winner = 2
		
	if highest_rank == "one_pair":
		if hand_obj_1.one_pair_value() > hand_obj_2.one_pair_value():
			winner = 1
		elif hand_obj_1.one_pair_value() == hand_obj_2.one_pair_value():
			if sorted(hand_obj_1.values, reverse=True) > sorted(hand_obj_2.values, reverse=True):
				winner = 1
			else:
				winner = 2			
		else:
			winner = 2
	
	return winner
		
	
with open("54-poker.txt") as f_obj:
	all_hands = f_obj.read().splitlines()

player1_wins = 0

for hand in all_hands:
	split_hand = hand.split()
	player1, player2 = split_hand[:5], split_hand[5:]
	player1_hand = Hand(player1); player2_hand = Hand(player2)
	player1_highest = player1_hand.rank_number(); player2_highest = player2_hand.rank_number()
	
	if player1_highest > player2_highest:
		player1_wins += 1
		
	if player1_highest == player2_highest:
		if draw_breaker(player1_hand, player2_hand) == 1:
			player1_wins += 1

print(player1_wins)
