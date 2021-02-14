
cordinates1  = [(1,5,10),(4,6,8),(10,15,10),(11,12,8)]
# Output - [(1,10),(5,8),(6,0),(10,10),(15,0)]
cordinates2 = [(1,10,4),(1,8,6),(1,6,8)]
# Output = [(1,8),(6,6),(8,4),(10,0)]
cordinates3 =  [(0,6,2),(5,10,8),(7,8,12)]
# Output - [(0,2), (5,8),(7,12),(8,8) (10,0)]
cordinates4 = [(1, 2, 8), (3, 6, 4), (3, 6, 10), (4, 7, 6), (5, 8, 12)]
# Output - [(1, 8), (2, 0), (3, 10), (5, 12), (8, 0)]

# this function will work if next rectangle start point is not equal to start point of previous point
def findOutline (cordinates):
    start,end,height = cordinates[0]
    output = [[start,height]]
    
    for i in range(1, len(cordinates)):
        
        newStart,newEnd,newHeight = cordinates[i]

        if newStart == start:
            # this code block is still not complete
            if newHeight > height:
                # updating height if its already added to output
                if output[-1][0] == newStart and output[-1][1] == height:
                    output[-1][1] = newHeight
                height = newHeight
                
                # print("start,end,height",start,end,height)
        else:
            # else block is executed when start points for rectangle are different

            # if next point starts after the end of last point that means a new rectangle will be created outside of first one
            # and it will not colide with last rectangle
            if newStart > end:
                output.append([end,0])
                output.append([newStart,newHeight])
                start,end,height = cordinates[i]
            
            elif newStart < end:
                # when start of next point is less then end of last point that means starting of next rectangle can intersect
                # new rectangle or fully submerge inside last one
                # next step check end of next rectangle
                if newEnd > end:
                    # if next rectangle ends after the last one that means it will cut the previous rectangle
                    # now we will need to compate height for both rectangle to get rise or drop
                    if newHeight < height:
                        # if next rectangle height is less than last one then its start point will be inside the rectangle
                        # and we will have a drop at previous end point
                        output.append([end,newHeight])
                        

                    elif newHeight > height:
                        # if next rectangle height is greater than last one then its start point will go outside of last rectangle
                        # and we will have a rise at start end point
                        output.append([newStart,newHeight])
                        
                    # if height is same for both then there is no rise and fall. just end will change to new point
                    start,end,height = newStart,newEnd,newHeight
                elif newEnd < end:
                    # in this case there are two chances if new height is less previous one it will submerge so no change
                    # if new height is greater then previous one we will have rise at start and drop at end
                    if newHeight > height:
                        output.append([newStart,newHeight])
                        output.append([newEnd,height])
                else:
                    # if new end and previous end is same then there will a rise at new start if newheight is greater
                    # if height is same or less then no change
                    if newHeight > height:
                        output.append([newStart,newHeight])
                    height = newHeight
            else:
                # if new start and previous end is same then there will be rise at new start if newheight is greater
                # there will be drop at newheight if height is low and no change if height is same
                    if newHeight != height:
                        output.append([newStart,newheight])
                    height = newHeight
                    end = newEnd
    
    # add last end point with height=0
    output.append([end,0])
    
    return output           

print("\n")

allCordinates = [cordinates1,cordinates2,cordinates3,cordinates4]

for oneCordinate in allCordinates:

    print("cordinates",oneCordinate)
    print("result",findOutline(oneCordinate))
    print("\n")
