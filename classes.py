import time
from functions import printf
turn = 0
items_list = []
class Player:
	def __init__(self, attack:int, defense:int, hp:int):
		self.attack = attack
		self.defense = defense
		self.hp = hp
		self.exp = 0
		
	def fight(self, enemy):
		self.enemy = enemy
		printf("You got yourself into a battle, what would you like to do?")
		try:
			move = int(input(
				"[1] Attack\n",
				"[2] Use item"
				))
		except ValueError:
			print("You introduced a non-valid option")
		if move == 1:
			self.damage_dealt = self.attack - enemy.defense
			self.wins = False
			enemy.wins = False
			enemy.hp -= self.damage_dealt
			printf(f"You dealt {self.damage_dealt} damage")
			if enemy.hp <= 0:
				printf("You win!")
				self.wins = True
				return self.wins
				break
			printf(f"Enemy has {enemy.hp} health")
			time.sleep(1)
		elif move == 2:
			printf("Choose your item:")
			time.sleep(0.5)
			print(items_list)
	def print_state(self):
		print(
			"You have", self.hp, "hp",
			"You have", self.defense, "defense"
			"You have", self.attack, "attack"
			"You have", self.exp, "exp"
		)