# Akul-SE
Scoring engine for Windows. Originally created for 2017 In-Class Competition. Primarily intended to score applications and intended to be used with CASS or CyberPatriot Scoring Engine.

Use the following command to compile into executable (makes code unreadable and doesn't require python installation):
```
$ cxfreeze main.py --target-dir dist
```
You will need to use pip to install cxfreeze. You will also need to run cxfreeze-postinstall to install it before you can use it.

You can also obfuscate ScoreVulns.py before running cxfreeze using the following command:
```
$ python -m compileall SetupVulns.py
```
From there, you can remove the .py and replace it with the generated .pyc file before running cxfreeze. ScoreVulns.py will otherwise be stored as a .py file in the dist folder. Not too much of a concern as it does not give away any vulnerabilities, but may provide hints (at image creator's discretion).
