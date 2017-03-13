%{?scl:%scl_package nodejs-boom}
%{!?scl:%global pkg_name %{name}}
%global enable_tests 0
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-boom
Version:    2.10.1
Release:    2%{?dist}
Summary:    HTTP friendly error objects
License:    BSD
URL:        https://github.com/spumko/boom
Source0:    http://registry.npmjs.org/boom/-/boom-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{enable_tests}
BuildRequires:    %{?scl_prefix}npm(code)
BuildRequires:    %{?scl_prefix}npm(lab)
%endif

%description
This library provides friendly JavaScript objects that represent HTTP errors.

%prep
%setup -q -n package

#fix perms
chmod 0644 README.md LICENSE images/* lib/* package.json

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/boom
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/boom

%nodejs_symlink_deps

%if 0%{enable_tests}
%check
%nodejs_symlink_deps --check
lab -a code -t 100 -L
%endif

%files
%{nodejs_sitelib}/boom
%doc README.md LICENSE images

%changelog
* Mon Sep 19 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.10.1-2
- index.js moved to /lib

* Wed Sep 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.10.1-1
- Updated with script

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.4.2-4
- rebuilt

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.4.2-3
- replace provides and requires with macro

* Mon Jun 24 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.2-2
- fix boom dep

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.2-1
- new upstream release 0.4.2

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.0-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.0-2
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.4.0-2
- Add support for software collections

* Mon Apr 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.0-1
- initial package
