Summary:	C++ wrappers for GConf
Summary(pl):	Interfejsy C++ dla GConfa
Name:		gconfmm
Version:	2.5.1
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	d0116f2d99e8e65fe61ad074a06fc057
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.5.1
BuildRequires:	glibmm-devel >= 2.3.7
BuildRequires:	gtkmm-devel >= 2.3.6
BuildRequires:	pkgconfig
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
Requires:	GConf2-devel >= 2.5.1
Requires:	glibmm-devel >= 2.3.7

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
%attr(755,root,root) %{_libdir}/libgconfmm-2.5.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgconfmm-2.5.so
%{_libdir}/libgconfmm-2.5.la
%{_libdir}/%{name}-*
%{_includedir}/%{name}-2.6
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgconfmm-2.5.a
