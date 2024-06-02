# Corteva Assessment

## Steps to Set Up and Run the Project

1. **Clone the repository**

2. **Install Python and pip**
   - Ensure Python 3.12.3 and pip are installed on your machine.

3. **Create a virtual environment**
   - Use `requirements.txt` to install all the necessary packages:

     ```sh
     pip install -r requirements.txt
     ```

4. **Set up PostgreSQL database**
   - Configure the database settings in `weather/settings.py` by updating the `DATABASES` variable.

5. **Create and apply migrations**
   - Run the following commands to set up the database schema:

     ```sh
     python manage.py makemigrations weather
     python manage.py migrate
     ```

6. **Upload data from text files**
   - Use the following Django command to upload data:

     ```sh
     python manage.py upload_weather_data
     ```

7. **Calculate and upload weather statistics**
   - Run the following command:

     ```sh
     python manage.py calculate_weather_statistics
     ```

   - Note: `upload_weather_data.py` and `calculate_weather_statistics.py` are located in the `weather/management/commands` directory.
   - The directory containing the text files is `weather/management/commands/wx_data`.

8. **Start the server**
   - Run the server with the following command:

     ```sh
     python manage.py runserver
     ```

   - The server will start at `http://127.0.0.1:8000/`.

## API Documentation

Use the following Swagger API documentation to access the APIs:

1. **Weather API**: `GET /api/weather` (with or without filters)
2. **Weather Statistics API**: `GET /api/weather/stats` (with or without filters)

API Documentation: [SwaggerHub - Corteva API](https://app.swaggerhub.com/apis/RAVIKIRANKHPUR/Corteva/1.0.0#/)

