#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for tracking models.
"""
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


@admin.register(models.RawDataVersion)
class RawDataVersionAdmin(BaseAdmin):
    """
    Custom admin for the RawDataVersion model.
    """
    list_display = (
        "id",
        "release_datetime",
        "pretty_download_size",
        "pretty_clean_size",
    )
    list_display_links = ('release_datetime',)
    list_filter = ("release_datetime",)


@admin.register(models.RawDataFile)
class RawDataFileAdmin(BaseAdmin):
    """
    Custom admin for the RawDataFile model.
    """
    list_display = (
        "id",
        "version",
        "file_name",
        "download_records_count",
        "clean_records_count",
        "load_records_count",
        "error_count",
        "download_columns_count",
        "clean_columns_count",
        "load_columns_count",
        "pretty_download_file_size",
        "pretty_clean_file_size"
    )
    list_display_links = ('id', 'file_name',)
    list_filter = ("version__release_datetime",)
