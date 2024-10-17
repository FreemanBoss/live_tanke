from django.db import models
from users.models import Student

class Payment(models.Model):
    """
    Represents a payment made by a student.

    Attributes:
        amount (Decimal): The amount of the payment.
        payment_date (Date): The date of the payment.
        payment_method (str): The method used for payment.
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        """
        Returns a string representation of the Payment object.

        Returns:
            str: A string representing the Payment object.
        """
        return f"{self.amount}"

