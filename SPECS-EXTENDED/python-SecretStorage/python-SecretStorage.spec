Vendor:         Microsoft Corporation
Distribution:   Mariner
%global srcname SecretStorage

Name:			python-%{srcname}
Version:		3.3.1
Release:		4%{?dist}
Summary:		Python bindings to FreeDesktop.org Secret Service API
URL:			https://github.com/mitya57/secretstorage
Source0:		%pypi_source
License:		BSD
BuildArch:		noarch

# Use the latest libsecret from upstream to run the tests as
# built libsecret does not ship those Python files, TODO make it so
Source1:		http://download.gnome.org/sources/libsecret/0.20/libsecret-0.20.4.tar.xz

BuildRequires:	/usr/bin/dbus-launch
BuildRequires:	/usr/bin/xvfb-run
BuildRequires:	python3-devel
BuildRequires:	python3-cryptography
BuildRequires:	python3-dbus
BuildRequires:	python3-gobject-base
BuildRequires:	python3-jeepney
BuildRequires:	python3-setuptools
BuildRequires:	python3-sphinx

%{?python_enable_dependency_generator}

%description
This module provides a way for securely storing passwords and other secrets.

It uses D-Bus Secret Service API that is supported by GNOME Keyring (>= 2.30)
and KSecretsService.

The main classes provided are secretstorage.Item, representing a secret item
(that has a label, a secret and some attributes) and secretstorage.Collection,
a place items are stored in.

SecretStorage supports most of the functions provided by Secret Service,
including creating and deleting items and collections, editing items, locking
and unlocking collections (asynchronous unlocking is also supported).


%package -n     python3-secretstorage
Summary:		%{summary}

Provides:		python3-%{srcname} = %{version}-%{release}
Obsoletes:		python3-%{srcname} < 3

%{?python_provide:%python_provide python3-secretstorage}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-secretstorage
This module provides a way for securely storing passwords and other secrets.

It uses D-Bus Secret Service API that is supported by GNOME Keyring (>= 2.30)
and KSecretsService.

The main classes provided are secretstorage.Item, representing a secret item
(that has a label, a secret and some attributes) and secretstorage.Collection,
a place items are stored in.

SecretStorage supports most of the functions provided by Secret Service,
including creating and deleting items and collections, editing items, locking
and unlocking collections (asynchronous unlocking is also supported).

%package -n python3-secretstorage-doc
Summary:	SecretStorage documentation
Obsoletes:		python-%{srcname}-doc < 2.3.1-11
%{?python_provide:%python_provide python3-secretstorage-doc}

%description -n python3-secretstorage-doc
Documentation for SecretStorage.

%prep
%autosetup -n %{srcname}-%{version}
tar xf %{SOURCE1}

%build
%py3_build

# Build the documentation
%{__python3} setup.py build_sphinx

# Remove unnecessary files generated by python-sphinx
find build -name '.buildinfo' -delete -print
find build -name 'doctrees' -type d -print -exec rm -r '{}' +

%install
%py3_install

%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
for MOCK in libsecret-0.20.4/libsecret/mock-service-{normal,only-plain,lock}.py; do
  xvfb-run -a dbus-launch --exit-with-session %{__python3} tests/run_tests.py ${MOCK}
done


%files -n python3-secretstorage
%doc changelog README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/secretstorage/

%files -n python3-secretstorage-doc
%doc build/sphinx/html/*

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.1-2
- Rebuilt for Python 3.10

* Tue Mar 16 2021 Charalampos Stratakis <cstratak@redhat.com> - 3.3.1-1
- Update to version 3.3.1 (#1895611)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Nils Philippsen <nils@tiptoe.de> - 3.2.0-2
- Remove stray white space in descriptions

* Wed Nov 11 2020 Adam Williamson <awilliam@redhat.com> - 3.2.0-1
- Update to version 3.2.0 (needed for new python-keyring)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Charalampos Stratakis <cstratak@redhat.com> - 3.1.2-1
- Update to version 3.1.2 (#1789073)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 24 2019 William Moreno Reyes <williamjmorenor@gmail.com> - 3.1.1-1
- Update to v3.1.1
  BZ#1679779

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-1
- Update to 3.1.0 (#1571015)
- Drop Python 2 subpackage (upstream does not support Python 2 any more)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-9
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.3.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 2.3.1-6
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-3
- Rebuild for Python 3.6

* Fri Nov 25 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.3.1-2
- Use python-cryptography instead of python-crypto as runtime requirement

* Sun Aug 28 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.3.1-1
- Update to 2.3.1
- Replace python-crypto BuildRequires with python-cryptography

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Mon May 16 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.1.4-1
- Update to 2.1.4
- Provide a python 2 subpackage
- Use python provides macros
- Use newest python macros
- Added license tag
- Enabled tests
- Added missing dependencies

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 17 2014 Christopher Meng <rpm@cicku.me> - 2.1.1-1
- Update to 2.1.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Christopher Meng <rpm@cicku.me> - 2.1.0-1
- Update to 2.1.0

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Mar 30 2014 Christopher Meng <rpm@cicku.me> - 2.0.0-1
- Update to 2.0.0

* Wed Nov 20 2013 Christopher Meng <rpm@cicku.me> - 1.1.0-1
- Update to 1.1.0

* Fri Nov 15 2013 Christopher Meng <rpm@cicku.me> - 1.0.0-0.3.bzr83
- Add license for doc package.
- Disable tests not runnable in Koji.

* Fri Nov 15 2013 Christopher Meng <rpm@cicku.me> - 1.0.0-0.2.bzr83
- Snapshot 83 rev to allow tests in mock.

* Tue Oct 22 2013 Christopher Meng <rpm@cicku.me> - 1.0.0-1
- Initial Package.