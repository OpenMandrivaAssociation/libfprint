%define	major	0
%define	libname	%mklibname fprint %{major}
%define	devname	%mklibname -d fprint

Summary:	Library for adding support for consumer fingerprint readers
Name:		libfprint
Version:	0.6.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.freedesktop.org/wiki/Software/fprint/libfprint
Source0:	http://people.freedesktop.org/~hadess/%{name}-%{version}.tar.xz

BuildRequires:	doxygen
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(MagickCore)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(udev)

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
%{_libdir}/libfprint.so.%{major}*
/lib/udev/rules.d/60-fprint-autosuspend.rules


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
%setup -q
%apply_patches

%build
%configure2_5x --disable-static
%make
pushd doc
make docs
popd

%install
%makeinstall_std

