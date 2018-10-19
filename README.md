# TextWrapper

A Python library to format text, wrapping lines into a limited characters amount, and with a option to align the text.

## Usage

```python
from textwrapper import wrap

text = 'This is an example of text justification.'
'\n'.join(list(wrap(text, 16)))

# returns 
"""
This is an
example of text
justification.
"""
```

## Test default text
```
$ python3 wrapper.py
```
