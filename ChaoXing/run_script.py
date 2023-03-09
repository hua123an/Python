import unittest
from Script.TetsLogin import TestLogin
s = unittest.makeSuite(TestLogin)
r = unittest.TextTestRunner()
r.run(s)
