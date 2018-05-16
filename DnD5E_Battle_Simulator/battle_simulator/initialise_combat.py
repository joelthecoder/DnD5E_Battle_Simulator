#Explicit imports

#Implicit imports
from .classes import *
from .combat_functions import *

#Other imports


def reset_combatants(init_combatants):
    #Initialise Battle
    for combatant in init_combatants:                   

        # Reset creature values #
        combatant.alive = True
        combatant.death_saving_throw_failure = 0
        combatant.death_saving_throw_success = 0
        combatant.conscious = True
        combatant.prone = False
        combatant.current_health = combatant.max_health
        combatant.enlarged = False        # Need a better wayto handle this        
        combatant.hasted = False
        combatant.hasted_bonus_armour = 0
        combatant.hasted_action = False
        combatant.hasted_action_used = False
        combatant.action_surge = 0
        combatant.extra_attack = 0
        
        # Clear any pending damage against the combatant that was not resolved (i.e. damage dealt via crit to unconscious player doesn't get deducted from hp)
        combatant.pending_damage().clear()

        # Reset weapons
        for weap in combatant.weapon_inventory():
            weap.ruined = False
            weap.broken = False
            weap.current_ammo = weap.ammunition
        
        # Set currently equipped weapon to first weapon in inventory
        combatant.current_Weapon = combatant.weapon_inventory()[0]

        # Reset equipment
        for eq in combatant.equipment_inventory():
            eq.current_charges = eq.max_charges

        # Hemorraging Critical tracking
        combatant.hemo_damage = 0        
        combatant.hemo_damage_type = 0

        #Setup feats
        combatant.luck_uses = 0
        for ft in combatant.creature_feats():
            if ft == feat.Sharpshooter:
                combatant.sharpshooter = True
                combatant.use_sharpshooter = False
            if ft == feat.Great_Weapon_Master:
                combatant.great_weapon_master = True
                combatant.use_great_weapon_master = False
            if ft == feat.Lucky:
                combatant.luck_uses = 3

        # Set up class features (i.e. Rage, Sneak Attack, innate abilities)
        initialise_class_features(combatant)      
                        
        # Set up spellslots
        initialise_class_spellslots(combatant)           
                
        # Racial Features
        # Goliath
        if combatant.race == race.Goliath:        
            combatant.stones_endurance = True
            combatant.stones_endurance_used = False    

        ### monsters###
        if combatant.creature_type == creature_type.Monster:
            if combatant.monster_type == monster_type.Ancient_Black_Dragon:
                combatant.multiattack = ["Bite","Claw","Claw"]
                combatant.breath_attack = True
                combatant.breath_damage_die = 8
                combatant.breath_range = 90               

            ### Trinket ###
            if combatant.monster_type == monster_type.Bear:
                combatant.multiattack = ["Bite","Claw"]

            ### Doty ###
            if combatant.monster_type == monster_type.Doty:                            
                combatant.multiattack = ["Bash","Headbutt"]

            ### Hill Giant
            if combatant.monster_type == monster_type.Hill:                            
                combatant.multiattack = ["Greatclub","Greatclub"]
                
def initialise_class_features(combatant):
    ### Initialise Class Abilities ###        
    for class_instance in combatant.player_classes():
        #############
        # Barbarian #
        #############
        if class_instance.player_class == player_class.Barbarian:
            # Rage (1st level)
            if class_instance.player_class_level >= 1:
                combatant.canrage = True
                combatant.raging = False
                # Number of rounds rage has been up for
                combatant.rage_duration = 0
                # Number of rounds rage can be sustained for
                combatant.max_rage_duration = 10 
                #+2 Rage Damage (1st through 8th)
                combatant.ragedamage = 2
            # Reckless Attack (2nd level)
            if class_instance.player_class_level >= 2:
                combatant.reckless = True        
                combatant.use_reckless = False
                # Danger Sense (2nd level)        
                combatant.saves.dex_adv = True                
            # Extra Attack (+1 at 5th level)
            if class_instance.player_class_level >= 5:
                if combatant.extra_attack == 0:
                    combatant.extra_attack = 1
            # Feral Instinct (7th level)
            if class_instance.player_class_level >= 7:
                combatant.feral_instinct = True
            # Brutal Critical (1 die, 9th level)
            if class_instance.player_class_level >= 9:
                combatant.brutal_critical = True
                combatant.brutal_critical_dice = 1
                #+3 Rage Damage (9th through 16th)
                combatant.ragedamage = 3
            # Relentless (11th level)
            if class_instance.player_class_level >= 11:
                combatant.relentless_rage = True
                combatant.relentless_rage_DC = 10        
            # Brutal Critical (2 die, 13th level)
            if class_instance.player_class_level >= 13:
                combatant.brutal_critical_dice = 2
            if class_instance.player_class_level >= 16:
                #+3 Rage Damage (9th through 16th)
                combatant.ragedamage = 4
            # Brutal Critical (3 die, 17th level)
            if class_instance.player_class_level >= 17:
                combatant.brutal_critical_dice = 3
                            
            ## Barbarian Subclasses ##
            # Path of the Beserker
            if class_instance.player_subclass == player_subclass.Beserker:
                # Frenzy (3rd level)
                if class_instance.player_class_level >= 3:
                    combatant.frenzy = True
                # Retaliation (14th level)
                if class_instance.player_class_level >= 14:
                    combatant.retaliation = True

            # Path of the Zealot
            if class_instance.player_subclass == player_subclass.Zealot:
                # Divine Fury (3rd level, 1d6+half barb level to first attack each turn while raging)
                if class_instance.player_class_level >= 3:
                    combatant.divine_fury = True
                    combatant.divine_fury_damage_type = damage_type.Necrotic
                # Fanatical Focus (6th level, reroll one failed save per rage, must take second roll)
                if class_instance.player_class_level >= 6:
                    combatant.fanatical_focus = True
                # Zealous Presence (10th level, once per LR advantage on attacks/saving throws to 10 creatures in 60 feet as bonus action until end of next turn)
                if class_instance.player_class_level >= 10:
                    combatant.zealous_presence = True
                # Rage Beyond death (14th level, while raging, fall below 0 you don't go unconscious - still make Death Saving Throws)
                if class_instance.player_class_level >= 14:
                    combatant.rage_beyond_death = True


        #############
        ## Fighter ##
        #############
        if class_instance.player_class == player_class.Fighter:
            # Action surge (1 at 2nd level
            if class_instance.player_class_level >= 2:
                combatant.action_surge += 1
            # Action surge (2 at 17th level)
            if class_instance.player_class_level >= 17:
                combatant.action_surge += 1

            # Extra Attack (+1 at 5th level)
            if class_instance.player_class_level >= 5:
                combatant.extra_attack = 1
            # Extra Attack (+1 at 11th level)
            if class_instance.player_class_level >= 11:
                combatant.extra_attack = 2
            # Extra Attack (+1 at 20th level)
            if class_instance.player_class_level >= 20:
                combatant.extra_attack = 3
            
            # Second Wind (1 use at 1st level)
            if class_instance.player_class_level >= 1:
                combatant.second_wind = True                        
        
            ## Fighter Subclasses ##
            # Gunslinger (examine profiencies for Firearm proficiency, use fighter levels to determine abilities)        
            if class_instance.player_subclass == player_subclass.Gunslinger:
                # Grit (3rd level)
                combatant.max_grit = wismod(combatant) #Some debate as to whether this should be Int or Wis (Int was used by Percy in some fights)
                combatant.current_grit = combatant.max_grit

                #Quickdraw (7th level)
                if class_instance.player_class_level >= 7:
                    combatant.quickdraw = True
                #Lightning Reload (15th level)
                if class_instance.player_class_level >= 15:
                    combatant.lighting_reload = True        
                #Vicious Intent (18th level)
                if class_instance.player_class_level >= 18:
                    combatant.vicious_intent = True       
                #Hemorrhaging Critical (20th level)
                if class_instance.player_class_level >= 20:
                    combatant.hemorrhaging_critical = True
            
        #############
        ### Rogue ###
        #############
        if class_instance.player_class == player_class.Rogue:
            # Sneak Attack
            if class_instance.player_class_level >= 1:
                combatant.sneak_attack = True
                combatant.sneak_attack_damage_die = 6
                combatant.sneak_attack_damage_die_count = int(round(class_instance.player_class_level/2))

            # Cunning Action (Dash/Hide/Disengage as Bonus)
            if class_instance.player_class_level >= 2:
                combatant.cunning_action = True
            # Uncanny Dodge (Use reaction to halve damage from melee strike)
            if class_instance.player_class_level >= 5:
                combatant.uncanny_dodge = True
            # Evasion (Fail Dex save = half damage, succeed = 0)
            if class_instance.player_class_level >= 7:
                combatant.evasion = True
            # Blindsense (always detect hidden/invis creatures in 10 feet)
            if class_instance.player_class_level >= 14:
                combatant.blindsense = True
            # Slippery Mind (prof in Wisdom saving throws)
            if class_instance.player_class_level >= 15:
                combatant.slippery_mind = True
            # Elusive (no attacks have advantage against you while not incapacitated)
            if class_instance.player_class_level >= 18:
                combatant.elusive = True
            # Stroke of Luck (any miss can hit, any fail check can critically succeed, recharge short/long rest)
            if class_instance.player_class_level >= 20:
                combatant.elusive = True

            ## Rogue Subclasses ##
            # Assassin
            if class_instance.player_subclass == player_subclass.Assassin:
                if class_instance.player_class_level >= 3:
                    combatant.assassinate = True

        #############
        ## Paladin ##
        #############
        if class_instance.player_class == player_class.Paladin:
            # Divine Smite (2nd level)
            if class_instance.player_class_level >= 2:
                combatant.divine_smite = True
                # Add Divine Smite to combatants spell-book
                add_divine_smite = True
                for existing_spell in combatant.spell_list():
                    if existing_spell.name == "Divine Smite":
                        add_divine_smite = False
                if add_divine_smite: 
                    divine_smite = spell()
                    init_spell(divine_smite,"Divine Smite",1,6,8,2,damage_type.Radiant,8,1,8,1,race.Undead,0)
                    combatant.spell_list().append(divine_smite)

            # Channel Divinity
            if class_instance.player_class_level >= 3: 
                combatant.channel_divinity = True

            # Extra Attack (5th level)
            if class_instance.player_class_level >= 5:
                # Extra attacks from multiclassing do not stack, only give one attack
                if combatant.extra_attack == 0:
                    combatant.extra_attack = 1

            # Improved Divine Smite (14th level)
            if class_instance.player_class_level >= 14:
                combatant.improved_divine_smite = True   
                
            ## Paladin Subclasses ##
            # Oath of Vengeance
            if class_instance.player_subclass == player_subclass.Vengeance:
                if class_instance.player_class_level >= 3:
                    combatant.vow_of_enmity = True
                    combatant.vow_of_enmity_target = None

def initialise_class_spellslots(combatant):
    reset_spellslots(combatant)
    ### Set maximum number of spellslots based on spells available to classes ###        
    for class_instance in combatant.player_classes():
        
        ### Paladin Spellslots ###
        if class_instance.player_class == player_class.Paladin:
            #if class_instance.player_class_level = 1:
            if class_instance.player_class_level >= 2:
                add_spellslot(combatant,1,2)                
            if class_instance.player_class_level >= 3:
                add_spellslot(combatant,1,1)
            if class_instance.player_class_level >= 4:
                add_spellslot(combatant,1,1)
            if class_instance.player_class_level >= 5:
                add_spellslot(combatant,2,2)
            #if class_instance.player_class_level >= 6:
            if class_instance.player_class_level >= 7:
                add_spellslot(combatant,2,1)
            #if class_instance.player_class_level >= 8:
            if class_instance.player_class_level >= 9:
                add_spellslot(combatant,3,2)
            #if class_instance.player_class_level >= 10:
            if class_instance.player_class_level >= 11:
                add_spellslot(combatant,3,1)
            #if class_instance.player_class_level >= 12:
            if class_instance.player_class_level >= 13:
                add_spellslot(combatant,4,1)
            #if class_instance.player_class_level >= 14:
            if class_instance.player_class_level >= 15:
                add_spellslot(combatant,4,1)
            #if class_instance.player_class_level >= 16:
            if class_instance.player_class_level >= 17:
                add_spellslot(combatant,4,1)
                add_spellslot(combatant,5,1)
            #if class_instance.player_class_level >= 18:
            if class_instance.player_class_level >= 19:
                add_spellslot(combatant,5,1)
            #if class_instance.player_class_level >= 20:

        ### Druid Spellslots ###
        if class_instance.player_class == player_class.Druid:
            if class_instance.player_class_level == 1:
                add_spellslot(combatant,1,2)
            if class_instance.player_class_level >= 2:
                add_spellslot(combatant,1,1)                     

def add_spellslot(combatant,spell_level,spellslot_count):
    for existing_spellslot in combatant.spellslots():
        if existing_spellslot.level == spell_level:
            existing_spellslot.current += spellslot_count
            existing_spellslot.max += spellslot_count
            return

    #Slot doesn't exist, create a new one
    newslot = spellslot()
    newslot.level = spell_level    
    newslot.current = spellslot_count
    newslot.max = spellslot_count
    combatant.spellslots().append(newslot)

def reset_spellslots(combatant):
    combatant.spellslots().clear()
        
def set_starting_positions(combatants):
    for combatant in combatants:
        if combatant.name == "Grog":
            combatant.xpos = 50
            combatant.ypos = 50
        if combatant.name == "Vax":
            combatant.xpos = 75
            combatant.ypos = 75
        if combatant.name == "Percy":
            combatant.xpos = 25
            combatant.ypos = 25

def init_spell(new_spell,name,min_spellslot_level,max_spellslot_level,damage_die,damage_die_count,damage_type,damage_die_per_spell_slot,damage_die_count_per_spell_slot,bonus_damage_die,bonus_damage_die_count,bonus_damage_target,range):
    new_spell.name = name
    new_spell.min_spellslot_level = min_spellslot_level
    new_spell.max_spellslot_level = max_spellslot_level
    new_spell.damage_die = damage_die 
    new_spell.damage_die_count = damage_die_count 
    new_spell.damage_type = damage_type 
    new_spell.damage_die_per_spell_slot = damage_die_per_spell_slot 
    new_spell.damage_die_count_per_spell_slot = damage_die_count_per_spell_slot 
    new_spell.bonus_damage_die = bonus_damage_die 
    new_spell.bonus_damage_die_count = bonus_damage_die_count 
    new_spell.bonus_damage_target = bonus_damage_target 
    new_spell.range = range