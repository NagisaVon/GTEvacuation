class fireAlarm:
    def __init__(self,freq): #freq is the number of drills in a year
        self.drillFrequency = freq/365
        #The lower the frequency the less prepared people are
        #the closer to 1 the frequency is, the less people will respond
    def returnFrequency(self):
        return(self.drillFrequency)
    
    
#Running the program
a = fireAlarm(1)
print(a.returnFrequency())