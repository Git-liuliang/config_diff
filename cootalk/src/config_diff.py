#! /usr/bin/python

import difflib,hmac,os,sys


import time
import logging
from cootalk.conf import mylogging
logger = logging.getLogger(__name__)
mylogging.load_my_logging_cfg()




class myHtmlDiff(difflib.HtmlDiff):
    _legend = " "







def Diff_file_content(local,remote):

    try:
        with open(local,'rb') as f: local_content = f.read()
        with open(remote,'rb')as f: remote_content = f.read()

        local_lines = [i for i in local_content.splitlines() if not i == '' and not i.startswith('#')]
        remote_lines = [i for i in remote_content.splitlines() if not i == '' and not i.startswith('#')]
        #d = difflib.Differ()
        d = myHtmlDiff()
	different = d.make_file(local_lines, remote_lines,context=True,fromdesc=local,todesc=remote)
        #different = d.compare(local_lines, remote_lines)
        #for i in different:
        #    if i.startswith('+') or i.startswith('-') or i.startswith('?'):
        #         print 'error>>>%s' % i.strip('\n')
	#	 logger.error('error>>>%s' % i.strip('\n'))
	return different
    except IOError,Argument:
        print 'error>>>\n',Argument
	logger.error('error>>>%s\n' % Argument)





def  file_list(res_list,pathname):
    # VisitDir is  os.path.walk need a callbalk function, must three args
    def VisitDir(arg, dirname, names):
        for filespath in names:
                res = os.path.join(dirname, filespath)
                if os.path.isfile(res)  and  'config_diff.py' not in res and '.git' not in res and '.idea' not in res:
                    res_list.append(res)
    os.path.walk(pathname,VisitDir,())
    return res_list


def core(local_dir):
	
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    remote_dir = os.path.join(BASE_DIR,'outfile','base')
    remote_filename_list = []
    file_list(remote_filename_list,remote_dir)
    out = []
    for index, remote_filename in enumerate(remote_filename_list):

        local_filename = remote_filename.replace('base',local_dir)
        print 'file_%s %s comparing ....>>>> '%(index,local_filename)
	logger.info('file_%s %s comparing ....>>>> '%(index,local_filename))
        res = Diff_file_content(local_filename,remote_filename)
	if "No Differences Found" not in res:
        	out.append(res)
    return out
        
if __name__ == '__main__':


    ###example:  local_dir=os.path.join('remote_file','172.18.3.180')
    core(local_dir)
