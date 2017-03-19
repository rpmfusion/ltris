Summary: Game of skill with falling blocks
Name: ltris
Version: 1.0.19
Release: 2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://lgames.sourceforge.net/
Source: http://dl.sf.net/lgames/%{name}-%{version}.tar.gz
Patch1: ltris-1.0.19-inlines.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL >= 1.1.4, SDL_mixer
BuildRequires: SDL-devel, SDL_mixer-devel, desktop-file-utils

%description
LTris as a tetris clone which means you have a bowl with blocks falling down.
By rotating and moving the blocks you try to assemble whole lines which then
disappear. LTris has three modes for this: Classic is the classical one where
you play until the bowl becomes filled, Figures resets the bowl contents to a
new figure for each level and adds suddenly appearing tiles and lines later
on and Multiplayer where up to three players either controlled by human or
CPU(!) compete and send completed lines to each other.


%prep
%setup
%patch1 -p1


%build
autoreconf -fiv
%configure --localstatedir=%{_var}/lib/games
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop


%post
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(2551, root, games) %{_bindir}/ltris
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/ltris48.gif
%{_datadir}/ltris/
%config(noreplace) %attr(664, root, games) %{_localstatedir}/lib/games/ltris.hscr


%changelog
* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 11 2015 Sérgio Basto <sergio@serjux.com> - 1.0.19-1
- Update to 1.0.19 .
- Added inlines.patch that fix FTBFS on F22 rfbz #3623.
- Added autoreconf -fiv .
- Added and use .desktop file and ltris icon from sources.
- Removed BR ImageMagick and convert comand to generate icon.
- Removed snipset that generate .desktop file.
- Clean spec file.

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.12-6
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.0.12-4
- rebuild for new F11 features

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.0.12-3
- rebuild for RPM Fusion

* Mon Mar 31 2008 Matthias Saou <http://freshrpms.net/> 1.0.12-1
- Update to 1.0.12.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.0.11-2
- Release bump to drop the disttag number in FC5 build.

* Fri Oct  7 2005 Matthias Saou <http://freshrpms.net/> 1.0.11-1
- Update to 1.0.11.
- Include new translation.

* Sat Feb 19 2005 Matthias Saou <http://freshrpms.net/> 1.0.10-1
- Update to 1.0.10.

* Wed Jan 26 2005 Matthias Saou <http://freshrpms.net/> 1.0.9-1
- Update to 1.0.9.

* Thu May 20 2004 Matthias Saou <http://freshrpms.net/> 1.0.6-1
- Rebuild for Fedora Core 2.
- Update to 1.0.6.
- Added menu entry icon.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.0.5-2
- Rebuild for Fedora Core 1.

* Sun Oct  5 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.5.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.4, doh!
- Rebuilt for Red Hat Linux 9.

* Fri Oct  4 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.

* Fri Jul 26 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.3.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Mon Jan 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.1.

* Thu Jan 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.

* Tue Apr 24 2001 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat 7.1.

* Tue Mar 13 2001 Matthias Saou <http://freshrpms.net/>
- Update to 010310.

* Tue Jan  2 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release for RedHat 7.0

