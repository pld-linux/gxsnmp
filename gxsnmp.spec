%define ver      0.13
%define rel      1
%define prefix   /usr

Summary: GXSNMP Network Management Application
Name: gxsnmp
Version: %ver
Release: %rel
Copyright: GPL
Group: X11/gnome
Source: ftp://coco.comstar.net/pub/gxsnmp/gxsnmp-%{ver}.tar.gz
BuildRoot: /tmp/gxsnmp-root
Obsoletes: gxsnmp
Packager: Gregory McLean <gregm@comstar.net>
URL: http://www.gxsnmp.org
Docdir: %{prefix}/doc

%description 
GXSNMP Is the SNMP network managament application.

%changelog

* Sat Feb 20 1999 Gregory McLean <gregm@comstar.net>

- Initial version

%prep
%setup

%build
# I do this as alpha's tend to return random id's
%ifarch alpha
  CFLAGS="$RPM_OPT_FLAGS" ./configure --host=alpha-redhat-linux --prefix=%prefix --sysconfdir="/etc"
%else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix --sysconfdir="/etc"
%endif
if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT/etc install

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin
%{prefix}/share/pixmaps
