## Документация к проекту 

## ПРОЕКТ API GITHUB + LOGGING INFO TO JSON + Parser

# Зависимости указаны в файле requirements.txt
# Команла для установки pip install -r requirements.txt

## **РУТЫ ДЛЯ ЗАПРОСОВ** *EntryPoint: http://localhost/get_info/
## **Получение всех назавний репозиториев их описания и когда было последнее изменение**


### Обязательные аргументы 

- `github_username` - Имя пользователья хитхаб репозитории которого мы хотим залогировать

### Пример запроса 

```form-data

  github_usrname: {username}

```

### Пример ответа

```JSON
{
  "data": {
    "all_repositories": [
      {
        "title_repository": "Title_1",
        "description_repository": "Description_1",
        "last_change_date": дд-мм-гггг чч-мм
      },
      {
        "title_repository": "Title_2",
        "description_repository": "Description_2",
        "last_change_date": дд-мм-гггг чч-мм
      }
    ]
  }
}
```

## LOGGER

# Далее нужно сделать консольное приложение которое будет отправлять
# Запросы тебе на API и полученные данные выводить в JSON файлы, у
# которых имя должно соответсвовать имени пользователя
# Так же при повторном запуске скрипта если появился новый репозиторий
# или описание, последнее изменение, они должны быть заменены в файле пользователя.


## Схема работы:

# GET-запрос на данные с консоли -> Обработка данных в консольном приложении
# -> Создание/изменение файла json (Который соответствует нику на GITHUB)