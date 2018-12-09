import results
import mail


roll_nos={'178x1a0585':"phani.sanam555@gmail.com",'178x1a0580':"dineshyepuri05@gmail.com"}
marks={}
 
for roll_no in roll_nos:
	finalResult = results.getResults(roll_no)
	marks[roll_no] = finalResult

print(marks)

for roll_num in marks:
 print(roll_num)
 mail.sendGmail("phani.sanam555@gmail.com","hulknanda",roll_nos[roll_num],marks.get(roll_num))

