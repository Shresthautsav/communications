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
            user_object = User.objects.get(email=row[0])
            # print(user_object.class_year)
            print(user_object.email)

            for i in range(7, 11):
                major = row[i].strip()
                print(major)
                if major is not None and major != '':
                    major_object = Department.objects.get(major=major)
                    user_object.department.add(major_object)

            user_object.save()
            # break
            count += 1
