class Battleship:
	count = 0

	def __init__(self,coordinate1,coordinate2,coordinate3,coordinate4):
		self.coordinate1 = coordinate1
		self.coordinate2 = coordinate2
		self.coordinate3 = coordinate3
		self.coordinate4 = coordinate4
	def shoot(self,guess):
		if guess == self.coordinate1:
			self.count = self.count + 1
		elif guess == self.coordinate2:
			self.count = self.count + 1
		elif guess == self.coordinate3:
			self.count = self.count + 1
		elif guess == self.coordinate4:
			self.count = self.count +1
		else:
			print("miss")
		if self.count == 4:
			print("you won")
		else:
			pass
		return self.count

board = [["0","1","2","3","4","5","6","7"],["a"," "," "," "," "," "," "," "],["b"," "," "," "," "," "," "," "],["c"," "," "," "," "," "," "," "],["d"," "," "," "," "," "," "," "],
["e"," "," "," "," "," "," "," "],["f"," "," "," "," "," "," "," "],["g"," "," "," "," "," "," "," "]]
for x in board:
	print(x)

print("You got a board. You can show your coordinates like a1 , b3 like that. Our coordinate limits are a-g and 1-7")
coordinate11 = input("Enter coordinate 1 for player 1: ")
coordinate12 = input("Enter coordinate 2 for player 1: ")
coordinate13 = input("Enter coordinate 3 for player 1: ")
coordinate14 = input("Enter coordinate 4 for player 1: ")

player1 = Battleship(coordinate11, coordinate12, coordinate13, coordinate14)

print("\n")

coordinate21 = input("Enter coordinate 1 for player 2: ")
coordinate22 = input("Enter coordinate 2 for player 2: ")
coordinate23 = input("Enter coordinate 3 for player 2: ")
coordinate24 = input("Enter coordinate 4 for player 2: ")

player2 = Battleship(coordinate21, coordinate22, coordinate23, coordinate24)

print("\n")

coordinates = ["a1","a2","a3","a4","a5","a6","a7","b1","b2","b3","b4","b5","b6","b7","c1","c2","c3","c4","c5","c6","c7",
"d1","d2","d3","d4","d5","d6","d7","e1","e2","e3","e4","e5","e6","e7","f1","f2","f3","f4","f5","f6","f7",
"g1","g2","g3","g4","g5","g6","g7",]
guess1_list = []
guess2_list = []
while True:
	guess1 = input("Player1 make guess: ")
	if guess1 in guess1_list or guess1 not in coordinates:
		while True:
			print("dont make same guess")
			guess1 = input("Player1 make guess: ")
			if guess1 in guess1_list or guess1 not in coordinates :
				pass
			else:
				print(player2.shoot(guess1))
				break
	else:
		print(player2.shoot(guess1))
	
	guess2 = input("Player2 make guess: ")
	if guess2 in guess2_list or guess2 not in coordinates :
		while True:
			print("dont make same guess")
			guess2 = input("Player2 make guess: ")
			if guess2 in guess2_list or guess2 not in coordinates :
				pass
			else:
				print(player1.shoot(guess2))
				break
	else:
		print(player1.shoot(guess2))


	guess1_list.append(guess1)
	guess2_list.append(guess2)

	if player1.count == 4 or player2.count == 4:
		print("\n")
		print("game over")
		break
	else:
		pass
