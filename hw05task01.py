def caching_fibonacci(): # Функція для обчислень значень чисел Фібоначі
    cache = {} # Оголошуємо пустий словник для кешу
    
    def fibonacci(n):
        if n <= 0: #  Перевіряємо якщо n = 0 передаємо 0
            return 0
        if n == 1: # Перевіряємо якщо n = 1 передаємо 1
            return 1
        if n in cache: # Перевіряємо чи є данне число у кеші
            return cache[n]
        cache[n] = fibonacci(n-1) + fibonacci(n-2) # Обчисллення числа Фібоначі
        return cache[n]
    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))