# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       forms
Date Created:   2015-12-12 18:46
Description:

"""

from django import forms
from django.forms.forms import DeclarativeFieldsMetaclass
from django.contrib.admin.helpers import AdminForm

import six


class DuckQuerySet(object):
    def __init__(self, duck_from, request):
        self.duck_from = duck_from
        self.request = request

    def count(self):
        return self.duck_from.get_count(self.request)

    def _clone(self):
        return self.duck_from.get_data(self.request)

    def __len__(self):
        return self.count()

    def __getitem__(self, item):
        if isinstance(item, int):
            return None

        if isinstance(item, slice):
            return self.duck_from.get_data(self.request, item.start, item.stop)


class DuckManager(object):
    def __init__(self, duck_form):
        self.duck_from = duck_form

    def get_queryset(self, request):
        return DuckQuerySet(self.duck_from, request)


class DuckMeta(object):
    class PK(object):
        def __init__(self, name):
            self.attname = name

    def __init__(self):
        self.meta = {
            'virtual_fields': [],
            'concrete_fields': [],
            'fields': [],
            'many_to_many': [],
            'swapped': False,
            'abstract': False,
            'ordering': []
        }

        self.form_cls = None

    def form_class_attr(self, key):
        return getattr(self.form_cls, key)

    def __getattr__(self, item):
        if item == 'pk':
            pk_name = self.form_class_attr('pk_name')
            return self.PK(pk_name)

        if item == 'verbose_name_plural':
            return self.form_class_attr('verbose_name')

        try:
            return self.meta[item]
        except KeyError:
            return self.form_class_attr(item)


class DuckMetaclass(type):
    def __new__(mcs, name, bases, attributes):
        _meta = DuckMeta()
        attributes['_meta'] = _meta
        cls = type.__new__(mcs, name, bases, attributes)
        _meta.form_cls = cls

        return cls


class DuckCombinedMetaclass(DeclarativeFieldsMetaclass, DuckMetaclass):
    pass


class DuckForm(six.with_metaclass(DuckCombinedMetaclass, forms.Form)):
    class DoesNotExist(Exception):
        pass

    app_label = None  # app will exist under
    model_name = None  # link url
    verbose_name = None  # name displayed in admin site
    object_name = None
    pk_name = None  # pk name

    _deferred = False
    _default_manager = None

    @classmethod
    def _prepare(cls):
        if not cls._default_manager:
            cls._default_manager = DuckManager(cls)

    def as_adminform(self):
        fieldsets = [(None, {'fields': self.fields.keys()})]
        return AdminForm(self, fieldsets, {})

    @classmethod
    def get_count(cls, request):
        """
        Get Total Count of dataset
        """
        raise NotImplementedError()

    @classmethod
    def get_data(cls, request, start=None, stop=None):
        """
        Data for the admin site to display.
        Data is a list, contains dict. dict keys are fields defined in form
        """
        raise NotImplementedError()

    @classmethod
    def get_data_by_pk(cls, request, pk):
        """
        Get Data by pk
        """
        raise NotImplementedError()

    @classmethod
    def create_data(cls, request, data):
        """
        Create new data.
        parameter data is a dict, keys are defined in form
        """
        raise NotImplementedError()

    @classmethod
    def update_data(cls, request, data):
        """
        Update data.
        parameter data is a dict, keys are defined in form
        """
        raise NotImplementedError()
