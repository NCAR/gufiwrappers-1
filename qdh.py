#!/usr/bin/env python
from __future__ import print_function
import __future__
import os
import getpass
import cmdline as cmdl
import glob
import gcache
import grprt
import timefuncs as tm

parsedata = {}

def checkListFields( listfields ):
    """
    Checks the list fields matches with expected entries
    """
    validfields = ['filename', 'size', 'owner', 'project', 'mtime', 'atime']
    for ent in listfields:
       if ent not in validfields:
           print("The field ",ent," not valid, the list of valid field is: ", validfields)
           exit(-1)
    return True

def procSizeRange( sizerange ):
    """
    Parse size string to return a 2 element list of sizes. 
    Full format is: size_lower_bound-size_upper_bound
    Few abbreviated conventions incorporated:
      1.  size_lower_bound- => sizes larger or equal to size_lower_bound
      2. -size_upper_bound  => sizes smaller or equal to size_upper_bound
      3.  size_bound        => size_lower_bound-
    """
    if sizerange == None:
       return []
    lst = sizerange.split('-')
    lstn = []
    for e in lst:
       if len(e) > 0:
          lstn.append(int(e))
    if len(lstn) == 1:
       if not sizerange.startswith('-'):
          lstn.append(-1)
       else:
          lstn.insert(0,-1)
    return lstn


def parseCmdLine( ):
    """
    Actual parser is in cmdline module, here things are just passed along
    """
    global parsedata
    username = getpass.getuser()
    gufitmp = os.path.join('/gpfs/fs1/scratch', username, 'gufi_tmp')
    cmdl.gufitmp = gufitmp
    parser = cmdl.parserForQdh( )
    args = parser.parse_args()
    try:
       fields = args.listd[0].split(',')
       checkListFields( fields )
    except:
       fields = None
    parsedata = {'gufitmp':args.gufitmp, 'verbosity':args.verbosity, 'cachedir':os.path.join(gufitmp, 'raw'),
         'fuids':args.fuids, 'fpids':args.fpids, 'sizer':procSizeRange( args.sizer ), 
         'writep':tm.procPeriod( args.writep ),
         'readp':tm.procPeriod( args.readp ), 'storage':args.storage[0], 'treename':args.treename,
         'byusers':args.byusers, 'byprojects':args.byprojects, 'bysubdirs':args.bysubdirs,
         'ncores':int(args.ncores), 'nsbins':int(args.nsbins), 'fields':fields} 
    return parsedata
    
if __name__ == "__main__":
    parsedata = parseCmdLine( )
    gcache.driver( parsedata )
    if parsedata['fields'] == None:
       grprt.driver( parsedata )
