#! /usr/bin/python 

from gittle import Gittle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))








repo_path = os.path.join(BASE_DIR,'outfile','base')
repo_url = 'git@git.cootel.com:liuliangliang/tomcat_config.git'



def run():

	if not os.listdir(repo_path):

		repo = Gittle.clone(repo_url, repo_path)

	#else:
		#repo = Gittle(repo_path, origin_uri=repo_url)
		#repo.pull()
		#repo.push()

if __name__ == '__main__':
        run()
