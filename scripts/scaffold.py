import os
import sys
import argparse
from datetime import datetime

def create_module(name):
    path = os.path.join('_modules', name)
    os.makedirs(path, exist_ok=True)
    index_path = os.path.join(path, 'index.md')
    if not os.path.exists(index_path):
        with open(index_path, 'w') as f:
            f.write(f"""---
layout: module
title: {name.replace('_', ' ').title()}
visible: true
---

# {name.replace('_', ' ').title()}

Module content goes here.
""")
        print(f"Created module at {index_path}")
    else:
        print(f"Module {name} already exists.")

def create_week(number):
    path = os.path.join('_weeks', f'week{number:02d}.md')
    os.makedirs('_weeks', exist_ok=True)
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write(f"""---
layout: week
title: Week {number}
visible: true
modules: []
---

Welcome to week {number}.
""")
        print(f"Created week at {path}")
    else:
        print(f"Week {number} already exists.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scaffold course content.')
    subparsers = parser.add_subparsers(dest='command')

    module_parser = subparsers.add_parser('module', help='Create a new module')
    module_parser.add_argument('name', help='Name of the module')

    week_parser = subparsers.add_parser('week', help='Create a new week')
    week_parser.add_argument('number', type=int, help='Week number')

    args = parser.parse_args()

    if args.command == 'module':
        create_module(args.name)
    elif args.command == 'week':
        create_week(args.number)
    else:
        parser.print_help()
