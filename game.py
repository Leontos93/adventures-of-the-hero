import random


class Character:
    def __init__(
        self, name, health=100, max_health=100, attack=10, level=1, experience=0
    ):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.level = level
        self.experience = experience

    def show_stats(self):
        print("Character Stats:")
        print(
            f"Name: {self.name} | Health: {self.health} | Attack: {self.attack} | Level: {self.level} | Experience: {self.experience}"
        )

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage! Remaining Health: {self.health}")

    def attack_enemy(self, enemy):
        enemy.take_damage(self.attack)
        print(f"{self.name} attacks {enemy.name} for {self.attack} damage!")

    def gain_experience(self, exp):
        self.experience += exp
        if self.experience >= 100:
            self.level += 1
            self.experience -= 100
            self.max_health += 20
            self.health = self.max_health
            self.attack += 5
            print(f"{self.name} has reached level {self.level}!")


def create_enemy(player_level):
    enemies = [
        {"name": "Goblin", "health": 30, "attack": 5, "exp": 20},
        {"name": "Orc", "health": 50, "attack": 8, "exp": 35},
        {"name": "Troll", "health": 80, "attack": 12, "exp": 50},
    ]

    enemy_template = random.choice(enemies)

    enemy = Character(
        name=enemy_template["name"],
        health=enemy_template["health"] * player_level,
        attack=enemy_template["attack"] * player_level,
    )

    enemy.exp_reward = enemy_template["exp"] * player_level

    return enemy


def battle(hero, enemy):
    print(f"\nA battle begins: {hero.name} VS {enemy.name}!")
    print("-" * 40)
    hero.show_stats()
    enemy.show_stats()
    print("-" * 40)

    round_num = 1
    while hero.is_alive() and enemy.is_alive():
        print(f"\n--- Round {round_num} ---")

        # Hero's turn
        hero.attack_enemy(enemy)
        if not enemy.is_alive():
            break

        input("\nPress Enter to continue...")

        # Enemy's turn
        enemy.attack_enemy(hero)
        if not hero.is_alive():
            break

        input("\nPress Enter to continue...")
        round_num += 1

    if hero.is_alive():
        print(f"\nVictory! {enemy.name} has been defeated!")
        hero.gain_experience(enemy.exp_reward)
    else:
        print(f"\nDefeat! {hero.name} has fallen in battle...")


# --- Game Start ---
hero = Character("Warrior")
enemy = create_enemy(hero.level)

battle(hero, enemy)

print("\n--- Final Stats ---")
hero.show_stats()
