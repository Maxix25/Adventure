import time
import random
from functions import *
from getpass import getpass as press_enter
turn = random.randrange(1,3)
back = False
player_wins = None
items_list = ["Potion", "Apple", "Potion"]
class Character:
	def __init__(self, damage:int, defense:int, hp:int):
		self.damage = damage
		self.defense = defense
		self.hp = hp
		self.exp = 0
		
	def fight(self, enemy):
		global turn
		global player_wins
		print("You enter into a fight!")
		self.player_state()
		print("---------------------------------------")
		enemy.enemy_state() 
		press_enter("Press ENTER to continue...")

		def player_turn():
			global turn
			global player_wins
			printf("It's your turn!, what would you like to do?")
			print(
				"[1] Attack",
				"[2] Use Item"
				)
			choice = option(2)
			while True:
				global back
				if choice == 1:
					self.damage_dealt = self.damage - enemy.defense
					enemy.hp -= self.damage_dealt
					printf(f"You dealt {self.damage_dealt} damage!")
					if enemy.hp <= 0:
						player_wins = True
					else:
						enemy.enemy_state()
				else:
					counter = 0
					object = 1
					for i in items_list:
						print(f"[{object}] {items_list[counter]}")
						counter += 1
						object += 1
					print(f"[{object}] Back")
					print("What item do you want to use?")
					choice = option(object)
					if choice == object:
						back = True
						break
					else:
						printf(f"You use the item {items_list[choice - 1]}")
						items_list.pop(choice - 1)  
						printf(f"Items remaining:")
						if items_list == []:
							print("No items left")
						else:
							for i in items_list:
								print(i)
							time.sleep(1)
				if back == True:
					continue
				turn = 2
				break
		def enemy_turn():
			global turn
			printf("It's the enemy's turn")
			action = random.randrange(1,3)
			if action == 1:
				printf("The enemy attacks!")
				enemy.damage_dealt = enemy.damage - self.defense
				self.hp -= enemy.damage_dealt
				time.sleep(1)
				printf(f"The enemy dealt {enemy.damage_dealt} damage")
				if self.hp <= 0:
					global player_wins
					player_wins = False
				else: 
					self.player_state()
			else:
				printf("The enemy uses an item!")
				time.sleep(1)
			turn = 1
		# Check the character turn
		while self.hp > 0 and enemy.hp > 0:
			if turn == 1:
				player_turn()
			elif turn == 2:
				enemy_turn()
			elif self.hp <= 0 and enemy.hp <= 0:
				# Check who won the fight
				if player_wins == True:
					printf("You win!")
					break
				else:
					printf("You lost...")
					break
	def player_state(self):
		print(
			"You have", self.hp, "hp",
			"\nYou have", self.defense, "defense"
			"\nYou deal", self.damage, "damage"
			"\nYou have", self.exp, "exp"
		)

	def gain_item(self):
		self.object_gained = random.choice(possible_items)
		printf(f"You gained a {self.object_gained}, remember to use it well...")
		items_list.append(self.object_gained)

	def enemy_state(enemy):
		print(
			"The enemy has", enemy.hp, "hp",
			"\nThe enemy has", enemy.defense, "defense"
			"\nThe enemy deals", enemy.damage, "damage"
		)
