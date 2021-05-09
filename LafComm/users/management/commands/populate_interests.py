from django.core.management.base import BaseCommand
from users.models import User, NewsletterSection
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
        interest_count = len(NewsletterSection.objects.all())
        print(interest_count)

        for row in csv_reader:
            if skipHeaderRow:
                skipHeaderRow = False
                continue

            user_object = User.objects.get(email=row[0])

            for i in range(11, 11+interest_count+1):
                interest = row[i].strip()
                print(interest)
                if interest is not None and interest != '':
                    try:
                        interest_object = NewsletterSection.objects.get(section_name=interest)
                        user_object.interest_newsletter.add(interest_object)
                    except:
                        print(interest + " not in DB")
                        continue

            user_object.save()
            count += 1
