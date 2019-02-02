from django.db import models
from django.urls import reverse
import uuid
import datetime as dt
# Create your models here.
class Variable(models.Model):
    name=models.CharField(max_length=20, help_text="Variable name")
    def __str__(self):
        return self.name
class VarType(models.Model):
    TYPES_CH= (
            ('RCM','Regional Climate Model'),
            ('GCM','Global Climate Model'),
            ('OBS','Observational')
            )
    typesdat= models.CharField(
            max_length=3,
            choices=TYPES_CH,
            blank=True,
            default='OBS',
            help_text="Type of data"
            )
    FREQ= (
            ('1hr','Hourly'),
            ('3hr','3hr'),
            ('day','Daily'),
            ('1M','Monthly'),
            ('seas','Seasonaly'),
            ('year','Annual')
            )
    typefreq=models.CharField(
            max_length=4,
            choices=FREQ,
            blank=True,
            default='day',
            help_text="Frequency of data"
            )
    GCMName=models.CharField(max_length=20, \
                                  help_text="Global Climate Model name",\
                                  blank=True)
    RCMName=models.CharField(max_length=20, \
                                  help_text="Regional Climate Model name",\
                                  blank=True)
#    def get_absolute_url(self):
#            """Returns the url to access a particular author instance."""
#            return reverse('vartype-detail', args=[str(self.id)])
    def __str__(self):
            return f'Type of data: {self.typesdat} - Frequency: {self.typefreq} - \
                     GCM: {self.GCMName} - RCM:{self.RCMName}'
class FileData(models.Model):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, \
#                          help_text='Unique ID for the file')
    variable=models.ForeignKey(Variable,on_delete=models.SET_NULL, null=True)
    vartype=models.ForeignKey(VarType,on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=40, help_text="File's name")
    path=models.CharField(max_length=40, help_text="Path's file")
    StartPeriod=models.DateTimeField(default=dt.datetime(9999,12,31))
    EndPeriod=models.DateTimeField(default=dt.datetime(9999,12,31))
    class Meta:
        ordering=['path']
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('datos-detail', args=[str(self.id)])
    def __str__(self):
        return f'{self.path}/{self.name}'
#class DataInstance(models.Model):
#    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, \
#                          help_text='Unique ID for the file')
#    filedata = models.ForeignKey(FileData, on_delete=models.SET_NULL, null=True) 
#    def __str__(self):
#        return f'{self.id} ({self.filedata.path}/{self.filedata.name})'