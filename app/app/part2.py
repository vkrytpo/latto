import random
from  .game import Tattslotto ,OzLatto ,PowerBall

class part2Tattslotto(Tattslotto):
  '''
   @name: 'Prsanth'
   @student number: 42750
   @lecturer’s name: "xxxxx"
   @Date: 06/12/2019
  '''
  def __init__(self , name ,day ,lower ,higher):
      #calling constructer of parent class Tattslotto.
      Tattslotto.__init__(self , name ,day ,lower ,higher)
      #set a extra attribute named msg for msg delivery.
      self.msg =""
  ''' 
    set_input for passing the input elements.. to game class ,as number of balls.
    it takes an argument of  type  list of integers. 
    and return in invalid messages , if inpout is invalid./.
  '''
  def set_input(self , input_num):
       self.theInput =input_num
       if (len(input_num) != self.numberOfRandoms) :
            self.msg= self.msg+ " invalid input ,"
  '''
    checkWinningNumbers is  returns the winnng ball number's as game rules are defined
  '''
  def checkWinningNumbers( self):
       rands =self.randomNumbers
       self.msg = self.msg +self.getDay() + " "+ self.getName() +" numbers are: " 
       z=" "+str(rands[0])+" "+str(rands[1])+" " +str(rands[2])+" "+str(rands[3])+" " +str(rands[4])+" " +str(rands[5])+" "
       print(z ,type(z))
       self.msg= self.msg + z
       self.msg= self.msg +"supplement numbers: "+str(rands[6]) +str(rands[7]) +" " 
       self.msg = self.msg +" "+ str(self.numberOfRandoms) +" user picks between "+ str(self.lowerValue) +" "+str(self.higherValue) +" "
       self.msg = self.msg+" 1 2 3 4 5 6 "
  '''  
    returns the winners balls as in message..
  '''
  def winners(self):
     #x is no of winners
     try:
       x=0
       y=0
       inp_nums= self.theInput.split(" ")
       num =self.randomNumbers
       lf= num.pop()
       ls= num.pop()
       for rand in num:
           if rand in inp_nums:
                x= x+1
           if rand in [ls ,lp]:
                y=y+1
       self.msg = self.msg+ "No.of winners are" ,str(x)," , " ,str(y) , "supps match." 
     except:
       pass
    

class part2OzLatto(OzLatto):
  '''
   @name: 'Prsanth'
   @student number: 42750
   @lecturer’s name: "xxxxx"
   @Date: 06/12/2019
  '''
  def __init__(self , name ,day ,lower ,higher):
        # calling constructer of parent class Tattslotto.
        OzLatto.__init__(self , name ,day ,lower ,higher)
        #setting an extra attributes as message passing.
        self.msg =""

  ''' 
  set_input for passing the input elements.. to game class ,as number of balls.
  it takes an argument of  type  list of integers. 
  and return in invalid messages , if inpout is invalid./.
  '''
  def set_input(self , input_num):
       self.theInput =input_num
       if (len(input_num) != self.numberOfRandoms) :
            self.msg= self.msg+ " invalid input  "

  '''
  checkWinningNumbers is  returns the winnng ball number's as game rules are defined
  '''
  def checkWinningNumbers( self):
       rands =self.randomNumbers
       self.msg = self.msg +self.getDay() + " "+ self.getName() +" numbers are: " 
       z=" "+str(rands[0])+" "+str(rands[1])+" " +str(rands[2])+" "+str(rands[3])+" " +str(rands[4])+" " +str(rands[5])+" "+str(rands[6])+ ", "
       self.msg= self.msg+ z
       self.msg= self.msg + "supplement numbers: " + str(rands[7]) + str(rands[8]) +", "
       self.msg = self.msg+" "+str(self.numberOfRandoms )+" user picks between " + " "+ str(self.lowerValue )+" "+ str(self.higherValue) +", "
       self.msg = self.msg+" 1 2 3 4 5 6 7  "
  '''  
      returns the winners balls as in message..
  '''
  def winners(self):
     #x is no of winners
     try:
       x=0
       y=0 
       inp_nums= self.theInput.split(" ")
       num =self.randomNumbers
       lf= num.pop()
       ls= num.pop()
       for rand in num:
           if rand in inp_nums:
                x= x+1
           if rand in [ls ,lp]:
                y=y+1
       self.msg = self.msg+ "No.of winners are" ,x ," , " ,y , "supps match." 
     except:
       pass
     




class part2PowerBall(PowerBall):
  '''
   @name: 'Prsanth'
   @student number: 42750
   @lecturer’s name: "xxxxx"
   @Date: 06/12/2019
  '''
  def __init__(self , name ,day ,lower ,higher):
      PowerBall.__init__(self , name ,day ,lower ,higher)
      self.msg =""
  ''' 
  set_input for passing the input elements.. to game class ,as number of balls.
  it takes an argument of  type  list of integers. 
  and return in invalid messages , if inpout is invalid./.
  '''
  def set_input(self , input_num):
    self.theInput =input_num
    if (len(input_num) != self.numberOfRandoms) :
       self.msg= self.msg+ " invalid input  "

  '''
  checkWinningNumbers is  returns the winnng ball number's as game rules are defined
  '''
  def checkWinningNumbers( self):
       rands =self.randomNumbers
       power_rand= random.randint(1 ,20)
       self.msg = self.msg +self.getDay() + " "+ self.getName() +" numbers are: " 
       z=" "+str(rands[0])+" "+str(rands[1])+" " +str(rands[2])+" "+str(rands[3])+" " +str(rands[4])+" " +str(rands[5])+" "+str(rands[6])+ ", "
       self.msg= self.msg+ z
       self.msg= self.msg +" POWER BALL is :- "+ str(power_rand)+", "
       self.msg = self.msg+" " +str(self.numberOfRandoms) +" user picks between " + str(self.lowerValue) +" "+ str(self.higherValue) +", "
       self.msg = self.msg+" 1 2 3 4 5 6 7 "
       x=0 
       inp_nums= self.theInput.split(" ")
       num =self.randomNumbers
       for rand in num:
          if rand in inp_nums:
              x= x+1
       if power_rand in num :
           self.msg= self.msg+ "No.of winners are" ,x ,"you have power ball" 
       else:
           self.msg =  self.msg+"No.of winners are" ,x ," and you don't have Power Ball." 


