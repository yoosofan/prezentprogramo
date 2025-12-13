# Based on google Geminimport re
import re
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.transforms import Transform
from docutils.writers.html5_polyglot import Writer as HTML5Writer, HTMLTranslator

# --- 1. Custom Node Definition ---
# Define a custom node for the 'yographviz' directive content.
# FIX: Inherit from nodes.Body to ensure correct dispatching in the translator.
class graphviz_block(nodes.Body, nodes.Element):
    """Custom node to hold the content of the yographviz directive."""
    pass

# --- 2. Custom Directive: 'yographviz' ---
class YOGraphviz(Directive):
    """
    Implements the 'yographviz' directive.
    Content is stored in a custom 'graphviz_block' node.
    """
    required_arguments = 0
    optional_arguments = 0
    has_content = True
    final_argument_whitespace = True

    def run(self):
        self.assert_has_content()
        # Join content lines into a single string for storage
        content = '\n'.join(self.content)

        # The second argument must be a Docutils node, not a string.
        # We wrap the content string in a nodes.Text node.
        return [graphviz_block(content, nodes.Text(content))]

# --- 3. Custom Transformer: Slide Structure and Metadata ---

class SlideTransformer(Transform):
    """
    Performs structural transformations required for the slideshow format:
    1. Converts '----' transition lines into 'slide' sections.
    2. Extracts :class: and :id: fields immediately following a section title
       and applies them to the slide/section node.
    """
    # Run late, after system transforms (like docinfo) but before the writer
    default_priority = 600

    def apply(self):
        document = self.document

        # 1. Handle :generator:, :style:, :javascript: custom metadata fields
        # These are initially parsed as standard docinfo fields.
        # We need to extract them and attach them to the document for the Writer.

        # Mapping of rst field name to document attribute name
        meta_fields = {
            'generator': 'generator_meta',
            'style': 'style_links',
            'javascript': 'script_links',
        }

        # Check if docinfo exists and process fields
        if document.get('docinfo'):
            for field in document['docinfo']:
                field_name = field[0].astext().lower()
                field_body = field[1].astext()

                if field_name in meta_fields:
                    # Store data on the document root node for the writer to pick up
                    attr_name = meta_fields[field_name]
                    document[attr_name] = field_body.split() # Split paths by whitespace

                    # Remove the field from the docinfo node to prevent it from being rendered
                    field.parent.remove(field)

        # 2. Convert '----' transitions into new sections/slides
        # Iterate over the document children to find transition nodes
        new_children = []
        current_section = None

        for child in document.children:
            if isinstance(child, nodes.transition) and child.astext().strip() == '----':
                # End the previous section (if any)
                if current_section is not None:
                    new_children.append(current_section)

                # Start a new section node for the slide
                current_section = nodes.section('', classes=['slide'])
                # No title for this section; it's a structural slide divider

            elif current_section is not None:
                # Add content to the current slide section
                current_section += child

                # 3. Handle :class: and :id: metadata for the current slide
                # Simple implementation: Look for a field_list right after the transition
                if isinstance(child, nodes.field_list):
                    self._extract_slide_metadata(current_section, child)
                    # Remove the field list node after processing
                    current_section.remove(child)

            else:
                # Content before the first slide/transition
                new_children.append(child)

        # Append the last section
        if current_section is not None:
            new_children.append(current_section)

        # Replace the document's children with the new structure
        document.children = new_children


    def _extract_slide_metadata(self, section_node, field_list_node):
        """Extracts :class: and :id: fields from a field_list and applies them to the section."""
        for field in field_list_node.children:
            field_name = field[0].astext().lower()
            field_body = field[1].astext().strip()

            if field_name == 'class':
                # Append to existing classes
                if 'classes' not in section_node:
                    section_node['classes'] = []
                section_node['classes'].extend(field_body.split())

            elif field_name == 'id':
                # Set id
                section_node['ids'] = [field_body]


# --- 4. Custom Writer and Translator ---

class SlideTranslator(HTMLTranslator):
    """
    Custom HTML translator to handle:
    1. Custom metadata in the <head>.
    2. The custom 'graphviz_block' node.
    """

    def visit_html_head(self, node):
        """
        Overrides the standard method to insert custom meta, style, and script tags
        based on data stored by the SlideTransformer.
        """
        # Call the parent method first to ensure standard head tags are included
        super().visit_html_head(node)

        # Add :generator: meta tag
        if 'generator_meta' in self.document:
            content = self.document['generator_meta'][0]
            self.head.append(self.emptytag(node, 'meta', name='generator', content=content))

        # Add :style: links
        if 'style_links' in self.document:
            for link in self.document['style_links']:
                self.head.append(self.emptytag(node, 'link', rel='stylesheet', href=link))

    def depart_html_head(self, node):
        # Add :javascript: script tags just before closing </head>
        if 'script_links' in self.document:
            for link in self.document['script_links']:
                self.head.append(self.starttag(node, 'script', src=link, type='text/javascript') + '</script>\n')

        super().depart_html_head(node)

    # Handler for the custom 'graphviz_block' node
    def visit_graphviz_block(self, node):
        # Open the div and immediately append the raw content
        self.body.append('<div class="graphviz">\n')
        self.body.append(node.astext())
        self.body.append('\n</div>\n')
        # Skip visiting children because we already rendered the content (node.astext())
        raise nodes.SkipNode

    def depart_graphviz_block(self, node):
        # No action needed due to the SkipNode raise in visit_graphviz_block
        pass

class SlideWriter(HTML5Writer):
    """Custom Writer that uses our custom HTML Translator."""
    supported = ('html', 'html5', 'slideshow')

    # We must explicitly set the translator class
    translator_class = SlideTranslator

    # The default transformer list is extended by the one defined on the component (Transformer.get_transforms)
    # Since we use docutils.core.publish_string, we will pass our custom transform directly.

# --- 5. Execution ---

def publish_to_html(source_rst):
    """
    The equivalent of using 'publish_cmd' with custom components.
    This function wires the custom components together.
    """
    from docutils.core import publish_string, default_description
    from docutils.parsers.rst import Parser
    from docutils.readers.standalone import Reader

    # Register the custom directive for the reST parser
    directives.register_directive('yographviz', YOGraphviz)

    # Pass our custom writer and transformer list
    # The transformer list includes our custom transformer along with the default ones
    settings_overrides = {
        'initial_header_level': 1,
        'report_level': 5, # Suppress all but severe errors/warnings
        # Add our custom transformer to the list of transforms to be applied
        'transforms': [SlideTransformer]
    }

    output = publish_string(
        source=source_rst,
        reader=Reader(),
        parser=Parser(),
        writer=SlideWriter(),
        settings_overrides=settings_overrides,
        enable_exit_status=True,
    )

    return output.decode('utf-8')

if __name__ == '__main__':
    # Example reStructuredText source demonstrating all new features
    example_rst = r"""
:generator: Docutils Slide Generator v1.0
:style: styles/main.css https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css
:javascript: scripts/app.js

=======================
Project Presentation
=======================

Introduction
============

This is the first section/slide content.
It uses the default reST sectioning.

The generator meta tag, CSS links, and JS links should appear in the <head>.

----

Slide 1: Custom Block
=====================

This section is created by the '----' transition line and automatically gets the 'slide' class.
The '----' acts as a visual and structural slide separator.

.. class:: featured-slide big-title
.. id:: first-slide-id

This text should be inside the slide section with classes 'slide' and 'featured-slide big-title', and id 'first-slide-id'.

.. yographviz::

  digraph G {
    A -> B;
    B -> C;
    C -> A;
  }

The content of yographviz is raw text inside a div with class "graphviz".

----

Slide 2: Summary

This is the final slide created by a new transition.
The four dashes '----' are treated as a structural break, not just a horizontal line.

"""

    print("--- Generated HTML Output ---")

    # Run the custom publishing pipeline
    html_output = publish_to_html(example_rst)

    # Print the output (usually the first 50 lines are sufficient to check the header and structure)
    print('\n'.join(html_output.splitlines()[:50]))
    print("...\n[Truncated for console display. Check source for full document.]\n...")

"""
This is a great catch. The `NotImplementedError` occurs because Docutils' node traversal system is unable to find the custom visitor methods (`visit_graphviz_block` and `depart_graphviz_block`) on the base `HTMLTranslator` class, which is ultimately responsible for the `unknown_visit` error.

Although we defined the methods on our inheriting class, `SlideTranslator`, the Docutils machinery sometimes requires custom block-level nodes to inherit from `nodes.Body` (in addition to `nodes.Element`) for the node type to be correctly dispatched within the document structure traversal.

I have updated the `graphviz_block` definition in `rst_slideshow_extension.py` to ensure it is correctly recognized as a body element, which should resolve the translation error.

### Changes in `rst_slideshow_extension.py`

I updated the inheritance of the custom node on **line 7**:

```python
# Old: class graphviz_block(nodes.Element):
# New: class graphviz_block(nodes.Body, nodes.Element):
```

This ensures the custom node is correctly recognized as a block-level content element, allowing the `SlideTranslator` to successfully intercept the node and execute the custom visitor methods.

http://googleusercontent.com/immersive_entry_chip/0
"""

"""
python3 run3.py
--- Generated HTML Output ---
Traceback (most recent call last):
  File "/home/ahmad/temp/prezent/src/prezentprogramo/run3.py", line 276, in <module>
    html_output = publish_to_html(example_rst)
  File "/home/ahmad/temp/prezent/src/prezentprogramo/run3.py", line 211, in publish_to_html
    output = publish_string(
        source=source_rst,
    ...<4 lines>...
        enable_exit_status=True,
    )
  File "/home/ahmad/install/14.0/lib/python3.14/site-packages/docutils/core.py", line 507, in publish_string
    output, _publisher = publish_programmatically(
                         ~~~~~~~~~~~~~~~~~~~~~~~~^
        source_class=io.StringInput, source=source, source_path=source_path,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<7 lines>...
        config_section=config_section,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        enable_exit_status=enable_exit_status)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ahmad/install/14.0/lib/python3.14/site-packages/docutils/core.py", line 794, in publish_programmatically
    output = publisher.publish(enable_exit_status=enable_exit_status)
  File "/home/ahmad/install/14.0/lib/python3.14/site-packages/docutils/core.py", line 272, in publish
    output = self.writer.write(self.document, self.destination)
  File "/home/ahmad/install/14.0/lib/python3.14/site-packages/docutils/writers/__init__.py", line 97, in write
    self.translate()
    ~~~~~~~~~~~~~~^^
  File "/home/ahmad/install/14.0/lib/python3.14/site-packages/docutils/writers/_html_base.py", line 162, in translate
    self.document.walkabout(visitor)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/home/ahmad/install/14.0/lib/python3.14/site-packages/docutils/nodes.py", line 232, in walkabout
    if child.walkabout(visitor):
       ~~~~~~~~~~~~~~~^^^^^^^^^
  File "/home/ahmad/install/14.0/lib/python3.14/site-packages/docutils/nodes.py", line 232, in walkabout
    if child.walkabout(visitor):
       ~~~~~~~~~~~~~~~^^^^^^^^^
  File "/home/ahmad/install/14.0/lib/python3.14/site-packages/docutils/nodes.py", line 232, in walkabout
    if child.walkabout(visitor):
       ~~~~~~~~~~~~~~~^^^^^^^^^
  File "/home/ahmad/install/14.0/lib/python3.14/site-packages/docutils/nodes.py", line 224, in walkabout
    visitor.dispatch_visit(self)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/home/ahmad/install/14.0/lib/python3.14/site-packages/docutils/nodes.py", line 2734, in dispatch_visit
    return method(node)
  File "/home/ahmad/install/14.0/lib/python3.14/site-packages/docutils/nodes.py", line 2757, in unknown_visit
    raise NotImplementedError(
        '%s visiting unknown node type: %s'
        % (self.__class__, node.__class__.__name__))
NotImplementedError: <class 'docutils.writers.html5_polyglot.HTMLTranslator'> visiting unknown node type: graphviz_block
(14.0) prezentprogramo$


"""

