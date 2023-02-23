Vendor:         Microsoft Corporation
Distribution:   Mariner
################################################################################
Name:             tomcatjss
################################################################################

Summary:          JSS Connector for Apache Tomcat
URL:              http://www.dogtagpki.org/wiki/TomcatJSS
License:          LGPLv2+
BuildArch:        noarch

# For development (i.e. unsupported) releases, use x.y.z-0.n.<phase>.
# For official (i.e. supported) releases, use x.y.z-r where r >=1.
Version:          8.1.0
Release:          1%{?_timestamp}%{?_commit_id}%{?dist}
#global           _phase -alpha1

# To generate the source tarball:
# $ git clone https://github.com/dogtagpki/tomcatjss.git
# $ cd tomcatjss
# $ git archive \
#     --format=tar.gz \
#     --prefix tomcatjss-VERSION/ \
#     -o tomcatjss-VERSION.tar.gz \
#     <version tag>
Source:           https://github.com/dogtagpki/tomcatjss/archive/v%{version}%{?_phase}/tomcatjss-%{version}%{?_phase}.tar.gz

# To create a patch for all changes since a version tag:
# $ git format-patch \
#     --stdout \
#     <version tag> \
#     > tomcatjss-VERSION-RELEASE.patch
# Patch: tomcatjss-VERSION-RELEASE.patch

################################################################################
# Java
################################################################################

%define java_devel java-17-openjdk-devel
%define java_headless java-17-openjdk-headless
%define java_home %{_jvmdir}/jre-17-openjdk

################################################################################
# Build Dependencies
################################################################################

# jpackage-utils requires versioning to meet both build and runtime requirements
# jss requires versioning to meet both build and runtime requirements
# tomcat requires versioning to meet both build and runtime requirements

# Java
BuildRequires:    ant
BuildRequires:    apache-commons-lang3
BuildRequires:    %{java_devel}
BuildRequires:    jpackage-utils >= 0:1.7.5-15

# SLF4J
BuildRequires:    slf4j
BuildRequires:    slf4j-jdk14

# JSS
BuildRequires:    jss >= 5.1.0

# Tomcat
%if 0%{?rhel} && ! 0%{?eln}
BuildRequires:    pki-servlet-engine >= 1:9.0.7
%else
BuildRequires:    tomcat >= 1:9.0.7
%endif

################################################################################
# Runtime Dependencies
################################################################################

# Java
Requires:         apache-commons-lang3
Requires:         %{java_headless}
Requires:         jpackage-utils >= 0:1.7.5-15

# SLF4J
Requires:         slf4j
Requires:         slf4j-jdk14

# JSS
Requires:         jss >= 5.0.0

# Tomcat
%if 0%{?rhel} && ! 0%{?eln}
Requires:         pki-servlet-engine >= 1:9.0.7
%else
Requires:         tomcat >= 1:9.0.7
%endif

# PKI
Conflicts:        pki-base < 10.10.0


%if 0%{?rhel}
# For EPEL, override the '_sharedstatedir' macro on RHEL
%define           _sharedstatedir    /var/lib
%endif

%description
JSS Connector for Apache Tomcat, installed via the tomcatjss package,
is a Java Secure Socket Extension (JSSE) module for Apache Tomcat that
uses Java Security Services (JSS), a Java interface to Network Security
Services (NSS).

################################################################################
%prep
################################################################################

%autosetup -n tomcatjss-%{version}%{?_phase} -p 1

################################################################################
%build
################################################################################

./build.sh \
    %{?_verbose:-v} \
    --work-dir=%{_vpath_builddir} \
    --version=%{version} \
    --jni-dir=%{_jnidir} \
    dist

################################################################################
%install
################################################################################

./build.sh \
    %{?_verbose:-v} \
    --work-dir=%{_vpath_builddir} \
    --version=%{version} \
    --java-dir=%{_javadir} \
    --doc-dir=%{_docdir} \
    --install-dir=%{buildroot} \
    install

################################################################################
%files
################################################################################

%license LICENSE

%defattr(-,root,root)
%doc README
%doc LICENSE
%{_javadir}/*

################################################################################
%changelog
* Mon Feb 14 2022 Dogtag PKI Team <devel@lists.dogtagpki.org> - 8.1.0-1
- Rebase to TomcatJSS 8.1.0

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 8.0.0-3
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 30 2021 Dogtag PKI Team <devel@lists.dogtagpki.org> - 8.0.0-1
- Rebase to TomcatJSS 8.0.0

* Thu Aug 12 2021 Dogtag PKI Team <devel@lists.dogtagpki.org> - 8.0.0-0.3.alpha2
- Rebase to TomcatJSS 8.0.0-alpha1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-0.2.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Dogtag PKI Team <devel@lists.dogtagpki.org> - 8.0.0-0.1.alpha1
- Rebase to TomcatJSS 8.0.0-alpha1