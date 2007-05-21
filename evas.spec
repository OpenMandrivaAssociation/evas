%define	name	evas
%define	version 0.9.9.038
%define release %mkrel 4

%define cvsrel 0

%define major 	1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enlightened canvas library
Name: 		%{name}
Version: 	%{version}
Epoch:		1
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot

BuildRequires: 	freetype-devel
BuildRequires: 	X11-devel
BuildRequires: 	eet-devel
BuildRequires: 	edb-devel
#BuildRequires: 	DirectFB-devel
BuildRequires:	cairo-devel
BuildRequires:	png-devel jpeg-devel 
#svg1-devel tiff3-devel xpm4-devel
BuildRequires:	multiarch-utils

%description
Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary: Enlightened Canvas Libraries
Group: System/Libraries
Obsoletes: evas < 1:0.9.9.037
Provides: evas = %{epoch}:%{version}-%{release}

%description -n %{libname}
Evas canvas libraries

Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}-devel
Summary: Enlightened Canvas Library headers and development libraries
Group: System/Libraries
Requires: %{libname} = %{epoch}:%{version}
Provides: lib%{name}-devel = %{epoch}:%{version}-%{release}
Provides: %{name}-devel = %{epoch}:%{version}-%{release}
Requires: edb-devel png-devel eet-devel

%description -n %{libname}-devel
Evas development headers and development libraries.

%prep
%setup -q

%build
%configure2_5x --enable-image-loader-gif --disable-valgrind \
  --enable-image-loader-png \
  --enable-image-loader-jpeg \
  --enable-image-loader-eet \
  --enable-font-loader-eet \
  --enable-image-loader-edb \
  --enable-image-loader-tiff \
  --enable-image-loader-xpm \
  --enable-image-loader-svg

#  --disable-cpu-mmx \
#  --disable-cpu-sse \
#  --disable-valgrind \
#  --disable-cairo-x11 \
#  --disable-directfb \

%make

%install
rm -fr %buildroot
%makeinstall
%multiarch_binaries %buildroot/%_bindir/evas-config

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/libevas.so.*
%{_libdir}/%name/*/*/*/*/*.so

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/libevas.so
%{_libdir}/libevas.*a
%{_libdir}/%name/*/*/*/*/*.la
%{_libdir}/%name/*/*/*/*/*.a
%{_includedir}/*.h
%{_bindir}/evas-config
%multiarch %multiarch_bindir/evas-config
%{_libdir}/pkgconfig/*





%changelog
* Fri May 18 2007 Antoine Ginies <aginies@mandriva.com> 0.9.9.038-4mdv2008.0
- adjust configure flag

* Wed May 16 2007 Antoine Ginies <aginies@mandriva.com> 0.9.9.038-3mdv2008.0
- CVS snapshot 20070516

* Mon Apr 23 2007 Pascal Terjan <pterjan@mandriva.org> 0.9.9.037-3mdv2008.0
+ Revision: 17526
- Don't require evas, it no longer exists
- Add the epoch in Obsoletes

* Sun Apr 22 2007 Pascal Terjan <pterjan@mandriva.org> 1:0.9.9.037-1mdv2008.0
+ Revision: 17126
- Add the description to the lib subpackage as it is now the main one
- Add obsoletes so that people don't keep the old binaries
- New snapshot
- Remove main binary as /usr/bin/evas_* and /usr/share/evas are no longer there

* Sun Apr 22 2007 Pascal Terjan <pterjan@mandriva.org> 1:0.9.9.032-3mdv2008.0
+ Revision: 17051
- devel requires edb-devel, png-devel and eet-devel (from pkgconfig)

  + Mandriva <devel@mandriva.com>


* Sun Dec 03 2006 Pascal Terjan <pterjan@mandriva.org> 0.9.9.032-2mdv2007.0
+ Revision: 90215
- Require the main package in -devel, it contains the .so of modules

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org> 1:0.9.9.032-1mdv2007.0
+ Revision: 53334
- add sources 0.9.9.032
- 0.9.9.032
- Import evas

* Fri Mar 24 2006 Austin Acton <austin@mandriva.org> 1:0.9.9.025-0.20060323.1mdk
- new cvs checkout
- update description

* Fri Feb 17 2006 Austin Acton <austin@mandriva.org> 0.9.9.023-0.20060216.1mdk
- new cvs checkout

* Tue Jan 17 2006 Austin Acton <austin@mandriva.org> 0.9.9.023-0.20060117.1mdk
- new cvs checkout

* Thu Jan 12 2006 Austin Acton <austin@mandriva.org> 0.9.9.022-0.20060111.1mdk
- new cvs checkout

* Thu Nov 24 2005 Austin Acton <austin@mandriva.org> 0.9.9.020-0.20051124.1mdk
- new cvs checkout
- disable directfb backend

* Thu Nov 24 2005 Lenny Cartier <lenny@mandriva.com> 0.9.9.020-0.20051112.2mdk
- rebuild for new libfusion

* Sat Nov 12 2005 Austin Acton <austin@mandriva.org> 0.9.9.020-0.20051112.1mdk
- new cvs checkout

* Wed Nov 09 2005 Austin Acton <austin@mandriva.org> 0.9.9.019-0.20051109.1mdk
- new cvs checkout

* Fri Nov 04 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.019-0.20051104.1mdk
- new cvs checkout

* Tue Sep 06 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.013-0.20050904.1mdk
- new cvs checkout

* Sun Aug 14 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.013-0.20050813.1mdk
- new cvs checkout

* Tue Jun 28 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.010-0.20050627.1mdk
- new cvs checkout

* Thu Jun 09 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.008-0.20050608.1mdk
- new cvs checkout

* Thu May 26 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.007-0.20050524.2mdk
- multiarch binaries

* Thu May 26 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.007-0.20050524.1mdk
- new cvs checkout

* Sun May 22 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.007-0.20050519.1mdk
- disable cairo (won't build with cairo 0.5.0)

* Sat May 14 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.007-0.20050511.4mdk
- really remove valgrind
- clean spec

* Fri May 13 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.007-0.20050511.3mdk
- disable valgrind to allow building on x86_64
- fix provides

* Fri May 13 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.007-0.20050511.2mdk
- fix epoch tags (thanks Olivier Thauvin)
- make buildrequires lib64 friendly

* Thu May 12 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.007-0.20050511.1mdk
- version 0.9.9.025 0.9.9.007, so epoch 1
- fix up spec
- disable mmx/sse (Morreale J-R)

* Wed Sep 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-1.20040913.1mdk
- 1.0.0 20040913

* Wed Jun 16 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0.0-1.20030730.3mdk
- rebuild

