# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.
# Шаги:
# 1. Создай класс Store:
# -Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
# -  метод для добавления товара в ассортимент.
# метод для удаления товара из ассортимента
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# метод для обновления цены товара.
# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
# В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.

class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_price(self, item):
        return self.items.get(item, None)

    def update_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price

store1 = Store('FindWear', ' Batumi,Arganekidze 18')
store2 = Store('Cropper', 'Manaco, Raite No ma note 34/35')
store3 = Store('Victoria', 'Kutaisi, Kutaisi 23')

store1.add_item('Shoes', 150)
store1.add_item('Socks', 75)
store1.add_item('Shirt', 100)
store1.add_item('Pants', 125)

store2.add_item('Shoes', 175)
store2.add_item('Socks', 100)
store2.add_item('Shirt', 150)
store2.add_item('Pants', 150)

store3.add_item('Shoes', 125)
store3.add_item('Socks', 120)
store3.add_item('Shirt', 120)
store3.add_item('Pants', 175)

print(store1.get_price('Shoes'))  # Output: 150
store1.update_price('Shoes', 160)
print(store1.get_price('Shoes'))  # Output: 160
store1.remove_item('Socks')
print(store1.get_price('Socks'))  # Output: None

print(store2.get_price('Shirt'))  # Output: 150
store2.update_price('Shirt', 130)
print(store2.get_price('Shirt'))  # Output: 130
store2.remove_item('Shirt')
print(store2.get_price('Shirt'))

print(store3.get_price('Pants'))  # Output: 175
store3.update_price('Pants', 200)
print(store3.get_price('Pants'))  # Output: 200
store3.remove_item('Shoes')
print(store3.get_price('Shoes'))
# Output: None








