#!python
#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

if __name__ == u"__main__":

	# First, load a minimum number of modules and show an empty app window. This
	# gives the user the feeling of a snappy response.
	import os, sys
	# Add the folder that contains the OpenSesame modules to the path. This is
	# generally only necessary if OpenSesame is directly run from source,
	# instead from an installation.
	if os.path.exists(os.path.join(os.getcwd(), 'libopensesame')):
		sys.path.insert(0, os.getcwd())
	import libopensesame.misc
	libopensesame.misc.parse_environment_file()
	import libopensesame.experiment
	from libopensesame.py3compat import *
	# Parse the command line options
	options = libopensesame.misc.opensesamerun_options()
	app = None
	# If the command line options haven't provided sufficient information to
	# run right away, present a GUI
	while not libopensesame.misc.opensesamerun_ready(options):
		# If PyQt4 is not available (e.g., this might be the case on Mac OS)
		# give an error instead of showing a GUI. This makes sure that even
		# without PyQt4, people can still run experiments.
		try:
			# Change Qt API
			import sip
			sip.setapi('QString', 2)
			sip.setapi('QVariant', 2)
			from qtpy import QtGui, QtCore, QtWidgets
		except:
			libopensesame.misc.messagebox(u"OpenSesame Run",
				u"Incorrect or missing options.\n\nRun 'opensesame --help' from a terminal (or command prompt) to see a list of available options, or install Python Qt4 to enable the graphical user interface.")
			sys.exit()
		# Create the GUI and show it
		import libqtopensesame.qtopensesamerun
		if app is None:
			app = QtWidgets.QApplication(sys.argv)
			myapp = libqtopensesame.qtopensesamerun.qtopensesamerun(options)
		myapp.show()
		app.exec_()
		# Update the options from the GUI
		options = myapp.options
		# Exit if the GUI was canceled
		if not myapp.run:
			sys.exit()
	# Decode the experiment path and logfile
	experiment = os.path.abspath(options.experiment)
	if isinstance(experiment, str):
		experiment = safe_decode(experiment,
			enc=libopensesame.misc.filesystem_encoding(), errors=u'ignore')
	# experiment_path = os.path.dirname(experiment)
	logfile = options.logfile
	if isinstance(logfile, str):
		logfile = safe_decode(logfile,
			enc=libopensesame.misc.filesystem_encoding(), errors=u'ignore')

	if options.debug:
		# In debug mode, don't try to catch any exceptions
		exp = libopensesame.experiment.experiment(u"Experiment",
			experiment, experiment_path=experiment_path)
		exp.set_subject(options.subject)
		exp.var.fullscreen = options.fullscreen
		exp.logfile = logfile
		exp.run()
		exp.end()
	else:
		# Try to parse the experiment from a file
		experiment_path = safe_decode(os.path.abspath(options.experiment),
			enc=libopensesame.misc.filesystem_encoding())
		try:
			exp = libopensesame.experiment.experiment(u"Experiment",
				experiment, experiment_path=experiment_path)
		except Exception as e:
			libopensesame.misc.messagebox(u"OpenSesame Run",
				libopensesame.misc.strip_tags(e))
			sys.exit()
		# Set some options
		exp.set_subject(options.subject)
		exp.var.fullscreen = options.fullscreen
		exp.logfile = logfile
		# Initialize random number generator
		import random
		random.seed()
		# Try to run the experiment
		try:
			exp.run()
		except Exception as e:
			# Try to nicely end the experiment, even though an exception
			# occurred.
			try:
				exp.end()
			except Exception as f:
				libopensesame.misc.messagebox(u"OpenSesame Run",
					libopensesame.misc.strip_tags(f))
			libopensesame.misc.messagebox(u"OpenSesame Run",
				libopensesame.misc.strip_tags(e))
	libopensesame.experiment.clean_up(exp.debug)
