from github import Github
import sys

username = "uthej.dev@gmail.com" #Insert your github username here
password = "u2105634219" #Insert your github password here

def GitInit():
    user = Github(username, password).get_user()
    repo_name = str(sys.argv[1])
    privacy = eval(str(sys.argv[2]))
    delete = eval(str(sys.argv[3]))
    if privacy:
        status = "Private"
    else:
        status = "Public"
    try:
        if delete:
            repo = user.get_repo(repo_name)
            repo.delete()
            print("\nSuccesfully Deleted Repository with Parameters: \n Name: {}\n".format(repo_name))
        else:
            repo = user.create_repo(repo_name, private=privacy)
            print("\nSuccesfully Created Repository with Parameters: \n Name: {0} \n Privacy: {1}\n".format(repo_name, status))
    except IOError as e:
        print(e)
        pass
if __name__ == "__main__":
    GitInit()
