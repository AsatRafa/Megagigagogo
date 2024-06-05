from random import randint

class Person(object):
    def __init__(self, name="Undefined", lvl=1) -> None:
        self._name = name
        self._MaxHP = 100 + (lvl-1)*5
        self._CurrentHP = self._MaxHP        
        self._lvl = lvl
        self._MaxXP = 100
        self._CurrentXP = 0
        self._Damage = 10
        self._Crit = 2
        self._MaxMorale = 1
        self._CurrentMorale = self._MaxMorale
        self._recoveryHP = 1
        self._imprPoints = 3
        self._critProb = 0.1

        self._Strenght = 1 #Сила
        self._Dexterity = 1 #Ловкость
        self._Constitution = 1 #Выносливость
        self._Intelligence = 1 #Интелект
        self._Wisdom = 1 #Мудрость
        self._Charisma = 1 #Обаяние
        self._Lucky = 1 #Удача

    
    @property
    def critProb(self):
        print("getter method")
        return self._critProb

    @critProb.setter
    def imprPoints(self, cp):
        print("setter method")
        self._critProb = cp
    

    @property
    def imprPoints(self):
        print("getter method")
        return self._imprPoints

    @imprPoints.setter
    def imprPoints(self, nip):
        print("setter method")
        self._imprPoints = nip
    

    @property
    def CurrentMorale(self):
        print("getter method")
        return self._CurrentMorale

    @CurrentMorale.setter
    def CurrentMorale(self, ncr):
        print("setter method")
        if ncr < self.MaxMorale/2:
            self._CurrentMorale = self.MaxMorale/2
        else:
            self._CurrentMorale = ncr
    
    @property
    def MaxMorale(self):
        print("getter method")
        return self._MaxMorale


    @property
    def recoveryHP(self):
        print("getter method")
        return self._recoveryHP

    @recoveryHP.setter
    def CurrentMorale(self, nrhp):
        print("setter method")
        self._recoveryHP = nrhp

    @property
    def name(self):
        print("getter method")
        return self._name

    @name.setter
    def name(self, nName):
        print("setter method")
        self._name = nName

    @property
    def lvl(self):
        print("getter method")
        return self._lvl

    @lvl.setter
    def lvl(self, nlvl):
        print("setter method")
        self._lvl = nlvl

    @property
    def CurrentXP(self):
        print("getter method")
        return self._CurrentXP

    @CurrentXP.setter
    def CurrentXP(self, ncxp):
        print("setter method")
        self._CurrentXP = ncxp

    @property
    def MaxXP(self):
        print("getter method")
        return self._MaxXP

    @MaxXP.setter
    def MaxXP(self, nmxp):
        print("setter method")
        self._MaxXP = nmxp
    
    @property
    def MaxHP(self):
        print("getter method")
        return self._MaxHP

    @MaxHP.setter
    def MaxHP(self, nmhp):
        print("setter method")
        self._MaxHP = nmhp

    @property
    def CurrentHP(self):
        print("getter method")
        return self._CurrentHP

    @CurrentHP.setter
    def CurrentHP(self, nchp):
        print("setter method")
        if nchp >= self.MaxHP:
            self._CurrentHP = self.MaxHP
        elif nchp > 0 and nchp < self.MaxHP:
            self._CurrentHP = nchp
        else:
            self._CurrentHP = 0
    
    @property
    def Damage(self):
        print("getter method")
        return self._Damage

    @Damage.setter
    def Damage(self, ndam):
        print("setter method")
        self._Damage = ndam

    @property
    def Strenght(self):
        print("getter method")
        return self._Strenght

    @Strenght.setter
    def lvl(self, ns):
        print("setter method")
        self._Strenght = ns

    @property
    def Dexterity(self):
        print("getter method")
        return self._Dexterity

    @Dexterity.setter
    def Dexterity(self, nd):
        print("setter method")
        self._Dexterity = nd

    @property
    def Intelligence(self):
        print("getter method")
        return self._Intelligence

    @Intelligence.setter
    def Intelligence(self, ni):
        print("setter method")
        self._Intelligence = ni

    @property
    def Lucky(self):
        print("getter method")
        return self._Lucky

    @Lucky.setter
    def Lucky(self, nl):
        print("setter method")
        self._Lucky = nl

    @property
    def Constitution(self):
        print("getter method")
        return self._Constitution

    @Constitution.setter
    def Constitution(self, nc):
        print("setter method")
        self._Constitution = nc

    @property
    def Wisdom(self):
        print("getter method")
        return self._Wisdom

    @Wisdom.setter
    def Wisdom(self, nw):
        print("setter method")
        self._Wisdom = nw

    @property
    def Charisma(self):
        print("getter method")
        return self._Charisma

    @Charisma.setter
    def Charisma(self, nc):
        print("setter method")
        self._Charisma = nc
    
    def take_damage(self, dmg):
        self.CurrentHP(self.CurrentHP-dmg)
        self.is_dead()
    
    def is_dead(self):
        if self._CurrentHP == 0:
            print(f"{self.name} is dead!")
        return 1
    
    def addXP(self, xp):
        self.CurrentXP(self.CurrentXP+xp)

    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"Level: {self.lvl} (exp: {self.CurrentXP}/{self.MaxXP})")
        print(f"Health Point: {self.CurrentHP}/{self.MaxHP}")
        print(f"Damage: {self.Damage}")
        print(f"Attributes: Streng({self.Strenght}), Dext({self.Dexterity}), Intel({self.Intelligence}), Const({self.Constitution}), Wisd({self.Wisdom}), Charis({self.Charisma}), Lucky({self.Lucky})")
        print(f"Improvement points: {self.imprPoints}")


class Hero(Person):
    def __init__(self, name="Megab", lvl=1) -> None:
        super().__init__(name, lvl)
        self._MaxHP = 100 + (self._lvl - 1)*5 + (self._Strenght - 1)*5 + (self._Constitution - 1)*9
        self._CurrentHP = self._MaxHP
        self._Damage = (10 + (self._lvl - 1) + (self._Strenght - 1)*5)*self._CurrentMorale
        self._critProb = 0.1 + (self._Lucky-1)*0.01 + (self._lvl-1)*0.001

        





    def get_exp(self, exp):
        self.CurrentXP(self.CurrentXP+exp)
        self.next_lvl()

    def next_lvl(self):
        if self.CurrentXP >= self.MaxXP:
            self.CurrentXP(self.CurrentXP - self.MaxXP)
            self.lvl(self.lvl + 1)
            self.imprPoints(self.imprPoints + 2)
    
    def points_distribution(self, numChar):
        if self.imprPoints != 0:
            if numChar == 1:
                self.Strenght(self.Strenght+1)
                self.imprPoints(self.imprPoints-1)
            elif numChar == 2:
                self.Dexterity(self.Dexterity+1)
                self.imprPoints(self.imprPoints-1)
            elif numChar == 3:
                self.Intelligence(self.Intelligence+1)
                self.imprPoints(self.imprPoints-1)
            elif numChar == 4:
                self.Constitution(self.Constitution+1)
                self.imprPoints(self.imprPoints-1)
            elif numChar == 5:
                self.Wisdom(self.Wisdom+1)
                self.imprPoints(self.imprPoints-1)
            elif numChar == 6:
                self.Charisma(self.Charisma+1)
                self.imprPoints(self.imprPoints-1)
            elif numChar == 7:
                self.Lucky(self.Lucky+1)
                self.imprPoints(self.imprPoints-1)

    
class Enemy(Person):
    def __init__(self, name = "Gobo", lvl = 1):
        super().__init__(name, lvl)
        self._lvl = lvl
        
        self._Charisma = randint(1, self._lvl)
        self._Constitution = randint(1, self._lvl)
        self._Dexterity = randint(1, self._lvl)
        self._Intelligence = randint(1, self._lvl)
        self._Lucky = randint(1, self._lvl)
        self._Strenght = randint(1, self._lvl)
        self._Wisdom = randint(1, self._lvl)
        
        self._MaxHP = randint(0.1, 1.9)*100 + (self._lvl - 1)*5 + (self._Strenght - 1)*5 + (self._Constitution - 1)*9
        self._CurrentHP = self._MaxHP
        self._Damage = (randint(0.1, 1.9)*10 + (self._lvl - 1) + (self._Strenght - 1)*5)*self._CurrentMorale
        self._critProb = 0.1 + (self._Lucky-1)*0.01 + (self._lvl-1)*0.001


