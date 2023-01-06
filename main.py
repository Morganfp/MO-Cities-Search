"""
This file contains functions to create a map visualization and retrieve city coordinates using geopy and folium.
"""


# Import ArcGIS from geopy to retrieve city coordinates
from geopy.geocoders import ArcGIS
# Import folium for map visualization
import folium
# Import the connections.py module which contain heuristic values and distances
import connections



# Function to create a visualization of the map as a .html file
def mapCoor(coordinates, avg_lat, avg_lon):
        # Create a folium object to store the outputted map
        # Pass in the average latitude and longitude as the initial coordinates for the map
        mapobj = folium.Map(location = [avg_lat, avg_lon], zoom_start=8)
    
        # Iterate through each city in the coordinates list to display a marker at that city (apart from the last city)
        for location in coordinates[:-1]:
                folium.Marker(location=location).add_to(mapobj)

        # Add a red marker to the last location (index -1)
        folium.Marker(location=coordinates[-1], icon=folium.Icon(color='red', icon='none')).add_to(mapobj)
        
        # Add a line between each city
        folium.PolyLine(coordinates).add_to(mapobj)

        # Save the interactive map as a .html file
        mapobj.save ("index.html")



# Function to get the coordinates of the cities
def getCoor(cities):
        # Create an ArcGIS object to store each object
        nom = ArcGIS()
        # List to store each cities coordinates
        city_coor = []

        # Initialize variables used to calculate the average latitude and longitude
        avg_lat = 0
        avg_lon = 0
        num_cities = 0

        # Iterate through each city to get its coordinates
        for i in cities:
                # Initialize a variable to hold the current city using the geocode function
                location = nom.geocode(i + ", Missouri, United States")
                # Append a tuple containing the latitude and longitude of the current city to the city_coor list
                city_coor.append((location.latitude, location.longitude))
                # Increment the number of cities and the total latitude and longitude
                num_cities += 1
                avg_lat += location.latitude
                avg_lon += location.longitude
        
        # Calculate the average latitude and longitude
        avg_lat /= num_cities
        avg_lon /= num_cities

        # Pass all the city coordinates along with the average latitude and longitude to the mapCoor function
        mapCoor(city_coor, avg_lat, avg_lon)



# Function to go from a city to another city
def toCities(startCity, endCity):
        # If we're already at
        if(startCity == endCity):
                print("")

        # Seen dictionary to hold cities that have been considered along with their f(n)
        seen = {startCity: connections.heuristic_map[startCity][endCity]}
    
        # Set the g(n) (shortest distance from city n to starting city) to a high number
        gofn = dict.fromkeys(connections.heuristic_map,10000)
        # Set the starting cities g(n) to 0 
        gofn[startCity] = 0

        # Set the h(n) (distance from city n to the end city) to a high number
        hofn = dict.fromkeys(connections.heuristic_map,10000)
        # Set the starting cities h(n) to 0 
        hofn[startCity] = 0
        
        # Set the f(n) (estimate of how far a city n is from the end city) to a high number
        fofn = dict.fromkeys(connections.heuristic_map,10000)
        # Set the starting cities f(n) to 0 
        fofn[startCity] = 0

        # List to hold the best route to the end city
        path = []

        # While there are citites in the seen list
        while seen:
            # Initialize currMin to the city with the smallest f(n) value in the seen list
            currMin = min(seen, key=seen.get)

            # If currMin equals the end city, you have arrived at your destination  
            if(currMin == endCity):
                # Append the destination city to the path
                path.append(endCity)
                # Pass the cities to the getCoor function to calculate the coordinates of each city
                getCoor(path)
                return
            
            # Delete the city with the lowest f(n) from the set
            del seen[currMin]

            # Append the city with the lowest f(n) to the path list
            path.append(currMin)

            # Loop to check currMin's(current city we're looking at) neighbouring cities for the lowest g(n)
            for target in connections.connections[currMin]:
                # Check if the neighbouring cities g(n) using this current route is less than it's previous g(n) within the gofn dictionary
                if(connections.connections[currMin][target] < gofn[target]):
                    # Update the neighbouring cities(target) g(n) within the gofn dictionary
                    gofn[target] = connections.connections[currMin][target]

                    # Update the neighbouring cities(target) h(n) within the hofn dictionary
                    hofn[target] = connections.heuristic_map[target][endCity]

                    # Update the neighbouring cities(target) f(n) within the fofn dictionary
                    fofn[target] = gofn[target] + hofn[target]

                    # Add the neighbouring city(target) to the seen cities
                    seen[target] = fofn[target]



def main():
        # Ask the user to select an option
        callFunc = input("\nWelcome to the Missouri Route Planner program! Here is a list of available commands:\n\n1. Go to St. Louis \n2. Go from one city to another city\n")

        # Call the toCities function and pass St. louis as the destination city if the user wants to go to STL
        if callFunc == "1":
                # Ask the user for the origin city
                startCity = input("\nEnter the origin city: ")
                # If the city is not valid, inform the user
                if(startCity not in connections.heuristic_map):
                        print("\nInvalid origin city")
                        exit()

                # Call the toSTL function and pass the origin city as an argument
                toCities(startCity, "St. Louis")

        # Call the toCities function if the user wants to go to a city they select
        elif callFunc == "2":
                # Ask the user for the origin city
                startCity = input("\nEnter the origin city: ")
                # If the city is not valid, inform the user
                if(startCity not in connections.heuristic_map):
                        print("\nInvalid origin city")
                        exit()

                # Ask the user for the destination city
                endCity = input("\nEnter the destination city: ")
                # If the city is not valid, inform the user
                if(endCity not in connections.heuristic_map):
                        print("\nInvalid destination city")
                        exit()
                        
                # Call the toCities function and pass the origin and destination citites as arguments
                toCities(startCity, endCity)



# Call the main function
if __name__ == '__main__':
    main()
