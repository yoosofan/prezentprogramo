from docutils.parsers.rst import directives, Directive

class SlideDirective(Directive):
    """Directive for defining slides with attributes"""

    has_content = True
    option_spec = {
        'class': directives.class_option,
        'id': directives.unchanged,
        'ltr': directives.flag,
    }

    def run(self):
        section = nodes.section()
        section['classes'] = self.options.get('class', [])

        # Add ltr class if flag is present
        if 'ltr' in self.options:
            section['classes'].append('ltr')

        # Set ID if provided
        if 'id' in self.options:
            section['ids'] = [self.options['id']]

        # Parse the content
        self.state.nested_parse(self.content, self.content_offset, section)
        return [section]

# Register the directive
directives.register_directive('slide', SlideDirective)