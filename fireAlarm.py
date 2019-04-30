import random
class student:
    def __init__(self, memoryDecay,caution):
        self.memoryDecayRate = memoryDecay #how less prepared a student is per day
        self.preparedness = 0 #percentile chance prepared
        self.response = 100 #percentile chance to respond
        self.day = 0 #the current day
        self.cautiousLevel = caution #How much their response changes each day
    
    def nextDay(self, isThereAnAlarm):
        self.day += 1
        
        if isThereAnAlarm:
            self.preparedness = 100
            self.response -= 100-self.cautiousLevel
            if self.response <100: self.response = 0
        else:
            self.preparedness -= self.memoryDecayRate
            self.response += ((self.cautiousLevel*(1/6) *(100-self.preparedness)/100))
            if self.preparedness <0:
                self.preparedness = 0
            if self.response >100:
                self.response = 100

class fireDrill:
    def __init__(self,num):
        self.numberOfDrills = num
        
        self.drillDays = []
        for i in range(num):
            self.drillDays.append(random.randint(1,178))

def isThisADrillDay(self,day):
    if day in self.drillDays:
        return True
        else:
            return False
                
                def avgDaysBetweenDrill(self):
                    sumOfAvgDays = 0
for i in range(len(self.drillDays)):
    if(i)==0:
        sumOfAvgDays+=(self.drillDays[i])
            else:
                if(self.drillDays[i]>self.drillDays[i-1]):
                    sumOfAvgDays+=(self.drillDays[i]-self.drillDays[i-1])
                else:
                    sumOfAvgDays+=(self.drillDays[i-1]-self.drillDays[i])
    return sumOfAvgDays/self.numberOfDrills

#Assumption: on average, a student will not be prepared after one to two months of no drill
#Assumption: on avergae, there are 178 days per school year
#This means, 2 months (on average 61 days) will be 45 days (subtracting saturdays and sundays)
#Assumption: A student's caution levels can be between 100 (cautious all the time) and 0 (never cautious)
#This having an average caution level of about 75
#100 caution means they will always respond, 0 caution means they will never respond
#75 caution means that when there's a drill, their response will drop 25%
#When there isn't a drill, their response will raise up by 2/3 caution * (100-preparedness)/100
def average(stud,typ,drill):
    prepSum =0
    respSum =0
    for day in range(1,178):
        prepSum+= ((int)(stud.preparedness))
        respSum+= ((int)(stud.response))
        stud.nextDay(drill.isThisADrillDay(day))
    if typ == "preparedness":
        return prepSum/178
    else:
        return respSum/178

fire = fireDrill(50)
studentList = [student(100/(45-random.randint(0,22)),75-random.randint(-25,75)) for i in range(19)]

prepSum=0
respSum=0
for student in studentList:
    prepSum+=average(student,"preparedness",fire)
    respSum+=average(student,"resp",fire)

print("Number of Drills: "+(str)(fire.numberOfDrills))
print("Average number of Days between Drills: "+(str)(fire.avgDaysBetweenDrill()))
print("\nAverage Prepareness of Students: "+(str)((int)(prepSum/len(studentList))))
print("Average Responsenes of Students: "+(str)((int)(respSum/len(studentList))))


