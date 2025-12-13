# Based on DeepSeek

from docutils.core import publish_cmdline
from prezentprogramo.readers import PrezentprogramoReader
#from prezentprogramo.writers import SlideHTMLWriter
from prezentprogramo.writers import DebugSlideWriter

import sys

def publish_slides():
    """
    Main function to publish slides using Prezentprogramo
    """
    # Use the simpler writer if the main one has issues
    #from prezentprogramo.writers import SimpleSlideWriter

    overrides = {
        'math_output': 'MathML',
        #'output_encoding': 'unicode',
        'traceback': True,  # Always enable for our wrapper
        'halt_level': 2, #5,
        'debug': True,
    }

    argv = sys.argv[1:]

    if not argv:
        print("Usage: prezentprogramo source.rst [destination]")
        sys.exit(1)

    # Use the custom reader and writer
    publish_cmdline(
        reader=PrezentprogramoReader(),
        writer=DebugSlideWriter(), #SlideHTMLWriter(),
        settings_overrides=overrides,
        argv=argv
    )
def main():
    publish_slides()

# https://docutils.sourceforge.io/0.22/docs/api/publisher.html