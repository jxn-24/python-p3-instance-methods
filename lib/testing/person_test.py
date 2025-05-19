#!/usr/bin/env python3

from person import Person

import io
import sys
import types

class TestPerson:
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person"'''
        guido = Person()
        assert(type(guido) == Person)

class TestTalk:
    '''Person.talk() in person.py'''

    def test_is_method(self):
        '''is an instance method'''
        guido = Person()
        

    def test_prints_hello_world(self):
        '''prints "Hello World!"'''
        guido = Person()
        captured_out = io.StringIO()
        sys.stdout = captured_out
        
        sys.stdout = sys.__stdout__
        

class TestWalk:
    '''Person.walk() in walk.py'''

    def test_is_method(self):
        '''is an instance method'''
        guido = Person()
        

    def test_prints_the_person_is_walking(self):
        '''prints "The person is walking."'''
        guido = Person()
        captured_out = io.StringIO()
        sys.stdout = captured_out
    
        sys.stdout = sys.__stdout__
        
