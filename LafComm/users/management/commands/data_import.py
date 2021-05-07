from users.models import User,Department
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        User.objects.from_csv(
            'users/fixtures/final.csv'
            # dict(email="email"),
            # static_mapping = {
            #     'phone': ''
            # }
        )

    # def handle(self, *args, **kwargs):
    #     # Since the CSV headers match the model fields,
    #     # you only need to provide the file's path (or a Python file object)
    #     insert_count = User.objects.from_csv('users/fixtures/test.csv')
    #     # print "{} records inserted".format(insert_count)

# import csv
# from users.models import User,Department,NewsletterSection
# from django.core.management.base import BaseCommand


# class Command(BaseCommand):

#     def load_csv_file(path):
#         with open(path) as file_obj:
#             reader=csv.reader(file_obj)

#             # reader=[["utsav@gmail.com","utsav","shrestha"],["stsav@gmail.com","stsav","ghrestha"]]

#             def handle(self, *args, **kwargs):
#             # Since the CSV headers match the model fields,
#             # you only need to provide the file's path (or a Python file object)
#                 insert_count = Department.objects.from_csv('users/fixtures/majors.csv')
#             # print "{} records inserted".format(insert_count)

#                 for row in reader:
#                     Department.objects.create(
#                         major=row[0],
#                     )

#         # for row in reader:
#         #     User.objects.get_or_create(
#         #         email=row[1],
#         #         first_name=row[2],
#         #         last_name=row[3],
#         #         preferred_name=row[4],
#         #         gender=row[4],
#         #         phone=0,
#         #         relation_to_college=row[5],
#         #         class_year=row[7],
#         #         department=row[8],
#         #         interest_newsletter=row[9],
#         #         rating=5,
#         #     )
        