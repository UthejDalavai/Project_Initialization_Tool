import argparse
import os

path = "/My Projects/" # WorkSpace Path

parser = argparse.ArgumentParser(description='Initializing the Project.')

parser.add_argument('name', metavar='Name', type=str,
                    help='Enter the name of the project folder to be created.')
parser.add_argument('-p', default=False, action="store_true",
                    help='Creates Private Github Repository (default: Public)')
parser.add_argument('-d', default=False, action="store_true",
                    help='to delete project folder and Github Repository')
args = parser.parse_args()

PATH = path + str(args.name)
folderName = str(args.name)

try:
    if args.d:
        os.system('rmdir /S /Q "{}"'.format(PATH))
        os.system('cmd /c "python "{0}Project_Initialization_Tool/create.py" {1} {2} {3}"'.format(path,folderName, args.p, args.d))
        print("\nSuccesfully deleted project folder named '{}'\n".format(folderName))    
    else:
        os.makedirs(PATH)
        os.system('cmd /c "python "{0}Project_Initialization_Tool/create.py" {1} {2} {3}"'.format(path,folderName, args.p, args.d))
        os.system('cmd /c "cd {0} && git init && git remote add origin https://github.com/UthejDalavai/{1}.git && touch README.md"'.format(PATH, folderName))
        os.system('cmd /c "cd {0} && git add . && git commit -m "Initial commit" && git push -u origin master && git checkout -b dev && git push origin dev && git push --set-upstream origin dev && code ."'.format(PATH))
        print("\nSuccesfully created project folder named '{}'\n".format(folderName))
    print('\x1b[2;30;42m' + 'Success!' + '\x1b[0m')
except OSError as e:
    print("\n{1}".format(e.errno, e.strerror))
    print('\x1b[2;30;41m' + 'Error!' + '\x1b[0m')