# Gale_Project

USER'S GUIDE

Set up before starting:
- Python 3 and Pip3
- These packages on Python:
    - Flask
    - Requests
    - Python-dotenv
    - Folium
- a .env file that contains a key from the website below.
    https://www.iqair.com/us/air-pollution-data-api
    with the following format:

    AIRVISUAL_API_KEY= Your key

How to use the project:
- Blank project screen:
    ![Open Screen](OpenScreen.png)
- Enter location: 
    ![Enter Location](EnterLocation1.png)
    After you enter your chosen location, the following information will appear.
- Click on the location on the map:
    ![Map](Map.png)
    Click on the icon ob the map to see details about the location. You are able to scroll in or out and move around. 
- Click "More Weather Info":
    ![Weather Info](WeatherInfo.png)
    Click on the "More Weather Info" link to show additional info about the weather in the area.
- Click on the pollutant:
    ![Pollutant](Pollutant.png)
    Click on the pollutant to find additional info about it.
- Scroll down to find more info about AQI:
    ![AQI Info](AQIInfo.png)
    Scroll down on the screen to answer any questions you might have about what AQI is.
- Enter a new location:
    ![New Location](EnterLocation2.png)
    Play around a bit and try some new locations.

Any errors you might encounter:
- The program requires a response for each category to run. Although the    country might be obvious or repetitive, you will be prompted to enter one if you try to run the program without one. 

Quick intro on the API:
- to use the API make a hidden file with the API key. Then, import the API into your main file like so:
    url = f"http://api.airvisual.com/v2/countries?key={AIRVISUAL_API_KEY}"
- then create a list using data from the API:
    countries_dict_list = data['data']
    countries_lst = [country_dict ['country'] for country_dict in countries_dict_list]
- pull the info for state and city as well, and tie it to the user responses
- then, you will be able to grab weather data using this info
    weather_info = data['data']['current']['weather']
    additional info can be grabbed from the API using this process:
        a_temperature = int(weather_info.get('tp', 'N/A'))

Limitations/Caveats:
- I had originally wanted to include historical AQI info. My API would not allow this and I could not find a free API that would. If I were to keep working on this project I would try to make this happen