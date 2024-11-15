def stop_words(words: list):
    def wrapper(func):
        def inner(*args, **kwargs):
            censorship = func(*args, **kwargs)
            for word in words:
                censorship = censorship.replace(word, '*')
            return censorship
        return inner
    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"