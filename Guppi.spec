Summary:	Guppi - GNOME Plotting Engine
Name:		Guppi
Version:	0.34.5
Release:	1
License:	GPL
Group:		X11/GNOME/Applications
Group(pl):	X11/GNOME/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/guppi/%{name}-%{version}.tar.gz
Patch0:		Guppi-DESTDIR.patch
URL:		http://www.gnome.org/guppi/
BuildRequires:	gnome-print-devel >= 0.13.0
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
BuildRequires:	gtk+-devel > 1.2.0
BuildRequires:	libglade-devel
BuildRequires:	libxml-devel
BuildRequires:	guile-devel
BuildRequires:	gettext-devel
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	guile >= 1.3.4

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Guppi is an easy-to-use graphical interface for plotting data and
performing statistical manipulations.

%package devel
Summary:	Guppi libraries, includes, etc
Summary(pl):	Guppi - pliki nag³ówkowe, etc
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for Guppi.

%description -l pl devel
Pliki nag³ówkowe etc do Guppi.

%package static
Summary:	Guppi static libraries
Summary(pl):	Biblioteki statyczne Guppi
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Guppi static libraries.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
automake
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	appdir=%{_applnkdir}/Graphics

strip --strip-unneede $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* \
	$RPM_BUILD_ROOT%{_libdir}/guppi/plug-ins/%{version}/lib*.so.*.*

gzip -9nf AUTHORS BIBLIOGRAPHY ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/guppi
%dir %{_libdir}/guppi/plug-ins
%dir %{_libdir}/guppi/plug-ins/%{version}
%attr(755,root,root) %{_libdir}/guppi/plug-ins/%{version}/lib*.so*

%{_datadir}/guppi
%{_datadir}/pixmaps/*
%{_applnkdir}/Graphics/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/guppi/plug-ins/%{version}/lib*.a
