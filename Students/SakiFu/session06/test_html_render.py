#!/usr/bin/env python


import html_render as hr
import cStringIO

from html_render import Element, Html, Body, P, OneLineTag, H

from html_render import Title, SelfClosingTag, A, Ul, Li, Meta


def test_tag():
    assert hr.Html().tag == "html"
    assert hr.Body().tag == "body"
    assert hr.P().tag == "p"
    assert hr.Hr().tag == "hr"
    assert hr.Br().tag == "br"
    assert hr.Ul().tag == "ul"
    assert hr.Li().tag == "li"
    assert hr.Meta().tag == "meta"


def test_append():
    page = hr.Element("text")
    page.append("another_text")
    assert "text" in page.content
    assert "another_text" in page.content


def test_render():
    f = cStringIO.StringIO()
    page = hr.Element("text")
    page.append("text2")
    page.render(f)
    f.reset()
    assert f.read() == '{0}{1}{2}{3}{4}{5}{6}{7}'.format(hr.Element.indent,
                                                     "<html>\n",
                                                     hr.Element.indent * 2,
                                                     "text\n",
                                                     hr.Element.indent * 2,
                                                     "text2\n",
                                                     hr.Element.indent,
                                                     "</html>\n")


def test_html():
    html = hr.Html()
    f = cStringIO.StringIO()
    html.render(f)
    f.reset()
    assert f.read() == "<!DOCTYPE html>\n<html>\n</html>\n"


def test_body():
    f = cStringIO.StringIO()
    hr.Body().render(f)
    f.reset()
    assert f.read() == '{0}{1}{2}{3}'.format(hr.Body.indent, "<body>\n",
                                             hr.Body.indent, "</body>\n")


def test_p():
    f = cStringIO.StringIO()
    hr.P().render(f)
    f.reset()
    assert f.read() == '{0}{1}{2}{3}'.format(hr.P.indent, "<p>\n",
                                             hr.P.indent, "</p>\n")


def test_title():
    t = hr.Title("PythonClass - Session 6 example")
    f = cStringIO.StringIO()
    t.render(f)
    f.reset()
    assert f.read() == '{0}{1}'.format(hr.Title.indent,
                                       "<Title>PythonClass - Session 6 example</Title>\n")


def test_a():
    a = hr.A("http://google.com","link")
    f = cStringIO.StringIO()
    a.render(f)
    f.reset()
    assert f.read() == '{0}{1}{2}{3}{4}{5}'.format(hr.A.indent,
                                             '<a href="http://google.com">\n',
                                             hr.A.indent * 2, "link\n",
                                             hr.A.indent, "</a>\n")


def test_Ul():
    f = cStringIO.StringIO()
    hr.Ul().render(f)
    f.reset()
    assert f.read() == '{0}{1}{2}{3}'.format(hr.Ul.indent, "<ul>\n",
                                             hr.Ul.indent, "</ul>\n")


def test_Li():
    f = cStringIO.StringIO()
    hr.Li().render(f)
    f.reset()
    assert f.read() == '{0}{1}{2}{3}'.format(hr.Li.indent, "<li>\n",
                                             hr.Li.indent, "</li>\n")


def test_header():
    h2 = hr.H(2, "level2 header")
    f = cStringIO.StringIO()
    h2.render(f)
    f.reset()
    assert f.read() == '{0}{1}'.format(hr.H.indent, "<h2>level2 header</h2>\n")


def test_meta():
    meta = hr.Meta(charset="UTF-8")
    f = cStringIO.StringIO()
    meta.render(f)
    f.reset()
    assert f.read() == '{0}{1}'.format(hr.Meta.indent,
                                       '<meta  charset="UTF-8"/>\n')

