from django.db import models
from users.models import Agent, Student

class Conversation(models.Model):
    """
    Represents a conversation between a student and an agent.

    Attributes:
        student (Student): The student participating in the conversation.
        agent (Agent): The agent in charge of the hostel participating in the conversation.
        subject (str): The subject of the conversation.
        timestamp (DateTime): The timestamp when the conversation was initiated.
        is_read (bool): Indicates whether the conversation has been read by the recipient.
        is_archived (bool): Indicates whether the conversation has been archived by either party.
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="agents")
    subject = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the Conversation object.

        Returns:
            str: A string representing the Conversation object.
        """
        return f"Conversation between {self.student.email} and {self.agent.email}"

class ConversationMessage(models.Model):
    ...
