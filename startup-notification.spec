#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : startup-notification
Version  : 0.12
Release  : 5
URL      : http://www.freedesktop.org/software/startup-notification/releases/startup-notification-0.12.tar.gz
Source0  : http://www.freedesktop.org/software/startup-notification/releases/startup-notification-0.12.tar.gz
Summary  : Startup notification library
Group    : Development/Tools
License  : GPL-2.0
Requires: startup-notification-lib
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-aux)
BuildRequires : pkgconfig(xcb-event)

%description


%package dev
Summary: dev components for the startup-notification package.
Group: Development
Requires: startup-notification-lib
Provides: startup-notification-devel

%description dev
dev components for the startup-notification package.


%package lib
Summary: lib components for the startup-notification package.
Group: Libraries

%description lib
lib components for the startup-notification package.


%prep
%setup -q -n startup-notification-0.12

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
