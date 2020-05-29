import csv
def main():
    filename="StudentsPerformance.csv"
    rows=[]
    with open(filename, 'r') as csvfile: 
        csvreader = csv.reader(csvfile)
        nques1=(next(csvreader))
        
        nques=(int)(nques1[0])
        w=(next(csvreader))
        nattempts=(int)(w[0])
        if(len(nques1) >1 or len(w) >1):
            print("Don't Enter mutiple values for Number of questions or number of attempts " )
            return
        i=0
        j=0
        for row in csvreader:
           if(i<nques):
               if(j<nattempts):
                   choice=row[0].lower()
                   difficulty=row[1]
                   #print(row[2])
                   n=(int)(row[2])
                   if(len(row)<10 or len(row)>10):
                        print("Enter sufficient data and Try Again")
                        return
                   else:
                        #print(choice)
                        if((choice== "mcq") or (choice== "fillup") or (choice == "match")):
                            total=mcq(n,row)
                            #print(total)
                            rows.append(total)
                            
                        elif(choice == "coding"):
                            total=code(n,row)
                            rows.append(total)
                            #print(total)
                           
                            
                        else:
                            print("Enter valid details and try again")
                            return
               j=j+1

           if(j==nattempts):
                i+=1
                j=0
                printDiff(rows,nattempts)
                rows.clear()
           
                   
               
            


def printDiff(rows,n):
    total=0.0
    #print(rows)
    for x in rows:
        total+=x
    
    total=total/n
    ans=abs(total-0)
    if(ans<100.0):
        print("Easy Question")
    elif(ans<200.0):
        print("Medium Question")
    else:
        print("Hard Question")

def code(n,row):
        diff=row[1].lower()
        t=row[3]
        a=row[4]
        f=row[5]
        grade_points=0.0
        if(diff == "easy"):
            grade_points+=25
        elif(diff =="medium"):
            grade_points+=50
        elif(diff=="hard"):
            grade_points+=75
        else:
            print("Invalid values, Enter values in (Easy,Medium,Hard)")
            return
        time=list(t.split(","))
        attempts=list(a.split(","))
        feedback=list(f.split(","))
        part3=part1code(time,attempts,feedback,n)
        ncorrect=(int)(row[6])
        nwrong=(int)(row[7])
        npartial=(int)(row[8])
        maxmarks=(int)(row[9])
        part4=part2(ncorrect,nwrong,npartial,n)
        return(part3+(part4+grade_points))

    
def mcq(n,row):
        diff=row[1].lower()
        t=row[3]
        a=row[4]
        f=row[5]
        grade_points=0.0
        if(diff == "easy"):
            grade_points+=25
        elif(diff =="medium"):
            grade_points+=50
        elif(diff=="hard"):
            grade_points+=75
        else:
            print("Invalid values, Enter values in (Easy,Medium,Hard)")
            return
        time=list(t.split(","))
        attempts=list(a.split(","))
        feedback=list(f.split(","))
        part3=part1mcq(time,attempts,feedback,n)
        ncorrect=(int)(row[6])
        nwrong=(int)(row[7])
        npartial=(int)(row[8])
        maxmarks=(int)(row[9])
        part4=part2(ncorrect,nwrong,npartial,n)
        return(part3+part4+grade_points)

def part1code(time_in_minutes,times_compiled,feedback,n):
    a=0
    b=0
    c=0
    total=0.0
    for i in range (0,n):
        x=(int)(time_in_minutes[i])
        y=(int)(times_compiled[i])
        z=feedback[i].lower()
        if(x>45):
            a+=75
        elif(x>15):
            a+=50
        else:
            a+=25
        if(y>10):
            b+=75
        elif(y>5):
            b+=50
        else:
            b+=25
        if(z=="easy"):
            c+=25
        elif(z=="medium"):
            c+=50
        else:
            c+=75
        total+=(a+b+c)/3
    total=total/n
    return total
def part1mcq(time,attempts,feedback,n):
    a=0
    b=0
    c=0
    total=0.0
    for i in range (0,n):
        x=(int)(time[i])
        y=(int)(attempts[i])
        z=feedback[i].lower()
        if(x>90):
            a+=75
        elif(x>60):
            a+=50
        else:
            a+=25
        if(y>4):
            b+=75
        elif(y>2):
            b+=50
        else:
            b+=25
        if(z=="easy"):
            c+=25
        elif(z=="medium"):
            c+=50
        else:
            c+=75
        total+=(a+b+c)/3
    total=total/n
    return total
        
def part2(ncorrect,nwrong,npartial,n):
    ans=(float)((ncorrect+npartial)/n)
    if( abs(ans-0) >=0.75):
        return 25
    elif(abs(ans-0) <0.25):
        return 75
    else:
        return 50

if __name__ == '__main__':
    main()
