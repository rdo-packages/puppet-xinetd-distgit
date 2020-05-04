%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-xinetd
%global commit 8d460c4b64e357bd0ba0f2ca78509d999b59b21c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-xinetd
Version:        3.3.0
Release:        2%{?alphatag}%{?dist}
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
* Mon May 04 2020 RDO <dev@lists.rdoproject.org> 3.3.0-2.8d460c4git
- Update to post 3.3.0 (8d460c4b64e357bd0ba0f2ca78509d999b59b21c)



