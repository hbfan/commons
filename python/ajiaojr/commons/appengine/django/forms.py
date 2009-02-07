#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Ajiaojr Commons - Common python classes and functions used through out
#                   Ajiaojr's python code.
#
# Copyright (C) 2009 Qian Qiao <qian.qiao@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django import forms
from django.utils.translation import ugettext as _

from google.appengine.ext import db

class KeyNameInputField(forms.Field):
  default_error_messages = {
      'invalid_input': _(u'Input is invalid'),
    }
  
  def __init__(self, reference_class, *args, **kwds):
    assert issubclass(reference_class, db.Model)
    self.reference_class = reference_class
    
    super(KeyNameInputField, self).__init__(*args, **kwds)
    
  def clean(self, value):
    value = super(KeyNameInputField, self).clean(value)
    if not value:
      return None
    instance = self.reference_class.get_by_key_name(value)
    if instance is None:
      raise db.BadValueError(self.error_messages['invalid_input'])
    return instance
