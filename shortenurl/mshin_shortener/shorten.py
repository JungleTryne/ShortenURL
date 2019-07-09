import time
import random
from main.models import URLPair


def generate_code(length: int) -> str:
    '''Function generates code for URL. Returns code'''
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = ""
    seed = time.time()
    random.seed(seed)
    for i in range(length):
        code += alpha[random.randint(0, len(alpha)-1)]
    return code


def shorten_url(url) -> str:
    '''Returns finished shortened URL, base on website base URL'''
    base_url = "https://jungletryne.pythonanywhere.com/"
    all_urls = URLPair.objects.all().filter(initial_url=url)
    if len(all_urls) == 0:
        code = generate_code(7)
        while len(URLPair.objects.all().filter(new_url=code)) > 0: #if new code already exists
            code = generate_code(7)
        pair = URLPair(initial_url=url, new_url=code)
        pair.save()
    else:
        existing_code = list(all_urls)[0]
        code = existing_code.new_url
    return base_url+code