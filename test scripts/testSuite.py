from unittest import TestLoader, TestSuite, TextTestRunner
from Unittest_register import ehb_Test1
from Unittest_login import ehb_Test2
from Unittest_eventhallbooking import ehb_Test3
from Unittest_employee_editbooking import ehb_Test4
from Unittest_employee_deletebooking import ehb_Test5
from Uniitest_addpark import ehb_Test6
from Unittest_customer_editbooking import ehb_Test7
from Unittest_customer_bookingdelete import ehb_Test8
from Unittest_editpark import ehb_Test9
from Unittest_deletepark import ehb_Test10

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(ehb_Test1),
        loader.loadTestsFromTestCase(ehb_Test2),
        loader.loadTestsFromTestCase(ehb_Test3),
        loader.loadTestsFromTestCase(ehb_Test4),
        loader.loadTestsFromTestCase(ehb_Test5),
        loader.loadTestsFromTestCase(ehb_Test6),
        loader.loadTestsFromTestCase(ehb_Test7),
        loader.loadTestsFromTestCase(ehb_Test8),
        loader.loadTestsFromTestCase(ehb_Test9),
        loader.loadTestsFromTestCase(ehb_Test10),

    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)