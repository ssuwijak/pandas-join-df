# Pandas 
demo - how to read the 2 csv files and join them with their id key.

### Create virtual environment
1. create a project folder, `mkdir my_project`
2. enter into the project folder, `cd my_project`
3. create virtualenv and set prompt command, 
- create the v_foldernam for venv, `python -m venv v_foldername --prompt="my-env"`
- use the current folder for venv, `python -m venv . `

4. activate the created venv, `v_foldername\scripts\activate`
5. enter into the venv folder and initialize git,
- `cd v_foldername`
- `git init`

6. check installed packages in the venv, `python -m pip list`
7. install your needed packages in the venv, `python -m pip install pandas`
8. (optional) deactivate venv, `v_foldername\scripts\deactivate`

### Create the requirements.txt file
> Antivirus will alert while using pip
- venv not yet activated, `python -m pip freeze > requirements.txt`
- venv already activated, `pip freeze > requirements.txt`

### Install the packages by the requirement.txt file
> Antivirus will alert while installing the pacakages by pip
- venv not yet activated, `python -m pip install -r /path/to/requirements.txt`
- venv already activated, `pip install -r /path/to/requirements.txt`

### How to re-apply the .gitignore
1. Make changes in .gitignore file.
2. Run `git rm -r --cached . ` command.
3. Run `git add . ` command
4. `git commit -m "your commit message" ` or just git commit or continue working

*reference :* [How to refresh gitignore](https://sigalambigha.home.blog/2020/03/11/how-to-refresh-gitignore/)
