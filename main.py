# Пример веб-приложения

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# Для начала определим настройки запуска
hostName = 'localhost' # Адрес для доступа по сети
serverPort = 8000 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    '''
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    '''

    def do_GET(self):
        ''' Метод для обработки входящих GET-запросов '''
        self.send_response(200) # Отправка кода ответа
        self.send_header('Content-type', 'text/html') # Отправка типа данных
        self.end_headers() # Завершение формирования заголовков ответа
        with open('templates/contacts.html') as file:
            web_page = file.read()
        self.wfile.write(bytes(web_page, "utf-8")) # Тело ответа




if __name__ == '__main__':
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print('Server started http://%s:%s' % (hostName, serverPort))

    try:
        # Старт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавишь Ctr + c
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети


