Summary:	Utilites for gEDA project - netlist generator
Summary(pl.UTF-8):	Narzędzia dla projektu gEDA - generator połączeń
Name:		geda-gnetlist
Version:	1.2.0
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.geda.seul.org/pub/geda/release/v1.2/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fe435c8124df5ee85e46f3f1e329ff70
URL:		http://www.geda.seul.org/
BuildRequires:	libgeda-devel >= %{version}
BuildRequires:	pkgconfig
Requires:	geda-symbols >= %{version}
Requires:	libgeda >= %{version}
Obsoletes:	gnetlist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnetlist generates netlists from schematics drawn with gschem (the
gEDA schematic editor). It supports many output formats including
native, Tango, Spice, Allegro, PCB, Verilog...

%description -l pl.UTF-8
Gnetlist generuje pliki opisujące sieć połączeń między elementami
schematu narysowanego w edytorze gschem (z projektu gEDA). Obsługuje
wiele formatów wyjściowych, w tym natywny, Tango, Spice, Allegro, PCB,
Verilog...

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO docs/{README.*,vams/*.txt}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gEDA/scheme/*
%{_datadir}/gEDA/system-gnetlistrc
%{_mandir}/man*/*
%{_docdir}/geda-doc/readmes/*
%{_docdir}/geda-doc/man/*
