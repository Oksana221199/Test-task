| ID | 1 |
| :---- | :---- |
| **Title** | Ошибка при создании объявления с невалидными данными (sellerID\<111111) |
| **Description** | При создании объявления с невалидным значением sellerID (меньше 111111\) система возвращает успешный ответ с кодом 200 ОК и идентификатором нового объявления, вместо ожидаемого ответа с кодом 400 Bad Request и сообщением "не передан". |
| Priority | High |
| Reproduction Steps | 1\. Открыть Postman 2\. Выбрать запрос POST https://qa-internship.avito.com/api/1/item 3\. Установить параметры в body запроса: name: "Телефон" price: 85566 sellerID: 111110 4\. Отправить запрос |
| Expected Result | Запрос не должен быть отправлен, должно быть возвращено сообщение о статусе объявления \- "не передан" |
| Actual Result | Код ответа 200 ОК, возвращен идентификатор нового объявления |

| ID | 2 |
| :---- | :---- |
| Title | Ошибка при создании объявления с невалидными данными (sellerID\>999999) |
| Description | При создании объявления с невалидным значением sellerID (больше 999999\) система возвращает успешный ответ с кодом 200 ОК и идентификатором нового объявления, вместо ожидаемого ответа с кодом 400 Bad Request и сообщением "не передан" |
| Priority | High |
| Reproduction Steps | 1\. Открыть Postman 2\. Выбрать запрос POST https://qa-internship.avito.com/api/1/item 3\. Установить параметры в body запроса: name: "Фотоаппарат" price: 30000 sellerID: 1000000 4\. Отправить запрос |
| Expected Result | Запрос не должен быть отправлен, должно быть возвращено сообщение о статусе объявления \- "не передан" |
| Actual Result  | Код ответа 200 ОК, возвращен идентификатор нового объявления |

