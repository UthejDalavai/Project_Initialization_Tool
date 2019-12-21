# Project_Initialization_Tool

**Note:** This Project is developed only for windows users.

add the path of this directory in Environmental Variables to make this work globally.

### Download the tool & install:

> Make a workspace directory which holds all your projects - **ex: "My projects"**

    λ: mkdir "My Projects"
    λ: cd /My Projects

Git cloan the repository and install the requirements:

    λ: git clone "https://github.com/UthejDalavai/Project_Initialization_Tool.git"
    λ: cd ./Project_Initialization_Tool
    λ: pip install -r requirements

Change Github **"username"** and **"password"** in **"create.py"** file.

Change **"path"**  in **"projectinit.py"** if your workspace directory is not same as it is used in the example above.  

### Usage:

    λ: python projectinit.py --help
    λ: python projectinit.py <project name> (creates project folder and public github repository with README.md file)
    λ: python projectinit.py <project name> -p (to create private github repository)
    λ: python projectinit.py <project name> -d (to delete the project folder and Github repository)