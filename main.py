## Consol game
# Класс Hero:
# Атрибуты:
# Имя (name)
# Здоровье (health), начальное значение 100
# Сила удара (attack_power), начальное значение 20
# Методы:
# attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# is_alive(): возвращает True, если здоровье героя больше 0, иначе False

# Класс Game:
# Атрибуты:
# Игрок (player), экземпляр класса Hero
# Компьютер (computer), экземпляр класса Hero
# Методы:
# start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника)
# и объявляет победителя.

import random


class Hero:
    def __init__ (self, name, health, attack_power):
      self.name = name
      self.health = health
      self.attack_power = attack_power

    def attack(self, other):
      # print (f"Остаток здоровья {other.name} перед атакой = {other.health}.")
      print(f"Сила удара {self.name} = {self.attack_power}")
      other.health -= self.attack_power
      self.attack_power = random.randint(1, 20)
      print(f"Остаток здоровья {other.name} после атаки = {other.health}.")
      print(f"Сила удара следующего хода {self.name} = {self.attack_power}.")

    def is_alive(self):
      if self.health > 0:
        return True

    def info_health(self, other):
      print()
      print(f"Игрок {self.name}:\n"
            f"Здоровье = {self.health} единиц.\n"
            f"Сила удара = {self.attack_power} единиц.\n")
      print(f"Игрок {other.name}:\n"
            f"Здоровье = {other.health} единиц.\n"
            f"Сила удара = {other.attack_power} единиц.\n")


class Game:
    def __init__(self, player_name):
      self.player = Hero(player_name, 100, 20)
      self.computer = Hero("Computer", 100, 20)

    def start(self):
      print("Начало игры!\n")
      print(f"Игрок {self.player.name}:\n"
            f"Здоровье = {self.player.health} единиц.\n"
            f"Сила удара = {self.player.attack_power} единиц.\n")
      print(f"Игрок {self.computer.name}:\n"
            f"Здоровье = {self.computer.health} единиц.\n"
            f"Сила удара = {self.computer.attack_power} единиц.\n")

      while self.player.is_alive() and self.computer.is_alive():

        # Игрок атакует компьютер
        print(f"В атаку! Игрок {self.player.name} атакует {self.computer.name}!")
        self.player.attack(self.computer)
        if not self.computer.is_alive():
          print(f"\nУРА!!! УРА!!! УРА!!!\n"
                f"{self.player.name} победил {self.computer.name}!!!")
          break
        self.player.info_health(self.computer)

        # Компьютер атакует игрока
        print(f"Внимание! Игрок {self.computer.name} атакует {self.player.name}!")
        self.computer.attack(self.player)
        if not self.player.is_alive():
          print(f"\nФортуна отвернулась, увы!\n"
                f"{self.player.name} проиграл {self.computer.name}!\n"
                f"Удачи в следующих сражениях!!!")
          break
        self.computer.info_health(self.player)

if __name__ == "__main__":
  player_name = "Ivan" #input ("Введите имя своего игрока :")
  game = Game(player_name)
  game.start()
