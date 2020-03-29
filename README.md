# MIDI steganography


MIDI-steganography is a Python program that allows you to hide some message in a MIDI file. The size of the message depends on the characteristics of the MIDI file, more precisely depends on the number of notes within the file. In the file 'songs' you will find some MIDI examples, the ones which were used to prove the program.

For instance, the file 'Hans Zimmer - Time' allows only a message of 48 bits. Moreover, if you try to hide something in this file when playing the hidden file, the song will totally different. This does not mean that the program is useful. Contrariwise! files like 'Pink Floyd - Time' or  'Pink Floyd - Another Brick in the Wall' allow more than 10000 bits message furthermore when playing the hide MIDI file there is almost not any difference with the original file.  

## Prerequisites

 * [tkinter](https://docs.python.org/3/library/tkinter.html): Its main purpose is to display a GUI to choose the MIDI file when necessary.
 * [py_midicsv](https://github.com/timwedde/py_midicsv): Library aiming to main bidirectionally convert between the binary MIDI to CSV.
 Use the package manager [pip](https://pip.pypa.io/en/stable/) to install prerequisites, Tkinter is part of the standart library. If you installed all packages alongside with Python 3 you should be able to use it.

```bash
$ pip install py_midicsv
```
## Authors

* **Mateo Sanabria Ardila** - [Masanar](https://github.com/Masanar)
