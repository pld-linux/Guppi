Summary:	Guppi - GNOME Plotting Engine
Summary(pl):	Guppi - Silnik Rysuj±cy GNOME
Name:		Guppi
Version:	0.35.5
Release:	6
Epoch:		2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/Guppi/%{name}-%{version}.tar.bz2
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-use_AM_GNU_GETTEXT.patch
URL:		http://www.gnome.org/guppi/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	flex
BuildRequires:	gdk-pixbuf-devel >= 0.8.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	gtk+-devel > 1.2.0
BuildRequires:	guile-devel
BuildRequires:	libglade-devel
BuildRequires:	libxml-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	python-devel >= 2.1
BuildRequires:	readline-devel >= 4.2
BuildRequires:	xml-i18n-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	guile >= 1.3.4
Obsoletes:	Guppi-static

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Guppi is an easy-to-use graphical interface for plotting data and
performing statistical manipulations.

%description -l pl
Guppi jest ³atwym w u¿yciu graficznym interfejsem do rysowania
wykresów i obliczeñ statystycznych.

%package devel
Summary:	Guppi includes etc.
Summary(pl):	Guppi - pliki nag³ówkowe
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Obsoletes:	Guppi-static

%description devel
Header files for Guppi.

%description -l pl devel
Pliki nag³ówkowe do Guppi.

%package static
Summary:	Guppi static libraries
Summary(pl):	Biblioteki statyczne Guppi
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Guppi static libraries.

%description static -l pl
Biblioteki statyczne Guppi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c -i

CPPFLAGS="-I%{_includedir}/python2.1"; export CPPFLAGS

%configure \
	--enable-gnumeric

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appdir=%{_applnkdir}/Graphics \
	aclocaldir=%{_aclocaldir}

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
%attr(755,root,root) %{_libdir}/libguppiConf.sh
%dir %{_libdir}/guppi
%dir %{_libdir}/guppi/plug-ins
%dir %{_libdir}/guppi/plug-ins/%{version}
%dir %{_libdir}/guppi/plug-ins/%{version}/*
%dir %{_libdir}/guppi/plug-ins/%{version}/*/*
%{_libdir}/guppi/plug-ins/%{version}/*/*/*.plugin
%{_libdir}/guppi/plug-ins/%{version}/*/*/*.scm
%{_libdir}/guppi/plug-ins/%{version}/*/*/*.glade
%{_libdir}/guppi/plug-ins/%{version}/*/*/*.png
%attr(755,root,root) %{_libdir}/guppi/plug-ins/%{version}/*/*/*.so*

%{_datadir}/guppi
%{_datadir}/oaf
%{_pixmapsdir}/*
%{_applnkdir}/Graphics/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*
