# -*- coding: utf-8 -*-

__version__ = "0.3.0"

from .storedobject import StoredObject
from .ext.odmflask import FlaskStoredObject

from .query.querydialect import DefaultQueryDialect as Q
