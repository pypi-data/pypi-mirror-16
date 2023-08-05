# Tests of cluster-driven lab class
#
# Copyright (C) 2016 Simon Dobson
# 
# Licensed under the GNU General Public Licence v.2.0
#

from epyc import *

import unittest
import numpy
import time


class SampleExperiment(Experiment):
    '''A very simple experiment that adds up its parameters.'''

    def do( self, param ):
        total = 0
        for k in param:
            total = total + param[k]
        return dict(total = total)
            
        
class ClusterLabTests(unittest.TestCase):

    def setUp( self ):
        '''Create a lab in which to perform tests.'''
        self._lab = ClusterLab()

    def tearDown( self ):
        '''Close the conection to the cluster.'''
        self._lab.close()
        self._lab = None
        
    def testMixup( self ):
        '''Test that parameter spaces are suitably mixed, defined as not
        more than 0.5% of elements landing in their original place'''
        n = 1000
        
        l = numpy.arange(0, n)
        self._lab._mixup(l)
        sp = [ v for v in (l == numpy.arange(0, n)) if v ]
        self.assertTrue(len(sp) <= (n * 0.005))

    def testRunExprimentSync( self ):
        '''Test running an experiment and grabbing all the results by waiting'''
        n = 100

        r = numpy.arange(0, n)
        self._lab['a'] = r
        self._lab.runExperiment(SampleExperiment())
        time.sleep(5)
        self.assertTrue(self._lab.ready())
        res = self._lab.results()
        
        # check that the whole parameter space has a result
        self.assertEqual(len(res), n)
        for p in res:
            self.assertIn(p[Experiment.PARAMETERS]['a'], r)

        # check that each result corresponds to its parameter
        for p in res:
            self.assertEqual(p[Experiment.PARAMETERS]['a'], p[Experiment.RESULTS]['total'])

            
    def testRunExprimentAsync( self ):
        '''Test running an experiment and check the results come in piecemeal'''
        n = 500

        r = numpy.arange(0, n)
        self._lab['a'] = r
        self._lab.runExperiment(SampleExperiment())

        f = 0.0
        while f < 1:
            f1 = self._lab.readyFraction()
            self.assertTrue( f1 >= f )
            f = f1
        self.assertTrue(self._lab.ready())
        res = self._lab.results()
        
        # check that the whole parameter space has a result
        self.assertEqual(len(res), n)
        for p in res:
            self.assertIn(p[Experiment.PARAMETERS]['a'], r)

        # check that each result corresponds to its parameter
        for p in res:
            self.assertEqual(p[Experiment.PARAMETERS]['a'], p[Experiment.RESULTS]['total'])

