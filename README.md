# Решение задачи [№8](https://devman.org/challenges/8/) с сайта [devman.org](https://devman.org)

## Условие задачи:

Вам приходилось заходить во Вконтакте и смотреть, кто из друзей онлайн? 
Это довольно просто и удобно, а поэтому неинтересно.

Сегодня мы выполним эту задачу с помощью магии Питона. 
Написать скрипт будет не так просто и удобно, зато пользоваться им будет 
одно удовольствие.

Чтобы начать, форкни и склонируй репозиторий. 
Потом установи пакеты из requirements.txt. 
Он там один, но полезный – модуль для работы с АПИ Вконтакте.

Как только будет установлено, займись кодом. 
При запуске скрипта он должен спрашивать логин и пароль пользователя и 
выводить имена и фамилии тех его друзей, кто онлайн.

## Системные требования

```
Python 3.5.2+
Внешний модуль vk-requests
Внешний модуль win-unicode-console
```

## Установка

Windows

```    
git clone https://github.com/ram0973/8_vk_friends_online.git
cd 3_bars
pip install -r requirements.txt
```

Linux
```    
git clone https://github.com/ram0973/8_vk_friends_online.git
cd 3_bars
pip3 install -r requirements.txt
```
    
    
## Описание работы

Сначала надо создать приложение [здесь](https://vk.com/editapp?act=create)
Далее в настройках приложения получить ID приложения и вписать его в файле
.secrets как VK_APP_ID = ID_Приложения (пример в файле .secrets.example,
 можно переименовать или скопировать этот файл в .secrets)
 
Далее получаем бессрочный токен приложения: 
```
python vk_get_token.py
```

Откроется ваш браузер по умолчанию, и после авторизации в адресной строке 
 получаем строку типа https://oauth.vk.com/blank.html#access_token=ВАШ_ТОКЕН&expires_in=0&user_id=USER_ID
Токен будет между access_token= и &expires_in. Его надо будет скопировать
в файл .secrets как VK_APP_TOKEN = ВАШ_ТОКЕН (пример в файле .secrets.example)

Далее получаем список друзей онлайн:
```
python vk_friends_online.py
```

## Настройки

При желании можно поменять права приложения в файле vk_get_token.py 
в константе VK_SCOPE. После этого надо будет заново получить токен и прописать
 его в secrets.py.
 
Если нужно изменить название файла с с токеном, можно поменять константу 
SECRETS_FILE_NAME в vk_get_token.py. После этого надо обязательно указать 
 новое имя файла в .gitignore
 

## Запуск

Windows

python vk_get_token.py
python vk_friends_online.py
 
Linux
 
python3 vk_get_token.py
python3 vk_friends_online.py
 
## Лицензия

[MIT](http://opensource.org/licenses/MIT)