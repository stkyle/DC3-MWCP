import argparse
arg_parser = argparse.ArgumentParser()
arg_parser.prog = 'mwcp-tools'
arg_parser.description = 'utility for executing parser modules'
arg_parser.add_argument('-p', '--parser', type=str,
                        help='malware config parser to call')
arg_parser.add_argument('-v', '--verbose', help="increase output verbosity", action="store_true")
arg_parser.add_argument('-l', '--list', action="store_true",
                        default=False, help='list all malware config parsers')
arg_parser.add_argument('-k', '--listfields', action="store_true", default=False,
                        help='list all standardized fields and examples. See resources/fields.json')
arg_parser.add_argument('-a', '--parserdir', action='store', type=str,
                        metavar='DIR', dest='parserdir', help='parsers directory')
arg_parser.add_argument('-r', '--resourcedir', action='store', type=str,
                        metavar='DIR', dest='resourcedir', help='resources directory')
arg_parser.add_argument('-o', '--outputdir', action='store', type=str, metavar='DIR',
                        default='', dest='outputdir', help='output directory')
arg_parser.add_argument('-t', '--tempdir', action='store', type=str, metavar='DIR',
                        default=None, dest='tempdir', help='temp directory')
arg_parser.add_argument('-j', '--jsonoutput', action='store_true', default=False,
                        dest='jsonoutput', help='Enable json output for parser reports (instead of formatted text)')
arg_parser.add_argument('-n', '--disableoutputfiles', action="store_true", default=False,
                        dest='disableoutputfiles', help='disable writing output files to filesystem')
arg_parser.add_argument('-g', '--disabletempcleanup', action='store_true', default=False,
                        dest='disabletempcleanup', help='Disable cleanup of framework created temp files including managed tempdir')
arg_parser.add_argument('-f', '--includefileinfo', action='store_true', default=False, dest='includefilename',
                        help='include input file information such as filename, hashes, and compile time in parser output')
arg_parser.add_argument('-d', '--hidedebug', action="store_true",
                        default=False, dest='hidedebug', help='Hide debug messages in output')
arg_parser.add_argument('-u', '--outputfileprefix', action='store', type=str, metavar='FILENAME', default='', dest='outputfile_prefix',
                        help='string prepended to output files written to filesystem. specifying "md5" will cause output files to be prefixed with the md5 of the input file')
arg_parser.add_argument('-i', '--filelistindirection', action="store_true", default=False,
                        dest='filelistindirection', help='input file contains a list of filenames to process')
arg_parser.add_argument('-b', '--base64outputfiles', action="store_true", default=False,
                        dest='base64outputfiles', help='base64 encode output files and include in metadata')
arg_parser.add_argument('-w', '--kwargs', action='store', type=str, metavar='JSON', default='', dest='kwargs_raw',
                        help='module keyword arguments as json encoded dictionary if values in the dictionary use the special paradigm "b64file(filename)", then filename is read, base64 encoded, and used as the value')
arg_parser.print_help()
