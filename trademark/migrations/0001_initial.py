# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Brand'
        db.create_table(u'trademark_brand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trademark', self.gf('django.db.models.fields.related.ForeignKey')(related_name='brands', to=orm['trademark.Trademark'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('oscar.models.fields.autoslugfield.AutoSlugField')(allow_duplicates=False, max_length=100, separator=u'-', blank=True, unique=True, populate_from='name', overwrite=False)),
            ('formula', self.gf('trademark.models.fields.FormulaField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'trademark', ['Brand'])

        # Adding M2M table for field product_class on 'Brand'
        m2m_table_name = db.shorten_name(u'trademark_brand_product_class')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('brand', models.ForeignKey(orm[u'trademark.brand'], null=False)),
            ('productclass', models.ForeignKey(orm[u'catalogue.productclass'], null=False))
        ))
        db.create_unique(m2m_table_name, ['brand_id', 'productclass_id'])

        # Adding model 'Trademark'
        db.create_table(u'trademark_trademark', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('oscar.models.fields.autoslugfield.AutoSlugField')(allow_duplicates=False, max_length=100, separator=u'-', blank=True, unique=True, populate_from='name', overwrite=False)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['address.Country'])),
        ))
        db.send_create_signal(u'trademark', ['Trademark'])


    def backwards(self, orm):
        # Deleting model 'Brand'
        db.delete_table(u'trademark_brand')

        # Removing M2M table for field product_class on 'Brand'
        db.delete_table(db.shorten_name(u'trademark_brand_product_class'))

        # Deleting model 'Trademark'
        db.delete_table(u'trademark_trademark')


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
        u'catalogue.option': {
            'Meta': {'object_name': 'Option'},
            'code': ('oscar.models.fields.autoslugfield.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '128', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Required'", 'max_length': '128'})
        },
        u'catalogue.productclass': {
            'Meta': {'ordering': "['name']", 'object_name': 'ProductClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'options': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalogue.Option']", 'symmetrical': 'False', 'blank': 'True'}),
            'requires_shipping': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('oscar.models.fields.autoslugfield.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '128', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'}),
            'track_stock': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'trademark.brand': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Brand'},
            'formula': ('trademark.models.fields.FormulaField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'product_class': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'brands'", 'symmetrical': 'False', 'to': u"orm['catalogue.ProductClass']"}),
            'slug': ('oscar.models.fields.autoslugfield.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '100', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'}),
            'trademark': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'brands'", 'to': u"orm['trademark.Trademark']"})
        },
        u'trademark.trademark': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Trademark'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['address.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('oscar.models.fields.autoslugfield.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '100', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'})
        }
    }

    complete_apps = ['trademark']