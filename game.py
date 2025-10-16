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
        print(f"Статистика персонажу:")
        print(
            f"Ім'я: {self.name} Здоров'я: {self.health} Сила атаки: {self.attack} Рівень: {self.level} Досвід: {self.experience}"
        )

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} отримав {damage} шкоди! Здоров'я: {self.health}")

    def attack_enemy(self, enemy):
        enemy.take_damage(self.attack)
        print(f"{self.name} атакує {enemy.name} на {self.attack} шкоди!")

    def gain_experience(self, exp):
        self.experience += exp
        if self.experience >= 100:
            self.level += 1
            self.experience -= 100
            self.max_health += 20
            self.health = self.max_health
            self.attack += 5
            print(f"{self.name} досяг рівня {self.level}!")


def create_enemy(player_level):
    enemies = [
        {"name": "Гоблін", "health": 30, "attack": 5, "exp": 20},
        {"name": "Орк", "health": 50, "attack": 8, "exp": 35},
        {"name": "Тролль", "health": 80, "attack": 12, "exp": 50},
    ]

    enemy_template = random.choice(enemies)

    enemy = Character(
        name=enemy_template["name"],
        health=enemy_template["health"] * player_level,
        attack=enemy_template["attack"] * player_level,
    )

    enemy.exp_reward = enemy_template["exp"] * player_level

    return enemy


"""hero = Character("Герой")
for i in range(3):
    enemy = create_enemy(hero.level)
    enemy.show_stats()
    print(f"Нагорода: {enemy.exp_reward} досвіду\n")
hero = Character("Герой")
enemy = create_enemy(hero.level)
enemy.show_stats()
hero_1 = Character("Leonid")
enemy_1 = Character("Гоблін")
hero_1.attack_enemy(enemy_1)
enemy_1.show_stats()
hero_1.show_stats()
print(hero_1.is_alive())
hero_1.take_damage(5)"""
