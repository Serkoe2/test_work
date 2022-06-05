# Web приложение

<p>Приложение позволяет узнать текущий курс валют USD, EUR, GBP к рублю  и конвертировать в рубли  ( по курсу ЦБ )</p>
<p>DEMO https://r2s1d.herokuapp.com</p>

<h3>Функционал :</h3>
<ul>
  <li> Анимированные Кнопки USD/EUR/GBP конвертируют значение в рубли. Валюта соответсвует нажатой кнопке, результат выводится в поле</li>
  <li> Кнопка Clear очищает поле с выводом </li>
  <li> Приложение хранит данные в БД, ключом доступа к данным является параметр из сессии </li>
  <li> Кнопка Clear также очищает данные из таблицы </li>
  <li> Курс валюты подтягивается из api ЦБ https://www.cbr-xml-daily.ru/daily_json.js </li>
  <li> Курс валюты кешируется 1 раз в день в Redis </li>
</ul>


Десктоп
<img width="1366" alt="Снимок экрана 2022-06-04 в 22 48 15" src="https://user-images.githubusercontent.com/67203852/172023442-e8109d2e-c50b-4ecd-b286-6547f0cb878e.png">
Мобильная версия

![2022-06-04 22 59 10](https://user-images.githubusercontent.com/67203852/172023769-0012a095-fc9d-4a12-8a6f-5c05faaa9a9b.jpg)

<h3>Стек и технологии :</h3>
<ul>
  <li> Flask </li>
  <li> ORM sql alchemy </li>
  <li> Bootstrap </li>
  <li> Postgres </li>
  <li> Heroku </li>
  <li> Redis </li>
</ul>
