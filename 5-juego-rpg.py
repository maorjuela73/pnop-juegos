import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        print(f"{self.name} ataca a {enemy.name} y le inflige {damage} de daño.")
        enemy.take_damage(damage)

    def __str__(self):
        return f"{self.name} ({self.health} HP, {self.attack} ATK)"

class Ability:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def use(self, character, enemy):
        damage = random.randint(0, self.damage)
        print(f"{character.name} utiliza {self.name} y le inflige {damage} de daño a {enemy.name}.")
        enemy.take_damage(damage)

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        print(f"Comienza la batalla: {self.player.name} vs {self.enemy.name}")
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.attack_enemy(self.enemy)
            if self.enemy.is_alive():
                self.enemy.attack_enemy(self.player)

        if self.player.is_alive():
            print(f"{self.player.name} ha ganado la batalla.")
        else:
            print(f"{self.enemy.name} ha ganado la batalla.")

if __name__ == "__main__":
    # Crear personajes y habilidades
    player = Character("Héroe", 100, 20)
    enemy = Character("Monstruo", 80, 15)
    fireball = Ability("Bola de Fuego", 30)
    lightning_strike = Ability("Golpe de Rayo", 25)

    # Asignar habilidades al jugador
    player.abilities = [fireball, lightning_strike]

    # Comenzar la batalla
    battle = Battle(player, enemy)
    battle.start_battle()
