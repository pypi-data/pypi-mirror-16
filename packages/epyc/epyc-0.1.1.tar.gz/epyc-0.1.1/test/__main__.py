# Test suite
#
# Copyright (C) 2016 Simon Dobson
#
# Licensed under the GNU General Public Licence v.2.0
#

import unittest
from .experiments import *
from .labs import *
from .clusterlabs import *
from .notebooks import *
from .jsonnotebooks import *
from .sqlitenotebooks import *

experimentsSuite = unittest.TestLoader().loadTestsFromTestCase(ExperimentTests)
notebooksSuite = unittest.TestLoader().loadTestsFromTestCase(LabNotebookTests)
jsonnotebooksSuite = unittest.TestLoader().loadTestsFromTestCase(JSONLabNotebookTests)
labsSuite = unittest.TestLoader().loadTestsFromTestCase(LabTests)
clusterlabsSuite = unittest.TestLoader().loadTestsFromTestCase(ClusterLabTests)

suite = unittest.TestSuite([ experimentsSuite,
                             notebooksSuite, jsonnotebooksSuite,
                             labsSuite, clusterlabsSuite ])

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity = 2).run(suite)
