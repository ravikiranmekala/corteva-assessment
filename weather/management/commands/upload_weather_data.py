import os
import datetime
import time
import concurrent.futures
from django.core.management.base import BaseCommand, CommandError
from weather.models import Weather


class Command(BaseCommand):
    help = 'Upload weather data from files in a specified directory'

    def handle(self, *args, **kwargs):
        # Hardcoded directory relative to the location of this script
        base_dir = os.path.dirname(__file__)
        directory = os.path.join(base_dir,
                                 'wx_data')  # Assuming the files are in a folder named 'wx_data' within the same directory

        if not os.path.exists(directory):
            raise CommandError(f"The directory {directory} does not exist")

        file_paths = [os.path.join(directory, filename) for filename in os.listdir(directory) if
                      os.path.isfile(os.path.join(directory, filename))][:2]

        start_time = time.time()
        total_records = 0

        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            futures = {executor.submit(self.upload_file, file_path): file_path for file_path in file_paths}
            for future in concurrent.futures.as_completed(futures):
                try:
                    records_inserted = future.result()
                    total_records += records_inserted
                except Exception as e:
                    self.stderr.write(f"Error processing file: {futures[future]} - {e}")

        total_time = time.time() - start_time
        self.stdout.write(
            self.style.SUCCESS(f'Successfully uploaded weather data from all files in {total_time:.2f} seconds'))
        self.stdout.write(self.style.SUCCESS(f'Total records inserted: {total_records}'))

    def upload_file(self, file_path):
        station = os.path.splitext(os.path.basename(file_path))[0]
        self.stdout.write(f"Processing file: {file_path} for station: {station}")

        records_inserted = 0
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) != 4:
                    continue

                date_str, max_temp, min_temp, precipitation = parts
                date = datetime.datetime.strptime(date_str, '%Y%m%d').date()

                # Convert -9999 to None, otherwise divide by 10
                max_temp = None if int(max_temp) == -9999 else float(max_temp) / 10
                min_temp = None if int(min_temp) == -9999 else float(min_temp) / 10
                precipitation = None if int(precipitation) == -9999 else float(precipitation) / 10

                weather_data, created = Weather.objects.get_or_create(
                    station=station,
                    date=date,
                    defaults={
                        'maximum_temperature': max_temp,
                        'minimum_temperature': min_temp,
                        'precipitation': precipitation
                    }
                )

                if created:
                    records_inserted += 1

        return records_inserted