# BomSweeper
Remove BOM(Byte Order Marker) from files. 

Wrote this because I had some legacy source codes of several Android projects in UTF-8 with BOM, but couldn't find any software to do batching BOM removing operations on MAC OS.

##Usage

bs.py [-h] [--type TYPE] path

positional arguments:


  path:         path of the target folder


optional arguments:


  -h, --help:   show this help message and exit

  
--type TYPE:  file type

###Examples

Convert all files under a folder:

```python bs.py /path/to/the/target/folder```

Convert all java files under a folder:

```python bs.py /path/to/the/target/folder --type java```
