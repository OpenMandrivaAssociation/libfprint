%define major 0
%define libname %mklibname fprint %{major}
%define libnamedevel %mklibname -d fprint

Name:		libfprint
Version:	0.5.0
Release:	1
Summary:	Library for adding support for consumer fingerprint readers
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.freedesktop.org/wiki/Software/fprint/libfprint
Source0:	http://people.freedesktop.org/~hadess/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(udev)
BuildRequires:	doxygen

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
License:	GPL
Group:		System/Libraries
Summary:	Library for adding support for consumer fingerprint readers
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
libfprint is an open source software library designed to make it easy for
application developers to add support for consumer fingerprint readers to their
software.

%files -n %{libname}
%{_libdir}/libfprint.so.%{major}*
%{_udevrulesdir}/60-fprint-autosuspend.rules

#--------------------------------------------------------------------

%package -n %{libnamedevel}
License:	GPL
Group:		System/Libraries
Summary:	Development library for adding support for consumer fingerprint readers
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libnamedevel}
libfprint is an open source software library designed to make it easy for
application developers to add support for consumer fingerprint readers to their
software.

This package includes the headers and development library for building
applications that support finger print readers.

%files -n %{libnamedevel}
%{_includedir}/libfprint
%{_libdir}/libfprint.so
%{_libdir}/pkgconfig/libfprint.pc

#--------------------------------------------------------------------

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

%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-0.pre2.6mdv2011.0
+ Revision: 660250
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-0.pre2.5mdv2011.0
+ Revision: 602543
- rebuild

* Fri Apr 09 2010 Funda Wang <fwang@mandriva.org> 0.1.0-0.pre2.4mdv2010.1
+ Revision: 533315
- rebuild

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-0.pre2.3mdv2010.1
+ Revision: 511586
- rebuilt against openssl-0.9.8m

* Wed Dec 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1.0-0.pre2.2mdv2010.1
+ Revision: 479570
- Add buildrequire
- make %%libname provide %%name
- Fix patches
- Update to 0.1.0 pre2
  Sync patches with fedora
  Fix file list

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 0.0.6-4mdv2010.0
+ Revision: 438595
- rebuild

  + Funda Wang <fwang@mandriva.org>
    - add URL

* Sat Jan 31 2009 Funda Wang <fwang@mandriva.org> 0.0.6-3mdv2009.1
+ Revision: 335787
- rebuild

* Sun Jul 20 2008 Funda Wang <fwang@mandriva.org> 0.0.6-2mdv2009.0
+ Revision: 238915
- rebuild against latest imagemagick
- use configure2_5x

* Sat Jun 21 2008 Buchan Milne <bgmilne@mandriva.org> 0.0.6-1mdv2009.0
+ Revision: 227706
- New version 0.0.6

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.0.5-4mdv2008.1
+ Revision: 168578
- rebuilt against new imagemagick libs
- fix no-buildroot-tag

* Tue Jan 08 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.5-2mdv2008.1
+ Revision: 146505
- rebuilt against new imagemagick libs (6.3.7)

* Sat Dec 08 2007 Buchan Milne <bgmilne@mandriva.org> 0.0.5-1mdv2008.1
+ Revision: 116482
- Buildrequire openssl-devel
- import libfprint


