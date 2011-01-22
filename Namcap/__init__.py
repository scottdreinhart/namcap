# 
# namcap rules - __init__
# Copyright (C) 2003-2009 Jason Chu <jason@archlinux.org>
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

__tarball__ = """
  anyelf
  capsnamespkg
  depends
  directoryname
  elffiles
  emptydir
  fhsmanpages
  fhsinfopages
  filenames
  fileownership
  gnomemime
  hardlinks
  hicoloricons
  infodirectory
  libtool
  licensepkg
  lotsofdocs
  mimefiles
  missingbackups
  perllocal
  permissions
  scrollkeeper
  symlink
  urlpkg

""".split()

__pkgbuild__ = """
  arrays
  badbackups
  capsnames
  carch
  checksums
  invalidstartdir
  license
  pkgname
  rpath
  sfurl
  tags
  url

""".split()

__all__ = __tarball__ + __pkgbuild__

# vim: set ts=4 sw=4 noet:
