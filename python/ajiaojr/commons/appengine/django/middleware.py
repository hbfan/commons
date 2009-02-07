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

from ajiaojr.magpie import models

from google.appengine.api import users

class AddUserToRequestMiddleware(object):
  """
  Django middleware class that adds a user object to the request
  """

  def process_request(self, request):
    request.admin_mode = False
    request.user = None
    
    user = users.get_current_user()
    
    if user:
      request.user = models.ClubUser.find_by_user(user)
    
    if users.is_current_user_admin():
      request.admin_mode = True
