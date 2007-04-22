%define	name	evas
%define	version 0.9.9.037
%define release %mkrel 1

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
#BuildRequires:	cairo-devel
BuildRequires:	png-devel jpeg-devel
BuildRequires:	multiarch-utils

%description
Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary: Enlightened Canvas Libraries
Group: System/Libraries

%description -n %{libname}
Evas canvas libraries

%package -n %{libname}-devel
Summary: Enlightened Canvas Library headers and development libraries
Group: System/Libraries
Requires: %{libname} = %{epoch}:%{version}
Requires: %{name} = %{epoch}:%{version}
Provides: lib%{name}-devel = %{epoch}:%{version}-%{release}
Provides: %{name}-devel = %{epoch}:%{version}-%{release}
Requires: edb-devel png-devel eet-devel

%description -n %{libname}-devel
Evas development headers and development libraries.

%prep
%setup -q

%build
%configure2_5x --disable-cpu-mmx --disable-cpu-sse --disable-valgrind --disable-cairo-x11 --disable-directfb
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



