import datetime
import re

from bs4 import BeautifulSoup
import unittest


def count_tag_a(tag):
    if not tag: return 0
    # s = tag.a
    links = 0
    while tag is not None:
        if tag.name == 'a':
            links += 1
            tag = tag.find_next_sibling()
        else: tag = None
    return links


def parse(path_to_file):
    # Поместите ваш код здесь.
    # ВАЖНО!!!
    # При открытии файла, добавьте в функцию open необязательный параметр
    # encoding='utf-8', его отсутствие в коде будет вызвать падение вашего
    # решения на грейдере с ошибкой UnicodeDecodeError
    with open(path_to_file, encoding='utf-8') as file:
        # file_context = file.read()
        soup = BeautifulSoup(file, 'lxml')
    soup_div_bodyContent = soup.find('div', id='bodyContent')
    imgs = headers = linkslen = lists = 0
    tags_list = ['img']
    h1_h6 = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    tags_list += h1_h6
    for s in soup_div_bodyContent.find_all('img'):
        if int(s.get("width", 0)) > 199: imgs += 1
    for s in soup_div_bodyContent.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        if re.match('[ETC]', s.text): headers += 1

    # for s in soup_div_bodyContent.find_all(tags_list):
    #     if s.name == 'img':
    #         if int(s.get("width", 0)) > 199: imgs += 1
    #     elif s.name in h1_h6:
    #         if re.match('[ETC]', s.text): headers += 1
    pass
    # не очень хороший способ -------------
    # is_count = True
    # while is_count:
    #     if len(soup_div_bodyContent.select('a' + '+a' * linkslen)) != 0:
    #         linkslen += 3
    #     else:
    #         if len(soup_div_bodyContent.select('a' + '+a' * (linkslen-2))) == 0:
    #             linkslen -= 2
    #         if len(soup_div_bodyContent.select('a' + '+a' * (linkslen-1))) == 0:
    #             linkslen -= 1
    #         is_count = False
    # --------------------------------------
    pass

    for s in soup_div_bodyContent.find_all('a'):
        links = count_tag_a(s)
        if links > linkslen:
            linkslen = links

    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


def build_bridge(path, start_page, end_page):
    """возвращает список страниц, по которым можно перейти по ссылкам со start_page на
    end_page, начальная и конечная страницы включаются в результирующий список"""

    # напишите вашу реализацию логики по вычисления кратчайшего пути здесь


def get_statistics(path, start_page, end_page):
    """собирает статистику со страниц, возвращает словарь, где ключ - название страницы,
    значение - список со статистикой страницы"""

    # получаем список страниц, с которых необходимо собрать статистику
    pages = build_bridge(path, start_page, end_page)
    # напишите вашу реализацию логики по сбору статистики здесь

    return statistic


if __name__ == '__main__':
    time_start = datetime.datetime.now()
    unittest.main()
    # print(parse('wiki/Stone_Age'))
    time_end = datetime.datetime.now()
    time_work = time_end - time_start
    print("TIME =", time_work)
