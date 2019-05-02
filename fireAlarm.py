import random
import matplotlib.pyplot as plt
import numpy as np

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
        self.drillDays.sort() # For calculate days between

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
                sumOfAvgDays+=(self.drillDays[i]-self.drillDays[i-1])
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



avgD = []
avgP = []
avgR = []


for alarms in range(1, 51):
    avgList = [0,0,0] #days between, prep, respons
    for averageLoop in range(10):
        fire = fireDrill(alarms)
        studentList = [student(100/(45-random.randint(0,22)),75-random.randint(-25,75)) for k in range(19)]
        prepSum=0
        respSum=0
        for stu in studentList:
            prepSum+=average(stu,"preparedness",fire)
            respSum+=average(stu,"resp",fire)
        avgList[0] += (int)(fire.avgDaysBetweenDrill())
        avgList[1] += (int)(prepSum/len(studentList))
        avgList[2] += (int)(respSum/len(studentList))
    avgList[0] = (int)(avgList[0]/10)
    avgD.append(avgList[0])
    avgList[1] = (int)(avgList[1]/10)
    avgP.append(avgList[1])
    avgList[2] = (int)(avgList[2]/10)
    avgR.append(avgList[2])
    print("Number of Drills: "+(str)(fire.numberOfDrills))
    print("Average number of Days between Drills: "+(str)(avgList[0]))
    print("Average Preparedness of Students: "+(str)(avgList[1]))
    print("Average Responsiveness of Students: "+(str)(avgList[2]) + "\n\n" )

fig, (ax1, ax2, ax3) =  plt.subplots(3, 1, sharex = True)

ax1.plot(avgD)
ax1.set_title('Average number of Days between Drills')

ax2.plot(avgP)
ax2.set_title('Average Preparedness of Students')

ax3.plot(avgR)
ax3.set_title('Average Responsiveness of Students')

plt.tight_layout()
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# plt.show()
plt.savefig("a.png")
