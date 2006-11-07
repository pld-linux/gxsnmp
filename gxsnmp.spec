Summary:	GXSNMP Network Management Application
Summary(pl):	GXSNMP - aplikacja do zarz±dzania sieci±
Name:		gxsnmp
Version:	0.0.16
Release:	12
License:	GPL
Group:		X11/Applications
Source0:	ftp://coco.comstar.net/pub/gxsnmp/%{name}-%{version}.tar.gz
# Source0-md5:	d37f7c85fd96861e8e88e7092d2cb913
Patch0:		%{name}-mib-browser.patch
Patch1:		%{name}-am15.patch
Patch2:		%{name}-MIBs_path.patch
Patch3:		%{name}-ac_fixes.patch
Patch4:		%{name}-iputil.c_fix.patch
Patch5:		%{name}-desktop.patch
Patch6:		%{name}-errno.patch
Patch7:		%{name}-locale_names.patch
URL:		http://www.gxsnmp.org/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	libsmi-devel >= 0.2
BuildRequires:	libtool
BuildRequires:	mysql-devel >= 3.23.32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
GXSNMP is the SNMP network managament application.

%description -l pl
GXSNMP to aplikacja do zarz±dzania sieci± przez SNMP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

mv -f po/{no,nb}.po
sed -e 's/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/; s/AM_ACLOCAL_INCLUDE.*//' \
	configure.in > configure.in.new
mv -f configure.in.new configure.in

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--with-gnome \
	--with-mysql
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT \
	 Admindir=%{_desktopdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gxsnmp
%dir %{_libdir}/gxsnmp/plugins
%attr(755,root,root) /%{_libdir}/gxsnmp/plugins/lib*.so*
%{_desktopdir}/*.desktop
%{_datadir}/gxsnmp
%{_pixmapsdir}/gxsnmp
