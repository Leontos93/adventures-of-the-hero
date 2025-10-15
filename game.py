class Character:
    def __init__(
        self, name, health=100, max_health=100, atack=10, level=1, experience=0
    ):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.atack = atack
        self.level = level
        self.experience = experience

    def show_stats(self):
        print(f"Статистика персонажу:")
        print(
            f"Ім'я: {self.name} Здоров'я: {self.health} Сила атаки: {self.atack} Рівень: {self.level} Досвід: {self.experience}"
        )

    def is_alive(self):
        return self.health > 0


hero_1 = Character("Leonid")
hero_1.show_stats()
print(hero_1.is_alive())
