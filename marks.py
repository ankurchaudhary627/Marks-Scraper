from selenium import webdriver
from bs4 import BeautifulSoup
import functools as ft
import re
import csv

#converts marks to grade point
def grade(n):
	if n==100:
		return n//10
	if n>=45:
		return n//10+1
	elif n>=40 and n<45:
		return n//10
	else:
		return 0

#list of tuples to store USN, name and calculated sgpa of all students
sgpa=[]

#regular expression to find Student name:
regex=re.compile('<tdstyle="padding-left:15px"><b>:</b>(\w+[.]?\w+)</td>')

#last valid USN
last=198

for i in range(1,last+1):
	
	driver=webdriver.Chrome(executable_path=r'F:\Projects\Web Scraping\chromedriver.exe')   # Create a new instance of the Chrome driver 
	
	#generating the usn
	usn='1cr15cs'
	if i<10:
		usn=usn+'00'+str(i)
	elif i>=10 and i<100:
		usn=usn+'0'+str(i)
	else:
		usn+=str(i)

	driver.get('http://results.vtu.ac.in/vitaviresultcbcs/index.php')			#fetches the page
	ele=driver.find_element_by_name('lns')
	ele.send_keys(usn)
	
	try:
		#try checks if the usn is valid or not
		driver.find_element_by_id("submit").click()				
		doc=driver.page_source								#gets the page source of the web-site

		doc1=ft.reduce(lambda x,y:x+y,doc.split())					#getting the page source as a string without spaces
		
		x=re.search(regex,doc1)
		if x:
			name=x.group(1)

		driver.quit()

		if re.search(r'Semester:5',doc1):						#checks if the semester is 5
			soup=BeautifulSoup(doc,'lxml')						#creating the BeautifulSoup object
			b=soup.find('div',class_='divTableBody')
			bc1=b.find('div',class_='divTableRow')
			bc3=bc1.findNextSiblings()
			l=[]
			for i in range(8):
				bc4=bc3[i].findChildren()
				x=bc4[4].text
				l.append(x.rstrip(' '))
			
			l=list(map(int,l))							# l contains all subjects marks of a student

			gpa=0.0

			for i in range(0,len(l)):
				if i>5:
					gpa+=(grade(l[i])*2.0)
				else:
					gpa+=(grade(l[i])*4.0)

			sgpa.append((usn,name.strip(),str(gpa/28.0)))
	except:
		continue

#sort the list in decreasing order
sgpa.sort(key=lambda x:x[2],reverse=True)

#writing the list to a csv file
f=csv.writer(open('allmarks.csv','w',newline=''))
f.writerow(['USN','Name','SGPA'])
for i in range(len(sgpa)):
	f.writerow([sgpa[i][0],sgpa[i][1],sgpa[i][2]])
