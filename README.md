# frnkn

## Установка и разыертывание

### 1. Склонировать официальный репозиторий AirByte

  ```
  git clone https://github.com/airbytehq/airbyte.git
  ```
  
Перейти в папку `./airbyte` и запустить родной скрипт доустановки
(Папка `airbyte` будет основной папкой проекта)
  ```
  cd airbyte

  ./run-ab-platform.sh
  ```
Скрипт является инструментом управления следующих ассетов:
  <p>
    
  `docker_compose_yaml` `docker_compose_debug_yaml` `dot_env` `dot_env_dev` `flag`
  </p>
  <p>
Если запускать его без флагов, он скачивает эти ассеты с официального репозитория.
  </p>
  
  >Подробнее о скрипте:
  >```
  >./run-ab-platform.sh -h 
  >```

  
###  2. Склонировать репозиторий частей франкенштейна и скопировать их в основную папку проекта

Перейти в предыдущую папку и склонировать этот репозиторий рядом с папкой `./airbyte`
```
cd ..

git clone https://github.com/i-sergh/frnkn/tree/master.git
```

> В текущей дирректории должно быть две папки `./airbyte` и `./frnkn`
> ```
>  ls
> ```
>  `airbyte` `frnkn`

Для простоты копирования файлов, рекомендую предварительно удалить лишниеи файлы
```
cd frknn
rm README.md
rm -r .git
```
Скопировать файлы в папку проекта
```
cp -r * ../aibyte
```

# Запуск
Для запука переходим в папку проекта `./airbyte` и запускаем docker compose
```
 cd ../airbyte
 sudo docker-compose up
```

# Спецификация
>
>
# Проблемы
 На текущий момент `Debezium` работает с переменным успехом. На `Ubuntu 20.04` вылетает графическая оболочка с ошибкой 
 
