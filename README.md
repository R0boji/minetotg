# minetotg
![PyPI - Downloads](https://img.shields.io/pypi/dm/minetotg?style=flat-square)
![PyPI - Version](https://img.shields.io/pypi/v/minetotg?style=flat-square)
![PyPI - Status](https://img.shields.io/pypi/status/minetotg?style=flat-square)
![PyPI - License](https://img.shields.io/pypi/l/minetotg?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/minetotg?style=flat-square)

This project was created in order to help Minecraft community to transform game text formatting to Telegram HTML format.

### Installation

```
pip install minetotg
```

### Usage

#### Python Module
```python
from minetotg import reformat

some_reformatted_string = reformat("§kSpoiler§r§lBold§r")
print(some_reformatted_string) # Output: <tg-spoiler>Spoiler</tg-spoiler><b>Bold</b>
```

#### CLI
```commandline
python -m minetotg §kSpoiler§r§lBold§r
```
Output:
```commandline
<tg-spoiler>Spoiler</tg-spoiler><b>Bold</b>
```
