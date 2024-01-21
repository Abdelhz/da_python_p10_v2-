from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    contributors = models.ManyToManyField(CustomUser, through='Contributor')
    type = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("view_project", "Can view project"),
            ("edit_project", "Can edit project"),
            # i can add more permissions as needed
        ]

class Contributor(models.Model):
    PERMISSION_CHOICES = [
        ('view', 'View'),
        ('edit', 'Edit'),
        # i can add more permissions as needed
    ]    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_given_permission = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=200)
    # i can add any additional attributes for contributors here
    permission = models.CharField(max_length=4, choices=PERMISSION_CHOICES)


class Issue(models.Model):
    STATUS_CHOICES = [
            ('open', 'Open'),
            ('closed', 'Closed'),
            # add more statuses as needed
        ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    tag = models.CharField(max_length=200)
    # you might also want fields to track the status of the issue, priority, etc.
    priority = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, related_name='created_issues', on_delete=models.CASCADE)
    assignee = models.ForeignKey(CustomUser, related_name='assigned_issues', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)   
    status = models.CharField(max_length=6, choices=STATUS_CHOICES)

    class Meta:
        permissions = [
            ("view_issue", "Can view issue"),
            ("edit_issue", "Can edit issue"),
            # add more permissions as needed
        ]

class Comment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    # you might also want a field to track when the comment was created
    class Meta:
        permissions = [
            ("view_comment", "Can view comment"),
            ("edit_comment", "Can edit comment"),
            # add more permissions as needed
        ]