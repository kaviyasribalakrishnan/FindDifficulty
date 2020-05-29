import csv
def main():
    filename="StudentsPerformance.csv"
    rows=[]
   #reads the file data
    with open(filename, 'r') as csvfile: 
        csvreader = csv.reader(csvfile)
        nques1=(next(csvreader)) 
        nques=(int)(nques1[0])
        nattempts1=(next(csvreader))
        nattempts=(int)(nattempts1[0])
        i=0
        j=0
        #reads every line of the csv file starting from second line
        for row in csvreader:
           if(i<nques):
               if(j<nattempts):
                   choice=row[0].lower()
                   difficulty=row[1]
                   #print(row[2])
                   n=(int)(row[2])
                   #if length of a row is less than 10 then data is insufficient or greater than 10 then data is extra
                   if(len(row)<10 or len(row)>10):
                        print("Enter sufficient data and Try Again")
                        return
                   else:
                        #checking for choice of question 
                        if((choice== "mcq") or (choice== "fillup") or (choice == "match")):
                            total=mcq(n,row)
                            #adding the value into the list rows
                            rows.append(total)
                            
                        elif(choice == "coding"):
                            total=code(n,row)
                            #adding the value into the list rows
                            rows.append(total)

                        else:
                            #if the entered choice option is not correct
                            print("Enter valid details and try again")
                            return
               j=j+1

           if(j==nattempts):
                i+=1
                #to make the next iteration
                j=0
                #To print the result of that particular question
                printDiff(rows,nattempts)
                rows.clear()

#Function to print the final result                
def printDiff(rows,n):
    total=0.0
    #Taking average of the values
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

#Function to calculate result for coding type of question       
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

#Function to calculate result for mcq / fillups / match type of question  
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

    
#First part of the solution calculated using time_in_minutes,times_compiled,feedback,n for coding question
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
        elif(z=="hard"):
            c+=75
        else:
            print("Invalid option")
            return 0
        total+=(a+b+c)/3
    total=total/n
    return total
#First part of the solution calculated using time,attempts,feedback,n for mcq type question
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
        elif(z=="hard"):
            c+=75
        else:
            print("Invalid option")
            return
        total+=(a+b+c)/3
    total=total/n
    return total
      
#Part 2 solution is common bor both type     
def part2(ncorrect,nwrong,npartial,n):
    ans=(float)((ncorrect+npartial)/n) #difficulty index value
    if( abs(ans-0) >=0.75):
        return 25
    elif(abs(ans-0) <0.25):
        return 75
    else:
        return 50

if __name__ == '__main__':
    main()
