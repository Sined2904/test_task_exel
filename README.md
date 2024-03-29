# Test_task

### Описание
Сервис, проверяющий корректность исчисления НДФЛ сотрудникам

### Технологии
asgiref
Django
django-pandas
djangorestframework
et-xmlfile
numpy
openpyxl
pandas
python-dateutil
pytz
six
sqlparse
typing_extensions
tzdata

### Запуск проекта с помощью Docker
- Клонируйте проект к себе на копьютер
- Находясь в папке проекта выполните команду
```
docker compose up -d
```
- Перейдите по адресу "http://127.0.0.1:8000/api/"
- В открывшемся окне нажмите "Выбрать файл" и выбери таблицу с исходными данными
- Нажмите "Отправить"

Файл с отчетом сохранится в вашей папке "Загрузки"
В открывшемся файле нажать на ярлык в ячейке "Отклонение" и выбрать тип сортировки.



### Запуск проекта вручную
- Клонируйте проект к себе на копьютер
- Установите и активируйте виртуальное окружение
```
python -m venv venv
```
```
. venv/Scripts/activate
```
- Перейдите в папку с requirements.txt и установите зависимости 
```
pip install -r requirements.txt
``` 
- В корневой папке проекта выполните команду:
```
python manage.py runserver
```
- Перейдите по адресу "http://127.0.0.1:8000/api/"
- В открывшемся окне нажмите "Выбрать файл" и выбери таблицу с исходными данными
- Нажмите "Отправить"

Файл с отчетом сохранится в вашей папке "Загрузки"
В открывшемся файле нажать на ярлык в ячейке "Отклонение" и выбрать тип сортировки.


### Автор
Пиневич Денис


Github - Sined2904
Den2904@yandex.ru
TG - @PinevichD