from winreg import *
from win32com.client import Dispatch
import sys
import os.path

class applications:
    def check_reg(registry_key, value_name, correct_value, HKCU=False):
        """
        Used for scoring vulnerabilities in registry.
        Will only work with HKLM and HKCU as those are the most used.

        Keyword arguments:
        registry key - registry key to score. By default uses HKLM.
        e.g. 'SAM\SOFTWARE\7-Zip'

        value_name - name of value in key to score
        e.g. 'Path'
        
        correct value - the correct value (data) for vuln to be fixed
        e.g. '1' or 'C:\Program Files\7-Zip\'

        HKCU - boolean (True - use HKCU instead of HKLM, False - HKLM).
        By default, uses HKLM.
        
        Return - boolean (True - vuln fixed or False - not fixed)

        VR1248 is for errors reading registry value (obfuscation needed).
        """

        # Declare variables
        vuln_fixed = False
        # value is declared in context due to type

        
        # Try except to avoid revealing vulnerabilities
        try:
            # Gets value that is currently set
            # If specified HKCU
            if HKCU:
                reg = ConnectRegistry(None, HKEY_CURRENT_USER)
            else:
                reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
            key = OpenKey(reg, registry_key)
            value = QueryValueEx(key, value_name)[0] # Returns tuple (first value is actual value)
        except:
            print("VR1248") # Obfuscates for student. Can be used for debugging.
            return False # Exits function. TODO: May be better method.
            
        if value == correct_value:
            vuln_fixed = True
        
        return vuln_fixed
        
    def check_file(filename, scored_value, no_exist = False):
        """
        Used for scoring values in file.

        Keywrod arguments:
        File name. Please specify full directory.
        E.g. "/Program Files (x86)/FileZilla Server/Filezilla Server.xml"
        
        Scored value (value to look for)

        Value shouldn't exist (no_exist) - boolean
            (True is shouldn't exist is correct, False is should exist is correct).
        By default is False (will score if value exists in file).
        If specified True, will check if the value does not exist.

        Return - boolean (True - vuln fixed or False - not fixed)

        GA1643 is for if file does not exist (obfuscation needed).
        """
        
        # Declare variables
        vuln_fixed = False
        
        #This will close the script if it detects someone deleted the file. If they did and the script ran, it would complain and display the line with the error (which contains the answer).
        if not applications.file_exists(filename):
            print("GA1643") # Obfuscates for student. Can be used for debugging.
            return False # Exits function. TODO: May be better method.

        # Parse file as string. TODO: May not always be best method.
        str_file = open(filename).read()

        # If vuln is fixed if scored_value is not in file
        if no_exist:
            if not scored_value in str_file:
                vuln_fixed = True
        # Default - vuln is fixed if scored_value is in file
        else:
            if scored_value in str_file:
                vuln_fixed = True

        return vuln_fixed
            
    def file_exists(filename):
        """
        Used for scoring (or simply checking) if a file exists.

        Keyword arguments:
        File name. Please specify the full directory.
        E.g. "/Program Files (x86)/FileZilla Server/Filezilla Server.xml"

        Returns - boolean (True - file exists or False - doesn't exist)
        """

        # Declare variables
        file_exists = False

        # Checks if file exists
        if (os.path.isfile(filename)):
            file_exists = True
        else:
            file_exists = False

        return file_exists
            

    def get_file_version(path):
        """
        Used for getting the version of a program

        Keyword arguments:
        Path. Please specify the full directory including the filename.
        E.g. "/Program Files (x86)/FileZilla Server/Filezilla Server.xml"

        Returns - string version (x.x.x.x)
        """
        ver_parser = Dispatch('Scripting.FileSystemObject')
        info = ver_parser.GetFileVersion(path)

        if info == 'No Version Information Available':
            info = None
        return info

    def check_file_version(path, version):
        """
        Used for checking if the version of a program is correct.

        Keyword arguments:
        Path. Please specify the full directory including the filename.
        E.g. "/Program Files (x86)/FileZilla Server/Filezilla Server.xml"
        Version string "x.x.x.x"
        E.g. "42.0.0.1"

        Returns - boolean (true if matches)
        """
        if applications.get_file_version(path) == version:
            return True
        return False

def forensics(answer, forensics_file):
        """
        TODO
        """
        #Close the script if it detects someone deleted the forensics file.
        if (os.path.isfile(forensics_file)) != True:
            return False
        
        # Reads forensics answers
        response = open(forensics_file).read()

	# Removes case sensitivity. TODO: Add as parameter
        answer = answer.lower() 
        response = response.lower()

        #Return
        if answer in response:
            return True
        return False

#TODO class output
