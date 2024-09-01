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