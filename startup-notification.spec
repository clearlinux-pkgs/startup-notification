#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : startup-notification
Version  : 0.12
Release  : 17
URL      : http://www.freedesktop.org/software/startup-notification/releases/startup-notification-0.12.tar.gz
Source0  : http://www.freedesktop.org/software/startup-notification/releases/startup-notification-0.12.tar.gz
Summary  : Startup notification library
Group    : Development/Tools
License  : LGPL-2.0
Requires: startup-notification-lib = %{version}-%{release}
Requires: startup-notification-license = %{version}-%{release}
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-aux)
BuildRequires : pkgconfig(xcb-event)

%description


%package dev
Summary: dev components for the startup-notification package.
Group: Development
Requires: startup-notification-lib = %{version}-%{release}
Provides: startup-notification-devel = %{version}-%{release}
Requires: startup-notification = %{version}-%{release}

%description dev
dev components for the startup-notification package.


%package lib
Summary: lib components for the startup-notification package.
Group: Libraries
Requires: startup-notification-license = %{version}-%{release}

%description lib
lib components for the startup-notification package.


%package license
Summary: license components for the startup-notification package.
Group: Default

%description license
license components for the startup-notification package.


%prep
%setup -q -n startup-notification-0.12
cd %{_builddir}/startup-notification-0.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604601424
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604601424
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/startup-notification
cp %{_builddir}/startup-notification-0.12/COPYING %{buildroot}/usr/share/package-licenses/startup-notification/433183a061c599ed2443c625b3129d141dc1c290
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/startup-notification-1.0/libsn/sn-common.h
/usr/include/startup-notification-1.0/libsn/sn-launchee.h
/usr/include/startup-notification-1.0/libsn/sn-launcher.h
/usr/include/startup-notification-1.0/libsn/sn-monitor.h
/usr/include/startup-notification-1.0/libsn/sn-util.h
/usr/include/startup-notification-1.0/libsn/sn.h
/usr/lib64/libstartup-notification-1.so
/usr/lib64/pkgconfig/libstartup-notification-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libstartup-notification-1.so.0
/usr/lib64/libstartup-notification-1.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/startup-notification/433183a061c599ed2443c625b3129d141dc1c290
