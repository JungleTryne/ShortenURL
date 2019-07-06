import time
import random
from main.models import URLPair

def generate_code(length: int) -> str:
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = ""
    seed = time.time()
    random.seed(seed)
    for i in range(length):
        code += alpha[random.randint(0, len(alpha)-1)]
    return code


def shorten_url(url) -> str:
    base_url = "127.0.0.1:8000/"
    all_urls = URLPair.objects.all().filter(initial_url=url)
    if len(all_urls) == 0:
        code = generate_code(6)
        pair = URLPair(initial_url=url, new_url=code)
        pair.save()
    else:
        existing_code = list(all_urls)[0]
        code = existing_code.new_url
    return base_url+code