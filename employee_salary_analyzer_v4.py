employees = [
            {
                "name": "madhan",
                "dep": "sales",
                "salary": 10000,
                "bonus": 689,
            },
            {
                "name": "vinoth",
                "dep": "management",
                "salary": 40000,
                "bonus": 45000
            },
            {
                "name": "naveen",
                "dep": "ceo",
                "salary": 108000,
                "bonus": 10000,
            }
        ]

while True:
    print("\n-------------employee salary----------")
    print("1.View Employees")
    print("2.Search Employee")
    print("3.Salary Analysis")
    print("4.Add Employee")
    print("5.Exit")

    choice=input("enter your number here:")

    if choice=="1":
        for i in employees:
            print(i)

    elif choice=="2":
        print("---------employees details--------")
        name=input("enter your name:")
        found = False

        for n in employees:
            if n["name"].lower()==name.lower():
                print("employee founded")
                print("name:",n["name"])
                print("department:",n["dep"])
                print("salary:",n["salary"])
                print("Bonus:",n["bonus"])
                found = True

        if found == False:
                 print("not found")


    elif choice=="3":
       print("===========salary analysis===========")
       print("total employees:",len(employees))
       total_salary=0
       for i in employees:
           total=i["salary"] + i["bonus"]
           total_salary=total_salary+total
       print("total salary:",total_salary)

       average_salary=total_salary/len(employees)
       print("average_salary:",average_salary)

       hsalaries=[]

       for h in employees:
           hsalaries.append(h["salary"])

       highest_salary=max(hsalaries)
       print(highest_salary)

       lsalaries=[]

       for l in employees:
           lsalaries.append(l["salary"])

       lowest_salary=min(lsalaries)
       print(lowest_salary)

    elif choice=="4":
        print("-----------add employees----------")

        name=input("enter the employee name:")
        department=input("enter their department:")
        salary=input("enter their salary:")
        bonus=input("enter their bonus:")

        add_new_employee={
            "name":name,
            "dep":department,
            "salary":salary,
            "bonus":bonus
        }

        employees.append(add_new_employee)

    elif choice=="5":
        print("exited")
        break

    else:
        print("invail number")