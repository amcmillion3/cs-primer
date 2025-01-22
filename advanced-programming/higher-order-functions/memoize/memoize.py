import urllib.request

def memoize(fn):
    def inner(arg):
        if arg in cache:
            return cache[arg]
        res = fn(arg)
        cache[arg] = res
        return res
    return inner

cache = {}

def fetch(url):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        return content

@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # fetch = memoize(fetch)
    # print(fetch('http://google.com')[:80])
    # print(fetch('http://google.com')[80:160])
    # print(fetch('http://google.com')[160:240])
    # print(fetch('http://google.com')[240:320])

    print(fib(35))
