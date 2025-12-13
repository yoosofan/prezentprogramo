# Based on google Geminimport re
"""
https://github.com/adamzap/landslide/tree/master/landslide
and
https://github.com/ionelmc/python-darkslide

are like Hovercraft. These implementatioins don't use publish_cmd or publish_string.

I do know Hovercraft because I used it for many years and forked it by the name prezentprogramo.
But it cannot be updated when docutils updated and add features.
Rewriting it for new versions of doctils are not useful because it needs a lot of work and it can be done more easily by publish_ funcitons and also are upward compatible.

Other links are useless in this matter because they are using other technologies or even programmng languages

Thanks by the way

"""

import io
import sys
import os
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.core import publish_string

# --- Custom Node Definition (Fix for TypeError around line 17) ---

# The custom node must inherit from a Docutils node class like nodes.Element
# to ensure its __init__ calls the correct constructor in the docutils hierarchy,
# which knows how to handle rawsource, children, and attributes.
class graphviz_block(nodes.General, nodes.Element):
    """
    A custom Docutils node to represent the content of a graphviz directive.
    Inheriting from nodes.General and nodes.Element ensures correct initialization.
    """
    # The Docutils base node __init__ signature is __init__(self, rawsource='', *children, **attributes)
    # We maintain this signature to correctly pass arguments up the inheritance chain.
    def __init__(self, rawsource='', *children, **attributes):
        # FIX: The key fix is the correct inheritance (above) and ensuring we call super
        # with the expected arguments for a Docutils node.
        # This will now correctly call the docutils.nodes.Node.__init__
        super().__init__(rawsource, *children, **attributes)


# --- Custom Directive Definition (using the fixed node) ---

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

    # This run method was where the error occurred on line 37 during instantiation.
    def run(self):
        # Ensure there is content in the directive body
        self.assert_has_content()

        content = '\n'.join(self.content)

        # Create a single nodes.Text object to hold the content.
        text_node = nodes.Text(content)

        # FIX: Instantiate the custom node. We pass the children (text_node)
        # as a positional argument, which is then handled by the *children
        # in the graphviz_block.__init__.
        # self.block_text is the raw source text of the directive block.
        block = graphviz_block(self.block_text, text_node)

        # Apply standard docutils options (like :class: and :name:)
        self.set_classes([block])

        # A complete implementation would process 'content' (DOT code)
        # and insert the generated SVG/image here instead of just text.

        return [block]


# --- Helper Function for Publishing ---

def publish_to_html(source_rst):
    """
    Publishes the reStructuredText source string to an HTML string,
    registering the custom directive.
    """
    # Docutils requires directives to be registered before parsing begins.
    directives.register_directive('graphviz', GraphvizDirective)

    # We use io.StringIO for file-like objects for source and destination,
    # as is common when using docutils programmatically.
    destination = io.StringIO()

    # Using publish_string is the correct and modern way to process Docutils documents.
    output = publish_string(
        source=source_rst,
        writer_name='html', # The default HTML writer
        #destination=destination,
        settings_overrides={
            'output_encoding': 'unicode', # Prevents problems with Python's default encoding
            'initial_header_level': 2, # Start sections at H2
        },
        enable_exit_status=True,
    )
    # publish_string returns a tuple (output_string, publisher_object)
    return output[0]


# --- Example Usage ---

# Example rST content that uses the custom directive
example_rst = """
My Presentation Title
=====================

.. graphviz:: My Diagram

   digraph G {
       a -> b;
       b -> c;
       c -> a;
   }
"""

if __name__ == "__main__":
    try:
        html_output = publish_to_html(example_rst)
        print("--- Generated HTML Output ---")
        print(html_output)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

# That `TypeError` is a very specific issue in how you're defining and initializing a custom node within the Docutils framework\! It’s a common stumbling block when creating custom directives.
#
# The error message:
# `TypeError: object.__init__() takes exactly one argument (the instance to initialize)`
#
# This means that within your custom node's `__init__` method (`graphviz_block`), the call to `super().__init__` is resolving all the way up to Python's base `object` class, which only accepts `self` and no other arguments. This happens because your custom node class (`graphviz_block`) is likely not correctly inheriting from the required Docutils node classes (like `nodes.Element`).
#
# I have reconstructed and corrected the critical parts of `run7.py` to fix the inheritance issue, which should resolve the `TypeError`.
#
# Here is the revised `run7.py` file:
#
# http://googleusercontent.com/immersive_entry_chip/0
#
# ### What Caused the Error and How I Fixed It:
#
# 1.  **The Cause:** Your `graphviz_block` node class (around line 17) was likely not inheriting from a proper Docutils base class (e.g., `docutils.nodes.Element` or `docutils.nodes.Node`). Without this inheritance, the `super().__init__` call inside your custom node's constructor bypassed the Docutils initialization logic and went straight to Python's fundamental `object.__init__`, which doesn't accept the `rawsource` or `children` arguments you were passing.
# 2.  **The Fix:** I modified the definition of `graphviz_block` to explicitly inherit from `nodes.General` and `nodes.Element`:
#     ```python
#     class graphviz_block(nodes.General, nodes.Element):
#         This inheritance ensures that `super().__init__` resolves to the appropriate Docutils node constructor, which is designed to handle the arguments (`rawsource`, `*children`, `**attributes`) you were passing to it. I also explicitly registered the directive using `directives.register_directive('graphviz', GraphvizDirective)` inside the `publish_to_html` function, which is necessary when using `publish_string` programmatically.
#
#     ```
#
# Let me know if this successfully runs without the `TypeError` and if you'd like to dive into the next step, which would be processing the DOT code inside the directive's `run` method to generate actual SVG output\!


"""
Thanks for your answers. I've already added 'yographviz' to prezentprogramo to create graphs based on DOT language years ago. First by writing a simple program for my slide copied in the following links
https://github.com/yoosofan/slide/blob/main/tools/old_slide_runner_used4hovercraft.py
Then added it to my next project here
https://github.com/yoosofan/prezentprogramo/blob/main/hovercraft/__init__.py
class YoGraphvizDirective(Directive):


But I want to rewrite it from scratch to use the latest docutils features. It is neccessary to know how to use its technology as a developer but there is not much good documantations to expalin to do it properly. It has also several ways to implement things but it seems the best way is to use "publish_*" functions.
Am I right about it? I mean it is the best choice for using docutils for this application?

Your suggested code had another error.
By removing line 103 (destination=destination,) the first error is removed. But the following error is created:

An error occurred: 'GraphvizDirective' object has no attribute 'set_classes'

"""
