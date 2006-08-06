Summary:	C++ wrappers for GConf
Summary(pl):	Interfejsy C++ dla GConfa
Name:		gconfmm
Version:	2.14.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gconfmm/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	adcaeb572c466c1395b35d0271ac6438
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibmm-devel >= 2.10.0
BuildRequires:	gtkmm-devel >= 2.8.0
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	pkgconfig
Requires:	GConf2 >= 2.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for GConf. All classes are in the Gnome::Conf namespace.

%description -l pl
Interfejsy C++ dla GConfa. Wszystkie klasy s± w przestrzeni nazw
Gnome::Conf.

%package devel
Summary:	Devel files for gconfmm
Summary(pl):	Pliki nag³ówkowe dla gconfmm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.14.0
Requires:	glibmm-devel >= 2.10.0

%description devel
Devel files for gconfmm.

%description devel -l pl
Pliki nag³ówkowe dla gconfmm.

%package static
Summary:	Static gconfmm library
Summary(pl):	Statyczna biblioteka gconfmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gconfmm library.

%description static -l pl
Statyczna biblioteka gconfmm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgconfmm-2.6.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgconfmm-2.6.so
%{_libdir}/libgconfmm-2.6.la
%{_libdir}/%{name}-*
%{_includedir}/%{name}-2.6
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgconfmm-2.6.a
