
def gameboard(col,row):
  if col <= 7 and row <=7:
    for row in range(len(col)):
      if row%2 == 0:
        for col in range(len(row)):
          if col%2 == 0:
            if col != len(row):
              print(" ",end="")
            else:
              print(" ")
          else:
            print(" | ",end="")
            
    else:
      nOfStripe = len(col)
      print("-" * nOfStripe)
