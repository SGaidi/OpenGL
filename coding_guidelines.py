#!/usr/bin/env python
"""Python Coding Guidelines"""

try:
    import lower_case_with_underscores
    """ module name example """
except ImportError:
    pass
"""	import built-ins (e.g. os, time, telnetlib, etc)
	import third-party (e.g. paramiko, pyGame, etc)
	changes to path
	import my-modules (e.g. tools, parent_jira)
"""
	
__author__ = "Sarah Gaidi"
__version__ = "1.0.1"
__email__ = "gaidi.sarah@gmail.com"

gMixedCaseWithLeadingG = "global variable name example" #try avoiding using global variables as much as possible

def action_with_underscores(noun_with_underscores):
    """ function name example
        noun_with_underscores: variable name example
    """
    pass


class MixedCaseNoun():
    """ class name example """
    
    MixedCaseNoun = "public property name example"

    _noun_with_leading_underscores = "private propert name example"

    NOUN_ALL_CAPS = "constant name example"

    def mixedCaseExceptForFirstWordVerb():
        """ public method name example """
        pass

    def _verb_with_leading_underscores():
        """ private method name example """
        pass

    def __two_leading_underscores():
        """ really private data name example """
        pass

    def setMixedCaseNoun(self, MixedCaseNoun):
        """ MixedCaseNoun: parameter that match properties - SameAsProperties """
        self.MixedCaseNoun = MixedCaseNoun

    def FactoryMixedCase():
        """ factory function name example """
        pass


if __name__ == '__main__':
    pass