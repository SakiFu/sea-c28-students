class Element(object):
    indent = "  "
    tag = u"html"
    attr = ""

    def __init__(self, content=None, **kwargs):
        if content:
            self.content = [content]
        else:
            self.content = []
        if kwargs:
            self.attr = kwargs
        else:
            self.attr = None

    def append(self, str):
        self.content.append(str)

    def render(self, file_out, indent=""):
        if self.attr:
            attrs = [""]
            for attr in self.attr:
                attrs.append('{0}="{1}"'.format(attr, self.attr[attr]))
            attr = " ".join(attrs)
        else:
            attr = ""
        file_out.write("{0}{1}<{2}{3}>\n".format(indent, self.indent,
                                                 self.tag, attr))
        for line in self.content:
            try:
                line.render(file_out, indent + self.indent)
            except AttributeError:
                file_out.write("{0}{1}{2}\n".format(indent,
                                                    self.indent * 2,
                                                    line))
        file_out.write("{0}{1}</{2}>\n".format(indent, self.indent, self.tag))


class Html(Element):
    tag = u"html"

    def __init__(self, content=None, **kwargs):
        super(Html, self).__init__(content, **kwargs)
        self.indent = ""

    def render(self, file_out, indent=""):
        file_out.write(u"<!DOCTYPE html>\n")
        Element.render(self, file_out, indent)


class Body(Element):
    tag = u'body'

    def __init__(self, content=None, **kwargs):
        super(Body, self).__init__(content, **kwargs)


class P(Element):
    tag = u'p'


class Head(Element):
    tag = u'head'


class OneLineTag(Element):
    def __init__(self, content=None, **kwargs):
        super(OneLineTag, self).__init__(content, **kwargs)

    def render(self, file_out, indent=""):
        file_out.write("{0}{1}<{2}>{3}</{4}>\n".format(indent,
                                                       self.indent,
                                                       self.tag,
                                                       str(self.content[0]),
                                                       self.tag))


class H(OneLineTag):

    def __init__(self, level, content, **kwargs):
        self.tag = 'h' + str(level)
        super(H, self).__init__(content=content, **kwargs)


class Title(OneLineTag):
    tag = u'Title'


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        super(SelfClosingTag, self).__init__(content, **kwargs)

    def render(self, file_out, indent=""):
        if self.attr:
            attrs = [" "]
            for attr in self.attr:
                attrs.append(u'{0}="{1}"'.format(attr, self.attr[attr]))
            attr = u" ".join(attrs)
        else:
            attr = u""
        file_out.write(
            "{0}{1}<{2}{3}{4}/>\n".format(indent, self.indent, self.tag, attr, indent)
             )
        for line in self.content:
            try:
                line.render(file_out, indent + self.indent)
            except AttributeError:
                file_out.write(u"{}{}{}\n".format(indent, self.indent, line))


class Hr(SelfClosingTag):
    tag = u'hr'


class Br(SelfClosingTag):
    tag = u'br'


class A(Element):
    def __init__(self, link, content):
        self.tag = u"a"
        url = {u"href": link}
        super(A, self).__init__(content, **url)


class Ul(Element):
    tag = u'ul'


class Li(Element):
    tag = u'li'


class Meta(SelfClosingTag):
    tag = u'meta'
