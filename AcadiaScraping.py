
import requests
from bs4 import BeautifulSoup
import csv
import re

with open ('acadia.html', encoding="utf8") as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


courseTable = soup.find('table', class_ = 'main_table')

courseTitle = courseTable.find_all('b')
courseDesc = courseTable.find_all('i')

courseTitlesFixed = []

for i in range(len(courseTitle)):
    if re.search("Yes+", str(courseTitle[i])):
        pass
    else:
        courseTitlesFixed.append(courseTitle[i])

# print (len(courseTitlesFixed))
# print(len(courseDesc))




# for i in range(len(courseDesc)):
#     print(courseTitlesFixed[i])
#     print()
#     print(courseDesc[i])

csv_file = open('AcadiaCSCourses.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Course Title', 'Course Description'])

for i in range(len(courseDesc)):
    csv_writer.writerow([courseTitlesFixed[i], courseDesc[i]])


csv_file.close()

