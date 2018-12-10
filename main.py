import results
import mail
import json

def getEmail(data, hallticket):
	for student in data:
		if(hallticket == student['rollno']):
			return student['email']
def main():

	with open('data.json')as json_file:
	 data=json.load(json_file)
	#roll_nos={'178x1a0585':"phani.sanam555@gmail.com",'178x1a0580':"dineshyepuri05@gmail.com"}
	students = data['students']
	marks={}
	 
	for studentIndex in students:
		roll_no = studentIndex['rollno']
		finalResult = results.getResults(roll_no)
		marks[roll_no] = finalResult

	for roll_num in marks:
	 print(roll_num)
	 receiverId = getEmail(data['students'], roll_num)
	 mail.sendGmail("phani.sanam555@gmail.com","********",receiverId,marks.get(roll_num))

if __name__ == '__main__':
    main()
