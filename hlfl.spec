Summary:	High Level Firewall Language
Summary(pl):	Wysokopoziomowy jêzyk zapór ogniowych
Name:		hlfl
Version:	0.60.0
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://www.hlfl.org/hlfl/%{name}-%{version}.tar.bz2
URL:		http://www.hlfl.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{name} is a tool which can produce several types of firewalls from a
given set of rules written in a special language also called hlfl.

%description -l pl
%{name} to narzêdzie pozwalaj±ce generowaæ regu³y zapór ogniowych z
zadanego zestawu napisanego w specjalnym jêzyku zwanym hlfl.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/*hlfl doc/RoadMap doc/syntax.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
