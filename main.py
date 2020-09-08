#//Author: Miles Johnson mcj5246@psu.edu
#//Collaborator: Ryan Morgan rkm5607@psu.edu
#//Collaborator: Christopher Kurcz cjk6056@psu.edu
#//Collaborator: Laurence Castillo llc5360@psu.edu
#//Section: 7
#//Breakout: 12

def getLetterGrade(numGrade):
  if(numGrade >= 93.0):
    return "A"
  elif(numGrade >= 90.0):
    return "A-"
  elif(numGrade >= 87.0):
    return "B+"
  elif(numGrade >= 83.0):
    return "B"
  elif(numGrade >= 80.0):
    return "B-"
  elif(numGrade >= 77.0):
    return "C+"
  elif(numGrade >= 70.0):
    return "C"
  elif(numGrade >= 60.0):
    return "D"
  else:
    return "F"
  
def run():
  numGrade = input("Enter your CMPSC 131 grade: ");
  numGrade = float(numGrade)
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(numGrade)}.")
if __name__ == "__main__":
  run()