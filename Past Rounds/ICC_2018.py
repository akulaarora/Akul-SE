import sys
import os.path
from akul_se import applications
from akul_se import forensics


def main(argv):
        # Declare variables
        points = 0
        points_forensics = 0
        total = 0
        total_forensics = 0
        filezilla_file = "/Program Files (x86)/FileZilla Server/Filezilla Server.xml"
        
        html = """<html>
        <h1>Akul's Scoring Engine (for In Class Competition 2018)</h1>
        """
        
        # TODO: Poorly written
        # FILEZILLA
        # Score anonymous filezilla
        if applications.check_file(filezilla_file, "anonymous", True):
                html += "<p> - Anonymous access is unpermitted</p>"
                points += 1
        total += 1
        
        # Score data connection IP
        if applications.check_file(filezilla_file, "<Item name=\"Check data connection IP\" type=\"numeric\">2</Item>"):
                html += "<p> - Data connection IP set correctly</p>"
                points += 1
        total += 1
        
        # Score correct folder shared
        if applications.check_file(filezilla_file, "C:\ConfidentialShare"):
                html += "<p> - Sharing correct folder</p>"
                points += 1        
        total += 1

        # BROWSERS
        # Firefox updated
        if applications.check_file_version("/Program Files/Mozilla Firefox/firefox.exe", "62.0.3.6848"):
                html += "<p> - Updated firefox </p>"
                points += 1
        total += 1

        # Remove firefox add-on
        if applications.check_file("/Users/CAAdmin/AppData/Roaming/Mozilla/Firefox/Profiles/2fm5a2m1.default/extensions.json", "youtube", True):
                html += "<p> - Removed potentially unwanted youtube download add-on</p>"
                points += 1                
        total += 1

        # ie Protocols
        if applications.check_reg("SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings", "SecureProtocols", 2720, True):
                html += "<p> - Appropriate Internet Explorer protocols set</p>"
                points += 1   
        total += 1
        
        # ie esc
        if applications.check_reg("SOFTWARE\Microsoft\Active Setup\Installed Components\{A509B1A7-37EF-4b3f-8CFC-4F3A74704073}", "IsInstalled", 1):
                html += "<p> - Enabled IE ESC for administrators</p>"
                points += 1            
        total += 1

        # FORENSICS
        #fq1
        if forensics("f103b85a9349b605cb6fb8ddd75ffc86", "forensics.txt"):
                html += "<p> - FQ1 correct </p>"
                points_forensics += 1
        total_forensics += 1

        
        #fq2
        if forensics("S-1-5-21-3374165012-900943249-4075023912-1018", "forensics.txt"):
                html += "<p> - FQ2 correct </p>"
                points_forensics += 1
        total_forensics += 1
        
        #fq3
        if forensics("CyberEEEEEEEjis", "forensics.txt"):
                html += "<p> - FQ3 correct </p>"
                points_forensics += 1
        total_forensics += 1
        
        #fq4
        if forensics("500", "forensics.txt"):
                html += "<p> - FQ4 correct </p>"
                points_forensics += 1
        total_forensics += 1
        
        #fq5
        if forensics("n0boody", "forensics.txt"):
                html += "<p> - FQ5 correct </p>"
                points_forensics += 1
        total_forensics += 1

        #fq6
        if forensics("you_got_me_123", "forensics.txt"):
                html += "<p> - FQ6 correct </p>"
                points_forensics += 1
        total_forensics += 1
        
        # FINAL
        # Append last part of html and write to file
        html += "<h3>Applications Score: " + str(points) + "/" + str(total) + "</h3>"
        html += "<h3>Forensics Score: " + str(points_forensics) + "/" + str(total_forensics) + "</h3>" + "</html>"
        with open("AKUL_SE.html", "w") as html_file:
                html_file.write(html)


# Starts here
if __name__ == "__main__":
        main(sys.argv[1:]) # No parameters should be being passed

