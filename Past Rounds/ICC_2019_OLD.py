import sys
import os.path
from akul_se import applications


def main(argv):
        # Declare variables
        points = 0
        total = 0
        filezilla_file = "/Program Files (x86)/FileZilla Server/Filezilla Server.xml"
        
        html = """<html>
        <h1>Akul's Scoring Engine (for In Class Competition 2019)</h1>
        """
        
        
        # TODO: Poorly written
        # FILEZILLA
        # Score anonymous filezilla
        if applications.check_file(filezilla_file, "anonymous", True):
                html += "<p> - Anonymous access is unpermitted</p>"
                points += 1
        total += 1
                
        # Score autoban
        if applications.check_file(filezilla_file, "<Item name=\"Autoban enable\" type=\"numeric\">1</Item>"):
                html += "<p> - Autoban set correctly</p>"
                points += 1
        total += 1
        
        # Score data connection IP
        if applications.check_file(filezilla_file, "<Item name=\"Check data connection IP\" type=\"numeric\">2</Item>"):
                html += "<p> - Data connection IP set correctly</p>"
                points += 1
        total += 1

        # BROWSERS
        # Firefox updated
        if not applications.check_file_version("/Program Files/Mozilla Firefox/firefox.exe", "65.0"):
                html += "<p> - Updated Firefox </p>"
                points += 1
        total += 1

        # Remove Firefox add-on
        if applications.check_file("/Users/barista/AppData/Roaming/Mozilla/Firefox/Profiles/7spt0kxv.default/extensions.json", "Video DownloadHelper", True):
                html += "<p> - Removed potentially unwanted video downloadhelper add-on</p>"
                points += 1
        total += 1
        
        # IE Protocols
        if applications.check_reg("SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings", "SecureProtocols", 2560, True):
                html += "<p> - Appropriate Internet Explorer protocols set</p>"
                points += 1
        total += 1

        # FORBIDDEN FILES        
        # Forbidden File (Zip) (Permission Messed Up Hard to Delete, System File Protected)
        if not applications.file_exists("/Windows/ophcrack-3.7.0-bin.zip"):
                html += "<p> - Removed forbidden hacking tool ophcrack zip file</p>"
                points += 1
        total += 1
        
        # Forbidden File (Installer) (Permission Messed Up Hard to Delete)
        if not applications.file_exists("/Windows/RoastData/Fun Stuff/iTunes64Setup.exe"):
                html += "<p> - Removed prohibited software application installer</p>"
                points += 1
        total += 1
        
        # Pretend System File, PHP Backdoor (Permission Messed Up Hard to Delete, System File Protected)
        if not applications.file_exists("/Windows/System32/c99.php"):
                html += "<p> - Removed dangerous c99 php backdoor</p>"
                points += 1
        total += 1
        
        # Forbidden File (Media), MP3 (System File Protected)
        if not applications.file_exists("/Windows/Caffeine/CaffeineForWindowsMeOS/01-03- Hello Seattle.mp3"):
                html += "<p> - Removed forbidden media file 1 (mp3 file)</p>"
                points += 1
        total += 1
        
        # Forbidden File (Game) (System File Protected)
        if not applications.file_exists("/Users/cappuccino/Documents/Recipes and Fun/Fruity Garden (www.fullypcgames.com).rar"):
                html += "<p> - Removed forbidden fruity garden game archive file</p>"
                points += 1
        total += 1
        
        # Forbidden File (Media), JPG (Permission Messed Up Hard to Delete, System File Protected)
        if not applications.file_exists("/Users/espresso/Music/f00d/20190621_113048.jpg"):
                html += "<p> - Removed forbidden media file 2 (jpg file)</p>"
                points += 1
        total += 1
        
        
        # FINAL
        # Append last part of html and write to file
        html += "<h3>Score: " + str(points) + "/" + str(total) + "</h3>"
        with open("AKUL_SE.html", "w") as html_file:
                html_file.write(html)


# Starts here
if __name__ == "__main__":
        main(sys.argv[1:]) # No parameters should be being passed

