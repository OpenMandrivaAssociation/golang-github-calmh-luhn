# https://github.com/calmh/luhn
%global goipath github.com/calmh/luhn
Version:        2.0.0

%gometa

Name:           golang-github-calmh-luhn
Summary:        Luhn-mod-N implementation in Go
Release:        6%{?dist}
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-6
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 2.0.0-5
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.0-4
- Update to spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.0-1
- Update to version 2.0.0.

* Sun Sep 03 2017 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1
- First package for Fedora

