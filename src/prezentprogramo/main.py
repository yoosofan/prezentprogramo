#!/usr/bin/env python3
# Based on Grok 4 expert mode on X.com
# 2025/10/25 16:14:54

import sys
from html import escape

from docutils import nodes
from docutils.core import publish_cmdline, default_description
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.states import Body, state_classes
from docutils.parsers.rst import Parser as BaseParser
from docutils.readers.standalone import Reader as BaseReader
from docutils.transforms import Transform
from docutils.writers.html5_polyglot import Writer as BaseWriter, HTMLTranslator as BaseTranslator

# Custom node for slide breaks
class slide_break(nodes.General, nodes.Element):
    pass

# Custom directive for yographviz
class YographvizDirective(Directive):
    has_content = True

    def run(self):
        content = '\n'.join(self.content)
        html = f'<div class="graphviz">{escape(content)}</div>'
        return [nodes.raw('', html, format='html')]

directives.register_directive('yographviz', YographvizDirective)

# Custom Body state to handle specific transitions
class CustomBody(Body):
    def transition(self):
        line = self.state_machine.line.strip()
        if line == '----':
            return [slide_break()]
        else:
            return [nodes.transition()]

# Custom Parser using the custom Body
class CustomParser(BaseParser):
    def __init__(self):
        super().__init__()
        #self.state_classes = state_classes.copy()
        #self.state_classes['body'] = CustomBody
        #self.state_classes = tuple(
        #    ('body', CustomBody) if state_name == 'body' else (state_name, state_class)
        #    for state_name, state_class in self.state_classes
        #)

        #self.state_classes = tuple(new_state_classes)

        new_state_classes = []
        for state_class in self.state_classes:
            if state_class.__name__ == 'body':  # Check by class name
                new_state_classes.append(CustomBody)
            else:
                new_state_classes.append(state_class)

        self.state_classes = tuple(new_state_classes)

# Custom transforms
class CustomDocinfoTransform(Transform):
    default_priority = 360  # Before reference resolution

    def apply(self):
        if not self.document.children or not isinstance(self.document.children[0], nodes.docinfo):
            return
        docinfo = self.document.children[0]
        fields = {}
        to_remove = []
        for child in docinfo.children:
            if isinstance(child, nodes.field):
                name = child[0].astext().lower()
                value = ' '.join(child[1].astext().split())  # Normalize whitespace
                if name in ('generator', 'style', 'javascript'):
                    fields[name] = value
                    to_remove.append(child)
        for child in to_remove:
            docinfo.remove(child)
        self.document['custom_generator'] = fields.get('generator')
        self.document['custom_styles'] = fields.get('style', '').split()
        self.document['custom_scripts'] = fields.get('javascript', '').split()

class SlidesTransform(Transform):
    default_priority = 810  # After contents and other structural transforms

    def apply(self):
        pending = list(self.document.children)
        self.document.children = []
        current_section = None
        i = 0
        while i < len(pending):
            node = pending[i]
            if isinstance(node, (nodes.docinfo, nodes.decoration, nodes.topic, nodes.sidebar)):
                self.document.append(node)
                i += 1
                continue
            if current_section is None:
                current_section = nodes.section(classes=['slide'])
                self.document.append(current_section)
            if isinstance(node, slide_break):
                current_section = nodes.section(classes=['slide'])
                self.document.append(current_section)
                i += 1
                # Handle optional field_list for :class: and :id:
                if i < len(pending) and isinstance(pending[i], nodes.field_list):
                    field_list = pending[i]
                    for field in field_list:
                        name = field[0].astext().lower()
                        value = field[1].astext()
                        if name == 'class':
                            current_section['classes'].append(value)
                        elif name == 'id':
                            current_section['ids'] = [value]
                            current_section['names'] = [value]
                    i += 1
                continue
            current_section.append(node)
            i += 1

# Custom HTML Translator to inject custom head elements
class CustomTranslator(BaseTranslator):
    def __init__(self, document):
        super().__init__(document)
        custom_generator = document.get('custom_generator')
        if custom_generator:
            self.meta.append(f'<meta name="generator" content="{escape(custom_generator)}" />')
        for css in document.get('custom_styles', []):
            self.head.append(f'<link rel="stylesheet" href="{escape(css)}" />\n')
        for js in document.get('custom_scripts', []):
            self.head.append(f'<script src="{escape(js)}"></script>\n')

# Custom Writer using the custom translator
class CustomWriter(BaseWriter):
    def __init__(self):
        super().__init__()
        self.translator_class = CustomTranslator

# Custom Reader to include the custom transforms
class CustomReader(BaseReader):
    def get_transforms(self):
        return super().get_transforms() + [CustomDocinfoTransform, SlidesTransform]

# Main entry point, similar to rst2html5 but with custom components
#if __name__ == '__main__':
def main():
    argv = sys.argv[1:]
    if not argv:
        print("Usage: prezentprogramo source.rst [destination]")
        sys.exit(1)
    description = ('Generates HTML5 documents from standalone '
                   'reStructuredText sources with custom features. ' + default_description)
    print(argv)
    publish_cmdline(reader=CustomReader(),
                    parser=CustomParser(),
                    writer=CustomWriter(),
                    description=description,
                    argv=argv)
