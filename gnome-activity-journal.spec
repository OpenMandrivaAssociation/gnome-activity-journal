%define name gnome-activity-journal
%define version 0.3.2
%define unmangled_version 0.3.2
%define release %mkrel 1

Summary: GUI to browse and search your Zeitgeist activities
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://launchpad.net/%name/0.3/%version/+download/%{name}-%{unmangled_version}.tar.gz
License: GPLv3+
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-distutils-extra
BuildRequires: python-setuptools
BuildRequires: intltool
Url: https://launchpad.net/gnome-activity-journal
Requires: zeitgeist >= 0.3.1
Requires: gnome-python
Requires: gnome-python-gconf

%description

GNOME Activity Journal is a tool for easily browsing and finding files on 
your computer. It shows a chronological journal of all file activity and 
supports full-text search through Tracker.

%prep
%setup -q -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
rm -rf %buildroot %name.lang
python setup.py install --root=$RPM_BUILD_ROOT
%find_lang %name
mkdir -p %buildroot%_sysconfdir
mv %buildroot%_datadir/gconf %buildroot%_sysconfdir

%clean
rm -rf $RPM_BUILD_ROOT

%preun
%preun_uninstall_gconf_schemas %name

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS
%_sysconfdir/gconf/schemas/%name.schemas
%_bindir/%name
%py_puresitedir/*.egg-info
%_datadir/applications/%name.desktop
%_datadir/%name
%_datadir/icons/hicolor/*/*/*
%_mandir/man1/%name.1*
%_datadir/pixmaps/%name.svg
