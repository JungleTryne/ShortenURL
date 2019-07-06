import time
import random

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
    code = generate_code(6)
    return base_url+code