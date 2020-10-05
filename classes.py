import time
from funciones import printf
class Player:
    def __init__(self, attack, defense, hp):
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.exp = 0
    def fight(self, enemy):
        self.enemy = enemy
		while True:
			self.damage_dealt = self.damage - enemy.defense
			self.wins = False
			enemy.wins = False
			enemy.hp -= self.damage_dealt
			printf("You dealt", self.damage_dealt)
			if enemy.hp <= 0:
				printf("You win!")
				self.wins = True
				return self.wins
				break
			printf("Enemy has", enemy.hp, "health")
			time.sleep(1)
			enemy.damage_dealt = enemy.damage - self.defense
			self.hp -= enemy.damage_dealt
			printf("The enemy attacks!, enemy dealt you", enemy.damage_dealt, "damage")
			if self.hp <= 0:
				printf("You lose...")
				enemy.wins = True
				return enemy.wins
				break
			printf("You have", self.hp, "health")
			time.sleep(1)