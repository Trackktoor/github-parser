# Техническое задание для команды DD TEAM
# Время выполенения: 16 мая 2023 по 1 июня 2023 включительно
## **ОПИСАНИЕ ПРОЕКТОВ**


## НАИЛЬ

## ПРОЕКТ API GITHUB + LOGGING INFO TO JSON + Parser

### Для проверки будет иcпользоватья POSTMAN
### Также будет тестирование с копированием репозитрия (Должен быть файл requirements.txt)

## **РУТЫ ДЛЯ ЗАПРОСОВ** *EntryPoint: http://get_info/
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


## ДИМА

## ПРОЕКТ PARSER VK GROUPS + JSON 



## Пример выполнения программы

## Консоль
# $desktop: python3 parser_vk_groups.py
# $desktop: Enter link group: {link_group}
# $desktop: Data collection...
# $desktop: Data loaded into {group name in vk}.json file

### Пример JSON файла

```JSON
{
  "data": {
      {
        "title_group": "Title_1",
        "count_users": 250000,
        "avatar_group": "{path to image file}",
        "description_group": "Description_1"
      }
  }
}
