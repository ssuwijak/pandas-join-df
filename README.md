# Pandas 
demo - how to read the 2 csv files and join them with an id key

## create virtual environment
1. create a project folder, `mkdir my_project`
2. enter into the project folder, `cd my_project`
3. create virtualenv and set prompt command, `python -m venv v_foldername --prompt="my-env"`
4. activate the created venv, `v_foldername\scripts\activate`
5. enter into the venv folder and initialize git,
`cd v_folder`
`git init`

6. check installed packages in this venv, `python -m pip list`
7. install the needed package in this venv,
`python -m pip install pandas`

8. deactivate venv, `v_foldername\scripts\deactivate`

### Create the requirements.txt file
`pip freeze > requirements.txt`

### Install the packages by the requirement.txt file
`pip install -r /path/to/requirements.txt`

## how to re-apply the .gitignore
1. Make changes in .gitignore file.
2. Run `git rm -r --cached . ` command.
3. Run `git add . ` command
4. `git commit -m "your commit message" ` or just git commit or continue working

*reference :* [How to refresh gitignore](https://sigalambigha.home.blog/2020/03/11/how-to-refresh-gitignore/)