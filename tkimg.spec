#
# spec file for package tkimg
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           tkimg
BuildRequires:  tcllib
BuildRequires:  tk-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXft-devel
Url:            http://sourceforge.net/projects/tkimg
Summary:        More Image Formats for Tk
License:        BSD-3-Clause
Group:          Development/Libraries/Tcl
Version:        1.4.7
Release:        0
Source0:        %{name}%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains a collection of image format handlers for the Tk
photo image type, and a new image type, pixmaps.

The provided format handlers include bmp, gif, ico, jpeg, pcx, png,
ppm, ps, sgi, sun, tga, tiff, xbm, and xpm.

%package devel
Summary:        Header Files and C API Documentation for tkimg
Group:          Development/Libraries/Tcl

%description devel
Files needed to compile/link C code against tkimg.

%prep
%setup -q -n Img-Source-%{version}

%build
%configure \
        --libdir=%tcl_archdir \
        --with-tcl=%_libdir \
        --with-tk=%_libdir
make
chmod a-x ANNOUNCE ChangeLog README Reorganization.Notes.txt
chmod a-x changes license.terms doc/*.htm

#%check
#make test

%install
%makeinstall INSTALL_ROOT=%buildroot
chmod a-x %buildroot%tcl_archdir/*/*.a

%files
%defattr(-,root,root,-)
%doc ANNOUNCE ChangeLog README Reorganization.Notes.txt
%doc changes license.terms doc/*.htm
%doc %_mandir/*/*
%tcl_archdir/*
%exclude %tcl_archdir/*/*.a

%files devel
%defattr(-,root,root,-)
%_includedir/*
%tcl_archdir/*/*.a

%changelog

