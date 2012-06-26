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

Summary: 	Enlightened canvas library
Name:		evas
Epoch:		2
%if %{snapshot}
Version:	1.1.99.%{svnrev}
Release:	0.%{svndate}.1
%else
Version:	1.2.1
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

BuildRequires: chrpath
BuildRequires: doxygen
BuildRequires: xz
BuildRequires: jpeg-devel
BuildRequires: pth-devel
BuildRequires: giflib-devel
BuildRequires: ungif-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(edb)
BuildRequires: pkgconfig(eet) >= 1.6.1
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(libpng15)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(sdl)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xpm)

Conflicts: %{_lib}evas1-devel
Conflicts: %{_lib}evas1 < 1.1.99.66798-0.20120103.1

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
Obsoletes:	%{_lib}evas0-devel
Conflicts:	%{_lib}evas1-devel

%description -n %{develname}
Evas development headers and development libraries.

%prep
%if %{snapshot}
%setup -qn %{name}
%else
%setup -q
%endif

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
	--enable-software-sdl \
	--enable-fb \
	--enable-directfb \
	--enable-buffer \
	--enable-gl-xlib \
	--enable-pthreads \
	--disable-static

%make 
cd doc; %make doc

%install
rm -fr %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
rm -f %{buildroot}%{_libdir}/%{name}/modules/engines/software_16_sdl/*/module.a

%files
%doc AUTHORS COPYING README
%{_bindir}/evas_cserve
%{_bindir}/evas_cserve_tool
%{_libdir}/%{name}/modules/engines/*/*/*.so
%{_libdir}/%{name}/modules/loaders/*/*/*.so
%{_libdir}/%{name}/modules/savers/*/*/*.so

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/libevas.so
%{_includedir}/evas*
%{_libdir}/pkgconfig/*
%dir %{_datadir}/evas
%dir %{_datadir}/evas/examples
%{_datadir}/evas/examples/*

