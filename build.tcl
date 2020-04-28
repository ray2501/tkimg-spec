#!/usr/bin/tclsh

set arch "x86_64"
set base "tkimg1.4.10"
set fileurl "https://sourceforge.net/projects/tkimg/files/tkimg/1.4/tkimg%201.4.10/Img-1.4.10-Source.tar.gz"

set var [list wget $fileurl -O $base.tar.gz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tkimg.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete $base.tar.gz
