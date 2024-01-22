# WebSocket Slider Example

## English

This repository contains a simple example of a WebSocket server implemented in Python using the `aiohttp` library, along with an HTML page that displays data from
 the server and allows users to interact with a slider to send values back to the server.

### How It Works

The Python server (`app.py`) sets up a WebSocket endpoint at `ws://localhost:5000/echo` and serves an HTML page (`index1.html`).
The server sends updates from two text files (`test.txt` and `test1.txt`) to connected clients and listens for incoming slider values, which it then writes to `test3.txt`.
The HTML page contains two tables that display the values from `test.txt` and `test1.txt`, 
updating in real-time as the server sends new data. It also includes a slider that users can adjust. When the slider's value changes, it is sent to the server via the WebSocket connection and saved to `test3.txt`.

### Installation
To run this example, you will need Python 3. Install the required dependencies with the following command:
```bash
pip install -r requirements.txt
Start the server by running:
python app.py
Then, open the index4.html file in a web browser to view the page and interact with the slider.
Русский
Этот репозиторий содержит простой пример сервера WebSocket, реализованного на Python с использованием библиотеки aiohttp, а также HTML-страницу, которая отображает данные с сервера и позволяет пользователям взаимодействовать с ползунком для отправки значений обратно на сервер.
Как это работает
Python-сервер (app.py) настраивает конечную точку WebSocket по адресу ws://localhost:5000/echo и обслуживает HTML-страницу (index4.html). Сервер отправляет обновления из двух текстовых файлов (test.txt и test1.txt) подключенным клиентам и прослушивает входящие значения ползунка, которые затем записывает в test3.txt.

HTML-страница содержит две таблицы, которые отображают значения из test.txt и test1.txt, обновляясь в реальном времени по мере отправки новых данных сервером. Также на странице есть ползунок, который пользователи могут регулировать. Когда значение ползунка изменяется, оно отправляется на сервер через соединение WebSocket и сохраняется в test3.txt.

Установка
Для запуска этого примера вам понадобится Python 3. Установите необходимые зависимости с помощью следующей команды:
pip install -r requirements.txt
Запуск примера
python app.py
Затем откройте файл index4.html в веб-браузере, чтобы просмотреть страницу и взаимодействовать с ползунком.
