# Tests of JSON notebooks
#
# Copyright (C) 2016 Simon Dobson
# 
# Licensed under the GNU General Public Licence v.2.0
#

from epyc import *

import unittest
import os
from tempfile import NamedTemporaryFile


class SampleExperiment(Experiment):
    '''A very simple experiment that adds up its parameters.'''

    def do( self, param ):
        total = 0
        for k in param:
            total = total + param[k]
        return dict(total = total)

    
class JSONLabNotebookTests(unittest.TestCase):

    def testCreate( self ):
        '''Test creation of empty notebook (which won't create file)'''
        tf = NamedTemporaryFile()
        tf.close()
        fn = tf.name
        
        js = JSONLabNotebook(fn)
        self.assertTrue(js.isPersistent())
        self.assertEqual(js.name(), fn)

    def testCreateAndSave( self ):
        '''Test creation and saving of notebook'''
        tf = NamedTemporaryFile()
        tf.close()
        fn = tf.name
        
        try:
            e = SampleExperiment()
            params1 = dict( a = 1, b = 2 )
            rc1 = e.set(params1).run()
            params2 = dict( a = 1, b = 3 )
            rc2 = e.set(params2).run()

            js = JSONLabNotebook(fn, description = "A test notebook")
            js.addResult(rc1)
            js.addPendingResult(params2)
            js.commit()

            jsr = JSONLabNotebook(fn)
            self.assertEqual(jsr.description(), "A test notebook")
            self.assertEqual(jsr.pendingResults(), js.pendingResults())
            self.assertEqual(jsr.results(), js.results())
        finally:
            os.remove(fn)
 
    def testCreateAndUpdate( self ):
        '''Test creation and updating of notebook'''
        tf = NamedTemporaryFile()
        tf.close()
        fn = tf.name
        
        try:
            e = SampleExperiment()
            params1 = dict( a = 1, b = 2 )
            rc1 = e.set(params1).run()
            params2 = dict( a = 1, b = 3 )
            rc2 = e.set(params2).run()

            js = JSONLabNotebook(fn, description = "A test notebook")
            js.addResult(rc1)
            js.addPendingResult(params2)
            js.commit()

            js.addResult(rc2)
            js.commit()

            jsr = JSONLabNotebook(fn)
            self.assertEqual(jsr.description(), "A test notebook")
            self.assertEqual(len(jsr.pendingResults()), 0)
            self.assertEqual(jsr.results(), js.results())
        finally:
            os.remove(fn)
        
    def testCreateOverwrite( self ):
        '''Test the create flag'''
        tf = NamedTemporaryFile()
        tf.close()
        fn = tf.name

        try:
            e = SampleExperiment()
            params1 = dict( a = 1, b = 2 )
            rc1 = e.set(params1).run()
            
            js = JSONLabNotebook(fn, description = "A test notebook")
            js.addResult(rc1)
            js.commit()
            
            jsr = JSONLabNotebook(fn, create = True, description = "Nothing to see")
            self.assertEqual(jsr.description(), "Nothing to see")
            self.assertEqual(len(jsr.results()), 0)
            self.assertEqual(len(jsr.pendingResults()), 0)
        finally:
            os.remove(fn)
        
    def testCreateNoOverwrite( self ):
        '''Test that the create flag being false doesn't overwrite'''
        tf = NamedTemporaryFile()
        tf.close()
        fn = tf.name
        
        try:
            e = SampleExperiment()
            params1 = dict( a = 1, b = 2 )
            rc1 = e.set(params1).run()
            
            js = JSONLabNotebook(fn, description = "A test notebook")
            js.addResult(rc1)
            js.commit()
            
            jsr = JSONLabNotebook(fn, description = "Nothing to see")
            self.assertEqual(jsr.description(), "A test notebook")
            self.assertEqual(jsr.results(), js.results())
            self.assertEqual(len(jsr.pendingResults()), 0)
        finally:
            os.remove(fn)
        
    def testReadEmpty( self ):
        '''Test we can correctly load an empty file, resulting in an empty notebook''' 
        tf = NamedTemporaryFile()
        tf.close()
        fn = tf.name
        
        try:
            e = SampleExperiment()
            params1 = dict( a = 1, b = 2 )
            rc1 = e.set(params1).run()

            js = JSONLabNotebook(fn, description = "A test notebook")
            js.addResult(rc1)
            js.commit()

            js2 = JSONLabNotebook(fn, create = True, description = "Another test notebook")

            jsr = JSONLabNotebook(fn)
            self.assertEqual(jsr.description(), None)
            self.assertEqual(len(jsr.results()), 0)
            self.assertEqual(len(jsr.pendingResults()), 0)

            js2.commit()
            jsr = JSONLabNotebook(fn)
            self.assertEqual(jsr.description(), "Another test notebook")
            self.assertEqual(len(jsr.results()), 0)
            self.assertEqual(len(jsr.pendingResults()), 0)            
        finally:
            os.remove(fn)
            
            
