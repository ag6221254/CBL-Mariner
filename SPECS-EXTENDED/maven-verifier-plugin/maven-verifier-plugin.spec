Vendor:         Microsoft Corporation
Distribution:   Mariner
Name:           maven-verifier-plugin
Version:        1.0
Release:        30%{?dist}
Summary:        Maven Verifier Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-verifier-plugin/
Source0:        http://www.apache.org/dist/maven/plugins/%{name}-%{version}-source-release.zip

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-parent
BuildRequires: modello
BuildRequires: plexus-utils

%description
Assists in integration testing by means of evaluating 
success/error conditions read from a configuration file.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q 

%mvn_file :%{name} %{name}
%pom_remove_parent
%pom_add_parent org.apache.maven.plugins:maven-plugins:34

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0-30
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Severin Gehwolf <sgehwolf@redhat.com> - 1.0-27
- Move to maven-parent over maven-plugins-pom.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.0-24
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Merlin Mathesius <mmathesi@redhat.com> - 1.0-16
- Add missing BuildRequires to fix FTBFS (BZ#1405170).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0-12
- Use Requires: java-headless rebuild (#1067528)

* Wed Mar 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11
- Add missing BR: modello

* Sat Aug 10 2013 Mat Booth <fedora@matbooth.co.uk> - 1.0-10
- Fix FTBFS rhbz #992211
- Update for newer guidelines
- Install licence files

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 3 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0-4
- Build with maven v3.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Hui Wang <huwang@redhat.com> - 1.0-2
- Add missing requires maven2

* Wed Jun 02 2010 Hui Wang <huwang@redhat.com> - 1.0-1
- Initial version of the package
