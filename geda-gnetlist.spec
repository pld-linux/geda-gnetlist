Summary:	Utilites for gEDA project
Summary(pl):	Narzêdzia dla projektu gEDA
Name:		geda-gnetlist
Version:	20030901
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1e33f3a3bcac190bf209af58c31ccf93
URL:		http://www.geda.seul.org/
BuildRequires:	libgeda-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gEDA netlist generator.

%description -l pl
Generator plików opisuj±cych sieæ po³±czeñ dla projektu gEDA.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gEDA/scheme/*
%{_datadir}/gEDA/system-gnetlistrc
%{_mandir}/man*/*
