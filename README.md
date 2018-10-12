# Akul-SE
Scoring engine for Windows. Originally created for 2017 In-Class Competition. Intended to score applications and forensics and to be used with CASS or CyberPatriot Scoring Engine as a supplementary scoring engine. 

Use the following command to compile into executable (makes code unreadable and doesn't require python installation):
```
$ cxfreeze main.py --target-dir dist
```
You will need to use pip to install cxfreeze. You will also need to run cxfreeze-postinstall to install it before you can use it.

You can also obfuscate akul_se.py before running cxfreeze using the following command:
```
$ python -m compileall akul_se.py
```
From there, you can remove the .py and replace it with the generated .pyc file before running cxfreeze. ScoreVulns.py will otherwise be stored as a .py file in the dist folder. Not too much of a concern as it does not give away any vulnerabilities, but may provide hints (at image creator's discretion).

## Modifying the repository
If you have questions, please contact Akul. If you would like to contribute to this project, please fork this project and create a pull request once changes have been made. Developer access will be granted to anyone who actively wishes to continue developing this. See Issues section for things that need to be added to this project.

After rounds are over, please add to folder for previous rounds. This will act as future reference for anyone else.
