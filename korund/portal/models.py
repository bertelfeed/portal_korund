from django.db import models

class Topic(models.Model):
    topic_name = models.CharField(max_length=255)
    topic_description = models.TextField()

class Employee(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    employment_status = models.CharField(max_length=50, default='активный')
    employee_number = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    additional_info = models.TextField(blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    hire_date = models.DateField()
    termination_date = models.DateField(blank=True, null=True)

class Phone(models.Model):
    phone_number = models.CharField(max_length=20)
    phone_type = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    photo = models.CharField(max_length=255, blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='черновик')
    show_author = models.BooleanField(default=False)

class File(models.Model):
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

class Chat(models.Model):
    chat_name = models.CharField(max_length=255)
    creation_time = models.DateTimeField(auto_now_add=True)

class ChatParticipant(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    message_content = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)
    attached_file = models.CharField(max_length=255, blank=True, null=True)

class Education(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    graduation_year = models.IntegerField()

class ActivityLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    activity = models.TextField()
    activity_time = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    notification_text = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='непрочитано')

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    participant_list = models.TextField()

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    project_status = models.CharField(max_length=50, default='активный')
    project_leader = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    task_status = models.CharField(max_length=50, default='в процессе')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class DocumentArchive(models.Model):
    document_name = models.CharField(max_length=255)
    document_path = models.CharField(max_length=255)
    document_type = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    upload_date = models.DateField()
