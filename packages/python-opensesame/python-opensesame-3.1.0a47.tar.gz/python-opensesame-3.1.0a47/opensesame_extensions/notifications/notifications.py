# -*- coding: utf-8 -*-
"""
@author: Daniel Schreij

This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

This module is distributed under the Apache v2.0 License.
You should have received a copy of the Apache v2.0 License
along with this module. If not, see <http://www.apache.org/licenses/>.
"""

import QNotifications
from libopensesame.py3compat import *
from libqtopensesame.extensions import base_extension
import time

__author__ = u"Daniel Schreij"
__license__ = u"GPLv3"

class notifications(base_extension):

	def event_startup(self):
		self.old_notifications = {}
		self.expiration_time = 60 # a minute

		self.notification_area = QNotifications.QNotificationArea(
			self.tabwidget, useGlobalCSS=True)
		self.notification_area.move(0,15)
		self.notification_area.setEntryEffect(u'fadeIn', 200)
		self.notification_area.setExitEffect(u'fadeOut', 200)

	def event_notify(self, message, category='primary', timeout=5000,
		always_show=False, buttontext=None):
		""" Show a notification 'message' in the style 'notification type' for
		'timeout' milliseconds (where 0 milliseconds displays the notification
		indefinitely, until the user removes it)."""
		current_time = time.time()

		# See if notification has been shown before. If it is within
		# self.expiration_time, don't show it again.
		if not always_show:
			if (message, category, timeout) in self.old_notifications:
				prev_time = self.old_notifications[(message, category, timeout)]
				if current_time - prev_time < self.expiration_time:
					return
			# Add notification to old notifications list.
			self.old_notifications[(message, category, timeout, buttontext)] = current_time
		self.notification_area.display(message, category, timeout, buttontext)
