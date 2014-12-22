class Element(object):
    u"""Create an html elment object."""
    indent = u"    "
    tag = u"html"

    def __init__(self, content=None, **kwargs):
        if content:
            self.content = [content]
        else:
            self.content = []
        if kwargs:
            self.attribute = kwargs
        else:
            self.attribute = None

    def append(self, str_):
        self.content.append(str_)

    def render(self, file_out, ind=""):

        atr = ""
        file_out.write("{0}<{1}{2}>\n".format(self.indent,
                                              self.tag, atr))
        for line in self.content:
            try:
                line.render(file_out, self.indent)
            except AttributeError:
                file_out.write("{0}{1}\n".format(self.indent, line))
        file_out.write("{0}</{1}>\n".format(self.indent, self.tag))


class Html(Element):
    tag = u"html"
    
    def render(self, file_out, ind=u""):
        print u"in Html render method"
        file_out.write(u"<!DOCTYPE html>")
        # call the superclass render:
        Element.render(self, file_out, ind)


class Body(Element):
    tag = u'body'

    def __init__(self, content=None, **kwargs):
        super(Body, self).__init__(content, **kwargs)


class P(Element):
    tag = u'p'


class Head(Element):
    tag = u'head'


class OneLineTag(Element):
    def render(self, file_out, ind=""):
        file_out.write("{0}<{1}>".format(ind, self.tag))
        for content in self.content:
            file_out.write(content)
        file_out.write("{0}<{1}>\n".format(ind, self.tag))


class H(OneLineTag):
    tag = u"h"

    def __init__(self, level, content):
        self.tag = "<{0}>\n".format(self.tag, level)
        OneLineTag.__init__(self, content)


class Title(OneLineTag):
    tag = u'Title'


class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        file_out.write("{0}<{1}>\n".format(ind, self.tag))


class Hr(SelfClosingTag):
    tag = u'hr'


class Br(SelfClosingTag):
    tag = u'br'


class A(OneLineTag):
    tag = u"a"

    def __init__(self, link, content):
        Element.__init__(self, content, href=link)


class Ul(Element):
    tag = u'ul'


class Li(Element):
    tag = u'li'


class Meta(SelfClosingTag):
    tag = u'meta'
