%include	/usr/lib/rpm/macros.python
Summary:	Guppi - GNOME Plotting Engine
Summary(pl):	Guppi - Silnik Rysuj±cy GNOME
Summary(pt_BR):	Analisador e visualizador de dados do GNOME
Name:		Guppi
Version:	0.40.3
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/Guppi/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am_ac.patch
Source1:	%{name}.desktop
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
BuildRequires:	intltool
BuildRequires:	libglade-devel
BuildRequires:	libxml-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	python-devel >= 2.1
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-pythonprov
BuildRequires:	gnumeric >= 1.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	guile >= 1.3.4
Obsoletes:	libguppi15

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Guppi is an easy-to-use graphical interface for plotting data and
performing statistical manipulations.

%description -l pl
Guppi jest ³atwym w u¿yciu graficznym interfejsem do rysowania
wykresów i obliczeñ statystycznych.

%description -l pt_BR
Este pacote contém o Guppi, um analisador e visualizador de dados
baseado no GNOME.

%package devel
Summary:	Guppi includes etc.
Summary(pl):	Guppi - pliki nag³ówkowe
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}
Requires:	python-devel
Obsoletes:	libguppi15-devel

%description devel
Header files for Guppi.

%description -l pl devel
Pliki nag³ówkowe do Guppi.

%description -l pt_BR devel
Este pacote contém os arquivos necessários para desenvolvimento com o
Guppi.

%package static
Summary:	Guppi static libraries
Summary(pl):	Biblioteki statyczne Guppi
Summary(pt_BR):	Bibliotecas estáticas do Guppi
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Guppi static libraries.

%description static -l pl
Biblioteki statyczne Guppi.

%description -l pt_BR static
Bibliotecas estáticas para desenvolvimento baseado no Guppi.

%prep
%setup -q
%patch0 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
xml-i18n-toolize --copy --force
libtoolize --copy --force
gettextize --copy --force
aclocal -I %{_aclocaldir}/gnome
autoheader
autoconf
automake -a -c

CPPFLAGS="-I%{py_incdir}"; export CPPFLAGS

%configure \
	--enable-gnumeric \
	

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Graphics

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appdir=%{_applnkdir}/Graphics \
	aclocaldir=%{_aclocaldir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics

gzip -9nf AUTHORS BIBLIOGRAPHY ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/guppi
%dir %{_libdir}/guppi/plug-ins
%dir %{_libdir}/guppi/plug-ins/%{version}
%dir %{_libdir}/guppi/plug-ins/%{version}/*
%dir %{_libdir}/guppi/plug-ins/%{version}/*/*
%{_libdir}/guppi/plug-ins/%{version}/*/*/*.plugin
%{_libdir}/guppi/plug-ins/%{version}/*/*/*.glade
%{_libdir}/guppi/plug-ins/%{version}/*/*/*.png
%attr(755,root,root) %{_libdir}/guppi/plug-ins/%{version}/*/*/*.so*

%{_datadir}/guppi
%{_datadir}/oaf/*.oaf*
%{_pixmapsdir}/*
%{_applnkdir}/Graphics/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/libguppiConf.sh
%{_includedir}/gnome-*/*
%{_aclocaldir}/*.m4
