Summary:	Utilites for gEDA project - netlist generator
Summary(pl):	Narzêdzia dla projektu gEDA - generator po³±czeñ
Name:		geda-gnetlist
Version:	20040111
Release:	0.1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9bbeb64aea9455468d5aef16685a03de
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

%description -l pl
Gnetlist generuje pliki opisuj±ce sieæ po³±czeñ miêdzy elementami
schematu narysowanego w edytorze gschem (z projektu gEDA). Obs³uguje
wiele formatów wyj¶ciowych, w tym natywny, Tango, Spice, Allegro, PCB,
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
