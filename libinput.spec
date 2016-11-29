#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libinput
Version  : 1.5.2
Release  : 6
URL      : http://www.freedesktop.org/software/libinput/libinput-1.5.2.tar.xz
Source0  : http://www.freedesktop.org/software/libinput/libinput-1.5.2.tar.xz
Summary  : Input device library
Group    : Development/Tools
License  : MIT
Requires: libinput-bin
Requires: libinput-lib
Requires: libinput-doc
BuildRequires : doxygen
BuildRequires : graphviz
BuildRequires : grep
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libevdev)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libunwind)
BuildRequires : pkgconfig(mtdev)
BuildRequires : valgrind

%description
/*!@mainpage
libinput
========
libinput is a library that handles input devices for display servers and other
applications that need to directly deal with input devices.

%package bin
Summary: bin components for the libinput package.
Group: Binaries

%description bin
bin components for the libinput package.


%package dev
Summary: dev components for the libinput package.
Group: Development
Requires: libinput-lib
Requires: libinput-bin
Provides: libinput-devel

%description dev
dev components for the libinput package.


%package doc
Summary: doc components for the libinput package.
Group: Documentation

%description doc
doc components for the libinput package.


%package lib
Summary: lib components for the libinput package.
Group: Libraries

%description lib
lib components for the libinput package.


%prep
%setup -q -n libinput-1.5.2

%build
export LANG=C
%configure --disable-static --disable-libwacom
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/udev/hwdb.d/90-libinput-model-quirks.hwdb
/usr/lib64/udev/libinput-device-group
/usr/lib64/udev/libinput-model-quirks
/usr/lib64/udev/rules.d/80-libinput-device-groups.rules
/usr/lib64/udev/rules.d/90-libinput-model-quirks.rules

%files bin
%defattr(-,root,root,-)
/usr/bin/libinput-debug-events
/usr/bin/libinput-list-devices

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
