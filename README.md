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
    <img width="497" alt="Screenshot 2023-12-04 at 2 30 15 PM" src="https://github.com/analiesegale/AirQuality-Map_HCI584/assets/143448937/6929dd7b-ac96-4101-9bab-eb88d8223282">

- Enter location: 
    <img width="784" alt="Screenshot 2023-12-04 at 2 30 34 PM" src="https://github.com/analiesegale/AirQuality-Map_HCI584/assets/143448937/51d216b0-3585-4f4e-8571-aed2c3fe0a53">
    After you enter your chosen location, the following information will appear.
  
- Click on the location on the map:
    <img width="392" alt="Screenshot 2023-12-04 at 2 30 41 PM" src="https://github.com/analiesegale/AirQuality-Map_HCI584/assets/143448937/77b418d6-c7e1-43a4-bc15-51a4cb7a37e3">
    Click on the icon ob the map to see details about the location. You are able to scroll in or out and move around.
  
- Click "More Weather Info":
    <img width="749" alt="Screenshot 2023-12-04 at 2 30 54 PM" src="https://github.com/analiesegale/AirQuality-Map_HCI584/assets/143448937/50ba79b9-4045-4da8-84a3-c1c1ed29f373">
    Click on the "More Weather Info" link to show additional info about the weather in the area.
  
- Click on the pollutant:
    <img width="749" alt="Screenshot 2023-12-04 at 2 31 01 PM" src="https://github.com/analiesegale/AirQuality-Map_HCI584/assets/143448937/0c06ccd5-340d-4f12-b8bc-38b8ac7c88db">
    Click on the pollutant to find additional info about it.
  
- Scroll down to find more info about AQI:
    <img width="424" alt="Screenshot 2023-12-04 at 2 31 10 PM" src="https://github.com/analiesegale/AirQuality-Map_HCI584/assets/143448937/9c040ca4-e67b-471f-9271-3f560d585562">
    Scroll down on the screen to answer any questions you might have about what AQI is.
  
- Enter a new location:
    <img width="769" alt="Screenshot 2023-12-04 at 2 31 35 PM" src="https://github.com/analiesegale/AirQuality-Map_HCI584/assets/143448937/18255f5b-6270-400c-b64d-336416afaa0b">
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
