#!/usr/bin/env python

import os
import argparse
import gmapfuncs as gmap

def getUlist( usrstr, vartype ):
    """
    Parsing unames argument returns a list of users to filter
    """
    usrs = []
    if usrstr == None:
       return usrs
    for u in usrstr[0].split(','):
       if vartype == 'users':
          uid = gmap.getUid( u )
       else:
          uid = gmap.getPid( u )
       usrs.append(uid)
    return usrs

def procPeriod( perstr ):
    if perstr == None:
       return []





gufitmp = os.path.join('/gpfs/fs1/scratch', os.environ['LOGNAME'], 'gufi_tmp')
defcachepref = os.path.join(gufitmp, 'cache')

parser = argparse.ArgumentParser(description='Generate Cache DB for a given tree')
parser.add_argument('--cache-dir=', '-c', dest='cdir', default=defcachepref, 
                    metavar='path-name',
                    help='Absolute path name to store the GUFI query output\
                    default: ' + defcachepref)
grprprtby = parser.add_mutually_exclusive_group(required=False)
grprprtby.add_argument('--cache-mode', dest='cmode', action='store_true',
                       help='Generate cache for grprt')
grprprtby.add_argument('--list-mode=', dest='lmode',choices=['name','size','owner','project',\
                       'mtime','atime'], 
                       help='Generate list of files with one or more of these attributes in space\
                       separated format')

parser.add_argument('--unames=', dest='fuids', nargs='+', metavar=('User1','User2'),
                    help='for content owned only by users User1, User2..')
parser.add_argument('--projects=', dest='projs', nargs='+', metavar=('Proj1','Proj2'),
                    help='for content assocaited with projects Proj1, Proj2.., applicable\
                          only in HPSS')
parser.add_argument('--write-period=', dest='writep', metavar='YYYY[MM[DD]]-YYYY[MM[DD]]',
                    help='for content written during time window YYYY[MM[DD]]-YYYY[MM[DD]] \
                          either of begin or end period may be omitted for open interval but\
                          not both. For time specification 4-digit year is required, 2-digit\
                          month may be specified, if month is specified 2-digit may be specified.')
parser.add_argument('--read-period=', dest='readp',  metavar='YYYY[MM[DD]]-YYYY[MM[DD]]',
                    help='for content read during time window YYYY[MM[DD]]-YYYY[MM[DD]] \
                          either of begin or end period may be omitted for open interval but\
                          not both. For time specification 4-digit year is required, 2-digit\
                          month may be specified, if month is specified 2-digit may be specified.')
parser.add_argument('--nthreads', dest='nthreads', default=1, metavar='number-of-threads',
                     help='Number of threads to run GUFI query')
parser.add_argument(dest='Absolute path to query', help='Absolute path of the filesystem located in\
                          either in glade, campaign or HPSS')

args = parser.parse_args()


cachedir = args.cdir
users = getUlist( args.fuids, 'users' )
projects = getUlist( args.projs, 'projects' )
#writep = procPeriod( writep )
print(cachedir)
print(users)
print(projects)