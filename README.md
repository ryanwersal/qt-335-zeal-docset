# Qt 3.3.5 Docset for [Zeal](https://github.com/jkozera/zeal)/[Dash](http://kapeli.com/dash)

Very primitive docset for Qt 3.3.5. It is good enough for use but far from ideal.

### To Build

1. Clone this repo
2. Copy docs/html folder from your Qt 3.3.5 installation to the Documents folder (`qt335.docset/Contents/Resources/Documents/html/`)
3. Run `./gendocset.py`

### To Install

Copy the `qt335.docset` folder into Zeal's docset folder. You'll have to restart Zeal for it to pick up the new docset.

### What Works

- Classes
- Methods

### What Doesn't Work

- Most everything else
