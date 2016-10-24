# -*- coding: utf-8 -*-
import os
import webbrowser
from os.path import join, dirname
from dotenv import load_dotenv
import sys

SECRETS_FILE_NAME = '.secrets'
#  права приложения через запятую, без пробелов
#  https://vk.com/dev/permissions
VK_SCOPE = 'friends,offline'


def enable_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


if __name__ == '__main__':

    enable_win_unicode_console()

    dotenv_path = join(dirname(__file__), SECRETS_FILE_NAME)
    load_dotenv(dotenv_path)

    vk_app_id = os.environ.get('VK_APP_ID')
    if vk_app_id:
        url = 'https://oauth.vk.com/authorize?client_id=' + vk_app_id + \
          '&scope=' + VK_SCOPE + '&redirect_uri=' + \
          'https://oauth.vk.com/blank.html' + \
          '&display=page&v=5.59&response_type=token'
        webbrowser.open(url)
    else:
        print('Не указан VK_APP_ID в файле %s' % SECRETS_FILE_NAME)
