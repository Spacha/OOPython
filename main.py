DEFAULT_HEALTH = 100
DEFAULT_STREGTH = 50


class Character:
	LEVEL_UP_LIMIT = 1000 	# Constant: how much XP is required for a level up
	 						# This could be implemented as a function to the
	 						# requirement would grow each level.

	def __init__(self, name, max_health=None, strength=None, level=0):
		''' Initialize a new generic character. '''

		self.max_health = max_health
		self.health 	= self.max_health 	# always max HP in the beginning
		self.strength 	= strength
		self.level 		= level
		self.xp 		= 0 				# always zero XP in the beginning

		# start with empty inventory
		self.items = []

		# start with no helmet and armor
		self.helmet = None
		self.armor = None

	def drop_item(self, item_id):
		self.items.pop(item_id)

	def attack(self, target):
		target_died = target.take_damage(self.strength)

		# every kill grants XP 10 times the number of the target's level
		if target_died:
			self.give_xp( target.level * 10 )

	def give_xp(self, xp):
		""" . """
		self.xp += xp

		if self.xp >= self.LEVEL_UP_LIMIT:
			self.level_up()

	def level_up(self):
		""" A simple level-up process.  """

		self.level += 1 						# increase level...
		self.xp = self.xp - self.LEVEL_UP_LIMIT # overflow XP to next level progress

		# TODO: Every 5 levels, show a view to the player where they can
		# select a perk in order to improve their character's skills.
		# if self.level % 5 == 0:
		# 	self.choose_new_perk()



class Player(Character):
	def __init__(self, name):
		# init parent (a generic character object)
		Character.__init__(self, name, max_health=DEFAULT_HEALTH, strength=DEFAULT_STREGTH)


