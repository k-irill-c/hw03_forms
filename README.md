# backend_community_homework
# Описание проекта
Социальная сеть. Дает пользователям возможность создать учетную запись, публиковать и редактировать свои записи.
* Подключено приложение django.contrib.auth, его urls.py подключен к головному urls.py.
* Подключен паджинатор, он выводит по десять постов
* Создана навигация по разделам
## Стек технологий
* Python - язык программирования
* Django - фреймворк для веб-приложений на языке Python
* HTML - стандартизированный язык гипертекстовой разметки документов для просмотра веб-страниц в браузере
## Разворачивание проекта

* Склонировать репозиторий, перейти в проект:
```bash
git clone https://github.com/k-irill-c/hw03_forms
```

```bash
cd hw03_forms
```
* Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

```bash
. venv/bin/activate
```

* Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

* Выполнить миграции:

```bash
python manage.py migrate
```

* Запустите сервер:
```bash
python manage.py runserver
```
#### Автор
Кирилл С. студет Яндекс.Практикума
<!-- [![CI](https://github.com/yandex-praktikum/hw03_forms/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw03_forms/actions/workflows/python-app.yml) -->
