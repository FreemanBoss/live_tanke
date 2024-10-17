from itertools import count
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save

class User(AbstractUser):
    """
    Custom user model for authentication.

    Attributes:
        email (str): The email address of the user.
        username (str): The username of the user.
        role (str): The role of the user (Admin, Agent, Student).
    """

    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=100)

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        AGENT = "AGENT", "Agent"
        STUDENT = "STUDENT", "Student"

    base_role = Role.ADMIN

    role = models.CharField(max_length=12, choices=Role.choices)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']

    def save(self, *args, **kwargs):
        """
        Overrides the save method to set the default role for new users.
        """
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the User object.
        """
        return self.email

class AgentManager(BaseUserManager):
    """
    Custom manager for the Agent model.
    """
    def get_queryset(self, *args, **kwargs):
        """
        Overrides the get_queryset method to filter agents.
        """
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.AGENT)

class Agent(User):
    """
    Proxy model for agents.
    """
    base_role = User.Role.AGENT

    agent = AgentManager()

    class Meta:
        proxy = True

def counter(_count=count(1)):
    """
    Generates sequential numbers.
    """
    return next(_count)

@receiver(post_save, sender=Agent)
def create_agent_profile(sender, instance, created, **kwargs):
    """
    Signal to create an agent profile.
    """
    if created and instance.role == "AGENT":
        AgentProfile.objects.create(user=instance, agent_id=counter())

class AgentProfile(models.Model):
    """
    Profile model for agents.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agent_id = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "AgentProfile"
        verbose_name_plural = "AgentProfiles"

    def __str__(self):
        """
        Returns a string representation of the AgentProfile object.
        """
        return f"{self.user.email}"

class StudentManager(BaseUserManager):
    """
    Custom manager for the Student model.
    """
    def get_queryset(self, *args, **kwargs):
        """
        Overrides the get_queryset method to filter students.
        """
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)

class Student(User):
    """
    Proxy model for students.
    """
    base_role = User.Role.STUDENT

    student = StudentManager()

    class Meta:
        proxy = True

@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    """
    Signal to create a student profile.
    """
    if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user=instance, student_id=counter())

class StudentProfile(models.Model):
    """
    Profile model for students
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    @property
    def full_info(self):
        """
        Returns the full information of the student.

        Returns:
            str: The full information of the student.
        """
        return f"{self.user.email} - {self.phone_number}"


    class Meta:
        verbose_name = "StudentProfile"
        verbose_name_plural = "StudentProfiles"

    def __str__(self):
        """
        Returns a string representation of the StudentProfile object.
        """
        return f"{self.user.email}"

