class Animals:
    farm = []
    total_weight = []
    hunger = 'Животное сытое'

    def __init__(self, name: str, voice: str, weight: float):
        """
        Для дальнейшего ввода имени, голоса и веса животного
        """
        self.name = name
        self.voice = voice
        self.weight = weight
        Animals.farm.append(self)
        Animals.total_weight.append(weight)

    def want_eat(self):
        """
        Голодное животное
        """
        self.hunger = 'Животное голодное'

    def ate(self):
        """
        Сытое животное
        """
        self.hunger = 'Животное сытое'


class MilkAnimals(Animals):
    milk = 'Пора доить'

    def have_milk(self):
        """
        Животное пора доить
        """
        self.milk = 'Пора доить'

    def have_not_milk(self):
        """
        Животное подоили
        """
        self.milk = 'Молока нет'


class HairyAnimals(Animals):
    wool = 'Животное острижено'

    def have_wool(self):
        """
        Животное пора стричь
        """
        self.wool = 'Животное пора стричь'

    def have_not_wool(self):
        """
        Животное острижено
        """
        self.wool = 'Животное острижено'


class Bird(Animals):
    eggs = 'Пора собирать яйца'

    def have_eggs(self):
        """
        Пора собирать яйца у птицы
        """
        self.eggs = 'Пора собирать яйца'

    def have_not_eggs(self):
        """
        Яйца собраны
        """
        self.eggs = 'Яиц нет'


cow_1 = MilkAnimals(name='Манька', voice='Муу', weight=943)

goat_1 = MilkAnimals(name='Рога', voice='Мее', weight=63)
goat_2 = MilkAnimals(name='Копыта', voice='Мее', weight=75)

sheep_1 = HairyAnimals(name='Барашек', voice='Бее', weight=97)
sheep_2 = HairyAnimals(name='Кудрявый', voice='Бее', weight=82)

chicken_1 = Bird(name='Ко-Ко', voice='Куд-кудах', weight=2.1)
chicken_2 = Bird(name='Кукареку', voice='Куд-кудах', weight=1.8)

duck = Bird(name='Кряква', voice='Кря-кря', weight=2.9)

goose_1 = Bird(name='Серый', voice='Га-га-га', weight=4.2)
goose_2 = Bird(name='Белый', voice='Га-га-га', weight=4.7)


def show_weight():
    """
    Покажет общий вес всех животных, а также вес и имя саого тяжелого
    """
    print(f'Общий вес всех животных составляет {sum(Animals.total_weight)} кг')
    for animal in Animals.farm:
        if max(Animals.total_weight) == animal.weight:
            print(f'Самый тяжёлый житель фермы - {animal.weight} кг - {animal.name}')


show_weight()
