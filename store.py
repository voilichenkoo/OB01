#Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров. Ваша задача — создать класс `Store`,
# который можно будет использовать для создания различных магазинов.
# Шаги:
# 1. Создай класс `Store`:
# -Атрибуты класса:
#    - `name`: название магазина.
#    - `address`: адрес магазина.
#    - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# - метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
# 2. Создай несколько объектов класса `Store`:
#    Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них
#    несколько товаров.
# 3. Протестировать методы:
#   Выбери один из созданных магазинов и протестируй все его методы:
#   - добавь товар,
#   - обнови цену,
#   - убери товар и
#   - запрашивай цену.

class Store:
    def __init__(self, name,address, items = None):
        if items is None:
            items = {}
        self.name = name
        self.address = address
        self.items = items

    def add_item(self, item_name, price):
        self.items[item_name] = price


    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' был удален.")
        else:
            print(f"Товар '{item_name}' не найден в магазине {self.name}.")

    def price_item(self, item_name):
        return self.items.get(item_name)

    def new_price_item(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' не найден в магазине {self.name}.")



store1 = Store("Магазин1", "Улица 1", {"яблоко": 150, "банан": 125})
store2 = Store("Магазин2", "Улица 2", {"яблоко": 155, "банан": 130, "кокос": 360})
store3 = Store("Магазин3", "Улица 3", {"яблоко": 147, "банан": 120, "апельсин": 100})

print(store1.items)

store1.remove_item("банан")  
print(store1.items)

store1.remove_item("апельсин")
store1.add_item("кокос", 350)
print(store1.price_item("кокос"))
print(store1.price_item("Кокос"))
store1.new_price_item("кокос", 370)
print(store1.items)