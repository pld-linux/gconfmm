Summary:	C++ wrappers for GConf
Name:		gconfmm
Version:	2.0.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.0/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	automake
BuildRequires:	GConf2-devel >= 1.1.8
BuildRequires:	gtkmm-devel >= 2.0.1
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for GConf. All classes are in the Gnome::Conf namespace.

%package devel
Summary:	Devel files for gconfmm
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Devel files for gconfmm.

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
%attr(755,root,root) %{_libdir}/libgconfmm-2.0.so.*

%files devel
%{_includedir}/%{name}-2.0
%{_libdir}/libgconfmm-2.0.la
%{_libdir}/libgconfmm-2.0.so
%{_libdir}/%{name}-2.0
%{_pkgconfigdir}/%{name}-2.0.pc
