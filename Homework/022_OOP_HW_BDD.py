# Написать несколько классов для мебели:

# Класс мебель(высота, ширина, длина)
#     атрибуты
#         площадь
#         объём

class Furniture:

    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length

    # Decorator
    @ property
    def area(self):
        return self.length * self.width

    @ property
    def volume(self):
        return self.length * self.width * self.height

# Подкласс стол(тип дерева)

class Table(Furniture):

    def __init__(self, height, width, length, wood):
        super().__init__(height, width, length)
        self.wood = wood

# Подкласс Кровать(материал)

class Bed(Furniture):

    def __init__(self, height, width, length, material):
        super().__init__(height, width, length, material)
        self.material = material

# Подкласс Шкаф(назначение)

class Cabinet(Furniture):

    def __init__(self, height, width, length, purpose):
        super().__init__(height, width, length, purpose)
        self.purpose = purpose
