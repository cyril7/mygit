#!/usr/bin/python
import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
print 'Dedent:\n'
print dedented_text
