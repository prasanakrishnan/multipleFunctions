class multipleFunctions:
    def subfields():
        list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processung"]
        print("Sub-fields in AI are:")
        for subfields in list:
            print(subfields)
    def oddeven():
        num=int(input("Enter a number:"))
    
        if(num%2==0):
            print(num,"is even number")
        else:
            print(num,"is odd number")
    def eligible():
        gender=input("your gender:")
        age=int(input("your age:"))
        if(gender=="male" and age>=21):
            print("your eligible")
        elif(gender=="female" and age>=18):
            print("your eligible")
        else:
            print("your not eligible")
    def percentage():
        sub1=int(input("subject1="))
        sub2=int(input("subject2="))
        sub3=int(input("subject3="))
        sub4=int(input("subject4="))
        sub5=int(input("subject5="))
        Total=sub1+sub2+sub3+sub4+sub5
        print("Total:",Total)
        percentage=Total/5
        print("percentage:",percentage)

    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        height1=int(input("Height:"))
        height2=int(input("Height2:"))
        breadth1=int(input("Breadth:"))
        area=height*breadth/2
        print("area of triangle:",area)
        perimeter=height1+height2+breadth1
        print("perimeter of triangle:",perimeter)
