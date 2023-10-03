import datetime

# Заказы клиента
orders = [
 {
 'id': 1,
 'timestamp': datetime.datetime(2022, 10, 5),
 'products': ['product1', 'product2', 'product3']
 },
 {
 'id': 2,
 'timestamp': datetime.datetime(2022, 10, 14),
 'products': ['product2', 'product4', 'product5']
 },
 {
 'id': 3,
 'timestamp': datetime.datetime(2022, 9, 10),
 'products': ['product3', 'product6', 'product7']
 },
 {
 'id': 4,
 'timestamp': datetime.datetime(2022, 8, 20),
 'products': ['product1', 'product5', 'product8']
 }
]

def get_ordered_products(orders, days):
 result = set()

 # Получаем текущую дату
 today = datetime.datetime.now()

 # Вычисляем начальную дату
 start_date = today - datetime.timedelta(days=days)

 # Проходим по каждому заказу
 for order in orders:
 # Проверяем, попадает ли заказ в указанный временной интервал
    if start_date <= order['timestamp'] <= today:
 # Добавляем товары заказа в результат
 result.update(order['products'])

 return list(result)

# Получаем список товаров заказанных за последние 7 дней
last_7_days = get_ordered_products(orders, 7)
print("За последние 7 дней:")
print(last_7_days)

# Получаем список товаров заказанных за последние 30 дней
last_30_days = get_ordered_products(orders, 30)
print("За последние 30 дней:")
print(last_30_days)

# Получаем список товаров заказанных за последний год
last_365_days = get_ordered_products(orders, 365)
print("За последний год:")
print(last_365_days)