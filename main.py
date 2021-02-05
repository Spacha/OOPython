DEFAULT_HEALTH = 100
DEFAULT_STREGTH = 50

class Item:
	def __init__(self):
		pass

class Helmet(Item):
	def use(self, target):
		# check if the target can use a helmet
		if hasattr(target, 'helmet'):
			target.helmet = self

class Armor(Item):
	def use(self, target):
		# check if the target can use an armor
		if hasattr(target, 'armor'):
			target.armor = self

class HealthPotion(Item):
	def __init__(self, name, hp):
		self.name = name
		self.hp = hp

	def use(self, target):
		if hasattr(target, 'heal'):
			target.heal(self.hp)

class Character:
	XP_PER_LEVEL = 1000		# Constant: how much XP is required for a level up
							# This could be implemented as a function to the
							# requirement would grow each level.

	def __init__(self, name, max_health=None, strength=None, level=0):
		''' Initialize a new generic character. '''

		self.max_health = max_health
		self.health 	= self.max_health	# always max HP in the beginning
		self.strength 	= strength
		self.level 		= level
		self.xp 		= 0					# always zero XP in the beginning

		# start with empty inventory
		self.items = []

		# start with no helmet and armor
		self.helmet = None
		self.armor = None

	# ---------------------------------------
	#    ITEM RELATED
	# ---------------------------------------

	def add_item(self, item):
		self.items.push(item)

	def drop_item(self, item_id):
		self.items.pop(item_id)

	def use(self, item_id):
		self.items[item_id].use(self)

	# ---------------------------------------
	#    ACTIONS
	# ---------------------------------------

	def attack(self, target):
		target_died = target.take_damage(self.strength)

		# every kill grants XP 10 times the number of the target's level
		if target_died:
			self.give_xp( target.level * 10 )

	def heal(self, hp, allow_boost=False):
		'''
		Heal the character hp health points.
		To use a health boost, set allow_boost to True.
		'''
		self.health += hp

		# unless a health boosting is used, limit healing to maximum health
		if not allow_boost and self.health > self.max_health:
			self.health = self.max_health


	def give_xp(self, xp):
		'''
		Takes care of giving XP and handling level ups
		and other related things.
		'''
		self.xp += xp

		if self.xp >= self.XP_PER_LEVEL:
			self.level_up()

	def level_up(self):
		''' A simple level-up process.  '''

		self.level += 1 						# increase level...
		self.xp = self.xp - self.LEVEL_UP_LIMIT # overflow XP to next level progress

		# TODO: Every 5 levels, show a view to the player where they can
		# select a perk in order to improve their character's skills.
		# if self.level % 5 == 0:
		# 	self.choose_new_perk()

	def take_damage(self, base_damage):
		''' . '''

		# Calculate the damage to be taken:
		# Base damage
		# +- potion effects
		#  - armor & helmet ratings: 0-99 %
		damage = base_damage

		damage -= damage*(self.helmet.rating / 100)
		damage -= damage*(self.armor.rating / 100)

		self.health -= damage

		if self.health <= 0:
			self.health = 0
			died = True

			return self.die()


class Monster(Character):
	def __init__(self, name, health, strength):
		# init parent (a generic character object)
		Character.__init__(self, name, max_health=health, strength=strength)

	def die(self):
		print("Monster '{}' died.".format(self.name))

class Player(Character):
	def __init__(self, name):
		# init parent (a generic character object)
		Character.__init__(self, name, max_health=DEFAULT_HEALTH, strength=DEFAULT_STREGTH)

	def die(self):
		print("Game over.")
		sys.exit()

