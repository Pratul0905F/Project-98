def swaper():
    with open("t1.txt")as a:
        a_data=a.read()
        
    with open("t2.txt")as b:
        b_data=b.read()
    
    with open("t1.txt","w")as a:
        a.write(b_data)
    
    with open("t2.txt","w")as b:
        b.write(a_data)
swaper()