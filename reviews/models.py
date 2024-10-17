from django.db import models
from users.models import Student
from hostels.models import Hostel

class Review(models.Model):
    """
    Represents a review written by a student for a hostel.

    Attributes:
        student (Student): The student who wrote the review.
        hostel (Hostel): The hostel being reviewed.
        rating (int): The rating given to the hostel.
        review (str): The content of the review.
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the Review object.

        Returns:
            str: A string representing the Review object.
        """
        return f"{self.student.name} - {self.hostel.name}"

class Complaint(models.Model):
    """
    Represents a complaint made by a student.

    Attributes:
        complaint (str): The content of the complaint.
        resolved (bool): Indicates whether the complaint is resolved or not.
    """

    complaint = models.TextField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the Complaint object.

        Returns:
            str: A string representing the Complaint object.
        """
        return f"{self.complaint}"

    def resolve(self):
        """
        Method to resolve the complaint.

        Returns:
            bool: True if the complaint is resolved, False otherwise.
        """
        return not self.resolved

