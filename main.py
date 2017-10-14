import sys
import os.path
import ScoreVulns as scorer

def main(argv):
        # Declare variables
        points = 0;
        filezilla_file = "/Program Files (x86)/FileZilla Server/Filezilla Server.xml"
        html = """<html>
        <h1>Akul's Scoring Engine (for In Class Competition 2017)</h1>
        """

        # Score anonymous filezilla
        if scorer.score_file(filezilla_file, "anonymous", True):
                html += "<p> - Anonymous access is unpermitted</p>"
                points += 1
        
        # Score autoban
        if scorer.score_file(filezilla_file, "<Item name=\"Autoban enable\" type=\"numeric\">1</Item>"):
                html += "<p> - Autoban set correctly</p>"
                points += 1
                
        # Score correct folder shared
        if scorer.score_file(filezilla_file, "C:\CyberAegisShare"):
                html += "<p> - Sharing correct folder</p>"
                points += 1        

        # PHP Backdoor
        if scorer.file_exists(******TODO*****):
                html += "<p> - Removed php backdoor</p>"
                points += 1

        # Remove filezilla add-on
        if scorer.score_file("/Users/CAAdmin/AppData/Roaming/Mozilla/Firefox/Profiles/****TODO****/extensions.json", "chatzilla", True):
                html += "<p> - Removed potentially unwanted chatzilla add-on</p>"
                points += 1                

        #IE ESC
        if scorer.score_reg("SOFTWARE\Microsoft\Active Setup\Installed Components\{A509B1A7-37EF-4b3f-8CFC-4F3A74704073}", "IsInstalled", 1):
                html += "<p> - Enabled IE ESC for administrators</p>"
                points += 1            

        # IE Protocols
        if scorer.score_reg("SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings", "SecureProtocols", 2720, True):
                html += "<p> - Appropriate Internet Explorer protocols set</p>"
                points += 1   
        
        
        # Append last part of html and write to file
        html += "<p>Score: " + str(points) + "/7 </p>" + "</html>"
        with open("FTP_SE.html", "w") as html_file:
                html_file.write(html)



# Starts here
if __name__ == "__main__":
        main(sys.argv[1:]) # No parameters should be being passed

