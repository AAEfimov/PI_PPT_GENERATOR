# PPT Generator
### fork from (https://github.com/parthgupta1208/PresentSmart.git)

## 1) Install

Clone this repo

```
python3 -m venv venv
pip install -r requirements.txt
```

## 2) Вы должны получить доступ к GigaChat API 

```
https://developers.sber.ru/studio/
```

## 3) Вы должны получить GCS_DEVELOPER_KEY и GCS_CX

# Мы ещё не перевели данный генератор на yandex или другой сервис по поиску картинок. поэтому пока используем google api

```
Чтобы иметь возможность использовать эту библиотеку, вам необходимо включить API пользовательского поиска Google, сгенерировать учетные данные ключа API и настроить проект:

Посетите https://console.developers.google.com и создайте проект.

Посетите https://console.developers.google.com/apis/library/customsearch.googleapis.com и включите «API пользовательского поиска» для своего проекта.

Посетите https://console.developers.google.com/apis/credentials и сгенерируйте учетные данные ключа API для своего проекта.

Посетите https://cse.google.com/cse/all и в веб-форме, где вы создаете/редактируете свою систему пользовательского поиска, включите параметр «Поиск изображений», а для параметра «Сайты для поиска» выберите «Поиск по всей сети, но с акцентом на включенные сайты».

После настройки учетной записи и проекта разработчиков Google вам должны были быть предоставлены ключ API разработчика и проект CX.
```

## License

[MIT License](LICENSE)


