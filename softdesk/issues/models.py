"""
This module defines the data models for this Django app.

It includes models for CustomUser, Project, Contributor, Issue, and Comment.
Each model represents a different aspect of the app, such as users, projects, contributions,
issues, and comments.
"""

from django.db import models
from users.models import CustomUser
from projects.models import Project


class Issue(models.Model):
    """
    Issue model that represents an issue that users can report in a project.

    This model includes fields like title, description, project,issue_author,
    assignee, created_time, and updated_time.

    This model includes fields for status, priority, and tag, each of which has
    a set of predefined choices. The status field can be 'to-do', 'in-progress', or 'finished'.
    The priority field can be 'low', 'medium', or 'high'. The tag field can be 'bug', 'feature',
    or 'task'.
    """
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


class Comment(models.Model):
    """
    Comment model that represents a comment on an issue.

    This model includes fields like description, comment_author, issue, created_time, and updated_time.
    - the issue the comment is on
    - the author of the comment
    - the description of the comment
    - the date and time the comment was created and last updated
    Comment model that represents a comment made by a user on an issue.

    This model includes fields like content, issue, comment_author, created_time, and updated_time.
    """
    description = models.TextField()
    comment_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    # you might also want a field to track when the comment was created
