class Character:
    def __init__(self, name:str, health:int,attack_power:int):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        
    def describe(self):
        return f"{self.name} has {self.health} HP and {self.attack_power} attack."
    
    def attack(self, target:"Character")->None:
        target.health-=self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        
    def heal(self, amount:int)->None:
        self.health+=amount
        print(f"{self.name} heals for {amount} HP!")
    