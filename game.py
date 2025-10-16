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


def battle(hero, enemy):
    print(f"\nРозпочався бій: {hero.name} VS {enemy.name}!")
    print("-" * 40)
    hero.show_stats()
    enemy.show_stats()
    print("-" * 40)
    round_num = 1
    while True:
        print(f"\n--- Раунд {round_num} ---")
        hero.attack_enemy(enemy)
        if not enemy.is_alive():
            break
        else:
            input(f"\nНатисни Enter для продовження...")
        enemy.attack_enemy(hero)
        if not hero.is_alive():
            break
        else:
            input(f"\nНатисни Enter для продовження...")
        round_num += 1
    if hero.is_alive():
        print(f"\nПеремога! {enemy.name} переможений!")
        hero.gain_experience(enemy.exp_reward)
    else:
        print(f"\nПоразка! {hero.name} загинув у бою...")


hero = Character("Воїн")
enemy = create_enemy(hero.level)
battle(hero, enemy)
hero.show_stats()
