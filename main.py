from character import Character
from spell import Fireball, IceLance, LightningBolt


def main():
    hero = Character(10, 12, 15, 18, 20, 14, 'mage')
    
    print(f"Класс: {hero.character_class}")
    print(f"Здоровье: {hero.max_health}")
    print(f"Урон: {hero.damage}")
    print(f"Защита: {hero.defense}")
    print(f"Мана: {hero.mana}")
    hero.add_spell(Fireball())
    hero.add_spell(IceLance())
    hero.add_spell(LightningBolt())
    print("\nПрименяем Fireball...")
    try:
        dmg = hero.cast_spell(0)
        print(f"Нанесено урона: {dmg}")
        print(f"Осталось маны: {hero.mana}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()