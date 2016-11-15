%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-xinetd
%global commit a09c77e008377cb2ab36ca0893888f6ef4aadda0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-xinetd
Version:        2.0.0
Release:        2%{?alphatag}%{?dist}
Summary:        Configures xinetd and exposes the xinetd::service definition for adding new services.
License:        Apache-2.0

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
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 2.0.0-2.a09c77e.git
- Newton update 2.0.0 (a09c77e008377cb2ab36ca0893888f6ef4aadda0)

* Wed Sep 21 2016 Haikel Guemar <hguemar@fedoraproject.org> - 2.0.0-1.f9d6e18.git
- Newton update 2.0.0 (f9d6e186d60d2ae8c6582e59ba13e9c744358784)


