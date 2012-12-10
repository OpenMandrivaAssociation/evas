#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/evas evas; \
#cd evas; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf evas-$PKG_VERSION.tar.xz evas/ --exclude .svn --exclude .*ignore

%define snapshot 0
%if %{snapshot}
%define	svndate	20120103
%define	svnrev	66798
%endif

%define	major 1
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Summary:	Enlightened canvas library
Name:		evas
Epoch:		2
%if %{snapshot}
Version:	1.1.99.%{svnrev}
Release:	0.%{svndate}.1
%else
Version:	1.7.3
Release:	1
%endif
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
%if %{snapshot}
Source0:	%{name}-%{version}.tar.xz
%else
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz
%endif
Patch0:		evas-1.7.0-esvg.patch

BuildRequires:	chrpath
BuildRequires:	doxygen
BuildRequires:	xz
BuildRequires:	jpeg-devel
BuildRequires:	pth-devel
BuildRequires:	giflib-devel
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(edb)
BuildRequires:	pkgconfig(eet) >= 1.7.0
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libpng15)
# librsvg is no longer supported, we use esvg now for SVG support
BuildRequires:	pkgconfig(esvg)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xpm)

Conflicts:	%{_lib}evas1-devel
Conflicts:	%{_lib}evas1 < 1.1.99.66798-0.20120103.1

%description
Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary:	Enlightened Canvas Libraries
Group:		System/Libraries

%description -n %{libname}
Evas canvas libraries.

Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{develname}
Summary:	Enlightened Canvas Library headers and development libraries
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}evas0-devel < 2:1.7.0
Conflicts:	%{_lib}evas1-devel

%description -n %{develname}
Evas development headers and development libraries.

%prep
%if %{snapshot}
%setup -qn %{name}
%else
%setup -q
%endif
%patch0 -p1

%build
sed -i 's|bzip2|xz|g' config*
sed -i 's|bzip2|xz|g' Makefile*
sed -i 's|bzip2|xz|g' doc/Makefile*
sed -i 's|bz2|xz|g' Makefile*
sed -i 's|bz2|xz|g' doc/Makefile*

%if %{snapshot}
NOCONFIGURE=yes ./autogen.sh
%endif

%configure2_5x \
	--enable-image-loader-gif \
	--disable-valgrind \
	--enable-image-loader-png \
	--enable-image-loader-jpeg \
	--enable-image-loader-eet \
	--enable-font-loader-eet \
	--enable-image-loader-tiff \
	--enable-image-loader-xpm \
	--enable-image-loader-svg \
	--enable-cpu-mmx \
	--disable-cpu-sse \
	--enable-cpu-c \
	--enable-scale-sample \
	--enable-scale-smooth \
	--enable-convert-yuv \
	--enable-small-dither-mask \
	--enable-fontconfig \
	--enable-software-xlib \
	--enable-software-16-x11 \
	--enable-gl-sdl \
	--enable-fb \
	--enable-directfb \
	--enable-buffer \
	--enable-gl-xlib \
	--enable-pthreads \
	--disable-static

%make 
cd doc; %make doc

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/%{name}/modules/engines/software_16_sdl/*/module.a

%files
%doc AUTHORS COPYING README
%{_bindir}/evas_cserve*
%{_libdir}/%{name}/modules/engines/*/*/*.so
%{_libdir}/%{name}/modules/loaders/*/*/*.so
%{_libdir}/%{name}/modules/savers/*/*/*.so
%{_libdir}/%{name}/cserve2/loaders/*/*/*.so
%{_libdir}/dummy_slave
%{_libdir}/evas_cserve2
%{_libdir}/evas_cserve2_slave
%{_datadir}/%{name}/checkme

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/libevas.so
%{_includedir}/evas*
%{_libdir}/pkgconfig/*
%dir %{_datadir}/evas
%dir %{_datadir}/evas/examples
%{_datadir}/evas/examples/*



%changelog
* Tue Jun 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 2:1.2.1-1
+ Revision: 807042
- version update 1.2.1

* Wed Jan 04 2012 Matthew Dawkins <mattydaw@mandriva.org> 2:1.1.99.66798-0.20120103.1
+ Revision: 752361
- new snapshot version 1.1.99.66798
- cleaned up spec and merged with Unity Linux spec
- disabled static build

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 2:1.0.1-1
+ Revision: 681649
- update to new version 1.0.1

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 2:1.0.0-1
+ Revision: 633909
- 1.0.0 final

* Sat Dec 18 2010 Funda Wang <fwang@mandriva.org> 2:1.0.0-0.beta3.2mdv2011.0
+ Revision: 622816
- rebuild

* Sat Dec 18 2010 Funda Wang <fwang@mandriva.org> 2:1.0.0-0.beta3.1mdv2011.0
+ Revision: 622782
- 1.0 beta3

* Sun Nov 14 2010 Funda Wang <fwang@mandriva.org> 2:1.0.0-0.beta2.1mdv2011.0
+ Revision: 597516
- 1.0.0 beta2

* Wed Oct 13 2010 Funda Wang <fwang@mandriva.org> 2:1.0.0-0.beta.2mdv2011.0
+ Revision: 585299
- rebuild

* Wed Oct 13 2010 Funda Wang <fwang@mandriva.org> 2:1.0.0-0.beta.1mdv2011.0
+ Revision: 585290
- 1.0.0 beta

* Sat Jul 10 2010 Funda Wang <fwang@mandriva.org> 2:0.9.9.49898-1mdv2011.0
+ Revision: 549977
- update file list
- New version 0.9.9.49898

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 2:0.9.9.063-3mdv2010.1
+ Revision: 492241
- rebuild for new libjpeg v8

* Mon Dec 14 2009 Funda Wang <fwang@mandriva.org> 2:0.9.9.063-2mdv2010.1
+ Revision: 478439
- drop hard requires on libs

* Sun Dec 13 2009 Funda Wang <fwang@mandriva.org> 2:0.9.9.063-1mdv2010.1
+ Revision: 478106
- New version 0.9.9.063

* Sun Aug 23 2009 Funda Wang <fwang@mandriva.org> 2:0.9.9.062-4mdv2010.0
+ Revision: 419750
- rebuild for new libjpeg v7

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 2:0.9.9.062-3mdv2010.0
+ Revision: 411250
- add more BR

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 2:0.9.9.062-2mdv2010.0
+ Revision: 411249
- enable sdl backend

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 2:0.9.9.062-1mdv2010.0
+ Revision: 411105
- new version 0.9.9.062

* Tue Jul 07 2009 Funda Wang <fwang@mandriva.org> 2:0.9.9.061-2mdv2010.0
+ Revision: 393188
- rebuild for new eina

* Mon Jul 06 2009 Funda Wang <fwang@mandriva.org> 2:0.9.9.061-1mdv2010.0
+ Revision: 392863
- fix file list
- new version 0.9.9.061

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 2:0.9.9.060-1mdv2010.0
+ Revision: 370631
- New version 0.9.9.060

* Tue Mar 03 2009 Antoine Ginies <aginies@mandriva.com> 2:0.9.9.050-3mdv2009.1
+ Revision: 347820
- bump release
- fix libtool for release < 2009.1

* Fri Feb 27 2009 Antoine Ginies <aginies@mandriva.com> 2:0.9.9.050-2mdv2009.1
+ Revision: 345624
- add xcb-util-devel buildrequires
- update buildrequires
- fix xcb-devel buildrequires
- add xcb pixman-1-devel buildrequires
- SVN SNAPSHOT 20090227, release 0.9.9.050, update eet buildrequires version

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 2:0.9.9.050-1mdv2009.1
+ Revision: 292037
- New snapshot

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2:0.9.9.043-4mdv2009.0
+ Revision: 266734
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 2:0.9.9.043-3mdv2009.0
+ Revision: 213968
- sdl backends does not exists
- enalbe soft-16-x11

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 2:0.9.9.043-1mdv2009.0
+ Revision: 213941
- New version 0.9.9.043

  + Antoine Ginies <aginies@mandriva.com>
    - fix 2008.0 rebuild

* Thu Mar 27 2008 Pascal Terjan <pterjan@mandriva.org> 2:0.9.9.042-4mdv2008.1
+ Revision: 190650
- Have the libs to conflict too, else it breaks upgrade from 2008.0

* Tue Mar 18 2008 Antoine Ginies <aginies@mandriva.com> 2:0.9.9.042-3mdv2008.1
+ Revision: 188469
- increase release
- add a conflict with evas1

* Fri Feb 15 2008 Antoine Ginies <aginies@mandriva.com> 2:0.9.9.042-2mdv2008.1
+ Revision: 168880
- fix buildrequires (xcb-devel is not provided by libxcb1-devel)
- add some buildrequires, update configure options
- CVS snapshot 20080215
- adjust buildrequires

* Sat Feb 02 2008 Austin Acton <austin@mandriva.org> 2:0.9.9.042-1mdv2008.1
+ Revision: 161307
- sync
- new version
- back to major=0 (strange)
- tidy spec and provides
- drop config file

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 12 2007 Austin Acton <austin@mandriva.org> 1:0.9.9.041-3mdv2008.1
+ Revision: 108044
- adjust configure options
- tidy

* Wed Oct 31 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.041-2mdv2008.1
+ Revision: 104090
- new tarball from svn snapshot
- increase mkrel
- update buildrequires

* Thu Aug 30 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.041-1mdv2008.0
+ Revision: 76298
- fix missing evas-config
- fix path in tarball
- CVS SNAPSHOT 20070830, release 0.9.9.041
- use libxcb-devel not %%{mklibname xcb}-devel
- fix tiff-devel buildrequires (do not use major version)
- prevent major bug to happen again
- remove major in libxcb-devel buildrequires
- remove  libsvg-cairo1-devel buildrequires
- fix xcb1-devel buildrequires
- add directfb-devel, libsvg-cairo1-devel buildrequires
- add more buildrequires
- CVS snapshot 20070604
- add ./autogen.sh in %%make section
- ?\195?\169disable ddraw rendering
- CVS SNAPSHOT 20070529, release 0.9.9.038

* Tue May 29 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.038-7mdv2008.0
+ Revision: 32588
- enable gl evas rendering

* Tue May 29 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.038-6mdv2008.0
+ Revision: 32277
- adjust tiff3-devel buildrequires
- remove direcfb-buildrequires
- re-add directfb1-devel buildrequires
- remove directfb buildrequires
- add needed buildrequires
- active directfb, g, generic evas engines

* Thu May 24 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.038-5mdv2008.0
+ Revision: 30640
- increase mkrel
- CVS snapshot 20070524, release 0.9.9.038
- remove unwanted changelog

* Mon May 21 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.038-4mdv2008.0
+ Revision: 29102
- CVS snapshot 20070516, adjust configure options, release 0.9.9.038

* Mon Apr 23 2007 Pascal Terjan <pterjan@mandriva.org> 1:0.9.9.037-3mdv2008.0
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

