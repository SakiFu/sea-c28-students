class Element(object):
    indent = u"  "
    tag = u"html"
    attr = ""

    def __init__(self, content=None, **kwargs):
        if content:
            self.content = [content]
        else:
            self.content = []
        if kwargs:
            for k, v in kwargs.items():
                self.attr = '{0}{1} = "{2}"'.format(self.attr, k, v)

    def append(self, str_):
        self.content.append(str_)

    def render(self, file_out, ind=indent):
        if self.attr:
            file_out.write("{0}<{1}{2}>\n".format(
                           self.indent, self.tag, self.attr))
        else:
            file_out.write("{0}<{1}>\n".format(
                           self.indent, self.tag,))
        for line in self.content:
            try:
                line.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write("{0}{1}\n".format(ind, line))
        file_out.write("{0}</{1}>\n".format(self.indent, self.tag))


class Html(Element):
    tag = u"html"

    def render(self, file_out, ind=""):
        file_out.write(u"<!DOCTYPE html>\n")
        Element.render(self, file_out, ind)


class Body(Element):
    tag = u'body'
    indent = "    "

    def __init__(self, content=None, **kwargs):
        super(Body, self).__init__(content, **kwargs)


class P(Element):
    tag = u'p'
    indent = "        "


class Head(Element):
    tag = u'head'
    indent = "    "


class OneLineTag(Element):
    def render(self, file_out, ind=""):
        file_out.write("{0}<{1}>".format(ind, self.tag))
        for content in self.content:
            file_out.write(content)
        file_out.write("</{0}>\n".format(self.tag))


class H(OneLineTag):
    indent = "    "

    def __init__(self, level, content, **kwargs):
        self.tag = u'h' + str(level)
        super(H, self).__init__(content=content, **kwargs)


class Title(OneLineTag):
    tag = u'Title'
    indent = "        "


class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        file_out.write("{0}<{1}>\n".format(ind, self.tag))


class Hr(SelfClosingTag):
    tag = u'hr'
    indent = "    "


class Br(SelfClosingTag):
    tag = u'br'
    indent = "    "


class A(OneLineTag):
    tag = u"a"
    attr = ""
    indent = "    "

    def __init__(self, link, content):
        Element.__init__(self, content, href=link)


class Ul(Element):
    tag = u'ul'
    indent = "    "


class Li(Element):
    tag = u'li'
    indent = "        "


class Meta(SelfClosingTag):
    tag = u'meta'
    indent = "        "
