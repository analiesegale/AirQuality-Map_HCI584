Overview:
  My application pulls information about the air quality and other weather information for a chosen location. 
  This allows an easy way for users to visualize air quality information for a specific location.
  The application is powered by an API from AQICN to bring in data about current air qualities. Other weather info is pulled from the same API.
  Folium is used to create the map affiliated with the given air quality.

Final planning specs:
This project shows the user air quality information about a specific location. The idea is to allow an easy way for users to visualize air quality. This project will be a web application. This will be achieved by using a visual map that allows users to see a location and it's air quality. The location consists of latitude and longitude, and the map is based off of the user’s inputted location. Users are also able to view information about the air quality of a specific area and any cautionary statements. 
  Aspects included from my final planning specs:
    - Ability to grab inputted location from user
    - Ability to grab AQI and other info from API
    - Ability to visualize air quality on a map
    - Interactive map
  Aspects not included from my final planning specs:
    - Filtering abilites for different air qualities
    - Diagrams of air quality over time (was not able to find an API to faciliate this)

Installment/deployement:
  - No additional installments required other than what is in the User's Guide

User interaction/flow (images found in User's Guide):
  - User opens up application, blank screen showing title, "Air Quality Checker", and input areas for city, state, and country, and then a button that says "Check Air Quality". There is also additional AQI information on the page
  - User inputs their desired location and hits the button
      - After the button is hit the application needs to convert the input into a country, state, and city found in the API. The functions get_countries(), get_states_for_country(country), and get_cities_for_state(state, country), are doing this processing (found in main.py)
      - The function geocode_place(place_name) uses a free geocoding service that is used here as well (also found in main.py)
      - The function get_air_quality is used to pull the air quality from the API using the inputted location
  - The map is brought up showing the location. If you hover over the icon on the map it shows the AQI, and if you click it more info about the location is shown.
      - Within the get_air_quality function there is a section for the html and popup that goes with the icon
      - The function icon_colors(aqi) is used to determine the color of the icon, this corresponds with the severeness of the aqi
  - Also on the page is the AQI, health implications, the main pollutant, and an additional weather info button
      - Text is laid out in the HTML
  - User can click on "More weather info" to pull up info about the temp, wind direction, etc of their given location
      - Button implemented through the HTML, data pulled in the main.py file through response.status.code
  - User can click on the main pollutant to pull up additional info about the specific pollutant
      - Button implemented through the HTML, data pulled in through the get_air_quality() function
  - User can search for a new location and explore these options again

UX:
  - The text boxes needed to input the location are all grouped together above the "get air quality button" to allow the user to know where to put their info and what info is needed
  - All textual info is below the text boxes and the map is to the right, keeping the information neat and organized
  - Additional info about AQI in general is lower, to the right. This allows it to be there if needed but not in the way and crowding the page

Known issues:
  - I do not have any known issues with my current app, one potential issue may be that all three inputs for city, state, and country must be filled. Although, this is clearly demonstrated to the user. 
  - The UX could for sure be improved, the app is not very stylish as is, but works for its purpose.

Future work:
  - In the future I would like to implement a system that allows the user to explore historic AQI info. This was not attainable for this project because of the APIs available, but would be interesting down the line.
  - I would also like to improve the UX. This application is not very stylish, but allows the processing it requires.
  - Lastly, it would be interesting to use profiles within the application. Although, this is something I am not sure how to do.
