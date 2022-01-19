%define	major 2
%define	libname	%mklibname fprint %{major}
%define	devname	%mklibname -d fprint

Summary:	Library for adding support for consumer fingerprint readers
Name:		libfprint
Version:	1.94.2
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.freedesktop.org/wiki/Software/fprint/libfprint
Source0:	https://gitlab.freedesktop.org/libfprint/libfprint/-/archive/v%{version}/libfprint-v%{version}.tar.bz2

BuildRequires: doxygen
BuildRequires: meson
BuildRequires: gtk-doc
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(MagickCore)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gusb)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(pixman-1)

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

%package -n	%{libname}
License:	GPLv2
Group:		System/Libraries
Summary:	Library for adding support for consumer fingerprint readers
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
libfprint is an open source software library designed to make it easy for
application developers to add support for consumer fingerprint readers to their
software.

%files -n	%{libname}
#{_libdir}/libfprint.so.%{major}*
#/lib/udev/rules.d/60-fprint-autosuspend.rules


%package -n	%{devname}
License:	GPLv2
Group:		System/Libraries
Summary:	Development library for adding support for consumer fingerprint readers
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the headers and development library for building
applications that support finger print readers.

%files -n	%{devname}
%{_includedir}/libfprint
%{_libdir}/libfprint.so
%{_libdir}/pkgconfig/libfprint.pc

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%meson
%meson_build

%install
%meson_install
