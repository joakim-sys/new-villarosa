#!/usr/bin/env python
import os
import sys
import dotenv

if __name__ == "__main__":
    dotenv.load_dotenv()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
