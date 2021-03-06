# Обрезка ссылок с помощью Битли

Этот код может создавать короткие битли-ссылки из длинных URL и может выводить статистику по кликам битли-ссылок.

Этот код можно использовать только случае, если у вас есть Valid Token с https://bitly.com/

Как получить Valid Token можно узнать тут: https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-find-my-OAuth-access-token-

### Как установить
Скачиваем файлы в отдельную папку.

В этой же папке создаем .env файл.
Ваш .env должен содержать строку:
```
TOKEN=**ваш Valid Token**
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Использование
Используем консольный ввод.

1. Создать короткую ссылку битли:
```
python3 main.py https://link.com/

http://bit.ly/2A8OECy
```

2. Вывести количество переходов по кликам по битли-ссылке:
```
python3 main.py http://bit.ly/2A8OECy

Количество переходов по ссылке битли: 14
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
