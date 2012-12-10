%define name gnome-activity-journal
%define version 0.8.0
%define release %mkrel 1

Summary: GUI to browse and search your Zeitgeist activities
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://launchpad.net/%name/0.8/%version/+download/%name-%version.tar.gz
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
%setup -q -n %{name}-%{version}

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
%_datadir/pixmaps/%name.xpm
%_datadir/zeitgeist/_zeitgeist/engine/extensions/gnome_activity_journal.py


%changelog
* Mon Jul 18 2011 Götz Waschk <waschk@mandriva.org> 0.8.0-1mdv2011
+ Revision: 690223
- new version

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.6.0-2
+ Revision: 677707
- rebuild to add gconftool as req

* Thu Jan 27 2011 Götz Waschk <waschk@mandriva.org> 0.6.0-1
+ Revision: 633485
- new version
- update URL

* Wed Nov 03 2010 Götz Waschk <waschk@mandriva.org> 0.5.0.1-2mdv2011.0
+ Revision: 592937
- rebuild for new python 2.7

* Thu Sep 23 2010 Götz Waschk <waschk@mandriva.org> 0.5.0.1-1mdv2011.0
+ Revision: 580704
- new version

* Tue Aug 24 2010 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2011.0
+ Revision: 572932
- new version
- update file list
- update source URL

  + Olivier Faurax <ofaurax@mandriva.org>
    - bad extension for pixmaps (svg -> xpm)
    - forcing new release
    - Updated tar.gz to 0.3.4.1

* Thu Aug 05 2010 Götz Waschk <waschk@mandriva.org> 0.3.4.1-1mdv2011.0
+ Revision: 566419
- update to new version 0.3.4.1

* Sun Feb 21 2010 Götz Waschk <waschk@mandriva.org> 0.3.3-1mdv2010.1
+ Revision: 509023
- update to new version 0.3.3

* Wed Jan 20 2010 Götz Waschk <waschk@mandriva.org> 0.3.2-1mdv2010.1
+ Revision: 493968
- import gnome-activity-journal


