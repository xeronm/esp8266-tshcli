"""
Invokes django-admin when the django module is run as a script.

Example: python -m django check
"""

from .tshcli import main

if __name__ == "__main__":
    main()