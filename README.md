# :computer: PPT Generator - Software Engenering Project  

[![Update Ubuntu 22.04](https://github.com/AAEfimov/PI_PPT_GENERATOR/actions/workflows/python-app.yml/badge.svg)](https://github.com/AAEfimov/PI_PPT_GENERATOR/actions/workflows/python-app.yml)
[![docs](https://img.shields.io/badge/docs-latest-blue)](https://htmlpreview.github.io/?https://github.com/AAEfimov/PI_PPT_GENERATOR/blob/main/html/PI_PPT_GENERATOR/index.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/AAEfimov/PI_PPT_GENERATOR.svg)](http://isitmaintained.com/project/AAEfimov/PI_PPT_GENERATOR "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/AAEfimov/PI_PPT_GENERATOR.svg)](http://isitmaintained.com/project/AAEfimov/PI_PPT_GENERATOR "Percentage of issues still open")
[![docs](https://img.shields.io/badge/docs-latest-blue)](https://htmlpreview.github.io/?https://github.com/AAEfimov/PI_PPT_GENERATOR/blob/main/server/html/server/index.html)


## О проекте

Наш проект представляет streamlit web приложение для автоматической генерации презентаций.  
В проекте была использована GPT от Sber (GigaChat), а также LLAAM3 развёрнутая локально в docker.  
Наш сервис предоставляет возможность автоматически создать простую презентацию по клбючевым словам,  
с автоматическим добавлением изображений связанных по смыслу с сгенерированным текстом.  


![image](https://github.com/AAEfimov/PI_PPT_GENERATOR/assets/5468557/81ee4a81-9779-4bf6-a510-3e74ebd5e379)


### fork from (https://github.com/parthgupta1208/PresentSmart.git)

## Релизы

[Release list](https://github.com/AAEfimov/PI_PPT_GENERATOR/releases)

## 1) Make tokens (Заполняем файл .env)

```
export GPT_TOKEN=''
export GCS_DEVELOPER_KEY=''
export GCS_CX=''
```

Для работы с GPT от Sber необходимо зарегистрироваться на 

```
https://developers.sber.ru/studio/
```

и сгенерировать новый GPT Toketn

![image](https://github.com/AAEfimov/PI_PPT_GENERATOR/assets/5468557/96ce14b7-c199-4a48-807b-d88920afe141)

Полученный токен записать в файл 
### .env -> GPT_TOKEN=''

## Получаем токены GCS_DEVELOPER_KEY и GCS_CX от google для персонализированного поиска изображений  

### TODO: Мы ещё не перевели данный генератор на yandex или другой сервис по поиску картинок. поэтому пока используем google api

```
Чтобы иметь возможность использовать эту библиотеку, вам необходимо включить API пользовательского поиска Google, сгенерировать учетные данные ключа API и настроить проект:

Посетите https://console.developers.google.com и создайте проект.

Посетите https://console.developers.google.com/apis/library/customsearch.googleapis.com и включите «API пользовательского поиска» для своего проекта.

Посетите https://console.developers.google.com/apis/credentials и сгенерируйте учетные данные ключа API для своего проекта.

Посетите https://cse.google.com/cse/all и в веб-форме, где вы создаете/редактируете свою систему пользовательского поиска, включите параметр «Поиск изображений», а для параметра «Сайты для поиска» выберите «Поиск по всей сети, но с акцентом на включенные сайты».

После настройки учетной записи и проекта разработчиков Google вам должны были быть предоставлены ключ API разработчика и проект CX.
```

## 2) Build

Проект полностью представлен в 2-х docker контейнерах объеденённых внутренней сетью ppt-docker-net  
### Для установки docker и docker-compose обратитесь к официальной документации

## Модель llama3 и файл весов находтся под Data Version Controll 
### Выполните dvc pull, чтобы получить файлы

```
Collecting                                                                                                        |0.00 [00:00,    ?entry/s]
Fetching
Building workspace index                                                                                          |0.00 [00:00,    ?entry/s]
Comparing indexes                                                                                                |16.0 [00:00, 1.05kentry/s]
Applying changes                                                                                                  |8.00 [00:07,  1.11file/s]
A       ollama/                                                                                                                             
1 file added
```
### Использована версия 8B. Размером примерно 4.3Gb

## Сборка проекта из docker-compose.yml

```
make build NO_GPU=0
nake up
```

## ВАЖНО

Если вы собираете образ на ПК без видеокарты, или с объёмом видеопамяти меньше 5Gb то команды нужно вызывать  
с флагом NO_GPU=1

## Команда:  

:arrow_forward: Богачева Анна,  
:arrow_forward: Ефимов Алексей,  
:arrow_forward: Кулиев Эмир,  
:arrow_forward: Миронова Александра.

## License

[MIT License](LICENSE)


