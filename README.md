# Blog
Тестовое задание на вакансию Junior Fill-Stack developer

Этот проект был выполнен с помощью IDE Pycharm.

Для запуска сайта, необходимо клонировать данный репозиторий и открыть в pycharm этот проект.
В виртуальном окружении нужно убедиться, что проект правильно загрузился, и папка проекта определена правильно.
Перейти в директорию, в которой находится файл manage.py и прописать: python manage.py runserver
или manage.py runserver.

В переменной DATABASES, которая находится в файле settings.py уже прописаны необходимые данные, чтобы подключиться к SQL серверу.

После запуска сервера, который по умолчанию будет по адресу: 127.0.0.1:8000 (порт будет определен автоматически).
Блог находится по адресу: 127.0.0.1:8000/articles/
Страница добавления новых статей находится по адресу: 127.0.0.1:8000/articles/add_article/

============================

ЗАТРУДНЕНИЯ:
В figma макете я не совсем понял логику статьи. На последней добавленной статье "Почему подросткам стоит изучать программирование?"
Есть заголовок и описание этой статьи. Но нет текста, чтобы его увидеть надо нажать читать, и перейти к полному содержанию этой статьи.
В то время как ниже, в других статьях, в частности, в статье "Как программирование развивает привычные отрасли?" есть новый атрибут,
с текстом "Профессии будущего". Что это?
В следствии этого: к каждой статье был добавлен атрибут Заголовок, чтобы можно было задавать статьям Заголовки,
которые будут отображаться снизу. Соответственно, на странице добавления статьи добавлена возможность добавлять заголовок к статьям.
На отображение последней статьи это никак не повлияло, там также выводится Название, "Текст" - думаю, оно же описание, и картинка.
Я понимаю, что релизация свойства "дата публикации" у статьи выполнена не совсем верна, поскольку тип в базе данных
является текством, вместо типа DateTime. Благодаря такому решению, полчилось реализовать вывод даты публикации
также как в шаблоне figma, код генерирует верную дату и время.

=============================

ИЗМЕНЕНИЯ:
Сверху, на странице добавления статьи, где написано "Блог / Добавление статьи"
Для удобства, в шапке страницы была добавлена кнопка перехода на страницу добавление новых статей.
Также добавлено новое поле для статьи, под названием Заголовок.
