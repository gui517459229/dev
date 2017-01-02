# -*- coding: utf-8 -*-
'''
Created on 2017年1月1日

@author: Administrator
'''
import urllib
from xml.etree import ElementTree
from foolib.testcase import FooTestCase


class FindBookTest(FooTestCase):
    '''foo测试用例基类
    '''
    owner = "v_xiuggui"
    timeout = 5
    priority = FooTestCase.EnumPriority.High
    status = FooTestCase.EnumStatus.Design
    
    def run_test(self):
        '''查询豆瓣图书信息
        '''
        self.start_step('获取书集信息')
        url='http://api.douban.com/book/subject/isbn/9787308083256 '
        ret=urllib.urlopen(url)
        data=ret.readlines()
#       print data
        self.assert_equal('获取书集信息', len(data)>0, True)
        #-----------------------------------
        self.start_step('解析书集信息')
        root=ElementTree.fromstringlist(data)
        node=root.getiterator()
        for t_node in node:
            if len(t_node.attrib)>0:
                print t_node.attrib
                
        
    

if __name__=='__main__':
    FindBookTest().debug_run()