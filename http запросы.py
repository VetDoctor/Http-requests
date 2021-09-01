# 1) Ищем самого умного героя

# from pprint import pprint
#
# import requests
#
# import json
#
# super_heroes = {}
#
# TOKEN = '2619421814940190'
#
# API = "https://superheroapi.com/api/2619421814940190/"
#
# hero_list = {'Hulk', 'Captain America', 'Thanos'}
#
# for name in hero_list:
#     responses = requests.get(API + f'/search/{name}')
#     hero_intelligence = responses.json()['results'][0]['powerstats']['intelligence']
#     hero_name = responses.json()['results'][0]['name']
#     super_heroes[hero_name] = hero_intelligence
# print(max(super_heroes))


# 2) Загружаем файл на ЯД

# import yadisk
# import os
# import glob
# from os import path
#
# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token
#
#     def upload(self, file_path: str):
#         """Метод загружает файлы по списку file_list на яндекс диск"""
#         if path.exists(file_path):  # ищем txt фалы по указанному пути
#             pattern = '*.txt'
#             glob_path = os.path.join(file_path, pattern)
#             list_files = glob.glob(glob_path)
#             for files in list_files:
#                 yd = yadisk.YaDisk(token='токен')
#                 yd.mkdir('/test/Python courses')  # создаем на ЯД папку
#                 yd.upload('*.txt', '/test/*.txt')  # загружаем в нее файлы
#
#
# if __name__ == '__main__':
#     # Получить путь к загружаемому файлу и токен от пользователя
#     path_to_file = ...
#     token = ...
#     uploader = YaUploader(token)
#     result = uploader.upload(path_to_file)
