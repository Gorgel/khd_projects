__author__ = 'gorgel'

import markdown2

from markdown2Mathjax import sanitizeInput, reconstructMath
from markdown2 import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):

    # thanks to https://github.com/constantAmateur/markdown2Mathjax
    extras = ["fenced-code-blocks", "spoiler"]
    tmp = sanitizeInput(value)
    markedDownText = markdown2.markdown(force_unicode(tmp[0]), extras = extras)
    finalOutput = reconstructMath(markedDownText,tmp[1])
    return mark_safe(finalOutput)

#old working code, save for now.
#@register.filter(is_safe=True)
#@stringfilter
#def custom_markdown(value):
#    extras = ["fenced-code-blocks"]
#
#    return mark_safe(markdown2.markdown(force_unicode(value),
#                                      extras = extras))