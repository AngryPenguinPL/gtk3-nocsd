Name:		gtk3-nocsd
Version:	3
Release:	1
Summary:	A hack to disable gtk+ 3 client side decoration 
License:	LGPL-2.1
URL:		https://github.com/PCMan/gtk3-nocsd
Source0:	https://github.com/PCMan/gtk3-nocsd/archive/v%{version}.tar.gz

BuildRequires: pkgconfig(pkg-config)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)

%description
gtk3-nocsd is a small module used to disable the client side decoration of Gtk+ 3.

%prep
%setup -q

%build
%make_build

%install
%make_install

%files
