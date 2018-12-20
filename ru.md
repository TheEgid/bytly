# Обрезка ссылок с помощью Битли

This Bitly url shorterer can creating short bitlinks from long urls and can recognising 
bitlinks-clicks statistics.
It is possible to use this code only if we have Valid Token from https://bitly.com/

### Как установить
Get your Valid Token from https://dev.bitly.com/get_started.html

Create .env file where main.py is located.

Your .env file should be this string:
```
TOKEN=**your token**
```


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Usage

creating short bitlinks:
```
>>> $ python3 main.py http://bit.ly/2A8OECy
Количество переходов по ссылке битли: 14
```

recognising bitlinks-clicks statistics:
```
>>> $ python3 main.py https://link.com/
http://bit.ly/2A8OECy
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).