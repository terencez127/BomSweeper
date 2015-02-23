# BomSweeper
Remove BOM(Byte Order Marker) from UTF-8 files. 

Wrote this because I had some legacy source codes of several Android projects in UTF-8 with BOM, but couldn't find any software to do batching BOM removing operations on MAC OS.

##Usage

bs.py [-h] [--type TYPE] path


&ensp;&ensp;&ensp;&ensp;**path**:         path of the target folder


&ensp;&ensp;&ensp;&ensp;**-h, --help**:   show this help message and exit

  
&ensp;&ensp;&ensp;&ensp;**--type TYPE**:  file type

###Examples

Convert all files under a folder:

&ensp;&ensp;&ensp;&ensp;```python bs.py /path/to/the/target/folder```

Convert all java files under a folder:

&ensp;&ensp;&ensp;&ensp;```python bs.py /path/to/the/target/folder --type java```
<br><br>
**Note**: Thanks to this answer on stackoverflow: http://stackoverflow.com/a/8898439
