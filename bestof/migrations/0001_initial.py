# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'bestof_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('sort_index', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'bestof', ['Category'])

        # Adding model 'Entry'
        db.create_table(u'bestof_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bestof.Category'])),
            ('sort_index', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'bestof', ['Entry'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'bestof_category')

        # Deleting model 'Entry'
        db.delete_table(u'bestof_entry')


    models = {
        u'bestof.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sort_index': ('django.db.models.fields.IntegerField', [], {})
        },
        u'bestof.entry': {
            'Meta': {'object_name': 'Entry'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bestof.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sort_index': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['bestof']