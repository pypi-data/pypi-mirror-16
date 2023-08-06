# --------------------------------------------------------------------------
# This extension adds a syntax-highlighting filter to Ibis templates.
#
# The filter accepts an input string and an optional language name:
#
#     {{ string|pygmentize:lang }}
#
# If the Pygments package is not available or if an appropriate lexer can
# not be found the filter will return the input text with any HTML special
# characters escaped.
#
# This extension is included for use in the bundled 'debug' theme.
#
# Author: Darren Mulholland <darren@mulholland.xyz>
# License: Public Domain
# --------------------------------------------------------------------------

import html
import ibis


try:
    import pygments
    import pygments.lexers
    import pygments.formatters
except ImportError:
    pygments = None


@ibis.filters.register('pygmentize')
def pygmentize(text, lang=None):
    if pygments:
        if lang:
            try:
                lexer = pygments.lexers.get_lexer_by_name(lang)
            except pygments.util.ClassNotFound:
                lexer = None
        else:
            try:
                lexer = pygments.lexers.guess_lexer(text)
            except pygments.util.ClassNotFound:
                lexer = None
        if lexer:
            formatter = pygments.formatters.HtmlFormatter(nowrap=True)
            text = pygments.highlight(text, lexer, formatter)
        else:
            text = html.escape(text)
    else:
        text = html.escape(text)
    return text
