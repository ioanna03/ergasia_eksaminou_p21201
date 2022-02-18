#CHOOSE A RANDOM LOCATION
import random
def columns():
    return random.randrange(0,9)
def row():
    return random.randrange(0,9)

#CHECKS IF THE ROOK IS THREATING ANOTHER PIECE,GIVEN HIS LOCATION

def rook_thr(rook,targ):
    count1=0
    count2=0
    if rook[0]==targ[0]:
        count1=1
    if rook[-1]==targ[-1]:
        count2=1
    return max(count1,count2)


#CHECKS IF THE BISHOP IS THREATENING ANOTHER PIECE,GIVEN HIS LOCATION
def bishop_thr(bishop,check_sq):
    targ_sq=[]
    square=[]
    count3=0

    #CHECK EACH SQUARE ON THE BOARD TO SEE IF THE BISHOP CAN MOVE THERE
    for rows in range(8):
        for col in range (8):
            square=[(rows+1),(col+1)]

            #CHECK IF THE SQUARE IS IN THE LEFT DIAGONAL WHICH STARTS FROMTHE TOP AND THE BISHOP CAN MOVE
            if sum(square)==sum(bishop):
                targ_sq.append(square)

             # CHECK IF THE SQUARE IS IN THE RIGHT DIAGONAL WHICH STARTS FROM BOTTOM AND THE BISHOP CAN MOVE
            if square[0] - bishop[0] == square[-1] - bishop[-1]:
                targ_sq.append(square)

            if square in targ_sq:
                count3=1




    return count3

def main():
    results=[]
    w_team =0
    for i in range(100):
        #SET LOCATION TO THE ROOK
            r_location=[columns(),row()]
            b_location=[columns(),row()]
            while r_location == b_location:
                b_location = [columns(), row()]

            test1=rook_thr(r_location,b_location)
            if max == 1:
                w_team=w_team+1
            test2=bishop_thr(b_location,r_location)
            if count3 == 1:
                b_team = b_team + 1
            test3=test1+test2
            result.append(test3)
    print("POINTS OF BLACK TEAM:"+b_team)
    print("POINTS OF WHITE TEAM:" + w_team)
