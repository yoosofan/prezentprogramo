from docutils import readers
from docutils.transforms import Transform
from docutils import nodes
import sys

class PrezentprogramoReader(readers.Reader):
    def get_transforms(self):
        return super().get_transforms() + [
            SlideDetectionTransform,      # Creates slide sections from ----
            SlideEnhancementTransform,    # Adds IDs, classes, ltr/rtl
            AttributeEnhancementTransform,# Processes :class: :id: etc.
            # Your other custom transforms...
        ]

class SlideDetectionTransform(Transform):
    default_priority = 700  # Run early
    #print('SlideDetectionTransform');

    def apply(self):
        """REQUIRED method - this was missing!"""
        print("DEBUG: SlideDetectionTransform.apply() called")
        self.detect_slide_breaks()

    def detect_slide_breaks(self):
        """Find ---- patterns and convert to slide sections"""
        # For now, let's just add a simple implementation
        # We'll enhance this later
        slide_count = 0

        # Find all sections and mark them as slides
        for section in self.document.findall(nodes.section):
            slide_count += 1
            section['classes'].append('slide')
            if not section.get('ids'):
                section['ids'] = [f'slide-{slide_count}']

        print(f"DEBUG: Marked {slide_count} sections as slides")

class SlideEnhancementTransform(Transform):
    default_priority = 800  # Run after detection
    #print('SlideEnhancementTransform')

    def apply(self):
        """REQUIRED method"""
        print("DEBUG: SlideEnhancementTransform.apply() called")

        slide_count = 0
        for section in self.document.findall(nodes.section):
            if 'slide' in section.get('classes', []):
                slide_count += 1

                # Ensure each slide has an ID
                if not section.get('ids'):
                    section['ids'] = [f'slide-{slide_count}']

                # Add basic positioning for impress.js
                section['data-x'] = str((slide_count - 1) * 1000)
                section['data-y'] = '0'

        print(f"DEBUG: Enhanced {slide_count} slides")

class AttributeEnhancementTransform(Transform):
    default_priority = 900  # Run last
    #print('AttributeEnhancementTransform')

    def apply(self):
        """REQUIRED method"""
        print("DEBUG: AttributeEnhancementTransform.apply() called")
        # Basic implementation - we'll enhance this later
        for node in self.document.findall(nodes.Element):
            self.process_basic_attributes(node)

    def process_basic_attributes(self, node):
        """Process basic node attributes"""
        # Add your attribute processing logic here
        pass

class FinalCleanupTransform(Transform):
    default_priority = 900  # Run last
    #print('FinalCleanupTransform')

'''
class SlideReader(readers.Reader):
    def parse(self):
        self.input = self.input.read()
        slide_contents = re.split(r'\n----+\n', self.input)
        document = self.new_document()
        for i, content in enumerate(slide_contents):
            section = nodes.section()
            section['classes'] = ['slide']
            section['ids'] = [f'slide-{i+1}']
            slide_doc = self.new_document()
            self.parser.parse(content, slide_doc)
            for node in slide_doc.children:
                section += node
            document += section
        return document
'''