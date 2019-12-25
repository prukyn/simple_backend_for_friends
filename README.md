# Simple Backend

### Опис
Нереально простий бек для друганів

### Залежності
- Python 3
- pip

### Встановлення

- Якщо в Вас Windows, то перед цим встановіть [Python 3](https://www.python.org/downloads/windows/)
- При встановлення натисніть **Add to PATH**
- Далі завантажте [pip](https://bootstrap.pypa.io/get-pip.py)
- Відкрийте в командному рядку папку куди скачали get-pip.py
- і напишіть ``python get-pip.py``

Далі виконуйте наступне

``git clone https://github.com/prukyn/simple_backend_for_friends.git``

або скачайте zip та розпакуйте його, якщо ``git`` не встановлено

 ``https://github.com/prukyn/simple_backend_for_friends/archive/master.zip``

```
cd simple_backend_for_friends
pip install -r requirements.txt
```

### Налаштування 
Для використання даного рішення необхідно створити базу Postgres з таблицями та
мінімально заповненими даними та мати написані працюючі запити на SQL.

В файлі `config.py` потрібно встановити основні параметри.

В поля ``HEADERS1-4`` необідно написати назви стовбців, які повертаються.

В поля ``QUERY1-4`` необхідно вставити запити.

### Використання
Після описаних вище маніпуляцій в папці проекту необхідно написати
``python run.py``

Сервер запуститься на http://127.0.0.1:5000/ 

Запити будуть доступні за посиланням http://127.0.0.1:5000/query1-4 відповідно

Як результат повернеться json в вигляді масиву з обʼєктами
наступного вигляду:
```
[
  {
    "BirthDate": "29-6-1996", 
    "DiplomaName": "REMEDYREPACK INC.", 
    "GroupCode": "P9sonV", 
    "Mark": "A", 
    "Name": "Mottram", 
    "Patronymic": "Wride", 
    "SpecialityName": "nm", 
    "Surname": "Ailyn"
  },
...
]
```
де ключі - наші HEADERS-и, а значення - результати запитів