import os
from sys import argv, exit
from git import Repo, InvalidGitRepositoryError, NoSuchPathError
join = os.path.join


def add_file(untracked, repo):
	repo.index.add([untracked])
	print "Added the file to the index"	
	
def delete_file(untracked_file):
	print "Are you sure you want to delete the file?(Y or N)"
	answer = str.lower(raw_input("> "))
	if answer == "y" or answer == "yes":
		os.delete(untracked_file)
	else:
		"Ok, let's skip this file"
	
def ignore_file(untracked_file):
	pass

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
	
	print "Welcome to the python git utility"
	print "Use this to help clean up your untracked files when they get out of hand"
	print "For each file decide whether to (A)dd the file to the index, (I)gnore the file by adding it to the git ignore, (D)elete the file, or (S)kip it all together"
	
	for untracked in repo.untracked_files:
		print untracked
		file_name = os.path.join(repoPath, untracked)
		decision = str.lower(raw_input("> "))
		if decision == "a" or decision == "add":
			pass
		else if decision == "s" or decision == "skip":
			pass
		else if decision == "d" or decision == "delete":
			pass
		else if decision == "i" or decision == "ignore":
			pass
		else:
			print "I don't understand, I'm just going to skip... Remember you can (A)dd, (D)elete, (S)kip, or (I)gnore"
	
if __name__ == '__main__':
	main()
	
