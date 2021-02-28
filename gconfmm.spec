Summary:	C++ wrappers for GConf
Summary(pl.UTF-8):	Interfejsy C++ dla GConfa
Name:		gconfmm
Version:	2.28.3
Release:	3
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gconfmm/2.28/%{name}-%{version}.tar.bz2
# Source0-md5:	ebcf96373cb0c71bc4cfad0e6da83779
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.19.1
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	glibmm-devel >= 2.14.1
BuildRequires:	gtkmm-devel >= 2.4.0
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	mm-common >= 0.9.5
BuildRequires:	pkgconfig
Requires:	GConf2-libs >= 2.19.1
Requires:	glibmm >= 2.14.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for GConf. All classes are in the Gnome::Conf namespace.

%description -l pl.UTF-8
Interfejsy C++ dla GConfa. Wszystkie klasy są w przestrzeni nazw
Gnome::Conf.

%package devel
Summary:	Devel files for gconfmm
Summary(pl.UTF-8):	Pliki nagłówkowe dla gconfmm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.19.1
Requires:	glibmm-devel >= 2.14.1

%description devel
Devel files for gconfmm.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla gconfmm.

%package static
Summary:	Static gconfmm library
Summary(pl.UTF-8):	Statyczna biblioteka gconfmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gconfmm library.

%description static -l pl.UTF-8
Statyczna biblioteka gconfmm.

%package apidocs
Summary:	Reference documentation for gconfmm
Summary(pl.UTF-8):	Szczegółowa dokumentacja dla gconfmm
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
Reference documentation for gconfmm.

%description apidocs -l pl.UTF-8
Szczegółowa dokumentacja dla gconfmm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdocdir=%{_gtkdocdir}/gconfmm-2.6

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgconfmm-2.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgconfmm-2.6.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgconfmm-2.6.so
%{_libdir}/%{name}-2.6
%{_includedir}/%{name}-2.6
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgconfmm-2.6.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gconfmm-2.6
