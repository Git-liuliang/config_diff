#! /usr/bin/python 
import os

class CheckFilename(object):

    def __init__(self,keydir,comparedir):

        self.keydir = keydir
        self.comparedir = comparedir

    def get_source_list(self):
        # count = 0
        # for root, dirs, files in os.walk(self.keydir):
        #     for each in files:
        #
        #         count += 1
        # return count
        res_list = []
        def VisitDir(arg, dirname, names):
            for filespath in names:
                res = os.path.join(dirname, filespath)
                if os.path.isfile(res) and 'config_diff.py' not in res and '.git' not in res and '.idea' not in res:
                    res_list.append(res)

        os.path.walk(self.keydir, VisitDir, ())
        return res_list




    def get_compare_list(self):
        res_list = []

        def VisitDir(arg, dirname, names):
            for filespath in names:
                res = os.path.join(dirname, filespath)
                if os.path.isfile(res) and 'config_diff.py' not in res and '.git' not in res and '.idea' not in res:
                    res_list.append(res)

        os.path.walk(self.comparedir, VisitDir, ())
        return res_list

    def check_res(self):

            res = []
	
	    for item in self.get_source_list():

                res.append(item.replace(self.keydir,self.comparedir))

            b3 = list(set(res) - set(self.get_compare_list()))
            #for item in self.get_compare_list():
		
            #    res.append(item.replace(self.comparedir,self.keydir))
		
            #b3 = list(set(self.get_source_list()) - set(res))
            return b3

