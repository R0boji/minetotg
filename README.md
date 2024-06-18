# minetotg
![PyPI - Downloads](https://img.shields.io/pypi/dm/minetotg?style=flat-square)

This project was created in order to help Minecraft community to transform game text formatting to Telegram HTML format.

### Installation

```
pip install minetotg
```

### Usage

```python
from minetotg import reformat

some_reformatted_string = reformat("§kSpoiler§r§lBold§r")
print(some_reformatted_string) # Output: <tg-spoiler>Spoiler</tg-spoiler><b>Bold</b>
```
