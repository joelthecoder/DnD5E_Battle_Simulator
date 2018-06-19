from enum import Enum, auto
import math
import random

class area_of_effect_shape(Enum):
    def __str__(self):
        return str(self.value)    
    Point = auto()
    Line = auto()
    Circle = auto()
    Square = auto()
    Cone = auto()

class origin_point(Enum):
    def __str__(self):
        return str(self.value)    
    Self = auto()
    Target = auto()
    PointInRange = auto()

class attribute(Enum):
   def __str__(self):
       return str(self.value)   
   Strength = auto()
   Dexterity = auto()
   Constitution = auto()
   Intelligence = auto()
   Wisdom = auto()
   Charisma = auto()

class ability_check_block():
    str_adv = bool()
    dex_adv = bool()
    con_adv = bool()
    int_adv = bool()
    wis_adv = bool()
    cha_adv = bool()

class saving_throw_block():
    str = int()
    str_adv = bool()
    dex = int()
    dex_adv = bool()
    con = int()
    con_adv = bool()
    intel = int()
    int_adv = bool()
    wis  = int()
    wis_adv = bool()
    cha = int()
    cha_adv = bool()

class statistic_block():
    str = int()
    dex = int()
    con = int()
    intel = int()
    wis  = int()
    cha = int()

class creature_condition():
    condition = int()
    source = None
    duration = int()

class condition(Enum):
    def __str__(self):
        return str(self.value)    
    Blinded = auto()
    Charmed = auto()
    Deafened = auto()
    Fatigued = auto()
    Frightened = auto()
    Grappled = auto()
    Incapacitated = auto()
    Invisible = auto()
    Paralyzed = auto()
    Posioned = auto()
    Prone = auto()
    Restrained = auto()
    Stunned = auto()
    Unconscious = auto()
    Exhaustion = auto()

class player_class_block():
    player_class = int()
    player_class_level = int()
    player_subclass = int()
    spellcasting_attribute = int()
    
class player_class(Enum):
    def __str__(self):
        return str(self.value)    
    Barbarian = auto()
    Bard = auto()
    BloodHunter = auto()
    Cleric = auto()
    Druid = auto()
    Fighter = auto()    
    Monk = auto()
    Rogue = auto()
    Ranger = auto()
    Sorcerer = auto()
    Paladin = auto()
    Warlock = auto()
    Wizard = auto()    
    
class player_subclass(Enum):
    def __str__(self):
        return str(self.value)    
    #Barbarian subclasses (Paths)
    PathOfTheBeserker = auto()
    PathOfTheZealot = auto()
    #BloodHunter subclasses
    OrderOfTheGhostslayer = auto()
    OrderOfTheProfaneSoul = auto()
    OrderOfTheLycan = auto()
    #Cleric subclasses (Domains)
    LifeDomain = auto()
    TrickeryDomain = auto()    
    #Fighter subclasses
    Battlemaster = auto()
    Gunslinger = auto()
    #Monk subclasses (Ways)
    WayOfTheCobaltSoul = auto()
    WayOfTheOpenHand = auto()
    #Paladin subclasses
    Oathbreaker = auto()   
    Vengeance = auto()    
    #Rogue subclasses
    ArcaneTrickster = auto()
    Assassin = auto()    
    Thief = auto()    
    #Ranger subclasses
    Beastmaster = auto()    
    #Warlock subclasses (Pacts)
    PactOfTheBlade = auto()
    PactOfTheChain = auto()
    #Wizard subclasses (Schools)
    Divination = auto()
    Evocation = auto() 
    Necromancy = auto()
    Transmutation = auto()

class crimson_rite():
    name = str()    
    damage_type = int()
    primal = bool() #True if Primal Rite, False if Esoteric
    activation_damage = int() #Normally = characterlevel, ghostslayer has it halved
    bonus_damage = int()
    bonus_damage_target = int()
    colour = str() #Colour text for flavour

class blood_curse():
    name = str()
    uses_bonus_action = bool()
    uses_reaction = bool()
    amplify_hit_die_cost = int()
    duration = int() #(0 = reaction/instant, 1=until beginning of next turn, other values determined by wis mod etc)

class cardinal_direction(Enum):
    #integers matter for this one
    def __str__(self):
        return str(self.value)    
    Stay = 0
    SouthWest = 1
    South = 2
    SouthEast = 3
    East = 4
    NorthEast = 5
    North = 6
    NorthWest = 7
    West = 8
    Random = 9        

class saving_throw(Enum):
    def __str__(self):
        return str(self.value)    
    Strength = auto()
    Dexterity = auto()
    Constitution = auto()
    Intelligence = auto()
    Wisdom = auto()
    Charisma = auto()

class ability_check(Enum):
    def __str__(self):
        return str(self.value)    
    Strength = auto()
    Dexterity = auto()
    Consitution = auto()
    Intelligence = auto()
    Wisdom = auto()
    Charisma = auto()

class creature_type(Enum):
    def __str__(self):
        return str(self.value)    
    Player = auto()
    Monster = auto()
    
#enumerable creature attributes
class race(Enum):
    def __str__(self):
        return str(self.value)    
    #PC Races
    Aasamir = auto()
    Dragonborn = auto()
    Human = auto()
    Half_Elf = auto()
    Half_Orc = auto()
    Gnome = auto()
    Goblin = auto()
    Goliath = auto() 
    Tiefling = auto()
    #Monster races
    Dragon = auto()
    Undead = auto()
    Construct = auto()
    Giant = auto()
    Beast = auto()
    Monstrosity = auto()

class subrace(Enum):
    def __str__(self):
        return str(self.value)    
    Revenant = auto()

class monster_type(Enum):
    def __str__(self):
        return str(self.value)        
    #Constructs
    Doty = auto()
    #Giants
    Hill = auto()
    #Beasts
    Bear = auto()
    #Dragons
    Ancient_Black_Dragon = auto()

class feat(Enum):
    def __str__(self):
        return str(self.value)    
    Sharpshooter = auto()
    Great_Weapon_Master = auto()
    Lucky = auto()
    Sentinel = auto()

#enumerable weapon attributes
class weapon_type(Enum):
    def __str__(self):
        return str(self.value)
    Firearm = auto()
    Dagger = auto()
    Longbow = auto()
    Crossbow = auto()
    Handaxe = auto()
    Greataxe = auto()
    Shortsword = auto()
    Scimitar = auto()
    Longsword = auto()
    Greatsword = auto()
    Quarterstaff = auto()
    Natural = auto()
    Unarmed = auto()

#Armour Type
class armour_type():
    def __str__(self):
        return str(self.value)
    Light = auto()
    Medium = auto()
    Heavy = auto()
    Shield = auto()

class fighting_style(Enum):
    def __str__(self):
        return str(self.value)
    Archery = auto()
    Defense = auto()
    Dueling = auto()
    Great_Weapon_Fighting = auto()
    Protection = auto()
    Two_Weapon_Fighting = auto()

#enumerable spells (undecided if this is the best way to handle spells, maybe only for item-granted ones)
class equipment_spells(Enum):
    def __str__(self):
        return str(self.value)
    CabalsRuin = auto()
    Enlarge = auto()
    Leap = auto()
    HandOfVecna = auto()
    Haste = auto()
    BladeReturn = auto()

class spell_school(Enum):
    def __str__(self):
        return str(self.value)
    Divination = auto()
    Transmutation = auto()
    Necromancy = auto()
    Evocation = auto()

class spell_casting_time(Enum):
    def __str__(self):
        return str(self.value)    
    Action = auto()
    Bonus_Action = auto()
    Reaction = auto()
    Instant = auto() # Instant spells apply basically automatically, i.e. Divine Smite
    
#Spell slots
# Generic object for tracking min/max spells and level
class spellslot():
    level = int()
    count = int()
    max = int()    

#Spells version 2
class spell():
   name = str()
   
   description = str()
   #Spell school
   school = int()
   
   #Player Class types that can cast this spell
   def player_classes(self):
        if not hasattr(self, "_player_classes"):
            self._player_classes = []
        return self._player_classes

   #Minimum spell slot to be expended to cast spell (0 = cantrip)
   min_spellslot_level = int()
   
   #Maximum spell slot to be expended with additional effect 
   #(i.e. divine smite at 8th level has 5th level properties)
   max_spellslot_level = int()

   # Casting Time - normally action/bonus action
   casting_time = int()

   # True if this spell is a spell attack, false if it's a DC save (range attribute determines range or touch)
   spell_attack = bool()   
   # Instances of damage; i.e. Eldritch blast gains additional beams at 5th, 11th, 17th level
   instance = int()
   # Castable range of spell to origin (i..e fireball = 150ft)
   range = int()
   # Spells' origin (point at which spell originates (i.e. fireball erupts from point you choose in range)
   origin = int()
   # Shape enumeration (shape that spell affects, i.e. fireball = 20 ft radius sphere)
   shape = int()
   shape_size = int()

   #Components
   verbal = bool()
   somatic = bool()
   material = bool()
   # Cost in GP for material (as if we'll ever get to that point)
   material_cost = int()

   #Damage information
   damage_die = int()
   damage_die_count = int()
   damage_type = int()

   #Additional damage to deal per spell slot gap between min_spell_slot (up to max)
   damage_die_per_spell_slot = int()
   damage_die_count_per_spell_slot = int()
   
   #Additional damage to deal based on class level
   #damage_die_per_class_level = int()
   #damage_die_count_per_class_level = int()
   
   #Bonus damage based on target
   bonus_damage_die = int()
   bonus_damage_die_count = int()
   bonus_damage_target = int()
       
   #Saving throw information; DC is set on the spell object 
   saving_throw = int()
   saving_throw_dc = int()   

#various damage types
class damage_type(Enum):
    def __str__(self):
        return str(self.value)
    Piercing = auto()
    Slashing = auto()
    Bludgeoning = auto()
    Force = auto()
    Fire = auto()
    Cold = auto()
    Lightning = auto()
    Necrotic = auto()
    Radiant = auto()
    Poison = auto()
    Psychic = auto()
    Acid = auto()
    Generic = auto() # Damage that is typeless and should never be subject to resistance/immunity/vulnerability, i.e. damage suffered by blood hunter for activating a crimson rite 

# Generic equipment class - used to track item-granted spells and feats
class equipment():
    name = ""
    grants_equipment_spell = int()
    max_charges = int()
    current_charges = int()
    damage_die= int()
    damage_die_count = int()
    damage_type = int()

#Weapon class - used to track weapon damage stats and other properties
class weapon():
    #Core attributes
    name = ""
    weapon_type = int()  
    magic = bool() # Determines if weapon is magic for purposes of damage resistance

    # Properties from handbook 
    martial = bool()
    finesse = bool()
    ammunition = bool()
    heavy = bool()
    light = bool()
    loading = bool()
    range = int()
    long_range = int()
    reach = int()
    thrown = bool()
    was_thrown = bool()
    two_handed = bool()
    versatile = bool()
    silvered = bool()

    # Special property to track wheter weapon is a "Monk Weapon", and can thus be used with Flurry of Blows
    monk_weapon = bool()

    # Main weapon damage 
    damage_die = int()
    damage_die_count = int()      
    weapon_damage_type = int()
        
    # Bonus damage (i.e. 1d6 Necrotic on Blood Axe)
    bonus_damage_die = int()
    bonus_damage_die_count = int()
    bonus_damage_type = int()
    # Special targetted effects (i.e. Dragonslayer Longsword gets 3d6 only against Dragon type)
    bonus_damage_target = int()
    
    # Crit bonus damage (i.e. 2d8 Necrotic on Fane Eater)
    crit_bonus_damage_die = int()
    crit_bonus_damage_die_count = int()
    crit_bonus_damage_type = int()

    # Magic modifiers (i.e. 2 for +2 weapon)
    magic_to_hit_modifier = int() #also use this on monster attacks (i.e. dragon gets +15 on claw, +8 of which comes from str mod - the rest has no source)
    magic_damage_modifier = int()

    # Firearm-specific properties
    reload = int()
    currentammo = int()
    misfire = int()
    broken = bool()
    ruined = bool()

    # Crimson Rite - when activated, the weapon inherits the crimson rite object off the player for damage calculation and to persist between turns
    active_crimson_rite = None

    # Warlock Pact of the Blade weapon toggle (flavour mainly)
    pact_weapon = bool()
class team():
    name = ""
    no_of_wins = int()
    battling = bool()

# Generic class for players and monster entities (called creature to be consistent with rulebook)
class creature():
    #Notes - brief description of current status of character
    notes = ""

    #Creature type - broadly defines monster vs player behaviour
    creature_type = int()

    #Monster type - narrows down monster list for specific abilities
    monster_type = int()

    # Team used to track allies/enemies (and not target the wrong one)
    team = team()
    # Core properties, common across creatures
    fullname = ""
    name = ""
    race = int()
    subrace = int()    
    
    max_health = int()
    current_health = int()        
        
    speed = int()   
    movement = int() #Distinct from speed, reflects movement per round and is consumed/reset at start of round
    desired_range = int() # Set by movement functions, determines the desired range that the combatant wants tok eep between them and target

    stats = statistic_block()
    saves = saving_throw_block()
    checks = ability_check_block()    

    main_hand_weapon = None # Weapon object
    offhand_weapon = None # Only populated if combatant is dual wielding and holding a different weapon in the off hand
    spellcaster = bool() #Simple boolean value to describe whether this character should focus on casting spells, or using weapons

    armour_class = int()
    armour_type = armour_type()
    
    #Extensible properties (1 to many)    
    def player_classes(self):
        if not hasattr(self, "_player_classes"):
            self._player_classes = []
        return self._player_classes

    def creature_conditions(self):
        if not hasattr(self, "_creature_conditions"):
            self._creature_conditions = []
        return self._creature_conditions

    def spell_list(self):
        if not hasattr(self, "_spell_list"):
            self._spell_list = []
        return self._spell_list           

    def spellslots(self):
        if not hasattr(self, "_spellslots"):
            self._spellslots = []
        return self._spellslots        

    def creature_feats(self):
        if not hasattr(self, "_creature_feats"):
            self._creature_feats = []
        return self._creature_feats    
       
    def weapon_inventory(self):
        if not hasattr(self, "_weapon_inventory"):
            self._weapon_inventory = [] 
        return self._weapon_inventory

    def weapon_proficiency(self):
        if not hasattr(self, "_weapon_proficiency"):
            self._weapon_proficiency = []
        return self._weapon_proficiency    

    def equipment_inventory(self):
        if not hasattr(self, "_equipment_inventory"):
            self._equipment_inventory = []
        return self._equipment_inventory      
    
    proficiency = int() # Determined by taking the PC's 'primary' class, based on the level - see initgrog for example
    
    #Combat/class/race/feat properties - variety of fields used to track whether abilities can be used, the count remaining for abilities, and other combat info
    # Class
    ## Generic
    extra_attack = int()            
    
    evasion = bool() # Can come from either Rogue or Monk class

    # Feat
    sharpshooter = bool()    
    use_sharpshooter = bool()    
    
    great_weapon_master = bool()
    use_great_weapon_master = bool()
    
    luck_uses = int()
    
    #############
    # Barbarian #
    #############
    barbarian_unarmored_defense = bool()
    canrage = bool()
    ragedamage = int()
    raging = bool()    
    rage_duration = int()
    max_rage_duration = int()
    reckless = bool()
    use_reckless = bool()

    brutal_critical = bool()
    brutal_critical_dice = int()
    relentless_rage = bool()
    relentless_rage_DC = int()
    feral_instinct = bool()

    # Beserker
    frenzy = bool()
    retaliation = bool()
    
    # Zealot
    divine_fury = bool()
    divine_fury_used = bool()
    divine_fury_damage_type = int()
    fanatical_focus = bool()
    zealous_presence = bool()
    rage_beyond_death = bool()

    #############
    #Blood Hunter
    #############    

    # Structures for maintaining the selected crimson rites/blood curses for the creature
    def crimson_rites(self):
        if not hasattr(self, "_crimson_rites"):
            self._crimson_rites = []
        return self._crimson_rites

    def blood_curses(self):
        if not hasattr(self, "_blood_curses"):
            self._blood_curses = []
        return self._blood_curses

    crimson_rite = bool()
    crimson_rite_damage_die = int()
    blood_maledict = bool()
    blood_maledict_uses = int()
    dark_velocity = bool()
    hardened_soul = bool()
    enduring_form = bool()
    sanguine_mastery = bool()

    ## Ghostslayer
    hallowed_veins = bool()
    supernal_flurry = bool()
    vengeful_spirit = bool()

    #############
    ## Fighter ##
    #############

    action_surge = int()
    second_wind = bool()
    fighting_style = int()
    
    ## Gunslinger 
    max_grit = int()
    current_grit = int()

    quickdraw = bool()
    lighting_reload = bool()
    vicious_intent = bool()
    hemorrhaging_critical = bool()
    hemo_damage = int()
    hemo_damage_type = int()  

    #############
    #### Monk ###
    #############
    monk_unarmored_defense = bool()
    martial_arts = bool()
    martial_arts_die = int()

    ki = bool()
    ki_points = int()
    max_ki_points = int()
    flurry_of_blows = bool()
    patient_defense = bool()
    step_of_the_wind = bool()
    unarmored_movement = bool()
    unarmored_movement_bonus = int()

    deflect_missiles = bool()

    slow_fall = bool()

    stunning_strike = bool()

    ki_empowered_strikes = bool()

    stillness_of_mind = bool()

    purity_of_body = bool()

    diamond_soul = bool()
    ## Open Hand

    ## Cobalt Soul

    #############
    ## Paladin ##
    #############
    channel_divinity = bool()
    divine_smite = bool()
    divine_health = bool()
    aura_of_protection = bool()
    aura_of_courage = bool()
    improved_divine_smite = bool()
    cleansing_touch = bool()

    ## Vengeance
    vow_of_enmity = bool()
    vow_of_enmity_target = None
      
    #############
    ### Rogue ###
    #############
    sneak_attack = bool()    
    sneak_attack_damage_die = int()
    sneak_attack_damage_die_count = int()    
    sneak_attack_used = bool() #Only one sneak attack per round

    cunning_action = bool()
    uncanny_dodge = bool()    

    blindsense = bool()
    slippery_mind = bool()
    elusive = bool()
    stroke_of_luck = bool()

    ## Assassin

    assassinate = bool()
    can_assassinate_target = bool()

    # Race
    ## Goliath #    
    stones_endurance = bool()
    stones_endurance_used = bool()

    # NPC properties - specific abilities that are NPC only and require different logic (i.e. multiattack as opposed to Extra Attack)
    multiattack = []
    breath_attack = bool()
    breath_range = int()
    breath_damage_die = int()

    # In-combat properties, reflect status of creature within battle attempt #
    
    starting_xpos = int()
    starting_ypos = int()
    xpos = int() # x co-ordinate
    ypos = int() # y co-ordinate
    zpos = int() # z co-ordinate (flying/vertical)
    initiative_roll = int() # Used to sort combatants in initiative order
    movement_used = bool() # Tracks if Movement step of turn has been used
    action_used = bool() # Tracks if Action step of turn has been used
    bonus_action_used = bool() # Tracks if Bonus Action step of turn has been used
    reaction_used = bool() # Tracks if Reaction step of turn has been used

    prone = bool() # Tracks if creature is prone (requires half movement to stand)
    conscious = bool() # Tracks if creature is conscious
    death_saving_throw_success = int() # Tracks succesful Death Saving Throws
    death_saving_throw_failure = int() # Tracks failed Death Saving Throws
    stabilised = bool() # Tracks stabilisation (i.e. 3 successes)
    alive = bool() # Tracks if creature is still alive

    enlarged = bool() # Tracks whether creature is affected by the Enlarge equipment spell
    hasted = bool() # Tracks whether creature is affected by the Haste equipment spell 
    hasted_bonus_armour = int() # Tracks the bonus armour granted by Haste
    hasted_action = bool() # Tracks whether the creature has a Hasted action
    hasted_action_used = bool() # Tracks whether the creature used their Hasted action
    disengaged = bool() #Has taken the Disengage action and does not provoke opportunity attacks
    dodging = bool() # Has taken the Dodge action and imparts disadvantage on inbound attacks
    
    # Tracks persistent advantage/disadvantage properties
    has_advantage = bool()
    has_disadvantage = bool() 

    # Tracks other miscellaneous conditoins
    head_shotted = bool() #Victim of Gunslinger Head Shot Trick Shot

    # Generic target object, linked to another creature in the find_target function
    target = None

    #Summary fields - for output at end of simulation    
    attacks_hit = int()
    attacks_missed = int()
    total_damage_dealt = int()    
    rounds_fought = int()    

    #Tracks damage built up over an attack action (including weapon damage, bonus damage, crit damage)
    def pending_damage(self):
        if not hasattr(self, "_pending_damage"):
            self._pending_damage = [] 
        return self._pending_damage

class pending_damage():
    pending_damage_type = int()
    pending_damage = int()

# Helper Functions
# Keep functions that need to be accessed from around the program here, as long as they don't require any outside knowledge (i.e. are constructed just from the nature of classes)

def melee_range():
    #Treating default melee weapon range as 5 feet, upped to 8 to avoid clipping issues on corners of grid
    return 8

# Check if Great Weapon Fighting is allowed - must have Fighting Style, and appopriate weapon with the correct properties in both hands
def greatweaponfighting(combatant):
    if (combatant.fighting_style == fighting_style.Great_Weapon_Fighting and 
    ((combatant.main_hand_weapon.two_handed or combatant.main_hand_weapon.versatile) and combatant.offhand_weapon == combatant.main_hand_weapon)) :
        return True
    return False

# Return the class level for a given class attached to the player
def get_combatant_class_level(combatant,combatant_class):
    for class_instance in combatant.player_classes():
        if class_instance.player_class == combatant_class:
            return class_instance.player_class_level

# Returns the total character level for all classes attached to the player (necessary for calculating proficiency and some class features)
def characterlevel(combatant):
    player_level = 0
    for class_instance in combatant.player_classes():
        player_level += class_instance.player_class_level
    return player_level

# Returns the proficiency bonus of the player
def calc_proficiency(combatant):
    prof_calc = 7+characterlevel(combatant)
    return math.floor(prof_calc/4)

# Custom rounding function to ensure we can reliably round values to the nearest 5 feet (for grid calculations)
def round_to_integer(x, base):
    return int(base * round(float(x)/base))

# Return the weighted statistic modifiers 
def strmod(combatant):
    return math.floor((combatant.stats.str-10)/2)

def dexmod(combatant):
    return math.floor((combatant.stats.dex-10)/2)

def intmod(combatant):
    return math.floor((combatant.stats.intel-10)/2)

def wismod(combatant):
    return math.floor((combatant.stats.wis-10)/2)

def conmod(combatant):
    return math.floor((combatant.stats.con-10)/2)

def chamod(combatant):
    return math.floor((combatant.stats.cha-10)/2)

# Rolls a dice (initiates a new random seed on each call) #
def roll_die(die):
    random.seed
    return random.randint(1,die)
