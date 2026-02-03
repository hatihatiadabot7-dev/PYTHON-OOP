class Hero:
    def __init__(self, name, job, hp, hero_type="hero"):
        self.name = name
        self.job = job
        self.hp = hp
        self.type = hero_type
        print(f"✨ {self.name} memasuki arena!")

    def __str__(self):
        return(f"{self.name} | JOB: {self.job} | HP: {self.hp} | TYPE: {self.type}")

    def is_alive(self):
        return self.hp > 0
    
    def attack(self, enemy):
        print(f"{self.name} Menyerang {enemy.name}")
        

    def take_damage(self, ludah):
        self.hp -= ludah
        print(f"{self.name} terkena ludah sebanyak {ludah} kali!!")
        if self.hp <= 0:
            print(f"{self.name} MATIII")

    def combo(self, enemy):
        print(f"{self.name} Mengulti {enemy.name}")

    def tercombo(self, ludah):
        self.hp -= ludah
        print(f"{self.name} terkena Ultii {ludah} kali!!")
        if self.hp <= 0:
            print(f"{self.name} MATIII")
        

    def bakar(self, enemy):
        print(f"{self.name} membakar {enemy.name} awoakwoakwok")

    def terbakar(self, api):
        self.hp -= api
        print(f"{self.name} terkena bakaran sebesar {api} DAMAGE!!!")
        if self.hp <= 0:
            print(f"{self.name} MATIII")

    def semekdon(self, enemy):
        print(f"{self.name} MENYEMEKDON {enemy.name} awoakwoakwok!!")

    def tersemekdon(self, semekdon):
        self.hp -= semekdon
        print(f"{self.name} DISEMEKDONN {semekdon}KALII!!!")
        if self.hp <= 0:
           self.hp = 0
        print(f"{self.name} MATIII")
        print("--- PERMAINAN SELESAI ---")
        print("BOYAAHHHH...")
        print("======================")
    
    def regen(self, odading):
        self.hp += odading
        print(f"{self.name} mendapatkan odading +{odading}")
       

sopo = Hero("Sopo", "Tank", 100)
dontol = Hero("Dontol", "Tank", 100)
adit = Hero("Adit", "Assasin", 100)
ucup = Hero("Ucup", "Fighter", 100)
adel = Hero("Adel", "Mage", 100)   
goblin = Hero("Goblin", "Monster", 50, "Normal")
yinlong = Hero("Yinlongg", "Monster", 100, "Raja")

print("======================================")
print(sopo)
print(dontol)
print(adit)
print(ucup)
print(adel)
print(goblin)
print(yinlong)

print("=======================================")
print("--- BATTLE START ---")
sopo.attack(goblin)
goblin.take_damage(5)
dontol.attack(goblin)
goblin.take_damage(5)
adit.attack(goblin)
goblin.take_damage(10)
ucup.attack(goblin)
goblin.take_damage(10)
adel.combo(goblin)
goblin.tercombo(20)
print(goblin)
yinlong.bakar(adel)
adel.terbakar(90)
print(adel)
adel.regen(25)
print(adel)
sopo.combo(yinlong)
ucup.combo(yinlong)
yinlong.tercombo(20)
print(yinlong)
yinlong.attack(adit)
adit.take_damage(25)
print(adit)
adit.attack(yinlong)
yinlong.take_damage(10)
adel.combo(yinlong)
adit.combo(yinlong)
sopo.combo(yinlong)
yinlong.tercombo(60)
print(yinlong)
yinlong.regen(25)
print(yinlong)
yinlong.bakar(adel)
adel.terbakar(35)
ucup.semekdon(yinlong)
yinlong.tersemekdon(35)




