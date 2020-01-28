Summary:	Toolkit to write GTK+3 based frontends to libretro
Summary(pl.UTF-8):	Biblioteka narzędziowa do pisania opartych na GTK+3 frontendów do libretro
Name:		retro-gtk
Version:	0.18.1
Release:	1
License:	GPL v3+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/retro-gtk/0.18/%{name}-%{version}.tar.xz
# Source0-md5:	d8ebec681ca21f038821171731310931
URL:		https://gitlab.gnome.org/GNOME/retro-gtk
BuildRequires:	cairo-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	libepoxy-devel
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	xz
Requires:	glib2 >= 1:2.50
Requires:	gtk+3 >= 3.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
retro-gtk wraps the libretro API for use in GTK+ applications such as
GNOME Games.

%description -l pl.UTF-8
retro-gtk obudowuje API libretro w sposób nadający się do użycia w
aplikacjach GTK+, takich jak GNOME Games.

%package devel
Summary:	Header files for retro-gtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki retro-gtk
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdk-pixbuf2-devel >= 2.0
Requires:	glib2-devel >= 1:2.50

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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md UNIMPLEMENTED.md
%attr(755,root,root) %{_bindir}/retro-demo
%attr(755,root,root) %{_libdir}/libretro-gtk-0.14.so.0
%{_libdir}/girepository-1.0/Retro-0.14.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libretro-gtk-0.14.so
%{_includedir}/retro-gtk
%{_datadir}/gir-1.0/Retro-0.14.gir
%{_pkgconfigdir}/retro-gtk-0.14.pc

%files -n vala-retro-gtk
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/retro-gtk-0.14.deps
%{_datadir}/vala/vapi/retro-gtk-0.14.vapi
