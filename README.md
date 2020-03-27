# Cервис, который считает, сколько раз встречается слово Python в http-ответе сервера.

## Запуск 
```
git clone https://github.com/scherbininvladimir/sf-e8-homework
cd sf-e8-homework
docker-compose build
docker-compose up -d
```

## Использование
```
http://localhost:5000
```

 Поскольку рекомендуемая в задании модель не предполагает хранения информации о неуспешных запросах, "None" в полях "Кол-во вхождений" и "HTTP STATUS CODE" означает ошибку.
