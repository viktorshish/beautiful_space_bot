# beautiful_space_bot
beautiful_space_bot скачивает фотографии космоса с сайтов: SpaceX и NASA. И размещает их в вашем Телеграм Боте

***
## Как установить
- Для скачивания фотографий с сайта **[NASA](https://api.nasa.gov/)** получите API-key. Зарегистрируйтесь на [сайте](https://api.nasa.gov/). API-key прейдёт к вам на почту. API-key выглядит наподобие такой строки: 17c09e20ad155405123ac1977542fecf00231da7.
- Для размещения фотографий,  создайте  телеграм-бот с помощью  [**телеграм-бота**](https://t.me/BotFather) и получите токен. Токен выглядит наподобие такой строки: 
```6552612291:AAHL80fIRBI4vRypY2L5K3RXr3F2-tVYf9Q```
- Добавьте созданный бот в ваш канал и выдайте ему права администратора.
- Создайте в корне проекта, файл ```.env```
Пропишите в нем:
```
NASA_API_KEY=ВАШ ТОКЕН
SPACE_TELEGRAM_TOKEN=ВАШ ТОКЕН
SPACE_CHANNEL_ID=@ИМЯ КАНАЛА
```
- Для изоляции проекта рекомендуется развернуть виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
- Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
## Использование
### fetch_spacex_images
- Загрузит фото от SpaceX по-указанному ID запуска.
  ```
  python fetch_spacex_images.py ИМЯ_ФОТО -id ID_ЗАПУСКА
  ```
    где:
    **ИМЯ_ФОТО** - как хотите назвать скачанные фотографии, **указывать обязательно**.

     **ID_ЗАПУСКА** - выглядит наподобие такой строки: **6243adcaaf52800c6e919254**. Можно получить по [АПИ](https://api.spacexdata.com/v5/launches)

- Если ID запуска не указан, качает фото с последнего запуска:
  ```
  python fetch_spacex_images.py ИМЯ_ФОТО
  ```
- Получить краткую справку по скрипту:
  ```
  python fetch_spacex_images.py -h
  ```
***
### fetch_nasa_apod
- Загрузит APOD-фотографию NASA
```
python fetch_nasa_apod.py ИМЯ_ФОТО
```
где:
    **ИМЯ_ФОТО** - как хотите назвать скачанные фотографии, **указывать обязательно**.
- Чтобы загрузить много фотографий ,  укажите необходимое количество:
```
python fetch_nasa_apod.py ИМЯ_ФОТО -с КОЛИЧЕСТВО
```
- Получить краткую справку по скрипту:
```
python fetch_nasa_apod.py -h
```
***
### fetch_epic
- Загрузит вчерашние EPIC-фотографии NASA.
```
python fetch_epic.py
```
- Загрузит EPIC-фотографии на нужную дату:
```
python fetch_epic.py -d ДАТА
```
Дату укажите в формате **YYYY-MM-DD**
- Получить краткую справку по скрипту:
```
python fetch_epic.py -h
```
***
### Запуск Бота
- Для публикации случайной фотографии:
```
python bot.py
```
- Для публикации конкретной фотографии:
```
python bot.py -n ИМЯ_ФОТО
```
- Для публикации всех скачанных фотографий раз в 4 часа. 
```
python bot.py -a
```
Если вдруг все фото из директории будут опубликованы – он просто начинает публиковать их заново, перемешав фото в случайном порядке.
- Для изменения интервала публикации:
```
python bot.py -a -t ВРЕМЯ_В_СЕКУНДАХ
```
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
