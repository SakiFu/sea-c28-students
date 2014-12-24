def p_wrapper(func):
    def new_function(*args, **kwargs):
        string = func(*args, **kwargs)
        string = "<p>{0}</p>".format(string)
        return string
    return new_function


@p_wrapper
def return_string(string):
    return string


@p_wrapper
def string_multiplier(string):
    return string * 5


@p_wrapper
def string_b(string):
    return "<b>{0}</b>".format(string)


if __name__ == '__main__':
    assert return_string("I'm wrapped by a p tag.") ==\
        "<p>I'm wrapped by a p tag.</p>"

    assert string_multiplier("I'm string")

    assert string_b("I'm a b tag and a p tag.")
