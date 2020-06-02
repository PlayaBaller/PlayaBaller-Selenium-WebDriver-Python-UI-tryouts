import unittest
from basicWeb.test_loginOnPr import TestLogin, driver
from basicWeb.test_dragndrop import TestDragnDrop

testcaseone = unittest.TestLoader().loadTestsFromTestCase(TestDragnDrop)

unittest.TextTestRunner(verbosity=2).run(testcaseone)
