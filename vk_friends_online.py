# -*- coding: utf-8 -*-
import os
import sys
import vk_requests
from os.path import join, dirname
from dotenv import load_dotenv

from vk_get_token import SECRETS_FILE_NAME


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

    vk_app_token = os.environ.get('VK_APP_TOKEN')

    if vk_app_token:
        api = vk_requests.create_api(access_token=vk_app_token)
    else:
        print('Не указан токен в файле %s' % SECRETS_FILE_NAME)
        exit(1)

    friends_online = api.friends.getOnline()
    friends_online_list = api.users.get(
        user_ids=', '.join([str(x) for x in friends_online]))
    print('\nВаши друзья онлайн:\n')
    for friend in friends_online_list:
        print('%s %s' % (friend['first_name'], friend['last_name']))
