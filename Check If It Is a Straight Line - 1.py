class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x=coordinates[1][0] - (coordinates[0][0]) 
        y = coordinates[1][1] - (coordinates[0][1]) 
        try:
            z=y//x
        except: #in case z=0
            print()
        if len(coordinates) == 2:
            return True
        
        for i in range(1,len(coordinates)):
            try:
                if (( (coordinates[i][1]) - (coordinates[i-1][1]) ) // ((coordinates[i][0]) - (coordinates[i-1][0]))) == z :
                    
            
                    continue
            except:
                print()
                return False
            else:
                return False
        return True
                