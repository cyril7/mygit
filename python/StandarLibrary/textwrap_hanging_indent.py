#!/usr/bin/python
import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text).strip()
print textwrap.fill(dedented_text, 
                    initial_indent = '',
                    subsequent_indent = ' ' * 4,
                    width = 50,
                    )
[root@gz01-prod-ops-salt-g001-001 /apps/sh/standarlibrary]#
