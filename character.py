import d20
from d20 import roll
import random
import pprint
from random import randint
import data as d

# TODO: Rethink rolls (especially for improvements) Can I reuse the roll function in some way?

class Character():
    def __init__(self):
        """ The base chatracter """

        self.name = 'None'
        self.occupation = 'None'
        self.age = None
        self.gender = 'None'
        self.birthplace = 'None'
        self.residence = 'None'
        self.skills = []
        self.stats = {}


    def generateCharacter(self):
        """ Generate the character """

        # Generate base stats
        for stat in d.stats_list:
            roll = self.rollStats(stat)
            self.stats.update(roll)

        self.age = self.generateAge()
        # self.stats.update(self.age)
        print("Age: " + str(self.age))
        
        self.gender = self.generateGender()
        # self.stats.update(self.gender)
        print("Gender: " + self.gender)

        hit = self.generateHitpoints(self.stats['constitution'], self.stats['size'])
        self.stats.update(hit)
        print("Hit Points: " + str(self.stats['hitpoints']))
        
        magic = self.generateMagicPoints(self.stats['power'])
        self.stats.update(magic)
        print("Magic Points: " + str(self.stats['magicpoints']))

        sanity = self.generateSanityPoints(self.stats['power'])
        self.stats.update(sanity)
        print("Sanity Points: " + str(self.stats['sanity']))

        luck = self.generateLuck()
        self.stats.update(luck)
        print("Luck: " + str(self.stats['luck']))

        movementrate = self.generateMovementRate(self.stats['dexterity'], self.stats['strength'], self.stats['size'])
        self.stats.update(movementrate)
        print("Movement Rate: " + str(self.stats['movementrate']))

        self.ageModifiers()


    def rollStats(self, stat):
        """ Stats rolls (Max 99) """
        roll = d20.roll(d.rolls[stat])
        print(f'Roll: {stat} ({roll})')
        rolled_stat = {stat : roll.total}

        return rolled_stat


    def generateAge(self):
        """ Randomly generate an age between 15 and 90 """
        age = random.randint(15,90)

        return age


    def generateGender(self):
        """ Randomly select Male of Female """
        gender = random.choice(["Male", "Female"])

        return gender


    def generateHitpoints(self, constitution, size):
        """ Hit Points equal SIZ + CON divided by 10 (round down) """
        hitpoints = {'hitpoints': round((int(constitution) + int(size)) / 10)}

        return hitpoints


    def generateLuck(self):
        """ Roll 3D6 multiplied by 5 for Luck """
        luck = self.rollStats('luck')

        return luck


    def generateMagicPoints(self, power):
        """ Magic Points equal one fifth of POW """
        magicpoints = {'magicpoints': round(int(power) / 5)}

        return magicpoints


    def generateSanityPoints(self, power):
        """ Sanity Points equals the POW characteristic """
        sanitypoints = {'sanity': power}

        return sanitypoints


    def generateMovementRate(self, dexterity, strength, size):
        """ calculate movement rate """

        # Both DEX and STR are each less than SIZ: MOV 7
        if (dexterity < size) and (strength < size):
            movementrate = 7

        # Either STR or DEX is equal to or greater than SIZ, or if all are equal: MOV 8
        if (dexterity >= size) or (strength >= size) or (dexterity and strength == size):
            movementrate = 8

        # Both STR and DEX are each greater than SIZ: MOV 9
        if (dexterity and strength) > size:
            movementrate = 9

        movementrate = {'movementrate': movementrate}
        return movementrate


    def improvementRoll(self, stat, check, improvement):
        """ Improvement check, and then apply if successful """
        if int(check) > 1:
            roll = d20.roll(check + d.rolls['percentile'] + 'kh1')
        else:
            roll = d20.roll(check + d.rolls['percentile'])

        print(f'Roll: improvement check ({stat}): {roll}')

        if int(roll.total) > int(self.stats[stat]):
            roll = d20.roll(improvement + d.rolls['improvement'])
            print(f"Roll: improvement roll: {roll}")
            self.modifyStat('education', '+' + str(roll.total))

        else:
            print("Modifier: improvement check failed!")


    def modifyStat(self, stat, modifier):
        """ Modify the stat, based on the modifier passed to it """
        current_stat = self.stats[stat]
        self.stats[stat] = int(self.stats[stat]) + int(modifier)
        print(f"Modifier: {modifier} to {stat} ({current_stat}): {self.stats[stat]}")


    def rerollStat(self, stat, quantity):
        """ Reroll stats """
        rerolls = []
        count = 0
        current_stat = self.stats[stat]

        print(f"Modifier: re-rolling {stat} ({current_stat})")
        
        while(quantity > count):
            reroll = self.rollStats(stat)
            rerolls.append(reroll[stat])
            count = count + 1

        print(f"Modifier: {stat} rerolls: {rerolls}")
        reroll_value = max(rerolls)
        if int(reroll_value) > int(current_stat):
            print(f"Modifier: setting {stat} to {reroll_value}")
            self.stats[stat] = reroll_value
        else:
            print(f"Modifier: Keeping current {stat} ({current_stat})")


    def reduceStats(self, points, stats, allow_zero = False):
        """ Randomly reduce stats between a list of stats, if passed, otherwise, just reduce 1 stat accordingly """
        stats_list = len(stats)
        parts = []
        new_points = points

        if (stats_list > points):
            raise ValueError("Number of parts can't be higher than the number");

        for i in range(1, stats_list + 1):
            if (i == stats_list):
                parts.append(new_points)
                break
            else: 
                remaining_points = randint(0, new_points) if allow_zero else randint(1, (new_points - (stats_list - i)) // 2)

            new_points -= remaining_points
            parts.append(remaining_points)

        random.shuffle(parts)
        
        # to convert lists to dictionary 
        res = {} 
        for key in stats: 
            for value in parts: 
                res[key] = value 
                parts.remove(value) 
                break

        for stat in res:
            self.modifyStat(stat, '-' + str(res[stat]))


    # TODO: def combatValues():
    #     # Determine Damage Bonus & Build by adding STR + SIZ and looking up the result in INvestigators Handbook (p65)


    # TODO: def skillsOccupation():
    #     # Decide Occupation & Allot Points to Skills
    #     # Choose an occupation (Chapter 4) and note the occupation skills and Credit Rating.
    #     # Calculate occupation skill points using the characteristics specified by the occupation.
    #     # Allot these points across the occupation skills, not forgetting to put points into Credit Rating.
    #     # Add points to the base chances written next to each skill on the sheet.
    #     # Information on each skill can be found starting in Chapter 5.


    # TODO: def skillsPersonal():
    #     # Calculate personal interest points by multiplying INT by 2.
    #     # Allot these points to any skills to round out the investigator (not forgetting fighting and firearms skills, if appropriate).
    #     # The number for unarmed combat is your investigator’s Fighting (Brawl) skill.
    #     # Points not allotted are lost!


    # TODO: def determinFinances():
    #     # Look up your investigator’s Credit Rating on Table II: Cash and Assets (page 57) to deterimine Spending Level, Cash on Hand, and Assetts, and write these in.


    # TODO: def gearAndEquipment():
    #     # Write down any important items, weapons, or equipment your investigator possesses.
    #     # Consider useful tems that would normally go with your investigator’s occupation.
    #     # Speak to the Keeper if you are unsure.
    #     # Equipment lists can be found from page 238.
    #     # Weapon lists can be found from page 250.


    # TODO: def backstory():
    #     # Need to work on this


    def ageModifiers(self):
        """
        Apply age modifiers
        """

        if self.age in range(15,20):
            self.modifyStat('strength', '-5')
            self.modifyStat('size', '-5')
            self.modifyStat('education', '-5')
            self.rerollStat('luck', 2)
            
        if self.age in range(20,40):
            self.improvementRoll('education', '1', '1')
            
        if self.age in range(40,50):
            self.modifyStat('appearance', '-5')
            self.modifyStat('movementrate', '-1')
            self.improvementRoll('education', '2', '1')
            
        if self.age in range(50,60):
            self.modifyStat('appearance', '-10')
            self.modifyStat('movementrate', '-2')
            self.improvementRoll('education', '3', '1')
            self.reduceStats(10, ['strength', 'dexterity', 'constitution'])

        if self.age in range(60,70):
            self.modifyStat('appearance', '-10')
            self.modifyStat('movementrate', '-3')
            self.improvementRoll('education', '4', '1')
            self.reduceStats(20, ['strength', 'dexterity', 'constitution'])

        if self.age in range(70,80):            
            self.modifyStat('appearance', '-20')
            self.modifyStat('movementrate', '-4')
            self.improvementRoll('education', '4', '1')
            self.reduceStats(40, ['strength', 'dexterity', 'constitution'])

        if self.age in range(80,91):
            self.modifyStat('appearance', '-25')
            self.modifyStat('movementrate', '-5')
            self.improvementRoll('education', '4', '1')
            self.reduceStats(80, ['strength', 'dexterity', 'constitution'])


if __name__ == '__main__':
    character = Character()
    character.generateCharacter()
