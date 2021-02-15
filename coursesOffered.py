
import requests
from bs4 import BeautifulSoup
import csv

with open ('msvu.html', encoding="utf8") as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

courses = soup.find_all('span', class_="classDesc")
courseText = courses.text.split("\n")

for courseB in courseText: 
    print(courseB)
    print("*" * 50)

# finalCourseList = []

# csv_file = open('NSCCITSWebDCourses.csv', 'w')

# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Course Title', 'Course Description'])

# for i in range(len(courseText)):
#     if i > 3:
#         if i % 4 == 0:
#             finalCourseList.extend([courseText[i], courseText[i+1]])
#             csv_writer.writerow([courseText[i], courseText[i +1]])

# for course in finalCourseList:  
#     print(course)


# csv_file.close()

