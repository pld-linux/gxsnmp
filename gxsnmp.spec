Summary:	GXSNMP Network Management Application
Name:		gxsnmp
Version:	0.0.13
Release:	1
Copyright:	GPL
Group:		X11/GNOME
Source:		ftp://coco.comstar.net/pub/gxsnmp/%{name}-%{version}.tar.gz
BuildRequires:	ORBit-devel
BuildRequires:	gtk+-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
URL:		http://www.gxsnmp.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description 
GXSNMP Is the SNMP network managament application.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
gettextize --copy --force
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%{_bindir}/*
%{_datadir}/pixmaps

%changelog
