#! /usr/bin/python

import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


log_path = os.path.join(BASE_DIR,'log','all2.log')
hosts_path = os.path.join(BASE_DIR,'conf','hosts')
remote_file_path = os.path.join(BASE_DIR,'outfile','remote_file')
source_file_path = os.path.join(BASE_DIR,'outfile','base') 






def run():
	
	if os.listdir(source_file_path):
		shutil.rmtree(source_file_path)
		os.mkdir(source_file_path)

	if os.listdir(remote_file_path):

        	shutil.rmtree(remote_file_path)
        	os.mkdir(remote_file_path)

	if os.path.isfile(hosts_path):

        	os.remove(hosts_path)

	#if os.path.isfile(log_path):

        #	os.remove(log_path)



if __name__ == '__main__':
	run()		
