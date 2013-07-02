__author__ = 'harshit'


from django.db import models
from django.contrib.auth.models import User
import datetime


class BasicCofigurationFields( models.Model ):
    name = models.CharField( max_length = 250 )
    slug = models.SlugField( default = '', max_length = 100 )
    created_date = models.DateTimeField( default = datetime.datetime.now(), auto_now_add = True )
    modified_date = models.DateTimeField( default = datetime.datetime.now(), auto_now = True )
    display_flag = models.BooleanField( default = True )

    objects = models.Manager()
    #live = LiveEntryManager()
    #detail = DetailManager()

    class Meta:
        abstract = True


class City( BasicCofigurationFields ):

    country = models.ForeignKey( 'Country' )
    region = models.ManyToManyField( 'Region', through = 'RegionCity' )
    state = models.ForeignKey( 'State' )

    objects = models.Manager()
    #master_manager = MasterManager()

    def __unicode__( self ):
        return self.name

    class Meta:
        unique_together = ( 'country', 'slug' )
        ordering = ['name']

class Area( BasicCofigurationFields ):
    city = models.ForeignKey( City)

    objects = models.Manager()

    class Meta:
        verbose_name = 'City Area'

    def __unicode__( self ):
        return self.name + '-' + self.city.name


class Locality( BasicCofigurationFields ):
    area = models.ManyToManyField( Area ,through = 'LocalityArea')

    objects = models.Manager()

    def __unicode__( self ):
        return self.name

    class Meta:
        verbose_name = 'City Locality'
        ordering = ['name']



class LocalityArea(models.Model):
    city_id = models.ForeignKey(Locality)
    area_id = models.ForeignKey(Area)

class Region( BasicCofigurationFields ):
    """ Stores all the Region Details . Region to Country, State Mapping. """

    state = models.ManyToManyField( 'State', through = 'RegionState', null = True, blank = True )
    country = models.ForeignKey( 'Country' )

    def __unicode__( self ):
        return self.name

    class Meta:
        unique_together = ( 'country', 'slug' )



class State( BasicCofigurationFields ):

    country = models.ForeignKey( 'Country' )

    objects = models.Manager()
    #master_manager = MasterManager()

    def __unicode__( self ):
        return self.name
    class Meta:
        unique_together = ( 'country', 'slug' )
        ordering = ['name']

class RegionState( models.Model ):
    region = models.ForeignKey( Region )
    state = models.ForeignKey( State )

    def __unicode__( self ):
        return self.region.name + '-' + self.state.name

    class Meta:
        unique_together = ( 'region', 'state' )

class RegionCity( models.Model ):
    region = models.ForeignKey( Region )
    city = models.ForeignKey( City )

    def __unicode__( self ):
        return self.region.name + '-' + self.city.name

    class Meta:
        unique_together = ( 'region', 'city' )

class Country( BasicCofigurationFields ):

    objects = models.Manager()
    #master_manager = MasterManager()

    def __unicode__( self ):
        return self.name

class PinCode( models.Model ):

    pin_code = models.IntegerField( max_length = 6 )
    display_flag = models.BooleanField( default = True )
    city = models.ForeignKey( City )

    objects = models.Manager()
    #master_manager = MasterManager()

    def __unicode__( self ):
        return str( self.pin_code )

