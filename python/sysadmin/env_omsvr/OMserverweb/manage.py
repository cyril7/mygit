#!/usr/bin/env python
import os
import sys

sys.path.append('/devops/env_omsvr/OMserverweb')
sys.path.append('/devops/env_omsvr/')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OMserverweb.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
