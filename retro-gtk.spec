Summary:	Toolkit to write GTK+3-based frontends to libretro
Name:		retro-gtk
Version:	0.10.0
Release:	1
License:	GPL v3
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/retro-gtk/0.10/%{name}-%{version}.tar.xz
# Source0-md5:	491ff8be9a52ec3c11193a98c8ca895c
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	gtk+3-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
retro-gtk wraps the libretro API for use in GTK applications such as
GNOME Games.

%package devel
Summary:	Header files for retro-gtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki retro-gtk
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel
Requires:	glib2-devel
Requires:	gtk+3-devel
Requires:	pulseaudio-devel

%description devel
Header files for retro-gtk library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki retro-gtk.

%package -n vala-retro-gtk
Summary:	retro-gtk library API for Vala language
Summary(pl.UTF-8):	API biblioteki retro-gtk dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.22.0
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-retro-gtk
retro-gtk library API for Vala language.

%description -n vala-retro-gtk -l pl.UTF-8
API biblioteki retro-gtk dla języka Vala.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/retro-gtk

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_libdir}/libretro-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libretro-gtk.so.0
%{_libdir}/girepository-1.0/Retro-0.10.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libretro-gtk.so
%{_includedir}/retro-gtk-0.10
%{_pkgconfigdir}/retro-gtk-0.10.pc
%{_datadir}/gir-1.0/Retro-0.10.gir

%files -n vala-retro-gtk
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/retro-gtk-0.10.deps
%{_datadir}/vala/vapi/retro-gtk-0.10.vapi
