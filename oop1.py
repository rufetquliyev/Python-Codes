# Silah classı hazırlayın. Həmin classa string dəyərə sahib metal attributu verin. 
# Qarşılıq üçün hərhansı bir metal adı seçə bilərsiniz
    # 1. _init__() funksiyasında güllə sayını qeyd edəcək şəkildə qurun
    # 2. Silah classını inherit edib Avtomat və snayper classi yaradın.
    # 3. Həmin classlara ayrı-aryılıqda power dǝyǝri verin.
    # 4. Soldier classını yenidən hazırlayıb yaradacağınız objectǝ___init__() funksiyası vasitəsilə 
    # Avtomat və snayper classlarıyla yaratdığınız objectləri verin və self.weapon olaraq qeyd edin. Soldier atəş 
    # açdıqda rəqibinin canını weaponun poweri qədər azaltsın
    # 5. Atəş açdıqda silahın güllə sayından 1 çıxın
    # 6. Əsgər objectlərini len() funksiyası içində işlətdikdə silahının güllə sayını göstərən special method yazın.
    # Bunun üçün ____len__() special methodu istifadə olunacaq.

class Gun:
    metal = 'Polad'
    def __init__(self, bullets_count):
        self.bullets_count = bullets_count
        
class Automaton(Gun):
    power = 25

class Sniper(Gun):
    power = 90
    
class Soldier(Gun):
    health = 100
    def __init__(self, name, weapon):
        self.weapon = weapon
        self.name = name
    def fire(self, enemy):
        enemy.health -= self.weapon.power
        self.weapon.bullets_count -= 1

gun1 = Sniper(5)
gun2 = Automaton(15)

rufet = Soldier('Rufet', gun1)
ferid = Soldier('Ferid', gun2)

rufet.fire(ferid)
print(ferid.health)
print(rufet.weapon.bullets_count)