from users.models import User,Department
from django.core.management.base import BaseCommand
import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **options):
        file_name = options['file']
        csv_file = open(file_name)
        csv_reader = csv.reader(csv_file)

        skipHeaderRow = True
        count = 0
        for row in csv_reader:
            if skipHeaderRow:
                skipHeaderRow = False
                continue

            new_department = Department(
                major = row[0],
            )
            
            new_department.save()
            # break
            count += 1