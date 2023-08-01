from django.db import models
from django.db import models


# Create your models here.
class League(models.Model):

    # ATRIBUTOS:
    id_league = models.IntegerField(primary_key=True, db_column='id_league')
    name_league = models.CharField(max_length=100, db_column='name_league')
    link_league = models.CharField(max_length=250, db_column='link_league')
    # "primary_key=True": Determina que la columna << id_league >> es la primary Key de la tabla ya creada en MySql
    # db_column='...': Referencia la columna de la tabla en la db de cada atributo creado dentro del modelo.

    
    # META:
    class Meta:
        db_table = 'leagues'
        # "db_table" referecnia la tabla ya existente en la db en MySql correspondiente al actual modelo
        
        managed = False
        # False: por medio de está definición, django no administra la tabla en la db (no crea la tabla, la elimina ni la modifica)



class Links_leagues(models.Model):
    # ATRIBUTOS
    id_link = models.IntegerField(primary_key=True, db_column='id_link')
    link_league = models.CharField(max_length=150, db_column='link_league')


    # META
    class Meta:
        db_table = 'links_leagues'
        managed = False
