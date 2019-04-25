class fireAlarm:
    def __init__(self,freq): #freq is the number of drills in a school year
        self.drillFrequency = freq/178 #divided by the average number of school days per year
        #The lower the frequency the less prepared people are
        #the closer to 1 the frequency is, the less people will respond
    def returnFrequency(self):
        return(self.drillFrequency)
    
    def evacProb(self):
        #How prepared people are
            #goes up based on how close the freq is to 1
            pass
        #How likly a person in to respond
            #goes down based on how close the freq is to 1

#running the program
a = fireAlarm(1)
print(a.returnFrequency())