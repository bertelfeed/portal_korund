from django.db import models

"""
Make use of Django Admin, its powerful:

setup some __str__ methods
See more: https://docs.djangoproject.com/en/5.0/ref/models/instances/#str

setup some metadata (minimum of get_latest_by, ordering, verbose_name_plural, etc...)
See more: https://docs.djangoproject.com/en/5.0/ref/models/options/

Utilize verbose_name on fields
See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#verbose-name

Use field validators
See more: https://docs.djangoproject.com/en/5.0/ref/validators/
"""


class Topic(models.Model):
    # Maybe it's best not to overload the titles?
    # use name & description instead topic_name & topic_description
    topic_name = models.CharField(max_length=255)
    topic_description = models.TextField()

class Employee(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    # Use Django CharField choices
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
    employment_status = models.CharField(max_length=50, default='активный')
    # number as CharField?
    employee_number = models.CharField(max_length=50)
    # Use Django CharField choices
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
    role = models.CharField(max_length=50)
    # Email max length is 254 symbols
    # Source: https://stackoverflow.com/questions/386294/what-is-the-maximum-length-of-a-valid-email-address
    email = models.EmailField(max_length=100)
    additional_info = models.TextField(blank=True, null=True)
    # Use django ImageField instead of CharField for images.
    # Source: https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ImageField 
    photo = models.ImageField(default="media/default.png", blank=False, null=False, upload_to="media/")
    birth_date = models.DateField(blank=True, null=True)
    hire_date = models.DateField()
    termination_date = models.DateField(blank=True, null=True)

class Phone(models.Model):
    # Add regex validator
    # https://docs.djangoproject.com/en/5.0/ref/validators/
    phone_number = models.CharField(max_length=20)
    # Use Django CharField choices
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
    phone_type = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    # Use Django CharField choices
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
    status = models.CharField(max_length=50, default='черновик')
    show_author = models.BooleanField(default=False)

    # Add crated_at field
    # created_at = models.DateTimeField(auto_now_add=True)
    # Source: https://stackoverflow.com/questions/3429878/automatic-creation-date-for-django-model-form-objects

class File(models.Model):
    # ???
    # Check out Django FileField
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#filefield
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

class Chat(models.Model):
    chat_name = models.CharField(max_length=255)
    creation_time = models.DateTimeField(auto_now_add=True)
    
    # Wouldn't it be better to use django manyToMany field?
    # For example: participants = models.ManyToManyField(ChatParticipant)

class ChatParticipant(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    message_content = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)

    # Never use CharField on files, use Django FileField with validation instead
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#filefield
    attached_file = models.CharField(max_length=255, blank=True, null=True)

class Education(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    # Use Django CharField choices
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    # Use Django DateField
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.DateField
    graduation_year = models.IntegerField()

class ActivityLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # Utilize some common states instead of plain text?
    activity = models.TextField()
    activity_time = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    notification_text = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    # Use Django CharField choices
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
    status = models.CharField(max_length=50, default='непрочитано')

class Event(models.Model):
    # Use standartized field names
    # event_name --> name, event_description --> description
    event_name = models.CharField(max_length=255)
    event_description = models.TextField(blank=True, null=True)
    # Add auto_now_add
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#datefield
    start_time = models.DateTimeField()
    # Add future date validation
    # https://docs.djangoproject.com/en/5.0/ref/validators/
    end_time = models.DateTimeField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # ???
    # Use Django ManyToManyField
    # See more: https://docs.djangoproject.com/en/5.0/topics/db/examples/many_to_many/
    participant_list = models.TextField(blank=True, null=True)  # Можно использовать JSONField в Django 3.1+

class Project(models.Model):
    # Use standartized field names
    # project_name --> name, project_description --> description
    project_name = models.CharField(max_length=255)
    project_description = models.TextField(blank=True, null=True)
    # Add auto_now_add
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#datefield
    start_date = models.DateField()
    # Add future date validation
    # https://docs.djangoproject.com/en/5.0/ref/validators/
    end_date = models.DateField(blank=True, null=True)
    # Use Django CharField choices
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
    project_status = models.CharField(max_length=50, default='активный')
    project_leader = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='led_projects')

class Task(models.Model):
    # Use standartized field names
    # task_name --> name, task_description --> description
    task_name = models.CharField(max_length=255)
    task_description = models.TextField(blank=True, null=True)
    # Add auto_now_add
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#datefield
    start_date = models.DateField()
    # Add future date validation
    # https://docs.djangoproject.com/en/5.0/ref/validators/
    end_date = models.DateField(blank=True, null=True)
    # Use Django CharField choices
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
    task_status = models.CharField(max_length=50, default='в процессе')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')

class DocumentArchive(models.Model):
    # Totally bad idea of storing files
    # Make some `Attachment` model with Django FileField on it and use Foreign key on that model
    document_name = models.CharField(max_length=255)
    document_path = models.CharField(max_length=255)
    document_type = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # Add auto_now_add
    # See more: https://docs.djangoproject.com/en/5.0/ref/models/fields/#datefield
    upload_date = models.DateField()
