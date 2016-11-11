#!/usr/bin/env python
import ctypes
import sys
import gtz
import getopt


def usage():
    print('usage: sample.py [-h] [sample.gtz]')

def show_fileinfo(input_file):
    cl = gtz.new_decompressor(input_file)
    for (fn,fs,fg,dh) in cl: 
            start_line = 11
            get_size = 10
            print("Print the content from the 41th to the 80th lines of the fastq file.")
            def get_decompress_line(decompress_line):
                print(decompress_line),
            dh.decompress_toline(start_line,get_size,get_decompress_line)

def main(argv):
    try:
        opts,args = getopt.getopt(sys.argv[1:],'h') 
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for o,a in opts:
        if o == "-h":
            usage()
            sys.exit(1)
    
    if 0 == len(args):
        print("Required the gtz compress file")
        usage()
        sys.exit(1)
    for input_file in args:
        show_fileinfo(input_file)

if __name__ == '__main__':
    main(sys.argv)
