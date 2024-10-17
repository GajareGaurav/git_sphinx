import os

def create_init_files(start_path):
    """Create __init__.py files in all subdirectories."""
    for root, dirs, files in os.walk(start_path):
        if '__init__.py' not in files:
            init_path = os.path.join(root, '__init__.py')
            with open(init_path, 'w') as f:
                # For the main ai package, we might want to import submodules
                if root == start_path:
                    f.write('''# AI Package
from . import analytics
from . import ui
from . import utils
''')
                else:
                    f.write('# This file makes this directory a Python package\n')
            print(f"Created {init_path}")

# Replace this with the path to your ai directory
ai_path = r'C:\Users\gaurav.gajare\Desktop\wbgg-merged\onetru\ai'

create_init_files(ai_path)