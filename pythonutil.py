import os
from sys import argv, exit
from git import Repo, InvalidGitRepositoryError, NoSuchPathError
join = os.path.join

def main():
	if len(argv) < 2:
		print "Please specify a github repo"
		exit(1)
	
	repoPath = argv[1];
	
	try:
		repo = Repo(repoPath)
	except InvalidGitRepositoryError:
		print "Path is not a git repository"
		exit(1)
	except  NoSuchPathError:
		print "Path does not exist"
		exit(1)
	
	for untracked in repo.untracked_files:
		print untracked
	
if __name__ == '__main__':
	main()
	
