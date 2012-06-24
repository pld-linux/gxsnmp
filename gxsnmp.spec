Summary:	GXSNMP Network Management Application
Name:		gxsnmp
Version:	0.0.15.1
Release:	4
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://coco.comstar.net/pub/gxsnmp/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-mib-browser.patch
URL:		http://www.gxsnmp.org/
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
BuildRequires:	gtk+-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	perl
BuildRequires:	libsmi-devel >= 0.2
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_infodir	/usr/share/info
%define		_sysconfdir	/etc/X11/GNOME

%description 
GXSNMP Is the SNMP network managament application.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
gettextize --copy --force
CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g} -I%{_includedir}"
%configure \
	--disable-static \
	--with-gnome \
	--with-mysql \
	--with-pgsql
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT \
	 Admindir=%{_applnkdir}/Network/Misc

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gxsnmp
%dir %{_libdir}/gxsnmp/plugins
%attr(755,root,root) /%{_libdir}/gxsnmp/plugins/*
%{_applnkdir}/Network/Misc/*
%{_datadir}/gxsnmp
%{_datadir}/pixmaps/gxsnmp

%dir %{_datadir}/gnome/help/gxsnmp
%lang(en) %{_datadir}/gnome/help/gxsnmp/C
