import random 

class LuckyGame:
  '''
   this is a parent class of all classes , having  core features.
   @name: 'Prsanth'
   @student number: 42750
   @lecturer’s name: "xxxxx"
   @Date: 06/12/2019
  '''
  def __init__(self , name ,day ,lower ,higher):
    ''' setting up common attribute '''
    self.gameName = name
    self.dayOfGame = day
    self.numberOfRandoms = 0
    self.lowerValue = lower
    self.higherValue = higher
    self.randomNumbers = []

  def createRandomNumbers( self ):
      '''creating random numbers for random guess..'''
      for i in range(0, self.numberOfRandoms) :
           self.randomNumbers.append(random.randint(self.lowerValue ,self.higherValue))

  def getName( self ):
      '''returns name of game'''
      return self.gameName

  def getDay( self ):
      '''returns  day of game'''
      return self.dayOfGame

  def toString( self ):
      '''converts into string..'''
      pass

  def setNumberOfRandoms( self ,randomballs ):
      '''setting number of random balls..'''
      self.numberOfRandoms = randomballs

  def collectUserInput(self):
      '''collecting user input through terminall'''
      input_nums = self.theInput.split(" ")
      if (len(input_nums) != self.numberOfRandoms) :
           print(" Invalid input")

  def winners(self):
     '''returns winner of the game '''
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
       print( "No.of winners are" ,x ," , " ,y , "supps match." )
     except:
       pass
      
  def print(self):
      '''just a formated print about game details..'''
      print(self.gameName ,self.dayOfGame ,self.numberOfRandoms ,self.lowerValue , self.higherValue ,self.randomNumbers )

class Tattslotto(LuckyGame):
  '''
   this is a class for terminal based TattsLatto inheriting LuckyGame,
   @name: 'Prsanth'
   @student number: 42750
   @lecturer’s name: "xxxxx"
   @Date: 06/12/2019
  '''
  def __init__(self , name ,day ,lower ,higher):
      '''cal;ling constructor of parent class.'''
      LuckyGame.__init__(self , name ,day ,lower ,higher)
      self.theInput = ""

  def collectUserInput(self):
      '''collecting user input from teminal'''
      self.theInput = input("Input Your numbers for "+self.getName() + " "+ self.getDay()+ ": ")
      LuckyGame.collectUserInput(self)

  def checkWinningNumbers(self):
      '''matching the user input to randomnumbers , returns winner'''
      rands =self.randomNumbers
      print(self.getDay() + " "+ self.getName() ," numbers are: ")
      print(rands[0] ,rands[1] ,rands[2] ,rands[3] ,rands[4] ,rands[5] ,"supplement numbers: ", rands[6] ,rands[7])
      print(self.numberOfRandoms ," user picks between " ,self.lowerValue ,self.higherValue)
      print("1 2 3 4 5 6")
      
  def toString():
      pass

class OzLatto(LuckyGame):
  '''
    this is a class for terminal based Ozlatto inheriting LuckyGame,
   @name: 'Prsanth'
   @student number: 42750
   @lecturer’s name: "xxxxx"
   @Date: 06/12/2019
  '''
  def __init__(self , name ,day , lower ,higher):
      '''calling constructor of parent class'''
      LuckyGame.__init__(self , name ,day ,lower ,higher)
      self.theInput = ""

  def collectUserInput(self):
      '''collects user input trough terminal.'''
      self.theInput = input("Input Your numbers for "+self.getName() + " "+ self.getDay()+ ": ")
      LuckyGame.collectUserInput(self)


  def checkWinningNumbers(self):
      '''checking who ius winners as their ball-number.'''
      rands =self.randomNumbers
      print(self.getDay() + " "+ self.getName() ," numbers are: ")
      print(rands[0] ,rands[1] ,rands[2] ,rands[3] ,rands[4] ,rands[5] ,rands[6] ,"supplement numbers: ", rands[7] ,rands[8])
      print(self.numberOfRandoms ," user picks between " , self.lowerValue ,self.higherValue)
      print("1 2 3 4 5 6 7")

  def toString():
      pass
   
  
class PowerBall(LuckyGame):
  '''
    this is a class for terminal based Powerball inheriting LuckyGame,
    @name: 'Harish gatla'
    @student number: 43480
    @lecturer’s name: "xxxxx"
    @Date: 05/18/2019
  '''
  def __init__(self , name ,day ,lower ,higher):
      '''calling constructor of parent class'''
      LuckyGame.__init__(self , name ,day ,lower ,higher)
      self.theInput = ""

  def collectUserInput(self):
      '''collecting user input from teminal'''
      self.theInput = input("Input Your numbers for "+self.getName() + " "+ self.getDay()+ ": ")
      LuckyGame.collectUserInput(self)


  def checkWinningNumbers(self):
      '''returns who is winner as given input.'''
      rands =self.randomNumbers
      print(self.getDay() + " "+ self.getName() ," numbers are: ")
      power_rand= random.randint(1 ,20)
      print(rands[0] ,rands[1] ,rands[2] ,rands[3] ,rands[4] ,rands[5] ,rands[6] ,"POWER BALL is :- ",power_rand)
      print(self.numberOfRandoms ," user picks between " , self.lowerValue ,self.higherValue)
      print("1 2 3 4 5 6 7")
      x=0
      inp_nums= self.theInput.split(" ")
      num =self.randomNumbers
      for rand in num:
         if rand in inp_nums:
              x= x+1
      if power_rand in num :
           print( "No.of winners are" ,x ,"you have power ball" )
      else:
           print( "No.of winners are" ,x ," and you don't have Power Ball." )
     

  def toString():
      pass
  
if __init__ == '__main__':
	print("*"*50)

	first = Tattslotto("TatsLatto" ,"Saturday" ,1 ,45)
	first.setNumberOfRandoms(8)
	#first.print()
	first.collectUserInput()
	first.createRandomNumbers()
	first.checkWinningNumbers()
	first.winners()
	print("*"*50)

	second = OzLatto("OZ Latto" ,"Tuesday" ,1 ,45)
	second.setNumberOfRandoms(9)
	#second.print()
	second.collectUserInput()
	second.createRandomNumbers()
	second.checkWinningNumbers()
	second.winners()

	print("*"*50)

	second = PowerBall("Power ball" ,"Tuesday" ,1 ,45)
	second.setNumberOfRandoms(7)
	second.print()
	second.collectUserInput()
	second.createRandomNumbers()
	second.checkWinningNumbers()

	print("-"*50)
