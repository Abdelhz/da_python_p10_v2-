from django.db import models
from users.models import CustomUser

class Project(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('back-end', 'Back-end'),
        ('front-end', 'Front-end'),
        ('android', 'Android'),
        ('ios', 'IOS'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    contributors = models.ManyToManyField(CustomUser, through='Contributor', related_name='contributed_projects')
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES)
    project_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='authored_projects')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True) 

    class Meta:
        permissions = [
            #("view_project", "Can view project"),
            #("edit_project", "Can edit project"),
            #("edit_project", "Can edit project"),
            # i can add more permissions as needed
        ]
        

class Contributor(models.Model):
    PERMISSION_CHOICES = [
        ('can_view', 'Can_View'),
        ('can_edit', 'Can_Edit'),
        ('can_delete', 'Can_Delete'),
        # add more permissions as needed
        # permissions needs to be well defined later on
    ]
    role_choices = [
        ('author', 'Author'),
        ('contributor', 'Contributor'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_given_permission = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=role_choices, default='contributor')
    permission = models.CharField(max_length=20, choices=PERMISSION_CHOICES)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True) 