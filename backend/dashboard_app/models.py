from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    """A project board that holds multiple tasks and members."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_boards')
    title = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='boards')

    def __str__(self):
        return self.title


class Task(models.Model):
    """A task assigned to a board with status, priority, and user roles."""

    class Priority(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'

    class Status(models.TextChoices):
        TODO = 'to-do', 'To-do'
        IN_PROGRESS = 'in-progress', 'In progress'
        REVIEW = 'review', 'Review'
        DONE = 'done', 'Done'

    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255) 
    description = models.TextField(default='') 
    due_date = models.DateField()
    priority = models.CharField(max_length=15, choices=Priority.choices)
    status = models.CharField(max_length=15, choices=Status.choices) 

    creator = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_tasks'
    ) 
    assignee = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_tasks'
    ) 
    reviewer = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name='review_tasks'
    ) 

    def __str__(self):
        return f"{self.title} ({self.board.title})"


class Comment(models.Model):
    """A comment linked to a task, authored by a user."""

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.title}"