'''
34. Create a class Student and add member variables with False values. The variables
are as listed below. Marks will have a default value blank list.
1. Name
2. Reg No
3. Roll No
4. Standard
5. Admission Year
6. Marks
7. Result
Add a constructor that will assign Name, Reg No, Roll No, Standard, Admission
year. In the constructor add validation for Name to be only Alphabetic, Reg No to be
alphanumeric, Roll No, Standard nad Admission year to be numeric. All abobve
values will be accepted as string only.

Add a method that will accept a dictionary for marks containing subject as key and
marks as values. It will add the dictionary to the list of marks. Marks list will have
multiple elements and each element will be a dictionary only. Here there should be a
validation to acccept the marks which are less than or equal to 100 only. If the
obtained marks are less than 40 the result willl be fail otherwise pass. In the
dictionary the result can be added.

Add another method that will generate the result. This method will check if there
is any line in the marks having fail as result the result will be Fail and it will print the

*******************************************************************************
Name : <Student Name>
Roll No : <Roll No>                   Standard: <Standard>
*******************************************************************************
Subject    Total Marks     Passing Marks          Obtained Marks       Result
-------------------------------------------------------------------------------
<Sub 1>      100                 40              <obtained marks>    <result>
<Sub 1>      100                 40              <obtained marks>    <result>
<Sub 1>      100                 40              <obtained marks>    <result>
*******************************************************************************
TOTAL        <total>           <total>               <total>

Result: PASS / FAIL                                 Percentage: <percentage>
******************************************************************************
'''


class student:
    def __init__(self,name='', reg_no='', roll_no='', standard='', admission_year=''):
        if name.isalpha() and reg_no.isalnum() and roll_no.isnumeric() and standard.isnumeric() and admission_year.isnumeric():
            self.Name = name
            self.Reg_no = reg_no
            self.Roll_no = roll_no
            self.Standard = standard
            self.Admission_year = admission_year
        else:
            print("fill in the correct format ")
        self.Marks = []
        self.result = ''

    def marks(self,sub_dict):
        for i,j in sub_dict.items():
            if j>100:
                print(f"Jitna marks mila hai utna hi likh bhai {i} - {j} kya hai")
            elif j<40:
                self.Marks.append({i:{j:'fail'}})
            elif 39<j<101:
                self.Marks.append({i:{j:'pass'}})
        # print(self.Marks)
        # print(self.Marks[0])


    def show_result(self):
        total_marks = 100
        passing_marks = 40
        total_prapt = 0
        pf = []

        print("*"*90)
        print("Name :",self.Name)
        print(f"Roll No : {self.Roll_no} \t\t\t\t\t\t\t\t\t Standard : {self.Standard}")
        print("*"*90)
        print(f"Subject \t\t Total Marks \t\t Passing Marks \t\t Obtained Marks \t\t Result")
        print('-'*90)
        for i in range(len(self.Marks)):
            for j in self.Marks[i]:
                for k in self.Marks[i][j]:
                    # print(self.Marks[i][j])
                    print(f"{j} \t\t\t\t {total_marks} \t\t\t\t\t {passing_marks} \t\t\t\t {k} \t\t\t {self.Marks[i][j][k]}")
                    pf.append(self.Marks[i][j][k])
                    total_prapt += k

        # print(pf)
        if ('fail' in pf):
            self.result = "Fail"
        else:
            self.result = "Pass"



        print("*" * 90)
        print(f"Total \t\t\t\t 300 \t\t\t\t\t 120 \t\t\t\t {total_prapt} ")
        print(f"Result : {self.result} \t\t\t\t\t\t Percentage : {total_prapt / 3 } %")
        print("*" * 90)



subjects = ["Python","Java","PHP"]
marks = [int(input(f"enter marks {x}: "))for x in subjects]
# print(marks)
sub_dict = {subjects[i]:marks[i] for i in range(len(subjects))}
# print(sub_dict)


obj = student("vishalgupta",'2024','22166','12','1234')
obj.marks(sub_dict)
obj.show_result()