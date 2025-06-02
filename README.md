# Food Ordering System/Система управління замовленнями їжі
Ця система - базова модель для **управління замовленнями їжі** у ресторані. Вона складається з декількох взаємопов'язаних класів, кожен з яких відповідає за певний аспект функціонування.

## Класи: опис, можливості, структура
### Клас `MenuItem`
**Опис**

Клас `MenuItem` є фундаментальним будівельним блоком у системі управління рестораном. Розробленим для представлення окремих страв або напоїв, що пропонуються в меню. Його основне призначення — інкапсулювати всі відповідні деталі про страву, забезпечуючи цілісність даних за допомогою механізмів валідації.

**Можливості**
1.  *Зберігання деталізованої інформації про страву.*

Клас MenuItem дозволяє зберігати повний набір атрибутів, що описують одну страву. Це включає:
- назва страви: для ідентифікації;
- опис: список інгредієнтів та особливостей приготування;
- ціна: вартість страви;
- калорійність: енергетична цінність страви;
- вага: стандартна вага порції;
- список алергенів: важлива інформація для клієнтів з алергіями;
- статус доступності: чи можна замовити страву зараз;
- час приготування: орієнтовний час очікування для клієнта.

Ці атрибути дозволяють системі мати повне уявлення про кожен пункт меню.

2.   *Автоматична валідація вхідних даних.*

Однією з найважливіших можливостей класу є вбудована валідація даних під час ініціалізації об'єкта. Це забезпечує, що в систему потрапляють лише коректні та осмислені дані, запобігаючи логічним помилкам та помилкам типу.

Перевірка типів:

- гарантує, що `name`, `description` є рядками `(str)`;
- гарантує, що `price`, `weight_gram` є числами з плаваючою комою `(float)`;
- гарантує, що `calories`, `preparation_time_minutes` є цілими числами `(int)`;
- гарантує, що `allergens` є списком `(list)`;
- гарантує, що `is_available` є булевим значенням `(bool)`.

У разі невідповідності типу викликає `TypeError`.

Перевірка значень:

- непорожність: перевіряє, що `name`, `description` не є порожніми рядками;
- позитивні значення: перевіряє, що `price`, `calories`, `weight_gram`, `preparation_time_minutes` є додатними числами (більше 0);
- непорожній список алергенів: вимагає, щоб список `allergens` не був порожнім, якщо він наданий;
- доступність: вимагає, щоб `is_available` було `True` при ініціалізації, якщо страва доступна.

У разі некоректних значень викликає `ValueError`.

3. *Безпечний доступ до атрибутів.*

Клас надає набір публічних методів-гетерів `(get_name()`, `get_description()`, `get_price()`, `get_calories()`, `get_weight_gram()`, `get_allergens()`, `get_is_available()`, `get_preparation_time_minutes()`), які дозволяють зовнішньому коду безпечно отримувати значення приватних атрибутів (`_name`, `_price` тощо).

4. *Зручне представлення інформації.*

Метод `__str__` дозволяє отримати зрозуміле та відформатоване рядкове представлення об'єкта `MenuItem`.

*Демонстрація можливостей класу `MenuItem`*
```python
#Зберігання деталізованої інформації про страву.
    try:
        dish1 = MenuItem("Greek Salad", "A classic salad made with fresh vegetables and cheese.\n"
                                        "Ingredients: tomatoes, cucumber, red onion, green bell pepper, kalamata"
                                        "olives, feta cheese, olive oil, oregano, salt",
                         15.00, 230, 300.00, ["Milk", "Gluten"], True, 10)
        print("Position №1:", dish1)
    except (TypeError, ValueError) as e:
        print("Error creating dish1:", {e})
    print("\n")

#Position №1: 
#Dish Name: Greek Salad
#Description: A classic salad made with fresh vegetables and cheese.
#Ingredients: tomatoes, cucumber, red onion, green bell pepper, kalamataolives, feta cheese, olive oil, oregano, salt
#Price: $15.00
#Calories: 230 kcal
#Weight: 300.00 grams
#Allergens: Milk, Gluten
#Availability: Available
#Preparation time: 10 minutes

#Автоматична валідація вхідних даних.
    try:
        print("Position №4: Creating an incorrect value with a negative price.")
        dish4 = MenuItem("Salmon Nigiri", "Fresh salmon on seasoned rice.",
                         -5.00, 120, 80.00, ["Gluten"], True, 5) #Некоректна ціна
        print("Position №4:", dish4)
    except (TypeError, ValueError) as e:
        print("Error creating dish4:", {e})
    print("\n")

#Position №4: Creating an incorrect value with a negative price.
#Error creating dish4: {ValueError('The price of the dish needs to be a positive value.')}

#Безпечний доступ до атрибутів.

print(dish1.get_name()) #Greek Salad
print(dish2.get_calories()) #180
print(dish3.get_price()) #25.0

#Зручне представлення інформації.

print(dish3.__str__())

#Dish Name: Carbonara Pasta
#Description: Classic Italian pasta with egg, hard cheese, cured pork, and black pepper.
#Price: $25.00
#Calories: 550 kcal
#Weight: 250.00 grams
#Allergens: Gluten, Eggs, Dairy, Pork
#Availability: Available
#Preparation time: 15 minutes

```

**Структура класу**

1. *Атрибути*

| Назва атрибуту | Визначення атрибуту |
| ----------- | ----------- |
| `_name: str` | Назва страви. |
| `_description: str` | Детальний опис страви. |
| `_price: float` | Ціна страви. |
| `_calories: int` | Калорійність страви. |
| `_weight_gram: float` | Вага порції в грамах. |
| `_allergens: list` | Список алергенів, присутніх у страві. |
| `_is_available: bool` | Булеве значення, що вказує на доступність страви. |
| `_preparation_time_minutes: int` | Орієнтовний час приготування в хвилинах. |

2. *Методи*

| Назва методу | Визначення методу |
| ----------- | ----------- |
| `__init__` |  Приймає значення для всіх восьми атрибутів, перелічених вище, як аргументи. Виконує перевірку типів для кожного параметра, щоб переконатися, що вони відповідають очікуваним типам даних. Виконує перевірку значень для забезпечення логічної коректності. Якщо всі перевірки пройдені успішно, вхідні значення присвоюються відповідним приватним атрибутам. |
| `get_name() -> str` |  Повертає значення атрибута `_name: str`. |
| `get_description() -> str` | Повертає значення атрибута `_description: str`. |
| `get_price() -> float` | Повертає значення атрибута `_price: float`. |
| `get_calories() -> int` | Повертає значення атрибута `_calories: int`. |
| `get_weight_gram() -> float` | Повертає значення атрибута `_weight_gram: float`. |
| `get_allergens() -> list` | Повертає значення атрибута `_allergens: list`. |
| `get_is_available() -> bool` | Повертає значення атрибута `_is_available: bool`. |
| `get_preparation_time_minutes() -> int` | Повертає значення атрибута `_preparation_time_minutes: int`. |
| `__str__(self) -> str` | Визначає, як об'єкт `MenuItem` буде представлений у вигляді рядка. Він форматує всі ключові атрибути страви в читабельний, багаторядковий опис, включаючи статус доступності. |

### Клас `Menu`

**Опис**

Клас `Menu` слугує центральним компонентом для організації та відображення страв у системі управління рестораном. Він призначений для зберігання колекції об'єктів `MenuItem`, представляючи собою конкретне меню. Клас `Menu` забезпечує повний набір функцій для ефективного управління, пошуку та відображення доступних страв.

**Можливості**

1. *Створення та іменування меню.*

Клас Menu дозволяє створювати іменовані екземпляри меню. Кожен об'єкт `Menu` ініціалізується з унікальною назвою, яка служить для ідентифікації та організації.

Валідація назви меню:

- Перевірка типу: гарантує, що назва меню є рядком `(str)`. У випадку невідповідності викликає `TypeError`.
- Перевірка значення: гарантує, що назва меню не є порожнім рядком. У випадку порожнього рядка викликає `ValueError`.

2. *Додавання та видалення позицій меню.*

Menu надає методи для динамічного керування списком страв:

- Додавання позицій: метод `add_item()` дозволяє додавати об'єкти ```MenuItem``` до меню. Він забезпечує, що додаються лише дійсні об'єкти ```MenuItem```, підвищуючи цілісність даних.
- Видалення позицій: метод `remove_item()` дозволяє видаляти позиції меню за їхньою назвою. Якщо існує кілька позицій з однаковою назвою, будуть видалені всі відповідні.

3. Пошук позицій меню.

Метод `get_item()` дозволяє знаходити певну позицію `MenuItem` у меню за її назвою. Він повертає перший знайдений відповідний об'єкт `MenuItem` або `None`, якщо позицію не знайдено.

4.  *Відображення меню.*

Метод `display_menu()` друкує відформатоване представлення всього меню в консолі. Він спочатку відображає назву меню, а потім перераховує всі позиції, які воно містить, використовуючи метод `__str__` кожного `MenuItem`. Якщо меню порожнє, відображається відповідне повідомлення.

*Демонстрація можливостей класу `Menu`*

```python
    try:
        menu1 = Menu("Mediterranean Menu")
        menu1.get_name()
        menu1.add_item(dish1)
        menu1.add_item(dish2)
        menu1.add_item(dish3)
        menu1.display_menu()
        menu1.remove_item("Carbonara Pasta")
        print("\n")
        menu1.get_name()
        menu1.display_menu()
    except (TypeError, ValueError) as e:
        print("Error creating menu1:", {e})
    print("\n")

#Mediterranean Menu

#Dish Name: Greek Salad
#Description: A classic salad made with fresh vegetables and cheese.
#Ingredients: tomatoes, cucumber, red onion, green bell pepper, kalamataolives, feta cheese, olive oil, oregano, salt
#Price: $15.00
#Calories: 230 kcal
#Weight: 300.00 grams
#Allergens: Milk, Gluten
#Availability: Available
#Preparation time: 10 minutes

#Dish Name: Tuna Salad
#Description: Ingredients: canned tuna, lettuce, cherry tomatoes, cucumber, red onion, sweet corn, olive oil, lemon juice, salt and pepper
#Price: $19.00
#Calories: 180 kcal
#Weight: 350.00 grams
#Allergens: Lemon, Fish
#Availability: Available
#Preparation time: 10 minutes

#Dish Name: Carbonara Pasta
#Description: Classic Italian pasta with egg, hard cheese, cured pork, and black pepper.
#Price: $25.00
#Calories: 550 kcal
#Weight: 250.00 grams
#Allergens: Gluten, Eggs, Dairy, Pork
#Availability: Available
#Preparation time: 15 minutes

#Mediterranean Menu

#Dish Name: Greek Salad
#Description: A classic salad made with fresh vegetables and cheese.
#Ingredients: tomatoes, cucumber, red onion, green bell pepper, kalamataolives, feta cheese, olive oil, oregano, salt
#Price: $15.00
#Calories: 230 kcal
#Weight: 300.00 grams
#Allergens: Milk, Gluten
#Availability: Available
#Preparation time: 10 minutes

#Dish Name: Tuna Salad
#Description: Ingredients: canned tuna, lettuce, cherry tomatoes, cucumber, red onion, sweet corn, olive oil, lemon juice, salt and pepper
#Price: $19.00
#Calories: 180 kcal
#Weight: 350.00 grams
#Allergens: Lemon, Fish
#Availability: Available
#Preparation time: 10 minutes

    try:
        print("Creating an incorrect value with a empty name.")
        menu2 = Menu("")
        menu1.get_name()
    except (TypeError, ValueError) as e:
        print("Error creating menu2:", {e})
    print("\n")

#Creating an incorrect value with a empty name.
#Error creating menu2: {ValueError('Menu name cannot be empty.')}
```

**Структура класу**

1. *Атрибути*

|  Назва атрибуту | Визначення атрибуту |
| ----------- | ----------- |
|  `_name: str`  | Назва меню.  |

2. *Методи*

| Назва методу | Визначення методу |
| ----------- | ----------- |
| `__init__` |  Приймає значення для всіх восьми атрибутів, перелічених вище, як аргументи. Виконує перевірку типів для кожного параметра, щоб переконатися, що вони відповідають очікуваним типам даних. Виконує перевірку значень для забезпечення логічної коректності. Якщо всі перевірки пройдені успішно, вхідні значення присвоюються відповідним приватним атрибутам. |
| `get_name() -> str` |  Повертає значення атрибута `_name: str`. |
| `add_item(self, item: MenuItem)` | Додає наданий об'єкт `MenuItem` до внутрішнього списку елементів. |
| `remove_item(self, item_name: str)` | Видаляє елемент меню з меню за його назвою. Перебирає поточний список елементів меню та створює новий список, виключаючи елемент із відповідним ім'ям. |
| `get_item(self, item_name: str) -> MenuItem` | Отримує об'єкт `MenuItem` з меню за його назвою. Шукає елемент із заданою назвою в меню та повертає перший знайдений відповідний об'єкт `MenuItem`. |
| `display_menu(self)` | Виводить відформатований вигляд усього меню на консоль. |

### Клас Restaurant

**Опис**

Клас `Restaurant` розроблено для інкапсуляції всієї основної інформації про ресторан, від його назви та адреси до типу кухні та рейтингу клієнтів. Окрім зберігання деталей, він також керує меню ресторану, дозволяючи призначати та отримувати об'єкт Menu. Цей клас забезпечує цілісність даних за допомогою надійної валідації всіх початкових параметрів.

**Можливості**

1. *Комплексне управління інформацією про ресторан.*

Клас Restaurant надає повний набір атрибутів для опису ресторану:

- Назва: унікальний ідентифікатор ресторану.
- Адреса: фізичне розташування.
- Телефон: контактний номер для запитів та бронювання.
- Години роботи: гнучкий словник для визначення щоденного часу роботи.
- Тип кухні: визначає кулінарний напрямок.
- Рейтинг: середня оцінка задоволеності клієнтів за шкалою від 0 до 5.

2. *Сувора валідація вхідних даних.*

Ключовою особливістю класу `Restaurant` є вбудована валідація даних під час ініціалізації об'єкта. Це гарантує, що в систему потрапляють лише точні та осмислені дані, запобігаючи логічним помилкам та помилкам типу.

Перевірки типів:
- Гарантує, що `name, address` та `cuisine_type` є рядками '(str)'.
- Гарантує, що `phone` є цілим числом `(int)`.
- Гарантує, що `opening_hours` є словником `(dict)`.
- Гарантує, що `rating` є числом з плаваючою комою `(float)`.

У разі невідповідності типу виникає `TypeError`

Перевірки значень:

- Непорожність: перевіряє, що `name, address, opening_hours та cuisine_type` не є порожніми.
- Позитивний телефон: підтверджує, що phone є додатним цілим числом.
- Діапазон рейтингу: забезпечує, що `rating` знаходиться в діапазоні від 0 до 5 включно.

Якщо будь-яке значення не проходить ці перевірки, виникає ValueError.

3. *Безпечний доступ до атрибутів.*

Клас надає набір публічних методів-гетерів (`get_name(), get_address(), get_phone(), get_opening_hours(), get_cuisine_type(), get_rating(), get_menu()`), які дозволяють зовнішньому коду безпечно отримувати значення приватних атрибутів (`_name, _address` тощо).

4. *Призначення та отримання меню.*

Метод `set_menu()` дозволяє асоціювати об'єкт `Menu` з рестораном, дозволяючи йому пропонувати певні позиції меню. Він включає валідацію, щоб гарантувати, що можуть бути призначені лише екземпляри класу `Menu`. Метод `get_menu()` полегшує отримання поточного призначеного меню.

5. *Зручне строкове представлення.*

Метод `__str__` пропонує чітке та зрозуміле строкове представлення об'єкта Restaurant. Це включає всі його ключові деталі та назву його поточного призначеного меню, що полегшує відображення інформації про ресторан.

*Демонстрація можливостей класу Restaurant*
```python
    try:
        rest1 = Restaurant("Olivia", "Kyiv, Khreshchatyk, 15", 380964850106,
                           {"Monday-Friday": "10:00-22:00", "Saturday-Sunday": "11:00-23:00"},
                           "Greek", 5.0)
        rest1.set_menu(menu1)
        print("Restaurant Num1:", rest1)
    except (TypeError, ValueError) as e:
        print("Error creating rest1:", {e})
    print("\n")

#Menu 'Mediterranean Menu' has been set for restaurant 'Olivia'.
#Restaurant Num1: 
#Restaurant Name: Olivia
#Address: Kyiv, Khreshchatyk, 15
#Phone: 380964850106
#Cuisine: Greek
#Opening hours: {'Monday-Friday': '10:00-22:00', 'Saturday-Sunday': '11:00-23:00'}
#Rating: 5.0/5 stars
#Current menu: Mediterranean Menu

    try:
        rest2 = Restaurant("Bad Place", "Somewhere", 380954850106,
                           {"Daily": "10-20"},"Fast Food", 6.0)
        print("Restaurant Num2:", rest2)
    except (TypeError, ValueError) as e:
        print("Error creating rest2:", {e})
    print("\n")
#Error creating rest2: {ValueError('Rating must be between 0 and 5.')}
```

**Структура класу**


1. *Атрибути*

| Назва атрибуту      | Визначення атрибуту                                                |
| :------------------ | ----------------------------------------------------------------- |
| _name: str        | Назва ресторану.                                                   |
| _address: str     | Фізична адреса ресторану.                                          |
| _phone: int       | Контактний номер телефону ресторану.                               |
| _opening_hours: dict | Словник, що вказує години роботи ресторану.                       |
| _cuisine_type: str | Тип кухні, на якій спеціалізується ресторан.                      |
| _rating: float    | Середній рейтинг ресторану (від 0 до 5).                            |
| _menu: Menu | Об'єкт Menu, призначений ресторану, або None, якщо меню не встановлено.|

3. *Методи*

| Назва методу | Визначення методу |
| ----------- | ----------- |
| `__init__` |  Приймає значення для всіх восьми атрибутів, перелічених вище, як аргументи. Виконує перевірку типів для кожного параметра, щоб переконатися, що вони відповідають очікуваним типам даних. Виконує перевірку значень для забезпечення логічної коректності. Якщо всі перевірки пройдені успішно, вхідні значення присвоюються відповідним приватним атрибутам. |
| `get_name() -> str` |  Повертає значення атрибута `_name: str`. |
| `get_address(self) -> str` | Повертає значення атрибута `_address: str`. |
| `get_phone(self) -> int` | Повертає значення атрибута `_phone: int`. |
| `get_opening_hours(self) -> dict` | Повертає значення атрибута `_opening_hours: dict`. |
| `get_cuisine_type(self) -> str` | Повертає значення атрибута `_cuisine_type: str`. |
| `get_rating(self) -> float` | Повертає значення атрибута `_rating: float`. |
| `get_menu(self) -> Menu` | Повертає значення атрибута `_menu`. |
| `set_menu(self, menu: Menu)` | Призначає об'єкт `Menu` ресторану. Пов'язує певне меню з рестораном, дозволяючи йому пропонувати ці пункти меню. Перевіряє, чи наданий об'єкт справді є екземпляром класу `Menu`. |
| `__str__(self)` | Визначає, як об'єкт `Menu` буде представлений у вигляді рядка. Він форматує всі ключові атрибути страви в читабельний, багаторядковий опис, включаючи статус доступності. |

### Клас `Client`

**Опис**

Клас `Client` призначений для представлення клієнтів ресторану, зберігаючи їхню особисту та контактну інформацію.

**Можливості**

Клас Client дозволяє:

1. *Створювати об'єкти клієнтів: ініціалізація нового клієнта з перевіркою коректності наданих даних.*
2. *Зберігати контактну інформацію: надійно зберігає ім'я, прізвище, електронну пошту та номер телефону клієнта.*
3. *Надавати доступ до інформації: дозволяє отримати доступ до окремих полів (ім'я, прізвище, email, телефон) за допомогою спеціальних методів-гетерів.*
4. *Форматувати вивід інформації: генерує зручне для читання рядкове представлення об'єкта клієнта, включаючи повне ім'я, електронну пошту та номер телефону.*

*Демонстрація можливостей класу `Client`*
```python
    try:
        client1 = Client("Rodrigo", "Smith",
                         "rodrigo_smith@gmail.com", 380944850106)
        print("Client Num1:", client1)
    except (TypeError, ValueError) as e:
        print("Error creating client1:", {e})
    print("\n")

#Client Num1: 
#Client: Rodrigo Smith
#Email: rodrigo_smith@gmail.com
#Phone: 380944850106

    try:
        client2 = Client("Ann", "Smith",
                         "ann_smith.gmail.com", 380944850106)
        print("Client Num2:", client2)
    except (TypeError, ValueError) as e:
        print("Error creating client2:", {e})
    print("\n")

#Error creating client2: {ValueError('Invalid client email.')}
```

**Структура класу**

1. *Атрибути*

|  Назва атрибуту | Визначення атрибуту |
| ----------- | ----------- |
|  `_name: str`  | Приватне поле для зберігання імені клієнта. |
|  `_name: str`  | Приватне поле для зберігання прізвища клієнта. |
|  `_name: str`  | Приватне поле для зберігання адреси електронної пошти клієнта. |
|  `_name: str`  | Приватне поле для зберігання номера телефону клієнта. |


3. *Методи*

| Назва методу | Визначення методу |
| ----------- | ----------- |
| `__init__` |  Приймає значення для всіх восьми атрибутів, перелічених вище, як аргументи. Виконує перевірку типів для кожного параметра, щоб переконатися, що вони відповідають очікуваним типам даних. Виконує перевірку значень для забезпечення логічної коректності. Якщо всі перевірки пройдені успішно, вхідні значення присвоюються відповідним приватним атрибутам. |
| `get_name() -> str` |  Повертає значення атрибута `_name: str`. |
| `get_surname(self) -> str` | Повертає значення атрибута `_surname: str`. |
| `get_email(self) -> str` | Повертає значення атрибута `_email: str`. |
| `get_phone(self) -> int` | Повертає значення атрибута `get_phone: int`. |
| `__str__(self)` | Визначає, як об'єкт `Client` буде представлений у вигляді рядка. Він форматує всі ключові атрибути страви в читабельний, багаторядковий опис, включаючи статус доступності. |


### Клас `Order`

**Опис**

Клас `Order` представляє замовлення клієнта в системі ресторану. Він керує деталями замовлення, включаючи список замовлених страв, загальну вартість, поточний статус, а також пов'язаного клієнта та ресторан.

**Можливості**

Клас Order дозволяє:

1. *Створювати унікальні замовлення: автоматично присвоює унікальний номер кожному новому замовленню.*
2. *Прив'язувати замовлення до клієнта та ресторану: встановлює зв'язок між замовленням, клієнтом, який його розмістив, і рестораном, що його обслуговує.*
3. *Керувати позиціями замовлення: дозволяє додавати та видаляти страви `(MenuItem)` із замовлення, а також оновлювати їхню кількість.*
4. *Відстежувати час замовлення: зберігає точний час створення замовлення.*
5. *Оновлювати статус замовлення: дозволяє змінювати статус замовлення ("В очікуванні", "Підтверджено", "Доставлено").*
6. *Розраховувати загальну вартість: автоматично обчислює сумарну вартість усіх позицій у замовленні.*
7. *Відображати деталі замовлення: генерує повне, відформатоване зведення замовлення для зручного перегляду.*

*Демонстрація можливостей класу `Order`*

```python
    try:
        order1 = Order(client1, rest1)
        print(f"Correct order #{order1.get_order_number()} created.")
        if dish1:
            order1.add_item(dish1, 2)
        if dish2:
            order1.add_item(dish2, 3)
        if dish3:
            order1.add_item(dish3, 1)
        print(order1.display_order_details())
        print(f"Price: ${order1.get_total_price():.2f}")
        order1.update_status("Confirmed")
        print(f"New status of order #{order1.get_order_number()}: {order1.get_status()}")
        if dish1:
            order1.remove_item(dish1, )
            print(order1.display_order_details())
            order1.remove_item(dish1)
            print(order1.display_order_details())
    except (TypeError, ValueError) as e:
        print("Error creating order1:", {e})
    print("\n")

#Correct order #0 created.
#Added 2 x Greek Salad to order 0.
#Added 3 x Tuna Salad to order 0.
#Added 1 x Carbonara Pasta to order 0.
#Order Details (Order #0)
#Client: Rodrigo
#Restaurant: Olivia
#Order Time: 2025-06-02 23:11:09
#Status: Pending
#Items:
#Greek Salad x 2 ($15.00 each)
#Tuna Salad x 3 ($19.00 each)
#Carbonara Pasta x 1 ($25.00 each)
#Total: $112.00
#Price: $112.00
#Order 0 status updated to: Confirmed
#New status of order #0: Confirmed
#Removed Greek Salad from order 0.
#Order Details (Order #0)
#Client: Rodrigo
#Restaurant: Olivia
#Order Time: 2025-06-02 23:11:09
#Status: Confirmed
#Items:
#Tuna Salad x 3 ($19.00 each)
#Carbonara Pasta x 1 ($25.00 each)
#Total: $82.00
#Greek Salad not found in order 0.
#Order Details (Order #0)
#Client: Rodrigo
#Restaurant: Olivia
#Order Time: 2025-06-02 23:11:09
#Status: Confirmed
#Items:
#Tuna Salad x 3 ($19.00 each)
#Carbonara Pasta x 1 ($25.00 each)
#Total: $82.00

    try:
        order2 = Order(client2, rest1)
        print(f"Correct order #{order2.get_order_number()} created.")
        if dish1:
            order2.add_item(dish1, 2)
        if dish2:
            order2.add_item(dish2, 3)
        if dish3:
            order2.add_item(dish3, 1)
        print(order2.display_order_details())
        print(f"Price: ${order2.get_total_price():.2f}")
        order2.update_status("Confirmed")
        print(f"New status of order #{order2.get_order_number()}: {order2.get_status()}")
        if dish1:
            order2.remove_item(dish1, )
            print(order2.display_order_details())
            order2.remove_item(dish1)
            print(order2.display_order_details())
    except (TypeError, ValueError) as e:
        print("Error creating order2:", {e})
    print("\n")

#Error creating order2: {TypeError('Order must be associated with a valid Client.')}
```

**Структура класу**

1. *Атрибути*

|  Назва атрибуту | Визначення атрибуту |
| ----------- | ----------- |
|  `next_order_number: int`  | Атрибут класу, який відстежує наступний доступний унікальний номер замовлення. Збільшується при кожному створенні нового замовлення. |
|  `_order_number: int`  | Приватний атрибут екземпляра, унікальний ідентифікатор для кожного замовлення. |
|  `_client: Client`  | Приватний атрибут екземпляра, посилання на об'єкт `Client`, який зробив це замовлення. |
|  `_restaurant: Restaurant`  | Приватний атрибут екземпляра, посилання на об'єкт `Restaurant`, який обробляє це замовлення. |
|  `_items: dict[MenuItem, int]`  | Приватний атрибут екземпляра, словник, що зберігає страви (об'єкти `MenuItem`) та їхню кількість у замовленні. |
|  `_order_time: datetime`  | Приватний атрибут екземпляра, об'єкт datetime, що фіксує точний час створення замовлення. |
|  `_status: str`  | Приватний атрибут екземпляра, поточний статус замовлення (наприклад, "Pending", "Confirmed", "Delivered"). |

3. *Методи*

| Назва методу | Визначення методу |
| ----------- | ----------- |
| `__init__` |  Приймає значення для всіх восьми атрибутів, перелічених вище, як аргументи. Виконує перевірку типів для кожного параметра, щоб переконатися, що вони відповідають очікуваним типам даних. Виконує перевірку значень для забезпечення логічної коректності. Якщо всі перевірки пройдені успішно, вхідні значення присвоюються відповідним приватним атрибутам. |
| `get_order_number(self) -> int` |  Повертає унікальний номер замовлення. |
| `get_client(self) -> Client` | Повертає об'єкт `Client`, пов'язаний із замовленням. |
| `get_restaurant(self) -> Restaurant` | Повертає об'єкт `Restaurant`, пов'язаний із замовленням. |
| `get_order_time(self) -> datetime` | Повертає дату та час створення замовлення. |
| `get_status(self) -> str` | Повертає поточний статус замовлення. |
| `add_item(self, menu_item: MenuItem, quantity: int)` |  Додає вказану кількість `MenuItem` до замовлення або оновлює її, якщо елемент вже присутній. |
| `remove_item(self, menu_item: MenuItem)` | Повністю видаляє `MenuItem` із замовлення. |
| `get_total_price(self) -> float` | Обчислює та повертає загальну вартість усіх позицій у замовленні. |
| `update_status(self, new_status: str)` | Оновлює статус замовлення. |
| `display_order_details(self) -> str` | Повертає детальний, відформатований підсумок замовлення у вигляді рядка. |

Клас Notification

**Опис**

Клас `Notification` призначений для створення та управління повідомленнями, які можуть бути використані для сповіщення користувачів, наприклад, про оновлення замовлень або рекламні акції. Він дозволяє інкапсулювати всю необхідну інформацію про повідомлення, включаючи його зміст, одержувача, тип та час відправлення. Це забезпечує валідацію даних при створенні повідомлення, гарантуючи коректність інформації для подальшої обробки або надсилання.

**Можливості**

Клас `Notification` надає такі основні можливості:

1. Створення повідомлень: Ініціалізація повідомлення з вказанням його змісту, електронної пошти одержувача та типу повідомлення (наприклад, "Email", "SMS").
2. Валідація даних: Автоматична перевірка вхідних даних під час створення обєкта, що запобігає створенню недійсних повідомлень (наприклад, з порожнім текстом або некоректною електронною поштою).
3. Доступ до атрибутів: Безпечний доступ до змісту повідомлення, електронної пошти одержувача, типу повідомлення та часу відправлення за допомогою спеціальних методів-геттерів.
4. Симуляція відправлення: Імітація процесу відправлення повідомлення з фіксацією поточного часу відправлення.

Демонстрація можливостей класу `Notification`

```Python
    try:
        notif1 = Notification("Your order has been confirmed!", "rodrigo_smith@gmail.com")
        print(f"Type message: {notif1.get_notification_type()}")
        print(notif1.send())
    except (TypeError, ValueError) as e:
        print("Error creating notif1:", {e})

#Type message: Email
#Sending Email notification
#To: rodrigo_smith@gmail.com
#Message: Your order has been confirmed!
#Sent at: 2025-06-02 23:30:26
        
    try:
        notif2 = Notification("Your order has been confirmed!", "rodrigo_smith.gmail.com")
        print(f"Type message: {notif2.get_notification_type()}")
        print(notif2.send())
    except (TypeError, ValueError) as e:
        print("Error creating notif2:", {e})
        
#Error creating notif2: {ValueError('Recipient email must be a valid email string.')}
```

**Структура класу**

1. *Атрибути*

|  Назва атрибуту   |   Визначення атрибуту  |
|_message: str | Зміст повідомлення, що буде відправлено.|
|----------|-------------|
|_recipient_email: str | Електронна адреса одержувача повідомлення. |
|_notification_type: str | Тип повідомлення (наприклад, "Email", "SMS"). За замовчуванням "Email".|
|_sent_time: datetime | Мітка часу, коли повідомлення було відправлено. Початково None, встановлюється при виклику методу send().|

3. *Методи*

| Назва методу |  Визначення методу |
|--------|----------|
|__init__| Конструктор класу. Ініціалізує новий об'єкт Notification|
|get_message(self) -> str|  Повертає зміст повідомлення|
|get_recipient_email(self) -> str| Повертає електронну пошту одержувача.|
|get_notification_type(self) -> str| Повертає тип повідомлення|
|get_sent_time(self) -> datetime | Повертає мітку часу, коли повідомлення було відправлено|
|send(self)|Симулює відправлення повідомлення, встановлюючи поточний час відправлення (_sent_time).|
