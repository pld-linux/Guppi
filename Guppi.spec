Summary:	Guppi - GNOME Plotting Engine
Summary(cs):	Analýza a vizualizace dat pod GNOME
Summary(da):	GNOME-værktøj for analyse og visualisering af data
Summary(de):	GNOME Datenanalyse und -anzeige
Summary(es):	Análisis y Visualización de Datos de GNOME
Summary(fr):	Analyseur et visualiseur de données de GNOME
Summary(it):	Analisi e Visualizzazione Dati GNOME
Summary(ja):	GNOME ¥Ù¡¼¥¹¤Î¥Ç¡¼¥¿²òÀÏ¤ª¤è¤Ó»ë³Ð²½
Summary(nb):	GNOME-verktøy for analyse og visualisering av data
Summary(pl):	Guppi - Silnik Rysuj±cy GNOME
Summary(pt_BR):	Analisador e visualizador de dados do GNOME
Summary(sl):	Analiza podatkov in vizualizacija v GNOME
Summary(sv):	GNOME dataanalys och -visualisering
Summary(zh_CN):	Guppi - GNOME½»»¥Ê½Êý¾Ý·ÖÎö¹¤¾ß
Name:		Guppi
Version:	0.40.3
Release:	9
Epoch:		2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/Guppi/0.40/%{name}-%{version}.tar.bz2
# Source0-md5:	26ec6eb5b6fe7fb4e32ecff64d4f1b16
Source1:	%{name}.desktop
Patch0:		%{name}-am_ac.patch
Patch1:		%{name}-am_hack.patch
URL:		http://www.gnome.org/guppi/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	flex
BuildRequires:	gdk-pixbuf-gnome-devel >= 0.8.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	gtk+-devel > 1.2.0
BuildRequires:	intltool
BuildRequires:	libglade-gnome-devel
BuildRequires:	libxml-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BuildRequires:	gnumeric >= 1.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	ghostscript-fonts-std
Obsoletes:	libguppi15


%description
Guppi is an easy-to-use graphical interface for plotting data and
performing statistical manipulations.

%description -l cs
Guppi je nástroj pro analýzu a vizualizaci dat pro GNOME.

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
Guppi ¤Ï GNOME ¥Ù¡¼¥¹¤Î¥Ç¡¼¥¿²òÀÏ¤ª¤è¤Ó»ë³Ð²½¥·¥¹¥Æ¥à¤Ç¤¹¡£

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
Summary(cs):	Hlavièkové soubory pro vývoj aplikací s Guppi
Summary(de):	Include-Dateien zur Entwicklung von Guppi-basierten Anwendungen
Summary(es):	Ficheros de inclusión para el desarrollo de aplicaciones Guppi
Summary(fr):	Fichiers à inclure pour le développement d'applications basées sur Guppi
Summary(id):	File header untuk develop aplikasi Guppi
Summary(is):	Hausaskrár fyrir þróun á Guppi forritum
Summary(it):	File include per lo sviluppo di applicazioni basate su Guppi
Summary(nb):	Headerfiler for utvikling av Guppi-baserte applikasjoner
Summary(pl):	Guppi - pliki nag³ówkowe
Summary(pt):	Ficheiros de inclusão para desenvolver aplicações do Guppi
Summary(pt_BR):	Arquivos de inclusão para desenvolvimento
Summary(ru):	æÁÊÌÙ ÚÁÇÏÌÏ×ËÏ× ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÉÌÏÖÅÎÉÊ Guppi
Summary(sk):	Hlavièkové súbory pre vývoj Guppi aplikácií
Summary(sl):	Glave za razvoj programov z Guppi
Summary(sv):	Huvudfiler för att utveckla Guppi-baserade tillämpningar
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
Obsoletes:	libguppi15-devel

%description devel
Header files for Guppi.

%description devel -l cs
Balíèek obsahuje hlavièkové soubory pro vývoj aplikací pou¾ívajících
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
Þessi pakki inniheldur hausaskrár til þróunar Guppi biðlurum.

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
ðÁËÅÔ Guppi-devel ÓÏÄÅÒÖÉÔ ÆÁÊÌÙ ÚÁÇÏÌÏ×ËÏ×, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ
ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ Guppi.

%description devel -l sk
Hlavièkové súbory potrebné pre vývoj Guppi.

%description devel -l sl
Razvojni paket Guppi. Vsebuje glave, potrebne za razvijanje z Guppi.

%description devel -l sv
Paketet Guppi-devel innehåller huvudfilerna som behövs för utveckling
av med Guppi.

%package static
Summary:	Guppi static libraries
Summary(cs):	Statické knihovny pro vývoj aplikací s Guppi
Summary(da):	Statiske biblioteker for udvikling af Guppi-baserede programmer
Summary(de):	Statischen Bibliotheken zur Entwicklung von Guppi-basierten Anwendungen
Summary(es):	Bibliotecas estáticas para el desarrollo de aplicaciones Guppi
Summary(fr):	Bibliothèques statiques pour le développement d'applications basées sur Guppi
Summary(id):	Static library untuk develop aplikasi Guppi
Summary(is):	Aðgerðasöfn fyrir þróun á Guppi forritum
Summary(it):	Librerie statiche per lo sviluppo di applicazioni basate su Guppi
Summary(nb):	Statiske biblioteker for utvikling av Guppi-baserte applikasjoner
Summary(pl):	Biblioteki statyczne Guppi
Summary(pt):	Bibliotecas estáticas para desenvolver aplicações do Guppi
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com Guppi
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÉÌÏÖÅÎÉÊ Guppi
Summary(sk):	Statické kni¾nice pre vývoj Guppi aplikácií
Summary(sl):	Statiène knji¾nice za razvoj programov z Guppi
Summary(sv):	Statiska bibliotek för att utveckla Guppi-baserade tillämpningar
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Guppi static libraries.

%description static -l cs
Balíèek obsahuje statické knihovny pro vývoj aplikací pou¾ívajících
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
Þessi pakki inniheldur aðgerðasöfn til þróunar Guppi biðlurum.

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
ðÁËÅÔ Guppi-static ÓÏÄÅÒÖÉÔ ÓÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ
ÐÒÏÇÒÁÍÍ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ Guppi.

%description static -l sk
Statické kni¾nice potrebné pre vývoj Guppi.

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

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
xml-i18n-toolize --copy --force
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoheader}
%{__autoconf}
%{__automake}

%configure \
	--enable-shlib-factory \
	--enable-gnumeric

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appdir=%{_applnkdir}/Graphics \
	aclocaldir=%{_aclocaldir}

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BIBLIOGRAPHY ChangeLog NEWS README
#%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/guppi-gnumeric.so
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
#%%{_applnkdir}/Graphics/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/libguppiConf.sh
%{_includedir}/gnome-*/*
%{_aclocaldir}/*.m4
