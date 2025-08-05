import requests
from datetime import datetime


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        t_start = datetime.now()
        result = func(*args, **kwargs)
        t_finish = datetime.now()
        execution_time = t_finish - t_start
        milliseconds = round(execution_time.microseconds / 1000)
        print(f"Function completed in "
              f"{execution_time.seconds}s {milliseconds}ms")
        return result
    return wrapper


@measure_execution_time
def get_request(url: str):
    '''
    Отправка GET-запроса на сайт url.

    :param url: str: ссылка сайта
    :return: response.headers: заголовки ответов url
    :raises ConnectionError: Ошибка запроса к сайту
    '''

    response = requests.get(url)    # Отправка GET-запроса на сайт
    if response.status_code != 200:     # Проверка статус-кода ответа
        raise ConnectionError("Произошла ошибка:", response.status_code)
    return response.headers

url = 'https://google.com'
print(get_request(url))