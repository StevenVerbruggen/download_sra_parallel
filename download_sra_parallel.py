#!/usr/bin/env python
import traceback
import sys
import os
import argparse
import time


__author__ = 'Steven Verbruggen'



def main():
    starttime = time.time()

    print
    print("##############################")
    print("# Download parallel from SRA #")
    print("##############################")
    print

    # Parse arguments from command line
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS,
                                     description="This tool allows parallel download of multiple SRA files",
                                     add_help=False)

    man_args = parser.add_argument_group("Mandatory parameters")
    man_args.add_argument("--first", "-f", action="store", required=True, nargs="?", metavar="Integer", type=int,
                          help="The first SRA dataset to download (chronologically) (mandatory)")
    man_args.add_argument("--last", "-l", action="store", required=True, nargs="?", metavar="Integer", type=int,
                          help="The last SRA dataset to download (chronologically) (mandatory)")

    opt_args = parser.add_argument_group("Optional parameters")
    opt_args.add_argument("--help", "-h", action="help", help="Show help message and exit")
    opt_args.add_argument("--workdir", "-w", action="store", required=False, nargs="?", metavar="FOLDER", default="",
                          type=str, help="Working directory (default: CWD)")
    opt_args.add_argument("--tmp", "-t", action="store", required=False, nargs="?", metavar="FOLDER", default="",
                          type=str, help="Temporary folder (default: workdir/tmp)")
    opt_args.add_argument("--cores", "-c", action="store", required=False, nargs="?", metavar="INTEGER", default=1,
                          type=int, help="Amount of cores to use (default: 1)")

    args = parser.parse_args()

    # default workdir is CWD, default tmp
    if args.workdir == "":
        args.workdir = os.getcwd()
    if args.tmp == "":
        args.tmp = args.workdir + "/tmp/"
    if not os.path.isdir(args.tmp):
        os.mkdir(args.tmp)

    #List parameters
    print("Parameters:")
    for arg in vars(args):
        print('    %-15s\t%s' % (arg, getattr(args, arg)))

    ##########
    #  MAIN  #
    ##########

    if(args.first == args.last):
        command = "parallel-fastq-dump -s SRR"+str(args.first)+" -t "+str(args.cores)+" -O . --tmpdir "+args.tmp
        print(command)
        print
        sys.stdout.flush()
        os.system(command)
    else:
        for i in range(args.first, args.last+1):
            command = "parallel-fastq-dump -s SRR"+str(i)+" -t "+str(args.cores)+" -O . --tmpdir "+args.tmp
            print(command)
            print
            sys.stdout.flush()
            os.system(command)
            os.system("rm -rf ~/ncbi/public/sra/SRR"+str(i)+".sra.cache")
    os.system("rm -rf "+args.tmp)

    #End of program message
    print
    print("[%s]: PROGRAM COMPLETE" % (convert_time(time.time()-starttime)))
    print
    sys.stdout.flush()

    return


###### DIRECT TO MAIN ############
if __name__ == "__main__":
    try:
        main()
    except(Exception):
        traceback.print_exc()
##################################