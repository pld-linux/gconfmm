Summary:	C++ wrappers for GConf
Summary(pl):	Interfejsy C++ dla GConfa
Name:		gconfmm
Version:	2.0.1
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	be3a0ddfe4e76c99e1ad78c614e3efb4
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 1.1.8
BuildRequires:	gtkmm-glib-devel >= 2.0.1
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
Requires:	%{name} = %{version}
Requires:	GConf2-devel >= 1.1.8
Requires:	gtkmm-glib-devel >= 2.0.1

%description devel
Devel files for gconfmm.

%description devel -l pl
Pliki nag³ówkowe dla gconfmm.

%package static
Summary:	Static gconfmm library
Summary(pl):	Statyczna biblioteka gconfmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

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
%attr(755,root,root) %{_libdir}/libgconfmm-2.0.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgconfmm-2.0.so
%{_libdir}/libgconfmm-2.0.la
%{_libdir}/%{name}-2.0
%{_includedir}/%{name}-2.0
%{_pkgconfigdir}/%{name}-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgconfmm-2.0.a
