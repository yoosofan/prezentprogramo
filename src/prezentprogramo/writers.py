from docutils.writers.html5_polyglot import Writer, HTMLTranslator
from docutils import nodes
import os, sys

class SlideHTMLTranslator(HTMLTranslator):

    def __init__(self, document):
        super().__init__(document)
        self.section_count = 0
        self.slide_count = 0

    def visit_document(self, node):
        self.body.append('<div id="impress">\n')

    def depart_document(self, node):
        self.body.append('</div>\n')
        self.body.append('''
<script src="impress.js"></script>
<script>impress().init();</script>
''')

    def visit_section(self, node):
        if 'slide' in node.get('classes', []):
            self.slide_count += 1
            self.section_count += 1
            atts = {'class': 'step slide'}

            if node.get('ids'):
                atts['id'] = node.get('ids')[0]
            else:
                atts['id'] = f'slide-{self.slide_count}'

            atts['data-x'] = str((self.slide_count - 1) * 1000)
            atts['data-y'] = '0'

            self.body.append(self.starttag(node, 'div', **atts))
        else:
            super().visit_section(node)

    def depart_section(self, node):
        if 'slide' in node.get('classes', []):
            self.body.append('</div>\n')
            self.section_count -= 1
        else:
            super().depart_section(node)

    def visit_title(self, node):
        parent = node.parent
        if parent and 'slide' in parent.get('classes', []):
            self.body.append(self.starttag(node, 'h1', CLASS='title'))
        else:
            super().visit_title(node)

    def depart_title(self, node):
        parent = node.parent
        if parent and 'slide' in parent.get('classes', []):
            self.body.append('</h1>\n')
        else:
            super().depart_title(node)

class SlideHTMLWriter(Writer):

    def __init__(self):
        Writer.__init__(self)
        self.translator_class = SlideHTMLTranslator
        self.parts = {}

    def assemble_parts(self):
        writer = self.translator_class(self.document)
        self.visitor = writer
        self.document.walkabout(writer)

        self.parts = {
            'body': writer.body,
            'head': writer.head,
            'stylesheet': writer.stylesheet,
            'title': writer.title,
            'subtitle': writer.subtitle,
            'docinfo': writer.docinfo,
            'header': writer.header,
            'footer': writer.footer,
            'meta': writer.meta,
            'fragment': writer.fragment,
            'html_prolog': writer.html_prolog,
            'html_head': writer.html_head,
            'html_title': writer.html_title,
            'html_subtitle': writer.html_subtitle,
            'html_body': writer.html_body,
        }
        self.output = self.parts['body']

    def translate(self):
        self.assemble_parts()

class DebugSlideTranslator(HTMLTranslator):
    """
    Translator with built-in debug logging
    """

    def __init__(self, document):
        super().__init__(document)
        print(f"DEBUG: Translator initialized for {document}", file=sys.stderr)

    def visit_section(self, node):
        print(f"DEBUG: Visiting section with classes: {node.get('classes', [])}", file=sys.stderr)
        super().visit_section(node)

    def depart_section(self, node):
        print(f"DEBUG: Departing section", file=sys.stderr)
        super().depart_section(node)

    def visit_document(self, node):
        print("DEBUG: Starting document translation", file=sys.stderr)
        super().visit_document(node)

    def depart_document(self, node):
        print("DEBUG: Finished document translation", file=sys.stderr)
        super().depart_document(node)

class DebugSlideWriter(Writer):
    def __init__(self):
        super().__init__()
        self.translator_class = DebugSlideTranslator

# self.body.append(self.starttag(node, 'section', CLASS='slide', ID=node.get('ids', [''])[0]))
