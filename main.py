'''
Morgan Purcell & Sabby Macedo
Program to find the optimal route between two missouri citites using the A* search algorithm
October 27th 2022
'''

# dictionary to hold heristic values
heuristic_map = {
        "St. Joseph": {"St. Joseph": 0, "Kansas City": 56, "Joplin": 205, "Springfield": 221, "Rolla": 277, "Jefferson City": 215, "Columbia": 181, "Moberly": 157, "Hannibal": 194, "Troy": 254, "St. Charles": 286, "St. Louis": 303, "Lebanon": 237},
         "Kansas City": {"St. Joseph": 56, "Kansas City": 0, "Joplin": 156, "Springfield": 165, "Rolla": 219, "Jefferson City": 157, "Columbia": 124, "Moberly": 159, "Hannibal": 210, "Troy": 211, "St. Charles": 228, "St. Louis": 248, "Lebanon": 176},
         "Joplin": {"St. Joseph": 205, "Kansas City": 56, "Joplin": 0, "Springfield": 74, "Rolla": 179, "Jefferson City": 205, "Columbia": 235, "Moberly": 270, "Hannibal": 310, "Troy": 282, "St. Charles": 288, "St. Louis": 284, "Lebanon": 123},
         "Springfield": {"St. Joseph": 221, "Kansas City": 165, "Joplin": 74, "Springfield": 0, "Rolla": 112, "Jefferson City": 138, "Columbia": 169, "Moberly": 203, "Hannibal": 242, "Troy": 215, "St. Charles": 221, "St. Louis": 217, "Lebanon": 54},
         "Rolla": {"St. Joseph": 277, "Kansas City": 219, "Joplin": 179, "Springfield": 112, "Rolla": 0, "Jefferson City": 63, "Columbia": 93, "Moberly": 128, "Hannibal": 168, "Troy": 105, "St. Charles": 110, "St. Louis": 106, "Lebanon": 58},
         "Jefferson City": {"St. Joseph": 215, "Kansas City": 157, "Joplin": 205, "Springfield": 138, "Rolla": 63, "Jefferson City": 0, "Columbia": 32, "Moberly": 66, "Hannibal": 106, "Troy": 96, "St. Charles": 113, "St. Louis": 133, "Lebanon": 82},
         "Columbia": {"St. Joseph": 181, "Kansas City": 124, "Joplin": 235, "Springfield": 169, "Rolla": 93, "Jefferson City": 66, "Columbia": 0, "Moberly": 36, "Hannibal": 98, "Troy": 87, "St. Charles": 105, "St. Louis": 125, "Lebanon": 113},
         "Moberly": {"St. Joseph": 157, "Kansas City": 159, "Joplin": 270, "Springfield": 203, "Rolla": 128, "Jefferson City": 106, "Columbia": 36, "Moberly": 0, "Hannibal": 70, "Troy": 120, "St. Charles": 137, "St. Louis": 157, "Lebanon": 148},
         "Hannibal": {"St. Joseph": 194, "Kansas City": 210, "Joplin": 310, "Springfield": 242, "Rolla": 168, "Jefferson City": 96, "Columbia": 98, "Moberly": 70, "Hannibal": 0, "Troy": 63, "St. Charles": 97, "St. Louis": 117, "Lebanon": 188},
         "Troy": {"St. Joseph": 254, "Kansas City": 211, "Joplin": 282, "Springfield": 215, "Rolla": 105, "Jefferson City": 70, "Columbia": 87, "Moberly": 120, "Hannibal": 63, "Troy": 0, "St. Charles": 35, "St. Louis": 55, "Lebanon": 161},
         "St. Charles": {"St. Joseph": 286, "Kansas City": 228, "Joplin": 288, "Springfield": 221, "Rolla": 110, "Jefferson City": 113, "Columbia": 105, "Moberly": 137, "Hannibal": 97, "Troy": 35, "St. Charles": 0, "St. Louis": 23, "Lebanon": 167},
         "St. Louis": {"St. Joseph": 303, "Kansas City": 248, "Joplin": 284, "Springfield": 217, "Rolla": 106, "Jefferson City": 133, "Columbia": 125, "Moberly": 157, "Hannibal": 117, "Troy": 55, "St. Charles": 23, "St. Louis": 0, "Lebanon": 163},
         "Lebanon": {"St. Joseph": 237, "Kansas City": 176, "Joplin": 123, "Springfield": 54, "Rolla": 58, "Jefferson City": 82, "Columbia": 113, "Moberly": 148, "Hannibal": 188, "Troy": 161, "St. Charles": 167, "St. Louis": 163, "Lebanon": 0},
        }

# dictionary to hold distances between connected cities
connections = {
        "St. Joseph": {"Kansas City": 56},
         "Kansas City": {"St. Joseph": 56, "Joplin": 156, "Columbia": 124},
         "Joplin": {"Kansas City": 56, "Springfield": 74},
         "Springfield": {"Joplin": 74, "Lebanon": 54},
         "Rolla": {"Jefferson City": 63, "St. Louis": 106, "Lebanon": 58},
         "Jefferson City": {"Rolla": 63, "Columbia": 32},
         "Columbia": {"Kansas City": 124, "Jefferson City": 66, "Moberly": 36, "St. Charles": 105},
         "Moberly": {"Columbia": 36, "Hannibal": 70},
         "Hannibal": {"Moberly": 70, "Troy": 63},
         "Troy": {"Hannibal": 63, "St. Charles": 35},
         "St. Charles": {"Columbia": 105, "Troy": 35, "St. Louis": 23},
         "St. Louis": {"Rolla": 106, "St. Charles": 23},
         "Lebanon": {"Springfield": 54, "Rolla": 58},
        }


# functiont to go from any city to STL
def toSTL(startCity):
        # just call toCities and pass STL as a parameter for the endCity
        return toCities(startCity, "St. Louis")


# function to go from a city to another city
def toCities(startCity, endCity):
        # if we're already at
        if(startCity == endCity):
                print("")

        # seen dictionary to hold cities that have been considered along with their f(n)
        seen = {startCity: heuristic_map[startCity][endCity]}
    
        # set the g(n) (shortest distance from city n to starting city) to a high number
        gofn = dict.fromkeys(heuristic_map,10000)
        # set the starting cities g(n) to 0 
        gofn[startCity] = 0

        # set the h(n) (distance from city n to the end city) to a high number
        hofn = dict.fromkeys(heuristic_map,10000)
        # set the starting cities h(n) to 0 
        hofn[startCity] = 0
        
        # set the f(n) (estimate of how far a city n is from the end city) to a high number
        fofn = dict.fromkeys(heuristic_map,10000)
        # set the starting cities f(n) to 0 
        fofn[startCity] = 0

        # list to hold the best route to the end city
        path = []

        # while there are citites in the seen list
        while seen:
            # initialize currMin to the city with the smallest f(n) value in the seen list
            currMin = min(seen, key=seen.get)

            # if currMin equals the end city, you have arrived at your destination  
            if(currMin == endCity):
                # appened the end city to the path list
                path.append(endCity)
                # output the best route from the start city to the end city
                print("\nThe best route is: ")
                print(' -> '.join(path))
                exit()
            
            # delete the city with the lowest f(n) from the set
            del seen[currMin]

            # append the city with the lowest f(n) to the path list
            path.append(currMin)

            # loop to check currMin's(current city we're looking at) neighbouring cities for the lowest g(n)
            for target in connections[currMin]:
                # check if the neighbouring cities g(n) using this current route is less than it's previous g(n) within the gofn dictionary
                if(connections[currMin][target] < gofn[target]):
                    # update the neighbouring cities(target) g(n) within the gofn dictionary
                    gofn[target] = connections[currMin][target]

                    # update the neighbouring cities(target) h(n) within the hofn dictionary
                    hofn[target] = heuristic_map[target][endCity]

                    # update the neighbouring cities(target) f(n) within the fofn dictionary
                    fofn[target] = gofn[target] + hofn[target]

                    # add the neighbouring city(target) to the seen cities
                    seen[target] = fofn[target]


def main():
        # ask the user to select an option
        callFunc = input("1. Go to STL \n2. Go from one city to and other another city\n")

        # call the toSTL function if the user wants to go to STL
        if callFunc == "1":
                # ask the user for the origin city
                startCity = input("\nEnter the origin city: ")
                # if the city is not valid, inform the user
                if(startCity not in heuristic_map):
                        print("\nInvalid origin city")
                        exit()

                # call the toSTL function and pass the origin city as an argument
                toSTL(startCity)

        # call the toCities function if the user wants to go to a city they select
        elif callFunc == "2":
                # ask the user for the origin city
                startCity = input("\nEnter the origin city: ")
                # if the city is not valid, inform the user
                if(startCity not in heuristic_map):
                        print("\nInvalid origin city")
                        exit()

                # ask the user for the destination city
                endCity = input("\nEnter the destination city: ")
                # if the city is not valid, inform the user
                if(endCity not in heuristic_map):
                        print("\nInvalid destination city")
                        exit()
                        
                # call the toCities function and pass the origin and destination citites as arguments
                toCities(startCity, endCity)


# call the main function
if __name__ == '__main__':
    main()