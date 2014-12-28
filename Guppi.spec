#
# Conditional build:
%bcond_with	gnumeric	# build with support for GNOME1-based gnumeric
#
Summary:	Guppi - GNOME Plotting Engine
Summary(cs.UTF-8):	Analýza a vizualizace dat pod GNOME
Summary(da.UTF-8):	GNOME-værktøj for analyse og visualisering af data
Summary(de.UTF-8):	GNOME Datenanalyse und -anzeige
Summary(es.UTF-8):	Análisis y Visualización de Datos de GNOME
Summary(fr.UTF-8):	Analyseur et visualiseur de données de GNOME
Summary(it.UTF-8):	Analisi e Visualizzazione Dati GNOME
Summary(ja.UTF-8):	GNOME ベースのデータ解析および視覚化
Summary(nb.UTF-8):	GNOME-verktøy for analyse og visualisering av data
Summary(pl.UTF-8):	Guppi - Silnik Rysujący GNOME
Summary(pt_BR.UTF-8):	Analisador e visualizador de dados do GNOME
Summary(sl.UTF-8):	Analiza podatkov in vizualizacija v GNOME
Summary(sv.UTF-8):	GNOME dataanalys och -visualisering
Summary(zh_CN.UTF-8):	Guppi - GNOME交互式数据分析工具
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
BuildRequires:	gettext-tools
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
Requires:	fonts-Type1-urw
Requires:	gdk-pixbuf >= 0.11.0
Requires:	gnome-print >= 0.28
Requires:	libart_lgpl >= 2.2.0
Obsoletes:	libguppi15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guppi is an easy-to-use graphical interface for plotting data and
performing statistical manipulations.

%description -l cs.UTF-8
Guppi je nástroj pro analýzu a vizualizaci dat pro GNOME.

%description -l da.UTF-8
Guppi er et GNOME-baseret værktøj for analyse og visualisering af
data.

%description -l de.UTF-8
Guppi ist ein GNOME-basiertes System zur Datenanalyse und -anzeige.

%description -l es.UTF-8
Guppi es un sistema de análisis y visualización de datos basado en
GNOME.

%description -l fr.UTF-8
Guppi est un analyseur de données et un système de visualisation basé
sur GNOME.

%description -l it.UTF-8
Guppi è un sistema di analisi e visualizzazione dati basato su GNOME.

%description -l ja.UTF-8
Guppi は GNOME ベースのデータ解析および視覚化システムです。

%description -l nb.UTF-8
Guppi er et GNOME-basert verktøy for analyse og visualisering av data.

%description -l pl.UTF-8
Guppi jest łatwym w użyciu graficznym interfejsem do rysowania
wykresów i obliczeń statystycznych.

%description -l pt_BR.UTF-8
Este pacote contém o Guppi, um analisador e visualizador de dados
baseado no GNOME.

%description -l sv.UTF-8
Guppi är ett GNOME-baserad dataanalys- och -visualiseringssystem.

%package devel
Summary:	Guppi include files
Summary(cs.UTF-8):	Hlavičkové soubory pro vývoj aplikací s Guppi
Summary(de.UTF-8):	Include-Dateien zur Entwicklung von Guppi-basierten Anwendungen
Summary(es.UTF-8):	Ficheros de inclusión para el desarrollo de aplicaciones Guppi
Summary(fr.UTF-8):	Fichiers à inclure pour le développement d'applications basées sur Guppi
Summary(id.UTF-8):	File header untuk develop aplikasi Guppi
Summary(is.UTF-8):	Hausaskrár fyrir þróun á Guppi forritum
Summary(it.UTF-8):	File include per lo sviluppo di applicazioni basate su Guppi
Summary(nb.UTF-8):	Headerfiler for utvikling av Guppi-baserte applikasjoner
Summary(pl.UTF-8):	Guppi - pliki nagłówkowe
Summary(pt.UTF-8):	Ficheiros de inclusão para desenvolver aplicações do Guppi
Summary(pt_BR.UTF-8):	Arquivos de inclusão para desenvolvimento
Summary(ru.UTF-8):	Файлы заголовков для разработки приложений Guppi
Summary(sk.UTF-8):	Hlavičkové súbory pre vývoj Guppi aplikácií
Summary(sl.UTF-8):	Glave za razvoj programov z Guppi
Summary(sv.UTF-8):	Huvudfiler för att utveckla Guppi-baserade tillämpningar
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gnome-print-devel >= 0.28
Requires:	libglade-gnome-devel
Obsoletes:	libguppi15-devel

%description devel
Header files for Guppi.

%description devel -l cs.UTF-8
Balíček obsahuje hlavičkové soubory pro vývoj aplikací používajících
Guppi (GNOME Data Analysis and Visualization).

%description devel -l da.UTF-8
Guppi-devel indeholder headerfiler for udvikling af programmer som
bruger rutiner fra Guppi.

%description devel -l de.UTF-8
Das Paket Guppi-devel enthält Header-Dateien für die Entwicklung
mithilfe von Guppi.

%description devel -l es.UTF-8
El paquete Guppi-devel contiene ficheros de cabecera necesarios para
desarrollar Guppi.

%description devel -l fr.UTF-8
Le paquetage Guppi-devel contient fichiers d'en-tête nécessaires au
développement à l'aide de Guppi.

%description devel -l id.UTF-8
File header yang dibutuhkan untuk develop aplikasi Guppi.

%description devel -l is.UTF-8
Þessi pakki inniheldur hausaskrár til þróunar Guppi biðlurum.

%description devel -l it.UTF-8
Il pacchetto Guppi-devel include i file header necessari per lo
sviluppo mediante Guppi.

%description devel -l nb.UTF-8
Guppi-devel inneholder headerfiler for utvikling av applikasjoner som
bruker rutiner fra Guppi.

%description devel -l pl.UTF-8
Pliki nagłówkowe do Guppi.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos necessários para desenvolvimento com o
Guppi.

%description devel -l ru.UTF-8
Пакет Guppi-devel содержит файлы заголовков, необходимые для
разработки программ с использованием Guppi.

%description devel -l sk.UTF-8
Hlavičkové súbory potrebné pre vývoj Guppi.

%description devel -l sl.UTF-8
Razvojni paket Guppi. Vsebuje glave, potrebne za razvijanje z Guppi.

%description devel -l sv.UTF-8
Paketet Guppi-devel innehåller huvudfilerna som behövs för utveckling
av med Guppi.

%package static
Summary:	Guppi static libraries
Summary(cs.UTF-8):	Statické knihovny pro vývoj aplikací s Guppi
Summary(da.UTF-8):	Statiske biblioteker for udvikling af Guppi-baserede programmer
Summary(de.UTF-8):	Statischen Bibliotheken zur Entwicklung von Guppi-basierten Anwendungen
Summary(es.UTF-8):	Bibliotecas estáticas para el desarrollo de aplicaciones Guppi
Summary(fr.UTF-8):	Bibliothèques statiques pour le développement d'applications basées sur Guppi
Summary(id.UTF-8):	Static library untuk develop aplikasi Guppi
Summary(is.UTF-8):	Aðgerðasöfn fyrir þróun á Guppi forritum
Summary(it.UTF-8):	Librerie statiche per lo sviluppo di applicazioni basate su Guppi
Summary(nb.UTF-8):	Statiske biblioteker for utvikling av Guppi-baserte applikasjoner
Summary(pl.UTF-8):	Biblioteki statyczne Guppi
Summary(pt.UTF-8):	Bibliotecas estáticas para desenvolver aplicações do Guppi
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com Guppi
Summary(ru.UTF-8):	Статические библиотеки для разработки приложений Guppi
Summary(sk.UTF-8):	Statické knižnice pre vývoj Guppi aplikácií
Summary(sl.UTF-8):	Statične knjižnice za razvoj programov z Guppi
Summary(sv.UTF-8):	Statiska bibliotek för att utveckla Guppi-baserade tillämpningar
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Guppi static libraries.

%description static -l cs.UTF-8
Balíček obsahuje statické knihovny pro vývoj aplikací používajících
Guppi (GNOME Data Analysis and Visualization).

%description static -l da.UTF-8
Guppi-static indeholder statiske bibliotek for udvikling af programmer
som bruger rutiner fra Guppi.

%description static -l de.UTF-8
Das Paket Guppi-static enthält die statischen Bibliotheken für das
Guppi-Paket.

%description static -l es.UTF-8
El paquete Guppi-static contiene las bibliotecas estáticas para el
paquete Guppi.

%description static -l fr.UTF-8
Le paquetage Guppi-static contient les bibliothèques statiques pour le
paquetage Guppi.

%description static -l id.UTF-8
Static library yang dibutuhkan untuk develop aplikasi Guppi.

%description static -l is.UTF-8
Þessi pakki inniheldur aðgerðasöfn til þróunar Guppi biðlurum.

%description static -l it.UTF-8
Il pacchetto Guppi-static include le librerie statiche per il
pacchetto Guppi.

%description static -l nb.UTF-8
Guppi-static inneholder statiske bibliotek for utvikling av
applikasjoner som bruker rutiner fra Guppi.

%description static -l pl.UTF-8
Biblioteki statyczne Guppi.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento baseado no Guppi.

%description static -l ru.UTF-8
Пакет Guppi-static содержит статические библиотеки для разработки
программ с использованием Guppi.

%description static -l sk.UTF-8
Statické knižnice potrebné pre vývoj Guppi.

%description static -l sl.UTF-8
Paket Guppi-static vsebuje statične knjižnice, potrebne za razvijanje
z Guppi.

%description static -l sv.UTF-8
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
