from django import template

register = template.Library()


def repl(value: str, tag="<br>"):
    return value.replace("\n", tag)


def to_int(value):
    return int(value)


register.filter('repl', repl)
register.filter('to_int', to_int)