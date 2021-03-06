# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-07 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
        ('vocabs', '0001_initial'),
        ('idprovider', '0001_initial'),
        ('arche', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('idprovider_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='idprovider.IdProvider')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='ID')),
                ('path', models.CharField(blank=True, max_length=300, verbose_name='Dateipfad')),
                ('filename', models.CharField(blank=True, max_length=300, verbose_name='Dateiname')),
                ('entry_order', models.CharField(blank=True, max_length=300, verbose_name='Ordnungskriterium/Eingabe')),
                ('date_analogue', models.CharField(blank=True, max_length=300, verbose_name='Analoges Datum')),
                ('date_digitization', models.DateField(blank=True, null=True, verbose_name='Datum der Digitalisierung')),
                ('note', models.TextField(blank=True, verbose_name='Anmerkung')),
                ('content', models.TextField(blank=True, verbose_name='Inhalt')),
                ('combination', models.CharField(blank=True, max_length=300, verbose_name='Kombination')),
                ('location_id', models.CharField(blank=True, max_length=300, verbose_name='Fundnummer in FDB')),
                ('location_digitized_object', models.CharField(blank=True, max_length=300, verbose_name='Aufbewahrung Datei')),
                ('location_analogue', models.CharField(blank=True, max_length=300, verbose_name='Standort analog')),
                ('filesize', models.FloatField(blank=True, null=True, verbose_name='Dateigröße KB')),
                ('amendments', models.TextField(blank=True, verbose_name='Ergänzungen')),
                ('analogue_format', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='analogue_format', to='vocabs.SkosConcept', verbose_name='Analoges Format')),
                ('author', models.ManyToManyField(blank=True, related_name='author', to='places.Person', verbose_name='Autor')),
                ('curator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Person', verbose_name='Bearbeiter Digitalisierung')),
                ('digital_format', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='digital_format', to='vocabs.SkosConcept', verbose_name='Speicherformat')),
                ('in_collection', models.ForeignKey(blank=True, help_text='Resource is located in collection', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='arche.Collection', verbose_name='acdh:partOf')),
                ('institution', models.ManyToManyField(blank=True, related_name='institution_document', to='places.Institution', verbose_name='Institution')),
                ('medium', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medium', to='vocabs.SkosConcept', verbose_name='Medium')),
                ('place_digizization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_digizization', to='places.Institution', verbose_name='Ort der Digitalisierung')),
                ('place_of_origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Place', verbose_name='KG/Areal')),
                ('topic_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_group', to='vocabs.SkosConcept', verbose_name='Gruppe')),
            ],
            bases=('idprovider.idprovider',),
        ),
    ]
