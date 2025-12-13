from docutils.writers.html5_polyglot import Writer, HTMLTranslator

class SlideHTMLTranslator(HTMLTranslator):

    def __init__(self, document):
        print('Translator __init__')
        super().__init__(document)
        self.section_count = 0
        self.in_impress = False

    """
    def visit_document(self, node):
        # Start with impress.js structure
        self.body.append('<div id="impress">\n')
        print('visit_document(node)')

    def depart_document(self, node):
        self.body.append('</div>\n')
        print('depart document')
    """
    def visit_section(self, node):
        super().visit_section(node)
        print('visit section')

    def depart_section(self, node):
        super().depart_section(node)
        print('depart section')

    def visit_title(self, node):
        # Only call parent if we're not in a slide section
        parent = node.parent
        if not parent or 'slide' not in parent.get('classes', []):
            super().visit_title(node)
        else:
            # Custom title handling for slides
            self.body.append(self.starttag(node, 'h1', ''))

    def depart_title(self, node):
        parent = node.parent
        if not parent or 'slide' not in parent.get('classes', []):
            super().depart_title(node)
        else:
            self.body.append('</h1>\n')

    """
    def visit_title(self, node):
        # Only call parent if we're not in a slide section
        parent = node.parent
        if not parent or 'slide' not in parent.get('classes', []):
            super().visit_title(node)
        else:
            # Custom title handling for slides
            self.body.append(self.starttag(node, 'h1', ''))

    def depart_title(self, node):
        parent = node.parent
        if not parent or 'slide' not in parent.get('classes', []):
            super().depart_title(node)
        else:
            self.body.

    def visit_section(self, node):
        # Custom handling for slide sections
        if 'slide' in node.get('classes', []):
            self.section_level += 1
            atts = {'class': 'slide'}
            if node.get('ids'):
                atts['id'] = node.get('ids')[0]
            self.body.append(self.starttag(node, 'section', **atts))
        else:
            # Default section handling
            super().visit_section(node)
    def depart_section(self, node):
        if 'slide' in node.get('classes', []):
            self.section_level -= 1
            self.body.append('</section>\n')
        else:
            super().depart_section(node)
    def depart_document(self, node) -> None:
        # Close impress.js structure
        self.body.append('</div>\n')
        # Add impress.js initialization script
        self.body.append('<script src="js/impress.js"></script>\n')
        self.body.append('<script>impress().init();</script>\n')
    """

class SlideHTMLWriter(Writer):
    def __init__(self):
        super().__init__()
        self.translator_class = SlideHTMLTranslator
    """
    def translate(self):
        super().translate()
    """

# self.body.append(self.starttag(node, 'section', CLASS='slide', ID=node.get('ids', [''])[0]))
