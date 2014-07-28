# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Brand'
        db.create_table(u'brand_brand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('oscar.models.fields.autoslugfield.AutoSlugField')(allow_duplicates=False, max_length=100, separator=u'-', blank=True, unique=True, populate_from='name', overwrite=False)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('formula', self.gf('brand.models.fields.FormulaField')(max_length=100, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['address.Country'])),
        ))
        db.send_create_signal(u'brand', ['Brand'])


    def backwards(self, orm):
        # Deleting model 'Brand'
        db.delete_table(u'brand_brand')


    models = {
        u'address.country': {
            'Meta': {'ordering': "('-display_order', 'printable_name')", 'object_name': 'Country'},
            'display_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'is_shipping_country': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'iso_3166_1_a2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'iso_3166_1_a3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'iso_3166_1_numeric': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'printable_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'brand.brand': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Brand'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['address.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'formula': ('brand.models.fields.FormulaField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('oscar.models.fields.autoslugfield.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '100', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'})
        }
    }

    complete_apps = ['brand']