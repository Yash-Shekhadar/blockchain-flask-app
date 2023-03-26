# Blockchain-flask-app
Flask app for dataset interaction and mock API creation. As of now, it has 3 functional APIs:
The APIs have been hosted over Google Cloud's App Engine.

### Following are the API functinoalities and their demo URLs

1. Check the ship's existence (https://civic-genre-325102.ue.r.appspot.com/data/1)
2. Check if the ship has been involved in illegal encountering activity (https://civic-genre-325102.ue.r.appspot.com/encounter/1/06-14-22%2002:01:00/10-27-22%2000:00:00)
3. Check if the ship is fishing in illegal waters (https://civic-genre-325102.ue.r.appspot.com/location/1/13.5/14.67)

### Instructions to run the code on localhost

1. Open command prompt/terminal
2. Navigate to project's directory
3. Execute the command: **python main.py**
4. The app will be hosted on localhost
5. You can use following demo URLs to check the functioning of the APIs on **local system**

  - API 1: http://127.0.0.1:8080/data/1
  - API 2: http://127.0.0.1:8080/encounter/1/06-14-22%2002:01:00/10-27-22%2000:00:00
  - API 3: http://127.0.0.1:8080/location/1/13.5/14.67
  
(Note: These URLs are to test the functioning of the API on localhost. The APIs are also hosted over the internet. Refer to the links in previous section for the same)
