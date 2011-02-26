# -*- coding: utf-8 -*-
#
# namcap rules - kdeprograms
# Copyright (C) 2011 Rémy Oudompheng <remy@archlinux.org>
# 
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA
# 

from Namcap.ruleclass import *

class package(TarballRule):
	name = "kdeprograms"
	description = "Checks that KDE programs have kdebase-runtime as a dependency"
	def analyze(self, pkginfo, tar):
		if "depends" in pkginfo and 'kdelibs' in pkginfo["depends"]:
			binaries = [ f.name for f in tar
					if f.name.startswith("usr/bin") and f.isfile() ]
			if len(binaries) > 0:
				self.warnings.append(("kdebase-runtime-missing-dep %s", binaries))

# vim: set ts=4 sw=4 noet:
