%global appver  1.1.13
%global apprel  0

Name:           twintaillauncher
Version:        %{appver}
Release:        1%{?dist}
Summary:        A multi-platform launcher for your anime games

License:        GPL-3.0
URL:            https://twintaillauncher.app/
Source0:        https://github.com/TwintailTeam/TwintailLauncher/releases/download/ttl-v%{appver}/twintaillauncher_%{appver}_amd64.deb

ExclusiveArch: x86_64

# Dependencies based on Arch Linux PKGBUILD
Requires:       cairo
Requires:       desktop-file-utils
Requires:       gdk-pixbuf2
Requires:       glib2
Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       libappindicator-gtk3
Requires:       libayatana-appindicator-gtk3
Requires:       pango
Requires:       webkit2gtk4.1

# Build requires for extract DEB
BuildRequires:  binutils
BuildRequires:  tar
BuildRequires:  gzip

%description
Twintaillauncher is a multi-platform launcher that brings mod support, quality-of-life improvements, and advanced features to a variety of anime-styled games.
TTL is an all-in-one tool for downloading, managing, and launching your favorite anime games. It’s designed with flexibility, ease of use, and customization in mind.

%prep
# Extract .deb file
ar x %{SOURCE0}
tar -xzf data.tar.gz

%build
# No build stuff

%install
rm -rf %{buildroot}

# Copying stuff to buildroot
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{32x32,128x128,256x256@2}/apps
mkdir -p %{buildroot}/usr/lib/twintaillauncher/resources

# Actual files
cp -p usr/bin/twintaillauncher %{buildroot}%{_bindir}/twintaillauncher
cp -p usr/share/applications/twintaillauncher.desktop %{buildroot}%{_datadir}/applications/
cp -p usr/share/icons/hicolor/32x32/apps/twintaillauncher.png \
   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
cp -p usr/share/icons/hicolor/128x128/apps/twintaillauncher.png \
   %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
cp -p usr/share/icons/hicolor/256x256@2/apps/twintaillauncher.png \
   %{buildroot}%{_datadir}/icons/hicolor/256x256@2/apps/
cp -p usr/lib/twintaillauncher/resources/hpatchz %{buildroot}/usr/lib/twintaillauncher/resources/
cp -p usr/lib/twintaillauncher/resources/reaper %{buildroot}/usr/lib/twintaillauncher/resources/
cp -p usr/lib/twintaillauncher/resources/hkrpg_patch.dll %{buildroot}/usr/lib/twintaillauncher/resources/


%post
# Update desktop database & icon cache
update-desktop-database %{_datadir}/applications &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
# Update desktop database & icon cache after uninstall
update-desktop-database %{_datadir}/applications &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files
%{_bindir}/twintaillauncher
%{_datadir}/applications/twintaillauncher.desktop
%{_datadir}/icons/hicolor/32x32/apps/twintaillauncher.png
%{_datadir}/icons/hicolor/128x128/apps/twintaillauncher.png
%{_datadir}/icons/hicolor/256x256@2/apps/twintaillauncher.png
/usr/lib/twintaillauncher/resources/*

%changelog
* Wed Jan 07 2026 TukanDev <contact@tukandev.com> - 1.1.13-0
- Initial package for Fedora
- For detailed release notes check github releases page!
