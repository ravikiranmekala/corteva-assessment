# Corteva Assessment

## Steps to Setup and Run the Application

1. **Clone the Repository**

2. **Install Python and Pip**
   - Install Python 3.12.3 and pip.

3. **Create a Virtual Environment and Install Requirements**
   - Create a virtual environment.
   - Use `requirements.txt` to install all the requirements:
     ```sh
     pip install -r requirements.txt
     ```

4. **Set Up PostgreSQL Database**
   - Set up a PostgreSQL database.
   - Update the configurations in the `weather/settings.py` file's `DATABASES` variable.

5. **Create and Apply Migrations**
   - Run the following commands:
     ```sh
     python manage.py makemigrations weather
     python manage.py migrate
     ```

6. **Upload Data from Text Files**
   - Use the following Django command to upload the data:
     ```sh
     python manage.py upload_weather_data
     ```

7. **Calculate and Upload Weather Statistics**
   - Use the following Django command:
     ```sh
     python manage.py calculate_weather_statistics
     ```
   - `upload_weather_data.py` and `calculate_weather_statistics.py` are present in the `weather/management/commands` directory.
   - The directory containing the text files is `weather/management/commands/wx_data`.

8. **Start the Server**
   - Run the server with:
     ```sh
     python manage.py runserver
     ```
   - The server will start at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

9. **Access the APIs**
   - Use the following Swagger API documentation to access the APIs:
     - Weather: `/api/weather` (GET with or without filters)
     - Weather Statistics: `/api/weather/stats` (GET with or without filters)
   - [Swagger API Documentation](https://app.swaggerhub.com/apis/RAVIKIRANKHPUR/Corteva/1.0.0#/)

## Extra Credit - Deployment

- Kindly refer to [Deployment.md](https://github.com/ravikiranmekala/corteva-assessment/blob/main/Deployment.md) for steps and resources related to deploying the application on AWS.
