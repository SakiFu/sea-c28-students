
def p_wrapper(a_function):
    def new_function(string):
        return "<p>{0}</p>".format(string)
    return new_function


@p_wrapper
def return_string(string):
    return string

if __name__ == '__main__':
    assert return_string("I'm wrapped by a p tag.") ==\
        "<p>I'm wrapped by a p tag.</p>"
