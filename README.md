# frnkn

<br><br><br>


## Установка и развёртывание

---

<br>

### 1. Склонировать официальный репозиторий AirByte

<br>

  ```
  git clone https://github.com/airbytehq/airbyte.git
  ```
  
Перейти в папку `./airbyte` и запустить родной скрипт доустановки
(Папка `airbyte` будет основной папкой проекта)
  ```
  cd airbyte

  ./run-ab-platform.sh
  ```
<br>

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

<br>

###  2. Склонировать репозиторий частей франкенштейна и скопировать их в основную папку проекта

<br>

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

<br>

Для простоты копирования файлов, рекомендую предварительно удалить лишниие файлы
```
cd frknn
rm README.md
rm -r .git
```

<br>

Скопировать файлы в папку проекта
```
cp -r * ../aibyte
```

<br><br><br>

## Запуск

---

<br>

Для запука переходим в папку проекта `./airbyte` и запускаем docker compose
```
 cd ../airbyte
 sudo docker-compose up -d
```
Флаг `-d` ( `--detach` ) запускает контейнеры в фоновом режиме

<br>

> Для вывода логов конкретного контейнера 
> ```
> sudo docker logs CONTAINER_NAME
> ```

<br><br><br>

## Остановка и удаление

---

<br>

Для управления контейнерами через Docker compose нужно находиться в папке проекта `./airbyte`. Управление происходит через файл `docker-compose.yaml`. 
<br>
<br>
❗❗❗ Перед любыми обновлениями/изменениями `docker-compose.yaml` останавливайте работу контейнеров.
<br>

* Простая остановка контейнеров без их удаления
  ```
  sudo docker-compose stop
  ```
  
  <br>
  
* Остановка с удалением контейнеров и связанных с ними сетей. При этом тома контейнеров остаются нетронутыми. (Данная команда рекомендуется к использованию при обновлении/изменениями `docker-compose.yaml` )
  <br><br>
  ❗❗❗ При перезапуске контейнера с неименованным томом, имя его тома генерируется контейнеру заново. Это приводит к засорению памяти.  

  ```
  sudo docker-compose down
  ```
  <br>
  
* Для остановки контейнеров с полным их удалением, включая тома, нужно добавить флаг `-v`  ( `--volumes` )

  ```
  sudo docker-compose down -v 
  ```
  <br>
  
<br><br><br>

## Спецификация

---

<br>
 
¯\\_(ツ)_/¯ Скоро будет больше (?) 

<br><br><br>

## Проблемы

---

<br>

 На текущий момент `Debezium` работает с переменным успехом. На `Ubuntu 20.04` вылетает графическая оболочка с ошибкой 

 ```stderr
Fatal glibc error: CPU does not support x86-64-v2
```
