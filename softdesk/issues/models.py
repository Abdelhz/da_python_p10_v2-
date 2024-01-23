from django.db import models
from users.models import CustomUser
from projects.models import Project


class Issue(models.Model):
    STATUS_CHOICES = [
            ('to-do', 'To-do'),
            ('in-progress', 'In-progress'),
            ('finished', 'Finished'),
            # add more statuses as needed
        ]
    PRIORITY_CHOICES = [
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            # add more priorities as needed
        ]
    TAG_CHOICES = [
            ('bug', 'Bug'),
            ('feature', 'Feature'),
            ('task', 'Task')
            # add more tags as needed
        ]
    # the project the issue belongs to
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # details about the issue, such as title, description, etc.
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Fields tracking the tag of the issue, status, priority.
    tag = models.CharField(max_length=20, choices=TAG_CHOICES, default='task')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to-do')
    # Contributors directly related to the issue (author and assignee)
    issue_author = models.ForeignKey(CustomUser, related_name='created_issues', on_delete=models.CASCADE)
    assignee = models.ForeignKey(CustomUser, related_name='assigned_issues', on_delete=models.CASCADE)
    # date and time of the issue
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True) 

    class Meta:
        permissions = [
            #("view_issue", "Can view issue"),
            #("edit_issue", "Can edit issue"),
            #("edit_issue", "Can edit issue"),
            # add more permissions as needed
        ]

class Comment(models.Model):
    description = models.TextField()
    comment_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    # you might also want a field to track when the comment was created
    class Meta:
        permissions = [
            #("view_comment", "Can view comment"),
            #("edit_comment", "Can edit comment"),
            # add more permissions as needed
        ]
        
