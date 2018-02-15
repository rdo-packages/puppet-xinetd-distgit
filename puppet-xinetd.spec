%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-xinetd
%global commit b95c79caac894f508448ce918407381900f1cda0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-xinetd
Version:        3.0.0
Release:        1%{?alphatag}%{?dist}
Summary:        Configures xinetd and exposes the xinetd::service definition for adding new services.
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-xinetd

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Configures xinetd and exposes the xinetd::service definition for adding new services.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/xinetd/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/xinetd/



%files
%{_datadir}/openstack-puppet/modules/xinetd/


%changelog
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 3.0.0-1.b95c79cgit
- Update to post 3.0.0 (b95c79caac894f508448ce918407381900f1cda0)



