# Sprint_7
### Проект автоматизации тестирования приложения Яндекс Самокат
1. Этот проект содержит автотесты для API сервиса Яндекс.Самокат, включая следующие функции:

Создание курьера
Логин курьера
Создание заказа
Получение списка заказов

Структура репозитория:
Директория tests: включает файлы с тестами для функций. 
data: файл с тестовыми данными.
conftest: файл с фикстурами.
fake_data: файл со вспомогательными функциями: генерация данных с помощью библиотеки faker.
api_shop: файл со вспомогательными функциями: содержит генерацию тел запросов и запросы.
allure_results: JSON-файлы с результатами выполнения тестов для генерации отчетов. 
requirements.txt: список всех внешних зависимостей, необходимых для выполнения тестов. 
README.md: руководство по проекту. 
2. Основа для написания автотестов — фреймворки pytest
3. Установить зависимости:  
```bash  
pip install -r requirements.txt
```  
4. Команда для запуска тестов `pytest -v tests`
5. Сгенерирован Allure-отчёт.
