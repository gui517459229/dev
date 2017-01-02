# -*- coding: utf-8 -*-
'''
         示例测试用例
'''
#2016/11/21 QTAF自动生成

from foolib.testcase import FooTestCase
import time


class HelloTest(FooTestCase):
    '''示例测试用例
    '''
    owner = "Administrator"
    timeout = 5
    priority = FooTestCase.EnumPriority.High
    status = FooTestCase.EnumStatus.Design
    
    def run_test(self):
        self.log_info("hello testcase")
        self.assert_equal(True, True)
    
if __name__ == '__main__':
    HelloTest().debug_run()
    


