%define	name	evas
%define version 0.9.9.042
%define release %mkrel 2

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Enlightened canvas library
Name: 		%{name}
Version: 	%{version}
Epoch:		2
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot

BuildRequires: 	freetype-devel
BuildRequires: 	X11-devel
BuildRequires: 	eet-devel >= 0.9.10.042
BuildRequires: 	edb-devel >= 1.0.5.042
BuildRequires:	cairo-devel
BuildRequires:	png-devel, jpeg-devel 
Buildrequires:	tiff-devel
Buildrequires:  mesagl-devel
BuildRequires:	glitz-devel, ungif-devel, xpm-devel
#BuildRequires:	glew-devel

%description
Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary: Enlightened Canvas Libraries
Group: System/Libraries

%description -n %{libname}
Evas canvas libraries.

Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}-devel
Summary: Enlightened Canvas Library headers and development libraries
Group: System/Libraries
Requires: %{libname} = 2:%{version}
Provides: %{name}-devel = 2:%{version}-%{release}
Requires: edb-devel png-devel eet-devel

%description -n %{libname}-devel
Evas development headers and development libraries.

%prep
%setup -q

%build
%configure2_5x --enable-image-loader-gif \
  --disable-valgrind \
  --enable-image-loader-png \
  --enable-image-loader-jpeg \
  --enable-image-loader-eet \
  --enable-font-loader-eet \
  --enable-image-loader-edb \
  --enable-image-loader-tiff \
  --enable-image-loader-xpm \
  --enable-image-loader-svg \
  --enable-cpu-mmx \
  --enable-cpu-sse \
  --enable-cpu-c \
  --enable-scale-sample \
  --enable-scale-smooth \
  --enable-convert-yuv \
  --enable-small-dither-mask \
  --enable-fontconfig \
  --enable-software-x11 \
  --enable-directfb \
  --enable-fb \
  --enable-buffer \
  --enable-gl-x11 \
  --disable-gl-glew \
  --enable-xrender-x11 \
  --enable-pthreads \
  --enable-glitz-x11
%make

%install
rm -fr %buildroot
%makeinstall

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
%{_libdir}/pkgconfig/*

