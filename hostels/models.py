from django.db import models

class Hostel(models.Model):
    """
    Represents a hostel in the locality.

    Attributes:
        name (str): The name of the hostel.
        address (str): The address of the hostel.
        capacity (int): The maximum capacity of the hostel.
        description (str): The description of the hostel.
        nickname (str, optional): The nickname of the hostel, defaults to an empty string.

    Methods:
        popular_name (property): Returns the nickname of the hostel if available, otherwise returns the name.
        add_to_capacity: Increases the capacity of the hostel by a given number of apartments.

    """

    name = models.CharField(max_length=100)
    address = models.TextField()
    capacity = models.IntegerField()
    description = models.TextField()
    nickname = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name or self.name

    @property
    def popular_name(self):
        """
        Returns the nickname of the hostel if available, otherwise returns the name.

        Returns:
            str: The popular name of the hostel.
        """
        return self.nickname or self.name

    def add_to_capacity(self, no_of_apartment):
        """
        Increases the capacity of the hostel by a given number of apartments.

        Parameters:
            no_of_apartment (int): The number of apartments to add to the capacity.

        Returns:
            int: The updated capacity of the hostel.
        """
        self.capacity = self.capacity + no_of_apartment
        return self.capacity

class Room(models.Model):
    """
    Represents a room in the hostel.

    Attributes:
        hostel (Hostel): The hostel to which the room belongs.
        room_number (int): The number of the room in the hostel.
        room_type (str): The type of room in the hostel.
        capacity (int): The maximum number of occupants that can live in the room.
        price (Decimal): The price of the room or apartment in the hostel.
        status (bool): The status of the room whether allocated or not.

    Methods:
        allocate: Indicate that the room has been allocated.
        add_discount: Update the actual price of the room by applying a discount.

    """

    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=20)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return f"{self.hostel.name} - Room {self.room_number}"

    def allocate(self):
        """
        Indicate that the room has been allocated.

        Returns:
            bool: The status of the room.
        """
        return not self.status
    
    def add_discount(self, discount_price):
        """
        Update the actual price of the room by applying a discount.

        Parameters:
            discount_price (float): The discount percentage to be applied.

        Returns:
            Decimal: The updated price of the room.
        """
        self.price = self.price * discount_price
        return self.price

