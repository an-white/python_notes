import time
import logging
import requests
import threading
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s', )

URLS = [
    'https://realpython.com/'
    'https://codigofacilito.com/',
    'https://twitter.com/home',
    'https://www.google.com/',
    'https://es.stackoverflow.com/',
    'https://stackoverflow.com/',
    'https://about.gitlab.com/',
    'https://github.com/',
    'https://www.youtube.com/'
]


def generate_request(url):
    return requests.get(url)


def check_status_code(response):
    logging.info(f'>>> La respuesta del servidor es: {response.status_code}')


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:

        futuros = [executor.submit(generate_request, url) for url in URLS]

        for futuro in futuros:
            futuro.add_done_callback(
                lambda future: check_status_code(
                    future.result()
                )
            )

# otra forma
# def generate_request(url):
#     return requests.get(url)
#
#
# def check_status_code(future):
#     response = future.result()
#     logging.info(f'>>> La respuesta del servidor es: {response.status_code}')
#
#
# if __name__ == '__main_':
#     with ThreadPoolExecutor(max_workers=4) as executor:
#
#         for url in URLS:
#             futuro = executor.submit(generate_request, url)
#             futuro.add_done_callback(check_status_code)


