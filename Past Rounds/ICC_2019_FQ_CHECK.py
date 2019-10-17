import sys
import os.path
from akul_se import forensics


def main(argv):
        # Declare variables
        points = 0
        points_forensics = 0
        total = 0
        total_forensics = 0
        filezilla_file = "/Program Files (x86)/FileZilla Server/Filezilla Server.xml"
        
        html = """<html>
        <h1>ICC 2019 Forensics Questions Checker</h1>
        """

        # FORENSICS
        #fq1
        if forensics("1995AnGeL1004", "forensics.txt"):
                html += "<p> - FQ1 correct </p>"
                points_forensics += 1
        total_forensics += 1

        
        #fq2
        if forensics("2xKn0t", "forensics.txt"):
                html += "<p> - FQ2 correct </p>"
                points_forensics += 1
        total_forensics += 1
        
        #fq3
        if forensics("first{2_mUch_sUg@r}", "forensics.txt"):
                html += "<p> - FQ3 correct </p>"
                points_forensics += 1
        total_forensics += 1
        
        #fq4
        if forensics("second{I_AM:_s@LT}", "forensics.txt"):
                html += "<p> - FQ4 correct </p>"
                points_forensics += 1
        total_forensics += 1
        
        #fq5
        if forensics("EVENTHESHADOWNEEDSLIGHTTOEXIST", "forensics.txt"):
                html += "<p> - FQ5 correct </p>"
                points_forensics += 1
        total_forensics += 1

        #fq6
        if forensics("S-1-5-21-2444761002-1063474950-790320954-1015", "forensics.txt"):
                html += "<p> - FQ6 correct </p>"
                points_forensics += 1
        total_forensics += 1
                
        #fq7
        if forensics("SVTCARAT", "forensics.txt"):
                html += "<p> - FQ7 correct </p>"
                points_forensics += 1
        total_forensics += 1
                
        #fq8
        if forensics("3.0.6", "forensics.txt"):
                html += "<p> - FQ8 correct </p>"
                points_forensics += 1
        total_forensics += 1
        
        # FINAL
        # Append last part of html and write to file
        html += "<h3>Forensics Score: " + str(points_forensics) + "/" + str(total_forensics) + "</h3>" + "</html>"
        with open("AKUL_SE.html", "w") as html_file:
                html_file.write(html)


# Starts here
if __name__ == "__main__":
        main(sys.argv[1:]) # No parameters should be being passed

