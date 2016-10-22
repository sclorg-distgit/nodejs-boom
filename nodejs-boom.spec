%{?scl:%scl_package nodejs-boom}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-boom
Version:    0.4.2
Release:    4%{?dist}
Summary:    HTTP friendly error objects
License:    BSD
Group:      Development/Libraries
URL:        https://github.com/spumko/boom
Source0:    http://registry.npmjs.org/boom/-/boom-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
This library provides friendly JavaScript objects that represent HTTP errors.

%prep
%setup -q -n package

%nodejs_fixdep hoek 0.9

#fix perms
chmod 0644 README.md LICENSE images/* lib/* index.js package.json

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/boom
cp -pr lib index.js package.json %{buildroot}%{nodejs_sitelib}/boom

%nodejs_symlink_deps

#Yet Another Unpackaged Test Framework (lab)
#%%check
#make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/boom
%doc README.md LICENSE images

%changelog
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
