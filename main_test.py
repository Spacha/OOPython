import sys

'''
Player:
    PROPERTIES:
        max_health_points:  100
        health_points:      0 - max_health_points
        strength:           50
        defense:            100

    ACTIONS => METHODS:
        attack( type, target ): type = melee, ranged; target = ...
        die()
        speak( msg )
        heal(): health_points -> max_heath_points
        use_item( item ): item = healing_potion, skill_book

Enemy:
    PROPERTIES:
            max_health_points:  100
            health_points:      0 - max_health_points
            strength:           50
            defense:            100

        ACTIONS => METHODS:
            attack( type, target ): type = melee, ranged; target = ...
            die()
            speak( msg )

'''
class Item:
    def use(self, target):
        if item == "health_potion":
            print("Pelaaja joi helapotionin!")
            self.health += 50
        elif item == "strength_potion":
            pass
        elif item == "armor":
            pass
        elif item == "skill_book":
            pass

class HealthPotion:
    def __init__(self, hp):
        self.hp = hp

    def use(self, target):
        target.health += self.hp


class StrengthPotion:
    def use(self, target):
        pass

class SkillBook:
    def use(self, target):
        pass

class Armor:
    def __init__(self, name, rating, min_level):
        self.name       = name
        self.rating     = rating
        self.min_level  = min_level

    def use(self, target):
        target.defence += self.rating



# All Items in the Game
small_health_potion     = HealthPotion(10)
medium_health_potion    = HealthPotion(25)
large_health_potion     = HealthPotion(50)

bone_armor = Armor("Bone Armor", 50, 3)

class Player:
    name = ""
    max_health = 0
    health = 0
    strength = 0
    defense = 0

    def __init__(self, name="", max_health=0, strength=0, defense=0):
        self.name           = name
        self.max_health     = max_health
        self.health         = max_health
        self.strength       = strength
        self.defense        = defense

        print("Pelaaja luotiin")

    def attack(self):
        pass

    def die(self):
        print("{} is dead!".format( self.name ))

        # Game over!
        sys.exit("-> GAME OVER, YOU DIED <-")

    def speak(self, msg):
        print("{} is saying: \"{}\"".format( self.name, msg ))

    def heal(self):
        pass

    def use_item(self, item):
        item.use( self )

    def give_xp(self, xp):
        self.xp += xp
        print("{} sai XP:ta!".format(xp) )
        #self.check_level_up()

    '''
    def check_level_up(self):
        if self.xp >= 100:
            self.level += 1
            self.xp = 0
    '''

class Enemy:
    name = ""
    max_health = 0
    health = 0
    strength = 0
    defense = 0

    def __init__(self, name="", max_health=0, strength=0, defense=0):
        self.name           = name
        self.max_health     = max_health
        self.health         = max_health
        self.strength       = strength
        self.defense        = defense

        print("Vihu luotiin")

    def attack(self, target):
        target.health = target.health - self.strength

        if target.health <= 0:
            target.die()

    def die(self, killer):
        killer.give_xp(10)

        print("{} died!".format( self.name ))

    def speak(self, msg):
        print("{} is saying: \"{}\"".format( self.name, msg ))

print("** Peli alkaa! **\n")

# Game initialization
#   -> create map
#map_terrain = ...
map_name = "Home Valley"

#   -> create world
world_time = "Noon"

player = Player(
    "Bob",
    max_health=100,
    strength=50,
    defense=20
)
enemy_0 = Enemy(
    "Bolbasaur!",
    max_health=50,
    strength=50,
    defense=5
)

player.speak( "I'm gonna kill you so bad!" )
enemy_0.speak( "Yeah, we'll see about that!" )
enemy_0.attack( player )
enemy_0.attack( player )
player.use_item( "health_potion" )
enemy_0.attack( player )
enemy_0.attack( player )


print("\n** Peli päättyy! **")
