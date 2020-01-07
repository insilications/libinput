#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : libinput
Version  : 1.15.0
Release  : 56
URL      : https://www.freedesktop.org/software/libinput/libinput-1.15.0.tar.xz
Source0  : https://www.freedesktop.org/software/libinput/libinput-1.15.0.tar.xz
Source1  : https://www.freedesktop.org/software/libinput/libinput-1.15.0.tar.xz.sig
Summary  : Input device management and event handling library
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: libinput-bin = %{version}-%{release}
Requires: libinput-config = %{version}-%{release}
Requires: libinput-data = %{version}-%{release}
Requires: libinput-lib = %{version}-%{release}
Requires: libinput-libexec = %{version}-%{release}
Requires: libinput-license = %{version}-%{release}
Requires: libinput-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : cairo-dev32
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gdk-pixbuf-dev32
BuildRequires : glib-dev32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : graphviz
BuildRequires : graphviz-extras
BuildRequires : pango-dev32
BuildRequires : pkgconfig(32atk)
BuildRequires : pkgconfig(32check)
BuildRequires : pkgconfig(32fribidi)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32gtk+-3.0)
BuildRequires : pkgconfig(32libevdev)
BuildRequires : pkgconfig(32libudev)
BuildRequires : pkgconfig(32mtdev)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(fribidi)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libevdev)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(mtdev)
BuildRequires : python3-dev
BuildRequires : valgrind

%description
libinput
========
libinput is a library that provides a full input stack for display servers
and other applications that need to handle input devices provided by the
kernel.

%package bin
Summary: bin components for the libinput package.
Group: Binaries
Requires: libinput-data = %{version}-%{release}
Requires: libinput-libexec = %{version}-%{release}
Requires: libinput-config = %{version}-%{release}
Requires: libinput-license = %{version}-%{release}

%description bin
bin components for the libinput package.


%package config
Summary: config components for the libinput package.
Group: Default

%description config
config components for the libinput package.


%package data
Summary: data components for the libinput package.
Group: Data

%description data
data components for the libinput package.


%package dev
Summary: dev components for the libinput package.
Group: Development
Requires: libinput-lib = %{version}-%{release}
Requires: libinput-bin = %{version}-%{release}
Requires: libinput-data = %{version}-%{release}
Provides: libinput-devel = %{version}-%{release}
Requires: libinput = %{version}-%{release}
Requires: libinput = %{version}-%{release}

%description dev
dev components for the libinput package.


%package dev32
Summary: dev32 components for the libinput package.
Group: Default
Requires: libinput-lib32 = %{version}-%{release}
Requires: libinput-bin = %{version}-%{release}
Requires: libinput-data = %{version}-%{release}
Requires: libinput-dev = %{version}-%{release}

%description dev32
dev32 components for the libinput package.


%package lib
Summary: lib components for the libinput package.
Group: Libraries
Requires: libinput-data = %{version}-%{release}
Requires: libinput-libexec = %{version}-%{release}
Requires: libinput-license = %{version}-%{release}

%description lib
lib components for the libinput package.


%package lib32
Summary: lib32 components for the libinput package.
Group: Default
Requires: libinput-data = %{version}-%{release}
Requires: libinput-license = %{version}-%{release}

%description lib32
lib32 components for the libinput package.


%package libexec
Summary: libexec components for the libinput package.
Group: Default
Requires: libinput-config = %{version}-%{release}
Requires: libinput-license = %{version}-%{release}

%description libexec
libexec components for the libinput package.


%package license
Summary: license components for the libinput package.
Group: Default

%description license
license components for the libinput package.


%package man
Summary: man components for the libinput package.
Group: Default

%description man
man components for the libinput package.


%prep
%setup -q -n libinput-1.15.0
cd %{_builddir}/libinput-1.15.0
pushd ..
cp -a libinput-1.15.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578417451
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dlibwacom=false -Ddocumentation=false  builddir
ninja -v -C builddir
pushd ../build32
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Dlibwacom=false -Ddocumentation=false  builddir
ninja -v -C builddir
popd

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libinput
cp %{_builddir}/libinput-1.15.0/COPYING %{buildroot}/usr/share/package-licenses/libinput/c015511464588baeb0a5c640848a3f31d1a837b5
cp %{_builddir}/libinput-1.15.0/doc/api/style/LICENSE %{buildroot}/usr/share/package-licenses/libinput/5a48bb048772f9029b604fbdd869d92fddae1cef
pushd ../build32
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
/usr/lib/udev/libinput-device-group
/usr/lib/udev/libinput-fuzz-extract
/usr/lib/udev/libinput-fuzz-to-zero

%files bin
%defattr(-,root,root,-)
/usr/bin/libinput

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/80-libinput-device-groups.rules
/usr/lib/udev/rules.d/90-libinput-fuzz-override.rules

%files data
%defattr(-,root,root,-)
/usr/share/libinput/10-generic-keyboard.quirks
/usr/share/libinput/10-generic-lid.quirks
/usr/share/libinput/10-generic-trackball.quirks
/usr/share/libinput/30-vendor-aiptek.quirks
/usr/share/libinput/30-vendor-alps.quirks
/usr/share/libinput/30-vendor-contour.quirks
/usr/share/libinput/30-vendor-cypress.quirks
/usr/share/libinput/30-vendor-elantech.quirks
/usr/share/libinput/30-vendor-ibm.quirks
/usr/share/libinput/30-vendor-kensington.quirks
/usr/share/libinput/30-vendor-logitech.quirks
/usr/share/libinput/30-vendor-madcatz.quirks
/usr/share/libinput/30-vendor-microsoft.quirks
/usr/share/libinput/30-vendor-razer.quirks
/usr/share/libinput/30-vendor-synaptics.quirks
/usr/share/libinput/30-vendor-vmware.quirks
/usr/share/libinput/30-vendor-wacom.quirks
/usr/share/libinput/50-system-acer.quirks
/usr/share/libinput/50-system-apple.quirks
/usr/share/libinput/50-system-asus.quirks
/usr/share/libinput/50-system-chicony.quirks
/usr/share/libinput/50-system-cyborg.quirks
/usr/share/libinput/50-system-dell.quirks
/usr/share/libinput/50-system-google.quirks
/usr/share/libinput/50-system-hp.quirks
/usr/share/libinput/50-system-lenovo.quirks
/usr/share/libinput/50-system-system76.quirks
/usr/share/libinput/50-system-toshiba.quirks
/usr/share/zsh/site-functions/_libinput

%files dev
%defattr(-,root,root,-)
/usr/include/libinput.h
/usr/lib64/libinput.so
/usr/lib64/pkgconfig/libinput.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libinput.so
/usr/lib32/pkgconfig/32libinput.pc
/usr/lib32/pkgconfig/libinput.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libinput.so.10
/usr/lib64/libinput.so.10.13.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libinput.so.10
/usr/lib32/libinput.so.10.13.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/libinput/libinput-debug-events
/usr/libexec/libinput/libinput-debug-gui
/usr/libexec/libinput/libinput-debug-tablet
/usr/libexec/libinput/libinput-list-devices
/usr/libexec/libinput/libinput-measure
/usr/libexec/libinput/libinput-measure-fuzz
/usr/libexec/libinput/libinput-measure-touch-size
/usr/libexec/libinput/libinput-measure-touchpad-pressure
/usr/libexec/libinput/libinput-measure-touchpad-tap
/usr/libexec/libinput/libinput-quirks
/usr/libexec/libinput/libinput-record
/usr/libexec/libinput/libinput-replay

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libinput/5a48bb048772f9029b604fbdd869d92fddae1cef
/usr/share/package-licenses/libinput/c015511464588baeb0a5c640848a3f31d1a837b5

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/libinput-debug-events.1
/usr/share/man/man1/libinput-debug-gui.1
/usr/share/man/man1/libinput-debug-tablet.1
/usr/share/man/man1/libinput-list-devices.1
/usr/share/man/man1/libinput-measure-fuzz.1
/usr/share/man/man1/libinput-measure-touch-size.1
/usr/share/man/man1/libinput-measure-touchpad-pressure.1
/usr/share/man/man1/libinput-measure-touchpad-tap.1
/usr/share/man/man1/libinput-measure.1
/usr/share/man/man1/libinput-quirks-list.1
/usr/share/man/man1/libinput-quirks-validate.1
/usr/share/man/man1/libinput-quirks.1
/usr/share/man/man1/libinput-record.1
/usr/share/man/man1/libinput-replay.1
/usr/share/man/man1/libinput-test-suite.1
/usr/share/man/man1/libinput.1
