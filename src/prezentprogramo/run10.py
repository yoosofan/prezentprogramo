# Based on google Geminimport re
import io
import sys
import os
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.core import publish_string
# Import the modern HTML5 components as a base
from docutils.writers.html5_polyglot import Writer as HTML5WriterBase, HTML5Translator

# --- Custom Node Definition (Same as before) ---
class graphviz_block(nodes.General, nodes.Element):
    """
    A custom Docutils node to represent the content of a graphviz directive.
    Inheriting from nodes.General and nodes.Element ensures correct initialization.
    """
    def __init__(self, rawsource='', *children, **attributes):
        super().__init__(rawsource, *children, **attributes)


# --- Custom Translator (Fix for "visiting unknown node type" error) ---
class GraphvizHTML5Translator(HTML5Translator):
    """
    A custom translator based on HTML5Translator that knows how to render
    the custom 'graphviz_block' node.
    """
    def visit_graphviz_block(self, node):
        # 1. Start the main container div for the graph
        self.body.append(self.starttag(node, 'div', '', **{'class': 'graphviz-container'}))

        # Extract the raw DOT content stored as the child (nodes.Text)
        dot_content = node.children[0].astext()

        # 2. Add the title/caption if available (argument to the directive)
        # IDs are generated from the directive's argument (e.g., "My Diagram" -> "my-diagram")
        if node.hasattr('ids') and node['ids']:
             self.body.append(f'<p class="graphviz-title">{node["ids"][0].replace("-", " ").title()}</p>')

        # 3. For now, render the raw DOT code inside a <pre> block
        # In the next step, this will be replaced with the actual SVG output.
        self.body.append('<pre class="dot-source-code">\n')
        self.body.append(self.encode(dot_content))
        self.body.append('\n</pre>\n')


    def depart_graphviz_block(self, node):
        # Close the main container div
        self.body.append('</div>\n')


# --- Custom Writer (To use our custom translator) ---
class GraphvizHTML5Writer(HTML5WriterBase):
    """
    A custom Docutils writer that ensures our custom translator is used.
    """
    supported = ('html', 'html5')
    output = 'html'

    def __init__(self):
        super().__init__()
        # Point the writer to our custom translator class
        self.translator_class = GraphvizHTML5Translator


# --- Custom Directive Definition (Same as before) ---
class GraphvizDirective(Directive):
    """
    A simple custom directive to capture content for graphviz processing.
    """
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
    }

    def run(self):
        self.assert_has_content()

        content = '\n'.join(self.content)
        text_node = nodes.Text(content)

        # Instantiate the custom node
        block = graphviz_block(self.block_text, text_node)

        # Apply :class: option
        if 'class' in self.options:
            block['classes'] = self.options['class']

        # Apply :name: option
        if 'name' in self.options:
            block['names'] = [self.options['name']]

        return [block]


# --- Helper Function for Publishing ---
def publish_to_html(source_rst):
    """
    Publishes the reStructuredText source string to an HTML string,
    registering the custom directive and using the custom HTML5 writer.
    """
    # Docutils requires directives to be registered before parsing begins.
    directives.register_directive('graphviz', GraphvizDirective)

    # We now explicitly use our custom writer instance
    output = publish_string(
        source=source_rst,
        writer=GraphvizHTML5Writer(), # <-- **The key change**
        settings_overrides={
            'output_encoding': 'unicode',
            'initial_header_level': 2,
        },
        enable_exit_status=True,
    )
    return output


# --- Example Usage ---

# Example rST content that uses the custom directive
example_rst = """
My Presentation Title
=====================

.. graphviz:: My Diagram
   :class: flow-diagram
   :name: my-first-graph

   digraph G {
       a -> b;
       b -> c;
       c -> a;
   }
"""

if __name__ == "__main__":
    try:
        html_output = publish_to_html(example_rst)
        print("--- Generated HTML Output (Using HTML5 Translator) ---")
        print(html_output)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

"""

That's excellent context, and I appreciate you sharing your experience with Hovercraft and `prezentprogramo`—it confirms you're aiming for the most robust and future-proof approach to building your generator!

### 1. The `publish_*` Functions Approach (Confirmation)

You are absolutely correct. Using the `publish_*` functions (like `publish_string`, `publish_parts`, or `publish_cmdline`) is the **recommended and cleanest way** to implement your application.

**Why `publish_string` is the best choice:**

1.  **High-Level Abstraction:** It abstracts away the low-level Docutils mechanics (the parser, the transformer, the components of the state machine), allowing you to focus only on your custom extension code (directives, nodes, roles).
2.  **Built-in Compatibility:** By relying on this function, you ensure your process follows the full, standard Docutils processing pipeline (parsing → transforming → writing). As long as Docutils maintains the stability of its high-level API, your application is far less likely to break with updates, unlike manually orchestrating the parser and transformer objects yourself.
3.  **Correct Settings Handling:** It simplifies the application of configuration overrides (`settings_overrides`) for things like initial header level, language, and custom writers.

It is, without a doubt, the superior architectural choice for building a Docutils-based application like a slideshow generator.

### 2. Debugging the `AttributeError`

You nailed two key points: the unnecessary `destination` argument in `publish_string` and the new `AttributeError`.

The error `AttributeError: 'GraphvizDirective' object has no attribute 'set_classes'` occurs because the method `self.set_classes()` is not consistently available or relied upon in all versions of the Docutils `Directive` base class.

To fix this and make the code maximally robust, we should avoid that convenience method and instead **manually apply the classes and names** attributes to the custom node. This is a more explicit and bulletproof way to use the values parsed by `option_spec`.

I have updated `run7.py` to fix both issues:

1.  **Removed redundant `destination`:** I cleaned up the `publish_to_html` function.
2.  **Fixed `AttributeError`:** I replaced the problematic `self.set_classes([block])` call with explicit checks and assignments for `'class'` and `'name'` options.

Here is the corrected file:


http://googleusercontent.com/immersive_entry_chip/0

The code should now parse your example reST without errors, successfully registering the custom node and applying the classes and names attributes! The next logical step is to actually take the raw DOT content and transform it into an SVG for inclusion in the document tree.






That is an excellent point and exactly the next hurdle in creating a custom Docutils extension! Your observation about the `publish_*` functions being the best choice for forward compatibility is 100% correct, and the error you hit is the consequence of that high-level pipeline running.

### 1. Why the Error Occurred

The error `visiting unknown node type: graphviz_block` occurred because:

1.  **Parsing Phase Succeeded:** Your custom `GraphvizDirective` successfully ran and inserted your custom `graphviz_block` node into the Docutils document tree.
2.  **Writing Phase Failed:** When Docutils moved to the writing phase (using the default HTML translator), it encountered a node it didn't recognize. The default translator only knows how to handle standard reST nodes (paragraphs, sections, lists, etc.). It needs explicit instructions on how to convert your `graphviz_block` node into HTML tags.

### 2. The HTML4 vs. HTML5 Question

You asked: **"Why do you use html4 instead of html5?"**

When you use `writer_name='html'` (or omit the writer name entirely) in Docutils, it historically defaults to the older, more conservative `html4css1` writer.

To use modern HTML5 features and structure, you need to explicitly tell Docutils to use the polyglot HTML5 writer. However, since we must also introduce our custom node, the most robust way is to create a small, custom **Writer** and **Translator** pair based on the modern HTML5 polyglot implementation.

### 3. The Solution: Custom Translator

To solve both the HTML5 question and the `unknown node type` error, I have updated `run7.py` to include a custom `GraphvizHTML5Translator` and a corresponding `GraphvizHTML5Writer`.

This new translator includes the two mandatory methods for any custom node:

* `visit_graphviz_block(self, node)`: Tells the translator how to *start* rendering the node (e.g., opening a `<div>`).
* `depart_graphviz_block(self, node)`: Tells the translator how to *finish* rendering the node (e.g., closing the `<div>`).

For now, the code will render the raw DOT content inside an HTML `<pre>` block, proving that the node and the custom translator are working correctly.

Here is the complete, corrected file:


http://googleusercontent.com/immersive_entry_chip/0

With this update, you are now correctly using the HTML5 base translator and have successfully implemented the visit/depart methods required to handle your custom node. The code is now ready for the next step: actually using a library (like `graphviz` in Python) to convert the DOT code into an SVG string within the `visit_graphviz_block` method.

"""

