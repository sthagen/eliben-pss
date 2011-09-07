#!/usr/bin/env python

from psslib.defaultpssoutputformatter import DefaultPssOutputFormatter
from psslib.matchresult import MatchResult
from psslib.driver import pss_run

from psslib.colorama import init
import sys


#df = DefaultPssOutputFormatter(show_column_of_first_match=True)
#df.start_matches_in_file("joe/toe.poy")
#df.found_filename('sdsdfsdfsdf')
#df.context_separator()
#df.context_line('here I come\n', 45 )
#df.matching_line(MatchResult('abc = 24 + def - yuas\n', 40, [(6, 8), (11, 14)]))

pss_run(sys.argv[2:], pattern=sys.argv[1],
        only_find_files=False,
        #type_pattern='.*der\.pyc',
        search_all_types=True,
        show_column_of_first_match=True,
        )


#from psslib.utils import istextfile
#print istextfile(open('psslib/colorama/initialise.pyc'))

