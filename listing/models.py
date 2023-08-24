from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='room_images/')
    num_people = models.PositiveIntegerField(default=1)
    num_beds = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return f"Image for {self.room.title}"
    
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/',default= '/media')
    price = models.DecimalField(max_digits=10, decimal_places=2,default=100)
    date = models.DateField()
    event_information = models.TextField()

    def __str__(self):
        return self.title

    
class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return f"Image for {self.event.title}"
    
class AboutUsContent(models.Model):
    title = models.CharField(max_length=100)
    mission_statement = models.TextField()
    values = models.TextField()
    image = models.ImageField(upload_to='about_us_images/')  # Add this line for the image

    def __str__(self):
        return self.title
    
