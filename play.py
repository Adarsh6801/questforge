from domain.character import Character

if __name__ == "__main__":
    hero=Character("Aria", 100, 15)
    globlin=Character("Globin", 30, 5)
    
    print(hero.describe())
    print(globlin.describe())
    
    
    hero.attack(globlin)
    print(globlin.describe())
    
    adarsh=Character("Adarsh", 100, 12)
    abhinav=Character("Abhinav", 100, 15)
    print("----Battle 2 Begins with Adarsh And Abhinav----")
    abhinav.attack(adarsh)
    print(adarsh.describe())
    abhinav.attack(adarsh)
    print(adarsh.describe())
    adarsh.attack(abhinav)
    print(abhinav.describe())
    adarsh.attack(abhinav)
    print(abhinav.describe())
    adarsh.heal(20)
    print(adarsh.describe())
    abhinav.attack(adarsh)
    print(adarsh.describe())
    abhinav.attack(adarsh)
    print(adarsh.describe())
    abhinav.attack(adarsh)
    print(adarsh.describe())
    if adarsh.health > abhinav.health:
        print(f"{adarsh.name} wins the battle!")
    else:
        print(f"{abhinav.name} wins the battle!")