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


hero_1 = Character("Leonid")
hero_1.show_stats()
print(hero_1.is_alive())
hero_1.take_damage(5)
