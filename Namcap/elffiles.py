#
# namcap rules - elffiles
# Copyright (C) 2009 Hugo Doria <hugo@archlinux.org>
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
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

import os
from Namcap.util import is_elf, clean_filename

# Valid directories for ELF files
valid_dirs = ['bin/', 'sbin/', 'usr/bin/', 'usr/sbin/', 'lib/',
		'usr/lib/', 'usr/lib32/']

class package:
	def short_name(self):
		return "elffiles"
	def long_name(self):
		return "Check about ELF files outside some standard paths."
	def prereq(self):
		return "tar"
	def analyze(self, pkginfo, tar):
		ret = [[], [], []]
		invalid_elffiles = []

		for entry in tar:
			# is it a regular file ?
			if not entry.isfile():
				continue
			# is it outside standard binary dirs ?
			is_outside_std_dirs = True
			for d in valid_dirs:
				if entry.name.startswith(d):
					is_outside_std_dirs = False
					break
			if not is_outside_std_dirs:
				continue
			# is it an ELF file ?
			f = tar.extractfile(entry)
			if f.read(4) == b"\x7fELF":
				invalid_elffiles.append(entry.name)

		ret[0] = [("elffile-not-in-allowed-dirs %s", i)
				for i in invalid_elffiles]
		return ret

	def type(self):
		return "tarball"

# vim: set ts=4 sw=4 noet:
