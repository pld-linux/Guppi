%define  ver     0.34.2
%define  rel     1
%define  prefix  /usr

Summary: GNOME Plotting Engine
Name: Guppi
Version: %ver
Release: %rel
Copyright: GPL
Group: X11/GNOME/Applications
Source: ftp://ftp.gnome.org/pub/guppi/Guppi-%{ver}.tar.gz
Url: http://www.gnome.org/guppi
BuildRoot: /var/tmp/Guppi-%{ver}-root
Requires: guile >= 1.3.4

%description
GNOME is the GNU Network Object Model Environment. This powerful environment is both easy to use and easy to configure.

This package will install Guppi, a GNOME plotting engine.

Install this package if you want to test Guppi.

%description - pl
GNOME to skrót od GNU Network Object Model Environment (¶rodowisko sieciowego 
modelu obiektowego GNU). ¦rodowisko to jest ³atwe zarówno w uzyciu jak i konfiguracji.
Ten pakiet zainstaluje Guppi, silnik rysuj±cy GNOME.
nalezy go zainstalowac je¶li chce sie przetestowaæ Guppi.

%prep
%setup

%build
%ifarch alpha
  MYARCH_FLAGS="--host=alpha-redhat-linux"
%endif
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix $MYARCH_FLAGS --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install-strip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS BIBLIOGRAPHY ChangeLog NEWS README

%{prefix}/*

%changelog

* Mon Feb 28 2000 Kenny Graunke <graunke@teleport.com>
- Upgrade to 0.34.2 (which turns off readline, thank goodness)

* Mon Feb 22 2000 Kenny Graunke <graunke@teleport.com>
- This 0.34.1-1rl enables readline. If Guppi complains about undefined symbols
  in libguilereadline.so when you start it, get the readline disabled RPM.

* Mon Feb 22 2000 Kenny Graunke <graunke@teleport.com>

- Updated to 0.34.1 (using repackaged source, ugh), spec file rewrite
- This 0.34.1 source disables readline due to broken libguilereadline.so
  problems in every guile 1.3.4 x86 RPM I've seen...

* Wed Jan 26 2000 Conrad Steenberg <conrad@srl.caltech.edu>

- Some Alpha fixes for configure
- Remove some unneeded stripping foo and just do a 'make install-strip' instead.
- Move this changelog to the bottom of the file :-)

* Mon Jan 24 2000 Kenny Graunke <graunke@teleport.com>

- First Guppi RPM
