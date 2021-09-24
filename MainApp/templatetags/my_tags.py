from django import template

register = template.Library()


def repl(value: str, tag="<br>"):
    return value.replace("\n", tag)


register.filter('repl', repl)
