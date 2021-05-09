from django.core.management.base import BaseCommand
from users.models import User, Department
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

            new_user = User(
                email = row[0],
                first_name = row[1],
                last_name = row[2],
                preferred_name = row[3],
                gender = row[4],
                relation_to_college = row[5],
                class_year = row[6]
            )
            
            new_user.save()
            # break
            count += 1
