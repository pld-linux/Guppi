#
# Conditional build:
%bcond_with	gnumeric	# build with support for GNOME1-based gnumeric
#
Summary:	Guppi - GNOME Plotting Engine
Summary(cs):	Analıza a vizualizace dat pod GNOME
Summary(da):	GNOME-værktøj for analyse og visualisering af data
Summary(de):	GNOME Datenanalyse und -anzeige
Summary(es):	Análisis y Visualización de Datos de GNOME
Summary(fr):	Analyseur et visualiseur de données de GNOME
Summary(it):	Analisi e Visualizzazione Dati GNOME
Summary(ja):	GNOME ¥Ù¡¼¥¹¤Î¥Ç¡¼¥¿²òÀÏ¤ª¤è¤Ó»ë³Ğ²½
Summary(nb):	GNOME-verktøy for analyse og visualisering av data
Summary(pl):	Guppi - Silnik Rysuj±cy GNOME
Summary(pt_BR):	Analisador e visualizador de dados do GNOME
Summary(sl):	Analiza podatkov in vizualizacija v GNOME
Summary(sv):	GNOME dataanalys och -visualisering
Summary(zh_CN):	Guppi - GNOME½»»¥Ê½Êı¾İ·ÖÎö¹¤¾ß
Name:		Guppi
Version:	0.40.3
Release:	11
Epoch:		2
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/Guppi/0.40/%{name}-%{version}.tar.bz2
# Source0-md5:	26ec6eb5b6fe7fb4e32ecff64d4f1b16
Source1:	%{name}.desktop
Patch0:		%{name}-am_ac.patch
Patch1:		%{name}-am_hack.patch
Patch2:		%{name}-ac.patch
Patch3:		%{name}-link.patch
Patch4:		%{name}-am18.patch
URL:		http://www.gnome.org/guppi/
%{?with_gnumeric:BuildRequires:	ORBit-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gdk-pixbuf-gnome-devel >= 0.11.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.28
%{?with_gnumeric:BuildRequires:	gnumeric >= 1.0.3}
BuildRequires:	gtk+-devel > 1.2.0
BuildRequires:	intltool
BuildRequires:	libart_lgpl-devel >= 2.2.0
BuildRequires:	libglade-gnome-devel
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	gdk-pixbuf >= 0.11.0
Requires:	ghostscript-fonts-std
Requires:	gnome-print >= 0.28
Requires:	libart_lgpl >= 2.2.0
Obsoletes:	libguppi15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guppi is an easy-to-use graphical interface for plotting data and
performing statistical manipulations.

%description -l cs
Guppi je nástroj pro analızu a vizualizaci dat pro GNOME.

%description -l da
Guppi er et GNOME-baseret værktøj for analyse og visualisering af
data.

%description -l de
Guppi ist ein GNOME-basiertes System zur Datenanalyse und -anzeige.

%description -l es
Guppi es un sistema de análisis y visualización de datos basado en
GNOME.

%description -l fr
Guppi est un analyseur de données et un système de visualisation basé
sur GNOME.

%description -l it
Guppi è un sistema di analisi e visualizzazione dati basato su GNOME.

%description -l ja
Guppi ¤Ï GNOME ¥Ù¡¼¥¹¤Î¥Ç¡¼¥¿²òÀÏ¤ª¤è¤Ó»ë³Ğ²½¥·¥¹¥Æ¥à¤Ç¤¹¡£

%description -l nb
Guppi er et GNOME-basert verktøy for analyse og visualisering av data.

%description -l pl
Guppi jest ³atwym w u¿yciu graficznym interfejsem do rysowania
wykresów i obliczeñ statystycznych.

%description -l pt_BR
Este pacote contém o Guppi, um analisador e visualizador de dados
baseado no GNOME.

%description -l sv
Guppi är ett GNOME-baserad dataanalys- och -visualiseringssystem.

%package devel
Summary:	Guppi include files
Summary(cs):	Hlavièkové soubory pro vıvoj aplikací s Guppi
Summary(de):	Include-Dateien zur Entwicklung von Guppi-basierten Anwendungen
Summary(es):	Ficheros de inclusión para el desarrollo de aplicaciones Guppi
Summary(fr):	Fichiers à inclure pour le développement d'applications basées sur Guppi
Summary(id):	File header untuk develop aplikasi Guppi
Summary(is):	Hausaskrár fyrir şróun á Guppi forritum
Summary(it):	File include per lo sviluppo di applicazioni basate su Guppi
Summary(nb):	Headerfiler for utvikling av Guppi-baserte applikasjoner
Summary(pl):	Guppi - pliki nag³ówkowe
Summary(pt):	Ficheiros de inclusão para desenvolver aplicações do Guppi
Summary(pt_BR):	Arquivos de inclusão para desenvolvimento
Summary(ru):	æÁÊÌÙ ÚÁÇÏÌÏ×ËÏ× ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ĞÒÉÌÏÖÅÎÉÊ Guppi
Summary(sk):	Hlavièkové súbory pre vıvoj Guppi aplikácií
Summary(sl):	Glave za razvoj programov z Guppi
Summary(sv):	Huvudfiler för att utveckla Guppi-baserade tillämpningar
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	automake
Requires:	gnome-print-devel >= 0.28
Requires:	libglade-gnome-devel
Obsoletes:	libguppi15-devel

%description devel
Header files for Guppi.

%description devel -l cs
Balíèek obsahuje hlavièkové soubory pro vıvoj aplikací pou¾ívajících
Guppi (GNOME Data Analysis and Visualization).

%description devel -l da
Guppi-devel indeholder headerfiler for udvikling af programmer som
bruger rutiner fra Guppi.

%description devel -l de
Das Paket Guppi-devel enthält Header-Dateien für die Entwicklung
mithilfe von Guppi.

%description devel -l es
El paquete Guppi-devel contiene ficheros de cabecera necesarios para
desarrollar Guppi.

%description devel -l fr
Le paquetage Guppi-devel contient fichiers d'en-tête nécessaires au
développement à l'aide de Guppi.

%description devel -l id
File header yang dibutuhkan untuk develop aplikasi Guppi.

%description devel -l is
Şessi pakki inniheldur hausaskrár til şróunar Guppi biğlurum.

%description devel -l it
Il pacchetto Guppi-devel include i file header necessari per lo
sviluppo mediante Guppi.

%description devel -l nb
Guppi-devel inneholder headerfiler for utvikling av applikasjoner som
bruker rutiner fra Guppi.

%description devel -l pl
Pliki nag³ówkowe do Guppi.

%description devel -l pt_BR
Este pacote contém os arquivos necessários para desenvolvimento com o
Guppi.

%description devel -l ru
ğÁËÅÔ Guppi-devel ÓÏÄÅÒÖÉÔ ÆÁÊÌÙ ÚÁÇÏÌÏ×ËÏ×, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ
ÒÁÚÒÁÂÏÔËÉ ĞÒÏÇÒÁÍÍ Ó ÉÓĞÏÌØÚÏ×ÁÎÉÅÍ Guppi.

%description devel -l sk
Hlavièkové súbory potrebné pre vıvoj Guppi.

%description devel -l sl
Razvojni paket Guppi. Vsebuje glave, potrebne za razvijanje z Guppi.

%description devel -l sv
Paketet Guppi-devel innehåller huvudfilerna som behövs för utveckling
av med Guppi.

%package static
Summary:	Guppi static libraries
Summary(cs):	Statické knihovny pro vıvoj aplikací s Guppi
Summary(da):	Statiske biblioteker for udvikling af Guppi-baserede programmer
Summary(de):	Statischen Bibliotheken zur Entwicklung von Guppi-basierten Anwendungen
Summary(es):	Bibliotecas estáticas para el desarrollo de aplicaciones Guppi
Summary(fr):	Bibliothèques statiques pour le développement d'applications basées sur Guppi
Summary(id):	Static library untuk develop aplikasi Guppi
Summary(is):	Ağgerğasöfn fyrir şróun á Guppi forritum
Summary(it):	Librerie statiche per lo sviluppo di applicazioni basate su Guppi
Summary(nb):	Statiske biblioteker for utvikling av Guppi-baserte applikasjoner
Summary(pl):	Biblioteki statyczne Guppi
Summary(pt):	Bibliotecas estáticas para desenvolver aplicações do Guppi
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com Guppi
Summary(ru):	óÔÁÔÉŞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ĞÒÉÌÏÖÅÎÉÊ Guppi
Summary(sk):	Statické kni¾nice pre vıvoj Guppi aplikácií
Summary(sl):	Statiène knji¾nice za razvoj programov z Guppi
Summary(sv):	Statiska bibliotek för att utveckla Guppi-baserade tillämpningar
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Guppi static libraries.

%description static -l cs
Balíèek obsahuje statické knihovny pro vıvoj aplikací pou¾ívajících
Guppi (GNOME Data Analysis and Visualization).

%description static -l da
Guppi-static indeholder statiske bibliotek for udvikling af programmer
som bruger rutiner fra Guppi.

%description static -l de
Das Paket Guppi-static enthält die statischen Bibliotheken für das
Guppi-Paket.

%description static -l es
El paquete Guppi-static contiene las bibliotecas estáticas para el
paquete Guppi.

%description static -l fr
Le paquetage Guppi-static contient les bibliothèques statiques pour le
paquetage Guppi.

%description devel -l id
Static library yang dibutuhkan untuk develop aplikasi Guppi.

%description devel -l is
Şessi pakki inniheldur ağgerğasöfn til şróunar Guppi biğlurum.

%description static -l it
Il pacchetto Guppi-static include le librerie statiche per il
pacchetto Guppi.

%description static -l nb
Guppi-static inneholder statiske bibliotek for utvikling av
applikasjoner som bruker rutiner fra Guppi.

%description static -l pl
Biblioteki statyczne Guppi.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento baseado no Guppi.

%description static -l ru
ğÁËÅÔ Guppi-static ÓÏÄÅÒÖÉÔ ÓÔÁÔÉŞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ
ĞÒÏÇÒÁÍÍ Ó ÉÓĞÏÌØÚÏ×ÁÎÉÅÍ Guppi.

%description static -l sk
Statické kni¾nice potrebné pre vıvoj Guppi.

%description static -l sl
Paket Guppi-static vsebuje statiène knji¾nice, potrebne za razvijanje
z Guppi.

%description static -l sv
Paketet Guppi-static innehåller de statiska biblioteken för paketet
Guppi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

mv -f po/{no,nb}.po
sed -i -e 's/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/' configure.in
sed -i -e 's/nl no pl/nl nb pl/' configure.in

%build
%{__intltoolize}
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoheader}
%{__autoconf}
%{__automake}

%configure \
	%{!?with_gnumeric:--disable-gnumeric} \
	--enable-shlib-factory

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appdir=%{_desktopdir} \
	aclocaldir=%{_aclocaldir}

#install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/guppi/plug-ins/%{version}/plot/*/*.la

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BIBLIOGRAPHY ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libguppi.so.*.*.*
%attr(755,root,root) %{_libdir}/libguppitank.so.*.*.*
%{?with_gnumeric:%attr(755,root,root) %{_libdir}/guppi-gnumeric.so}
%dir %{_libdir}/guppi
%dir %{_libdir}/guppi/plug-ins
%dir %{_libdir}/guppi/plug-ins/%{version}
%dir %{_libdir}/guppi/plug-ins/%{version}/plot
%dir %{_libdir}/guppi/plug-ins/%{version}/plot/*
%{_libdir}/guppi/plug-ins/%{version}/plot/*/*.plugin
%{_libdir}/guppi/plug-ins/%{version}/plot/*/*.glade
%{_libdir}/guppi/plug-ins/%{version}/plot/*/*.png
%attr(755,root,root) %{_libdir}/guppi/plug-ins/%{version}/plot/*/*.so*

%{_datadir}/guppi
%{?with_gnumeric:%{_datadir}/oaf/*.oaf*}
%{_pixmapsdir}/guppi
%{_pixmapsdir}/gnome-guppi.png
#%%{_desktopdir}/*.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguppi.so
%attr(755,root,root) %{_libdir}/libguppitank.so
%{_libdir}/libguppi.la
%{_libdir}/libguppitank.la
%attr(755,root,root) %{_libdir}/libguppiConf.sh
%{_includedir}/gnome-1.0/libguppi
%{_includedir}/gnome-1.0/libguppitank
%{_aclocaldir}/libguppi.m4
