"""
Remove BOM(Byte Order Marker) from utf-8 files.
"""
import os, sys, argparse, codecs

BUFSIZE = 4096
BOMLEN = len(codecs.BOM_UTF8)

def init_options():
    parser = argparse.ArgumentParser(description='Remove BOM(Byte Order Marker) from utf-8 files.')
    parser.add_argument('path', type=str, help='path of the target folder')
    parser.add_argument('--type', dest='type', help='file type')
    return parser.parse_args()

def main():
    args = init_options()
    path = args.path
    file_type = args.type

    for root, dirs, files in os.walk(path):
        for f in files:
            if file_type != None and f.endswith('.' + file_type):
                with open(root + '/' + f, 'r+b') as fp:
                    chunk = fp.read(BUFSIZE)
                    if chunk.startswith(codecs.BOM_UTF8):
                        i = 0
                        chunk = chunk[BOMLEN:]
                        while chunk:
                            fp.seek(i)
                            fp.write(chunk)
                            i += len(chunk)
                            fp.seek(BOMLEN, os.SEEK_CUR)
                            chunk = fp.read(BUFSIZE)
                        fp.seek(-BOMLEN, os.SEEK_CUR)
                        fp.truncate()
                        print 'Converted: ' + root + f

if __name__ == '__main__':
    main()
