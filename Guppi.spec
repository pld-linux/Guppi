%include	/usr/lib/rpm/macros.python
Summary:	Guppi - GNOME Plotting Engine
Summary(cs):	Anal�za a vizualizace dat pod GNOME
Summary(da):	Gnome-v�rkt�j for analyse og visualisering af data
Summary(de):	GNOME Datenanalyse und -anzeige
Summary(es):	An�lisis y Visualizaci�n de Datos de Gnome
Summary(fr):	Analyseur et visualiseur de donn�es de Gnome
Summary(it):	Analisi e Visualizzazione Dati GNOME
Summary(ja):	GNOME �١����Υǡ������Ϥ���ӻ�в�
Summary(no):	GNOME-verkt�y for analyse og visualisering av data
Summary(pl):	Guppi - Silnik Rysuj�cy GNOME
Summary(pt_BR):	Analisador e visualizador de dados do GNOME
Summary(sl):	Analiza podatkov in vizualizacija v GNOME
Summary(sv):	GNOME dataanalys och -visualisering
Name:		Guppi
Version:	0.40.3
Release:	2
Epoch:		2
License:	GPL
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(it):	X11/Applicazioni
Group(ja):	X11/���ץꥱ�������
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Group(ru):	X11/����������
Group(sv):	X11/Till�mpningar
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
BuildRequires:	python-devel >= 2.2
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-pythonprov
BuildRequires:	gnumeric >= 1.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	guile >= 1.3.4
Requires:	ghostscript-fonts-std
Obsoletes:	libguppi15

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Guppi is an easy-to-use graphical interface for plotting data and
performing statistical manipulations.

%description -l cs
Guppi je n�stroj pro anal�zu a vizualizaci dat pro Gnome.

%description -l da
Guppi er et Gnome-baseret v�rkt�j for analyse og visualisering af
data.

%description -l de
Guppi ist ein GNOME-basiertes System zur Datenanalyse und -anzeige.

%description -l es
Guppi es un sistema de an�lisis y visualizaci�n de datos basado en
Gnome.

%description -l fr
Guppi est un analyseur de donn�es et un syst�me de visualisation bas�
sur Gnome.

%description -l it
Guppi � un sistema di analisi e visualizzazione dati basato su GNOME.

%description -l ja
Guppi �� GNOME �١����Υǡ������Ϥ���ӻ�в������ƥ�Ǥ���

%description -l no
Guppi er et GNOME-basert verkt�y for analyse og visualisering av data.

%description -l pl
Guppi jest �atwym w u�yciu graficznym interfejsem do rysowania
wykres�w i oblicze� statystycznych.

%description -l pt_BR
Este pacote cont�m o Guppi, um analisador e visualizador de dados
baseado no GNOME.

%description -l sv
Guppi �r ett GNOME-baserad dataanalys- och -visualiseringssystem.

%package devel
Summary:	Guppi include files
Summary(cs):	Hlavi�kov� soubory pro v�voj aplikac� s Guppi
Summary(de):	Include-Dateien zur Entwicklung von Guppi-basierten Anwendungen
Summary(es):	Ficheros de inclusi�n para el desarrollo de aplicaciones Guppi
Summary(fr):	Fichiers � inclure pour le d�veloppement d'applications bas�es sur Guppi
Summary(id):	File header untuk develop aplikasi Guppi
Summary(is):	Hausaskr�r fyrir �r�un � Guppi forritum
Summary(it):	File include per lo sviluppo di applicazioni basate su Guppi
Summary(no):	Headerfiler for utvikling av Guppi-baserte applikasjoner
Summary(pl):	Guppi - pliki nag��wkowe
Summary(pt):	Ficheiros de inclus�o para desenvolver aplica��es do Guppi
Summary(pt_BR):	Arquivos de inclus�o para desenvolvimento
Summary(ru):	����� ���������� ��� ���������� ���������� Guppi
Summary(sk):	Hlavi�kov� s�bory pre v�voj Guppi aplik�ci�
Summary(sl):	Glave za razvoj programov z Guppi
Summary(sv):	Huvudfiler f�r att utveckla Guppi-baserade till�mpningar
Group:		X11/Development/Libraries
Group(cs):	X11/V�vojov� prost�edky/Knihovny
Group(da):	X11/Udvikling/Biblioteker
Group(de):	X11/Entwicklung/Bibliotheken
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(it):	X11/Sviluppo/Librerie
Group(ja):	X11/��ȯ/�饤�֥��
Group(no):	X11/Applikasjoner/Biblioteker
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(pt):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(sv):	X11/Utveckling/Bibliotek
Group(uk):	X11/��������/��̦�����
Requires:	%{name} = %{version}
Requires:	python-devel
Obsoletes:	libguppi15-devel

%description devel
Header files for Guppi.

%description -l cs devel
Bal��ek obsahuje hlavi�kov� soubory pro v�voj aplikac� s Guppi (GNOME
Data Analysis and Visualization).

%description -l da devel
Guppi-devel indeholder headerfiler for udvikling af programmer som
bruger rutiner fra Guppi.

%description -l de devel
Das Paket Guppi-devel enth�lt Header-Dateien f�r das Guppi-Paket.

%description -l es devel
El paquete Guppi-devel contiene ficheros de cabecera para el paquete
Guppi.

%description -l fr devel
Le paquetage Guppi-devel contient fichiers d'en-t�te pour le paquetage
Guppi.

%description -l it devel
Il pacchetto Guppi-devel include i file header per il pacchetto Guppi.

%description -l no devel
Guppi-devel inneholder headerfiler for utvikling av applikasjoner som
bruker rutiner fra Guppi.

%description -l pl devel
Pliki nag��wkowe do Guppi.

%description -l pt_BR devel
Este pacote cont�m os arquivos necess�rios para desenvolvimento com o
Guppi.

%description -l sv devel
Paketet Guppi-devel inneh�ller huvudfilerna f�r paketet Guppi.

%package static
Summary:	Guppi static libraries
Summary(cs):	Statick� knihovny pro v�voj aplikac� s Guppi
Summary(da):	Statiske biblioteker for udvikling af Guppi-baserede programmer
Summary(de):	Statischen Bibliotheken zur Entwicklung von Guppi-basierten Anwendungen
Summary(es):	Bibliotecas est�ticas para el desarrollo de aplicaciones Guppi
Summary(fr):	Biblioth�ques statiques pour le d�veloppement d'applications bas�es sur Guppi
Summary(id):	Static library untuk develop aplikasi Guppi
Summary(it):	Librerie statiche per lo sviluppo di applicazioni basate su Guppi
Summary(no):	Statiske biblioteker for utvikling av Guppi-baserte applikasjoner
Summary(pl):	Biblioteki statyczne Guppi
Summary(pt):	Bibliotecas est�ticas para desenvolver aplica��es do Guppi
Summary(pt_BR):	Bibliotecas est�ticas do Guppi
Summary(ru):	����������� ���������� ��� ���������� ���������� Guppi
Summary(sk):	Statick� kni�nice pre v�voj Guppi aplik�ci�
Summary(sv):	Statiska bibliotek f�r att utveckla Guppi-baserade till�mpningar
Group:		X11/Development/Libraries
Group(cs):	X11/V�vojov� prost�edky/Knihovny
Group(da):	X11/Udvikling/Biblioteker
Group(de):	X11/Entwicklung/Bibliotheken
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(it):	X11/Sviluppo/Librerie
Group(ja):	X11/��ȯ/�饤�֥��
Group(no):	X11/Applikasjoner/Biblioteker
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(pt):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(sv):	X11/Utveckling/Bibliotek
Group(uk):	X11/��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
Guppi static libraries.

%description -l cs static
Bal��ek obsahuje statick� knihovny pro v�voj aplikac� s Guppi (GNOME
Data Analysis and Visualization).

%description -l da static
Guppi-static indeholder statiske bibliotek for udvikling af programmer
som bruger rutiner fra Guppi.

%description -l de static
Das Paket Guppi-static enth�lt die statischen Bibliotheken f�r das
Guppi-Paket.

%description -l es static
El paquete Guppi-static contiene las bibliotecas est�ticas para el
paquete Guppi.

%description -l fr static
Le paquetage Guppi-static contient les biblioth�ques statiques pour le
paquetage Guppi.

%description -l it static
Il pacchetto Guppi-static include le librerie statiche per il
pacchetto Guppi.

%description -l no static
Guppi-static inneholder statiske bibliotek for utvikling av
applikasjoner som bruker rutiner fra Guppi.

%description static -l pl
Biblioteki statyczne Guppi.

%description -l pt_BR static
Bibliotecas est�ticas para desenvolvimento baseado no Guppi.

%description -l sv static
Paketet Guppi-static inneh�ller de statiska biblioteken f�r paketet
Guppi.

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
