%define name libfprint
%define soname fprint
%define major 0
%define libname %mklibname %{soname} %{major}
%define libnamedevel %mklibname -d %{soname}

Name: %name
Version: 0.0.6
Release: %mkrel 1
License: LGPL
Group:   System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary: Library for adding support for consumer fingerprint readers
Source: http://prdownloads.sourceforge.net/fprint/libfprint-%{version}.tar.bz2
BuildRequires: libusb-devel glib2-devel imagemagick-devel openssl-devel

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

%package -n %{libname}
License: GPL
Group:   System/Libraries
Summary: Library for adding support for consumer fingerprint readers

%description -n %{libname}
libfprint is an open source software library designed to make it easy for
application developers to add support for consumer fingerprint readers to their
software.

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

%prep
%setup -q

%build
%configure
%make

%install
rm -Rf %{buildroot}
%makeinstall_std

%clean
rm -Rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libfprint.so.%{major}*

%files -n %{libnamedevel}
%{_includedir}/libfprint
%{_libdir}/libfprint.a
%{_libdir}/libfprint.la
%{_libdir}/libfprint.so
%{_libdir}/pkgconfig/libfprint.pc
