%define	major	1
%define	libname %mklibname %{name} %{major}
%define	devname %mklibname %{name} -d
%define _disable_ld_no_undefined 1

Summary:	Enlightened canvas library
Name:		evas
Epoch:		2
Version:	1.7.8
Release:	3
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		https://www.enlightenment.org/
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
Patch1:		evas-1.7.5-giflib5.patch
BuildRequires:	chrpath
BuildRequires:	doxygen
BuildRequires:	xz
BuildRequires:	pkgconfig(libjpeg)
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
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
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

%package -n %{devname}
Summary:	Enlightened Canvas Library headers and development libraries
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}evas0-devel < 2:1.7.0
Conflicts:	%{_lib}evas1-devel

%description -n %{devname}
Evas development headers and development libraries.

%prep
%setup -q
%patch1 -p0

%build
sed -i 's|bzip2|xz|g' config*
sed -i 's|bzip2|xz|g' Makefile*
sed -i 's|bzip2|xz|g' doc/Makefile*
sed -i 's|bz2|xz|g' Makefile*
sed -i 's|bz2|xz|g' doc/Makefile*

%configure \
	--enable-image-loader-gif \
	--disable-valgrind \
	--enable-image-loader-png \
	--enable-image-loader-jpeg \
	--enable-image-loader-eet \
	--enable-font-loader-eet \
	--enable-image-loader-tiff \
	--enable-image-loader-xpm \
	--enable-image-loader-svg \
%ifnarch %arm %mips
	--enable-cpu-mmx \
%endif
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
	--enable-buffer \
	--enable-gl-xlib \
	--enable-pthreads \
	--disable-static

%make_build
cd doc; %make doc

%install
%make_install
rm -f %{buildroot}%{_libdir}/%{name}/modules/engines/software_16_sdl/*/module.a

%files
%doc AUTHORS COPYING README
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/cserve2
%dir %{_datadir}/%{name}
%{_bindir}/evas_cserve*
%{_libdir}/%{name}/modules/*
%{_libdir}/%{name}/cserve2/*
%{_libdir}/dummy_slave
%{_libdir}/evas_cserve2
%{_libdir}/evas_cserve2_slave
%{_datadir}/%{name}/checkme

%files -n %{libname}
%{_libdir}/libevas.so.%{major}*

%files -n %{devname}
%{_libdir}/libevas.so
%{_includedir}/evas*
%{_libdir}/pkgconfig/*
%dir %{_datadir}/evas
%dir %{_datadir}/evas/examples
%{_datadir}/evas/examples/*
