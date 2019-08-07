from django.db import models


class Building(models.Model):
    building_number = models.IntegerField(primary_key=True, unique=True)
    # room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Room(models.Model):
    room_number = models.CharField(max_length=6)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)


class TimeSlots(models.Model):
    number_of_class = models.IntegerField(primary_key=True)
    time_slot_begin = models.TimeField('time of beginning')
    time_slot_end = models.TimeField('time of ending')


class Teacher(models.Model):
    full_name = models.CharField(max_length=200)


class DayOfWeek(models.Model):
    day_of_week = models.CharField(unique=True, max_length=10)


class ClassName(models.Model):
    class_name = models.CharField(max_length=200)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    number_of_class = models.OneToOneField(TimeSlots, on_delete=models.CASCADE)
    day = models.OneToOneField(DayOfWeek, on_delete=models.CASCADE, default=None)


class Group(models.Model):
    group_number = models.IntegerField(primary_key=True, unique=True)
    class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE)
