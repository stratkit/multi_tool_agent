##############
Activate the Virtual Environment (in terminal before running this script)
##############

# Create (one-time, no need to do this again)
python -m venv .venv

# Activate (each new terminal)

# macOS/Linux: source .venv/bin/activate
# Windows CMD: .venv\Scripts\activate.bat
# Windows PowerShell: .venv\Scripts\Activate.ps1


##############
# Find API Key, edit .env file (need to change it to txt file, unless Jupyter Labs can show hidden files)
mv .env env.txt

# then change back
mv env.txt .env




##############
# commands

pwd = shows current path
ls = shows contents of directory
ls -a = shows contents, including hidden
cd ../ = (versus cd /)
mv = change file name (ex: mv .existing_hidden_file updated_file_name.txt)
deactivate = turn off venv (see above, very important # macOS/Linux: source .venv/bin/activate)


#############
# How to run

1. source .venv/bin/activate # Activate the virtual environment (.venv)
2. adk run multi_tool_agent # launch the agent!