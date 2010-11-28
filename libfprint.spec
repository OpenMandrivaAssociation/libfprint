%define name libfprint
%define soname fprint
%define major 0
%define libname %mklibname %{soname} %{major}
%define libnamedevel %mklibname -d %{soname}

%define pre pre2

Name: %name
Version: 0.1.0
Release: %mkrel 0.%pre.5
License: LGPLv2+
Group:   System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary: Library for adding support for consumer fingerprint readers
URL: http://www.reactivated.net/fprint/wiki/Main_Page
Source: http://prdownloads.sourceforge.net/fprint/libfprint-%{version}-%pre.tar.bz2
# http://thread.gmane.org/gmane.linux.fprint/1321
Patch1:     0001-Add-udev-rules-to-set-devices-to-autosuspend.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=472103
Patch2:     0001-Add-gdk-pixbuf-support.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=499732
Source1:    aes1610.c
Patch3:     libfprint-aes1610-driver.patch
BuildRequires: libusb-devel glib2-devel imagemagick-devel openssl-devel
BuildRequires: doxygen
%description
libfprint is an open source software library designed to make it easy for
application developers to add support for consumer fingerprint readers to their
software.

Features:
    * Written in C
    * Licensed as LGPL-2.1
    * Depends on libusb for USB communication and glib
    * Primarily developed for linux, but should be fairly portable
    * Offers a single API to application developers to access the entire range
      of supported devices
    * Supports imaging - downloading live fingerprint scans from the device
    * Includes image processing/matching code
    * Supports enrollment/verification - enrolling a print from a known user,
      and then later comparing a live scan to the enrolled print 

#--------------------------------------------------------------------

%package -n %{libname}
License: GPL
Group:   System/Libraries
Summary: Library for adding support for consumer fingerprint readers
Provides: %name = %version-%release

%description -n %{libname}
libfprint is an open source software library designed to make it easy for
application developers to add support for consumer fingerprint readers to their
software.

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libfprint.so.%{major}*
%{_datadir}/hal/fdi/information/20thirdparty/10-fingerprint-reader-fprint.fdi
%{_sysconfdir}/udev/rules.d/60-fprint-autosuspend.rules

#--------------------------------------------------------------------

%package -n %{libnamedevel}
License: GPL
Group:   System/Libraries
Summary: Development library for adding support for consumer fingerprint readers
Requires: %libname = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %{libnamedevel}
libfprint is an open source software library designed to make it easy for
application developers to add support for consumer fingerprint readers to their
software.

This package includes the headers and development library for building
applications that support finger print readers.

%files -n %{libnamedevel}
%{_includedir}/libfprint
%{_libdir}/libfprint.la
%{_libdir}/libfprint.so
%{_libdir}/pkgconfig/libfprint.pc

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-0.1.0-pre2
%patch1 -p1
%patch2 -p1
cp -a %{SOURCE1} libfprint/drivers
%patch3 -p1 -b .aes1610

%build
autoreconf -f -i
%configure2_5x --disable-static 
%make
pushd doc
make docs
popd


%install
rm -Rf %{buildroot}
%makeinstall_std

%clean
rm -Rf %{buildroot}
