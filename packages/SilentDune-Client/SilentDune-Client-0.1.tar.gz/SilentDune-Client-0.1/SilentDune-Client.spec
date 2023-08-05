#################
# Global Vars
#
# Define which version of python we will be using
%if (0%{?fedora} >= 13 || 0%{?rhel} > 7)
%global with_python3 1
%if (0%{?fedora} >= 23 || 0%{?rhel} >= 8)
%global use_python3 1
%define pythonlib %{python3_sitelib}
%else
%define pythonlib %{python2_sitelib}
%endif
%endif

# Check if OS is using SystemD
%if (0%{?fedora} >= 14 || 0%{?rhel} >= 7 || 0%{?suse_version} >= 1210)
%global use_systemd 1
%endif

# SELinux defines from: https://fedoraproject.org/wiki/SELinux_Policy_Modules_Packaging_Draft
%global selinux_types %(%{__awk} '/^#[[:space:]]*SELINUXTYPE=/,/^[^#]/ { if ($3 == "-") printf "%s ", $2 }' /etc/selinux/config 2>/dev/null)
%global selinux_variants %([ -z "%{selinux_types}" ] && echo mls targeted || echo %{selinux_types})
%{!?_selinux_policy_version: %global _selinux_policy_version %(sed -e 's,.*selinux-policy-\\([^/]*\\)/.*,\\1,' /usr/share/selinux/devel/policyhelp 2>/dev/null)}

#################
# Package Info
#
%define name silentdune
%define version unknown
%define unmangled_version unknown
%define release 1

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Silent Dune Modular Firewall Service

License: GPLv3
Url: https://www.entpack.com
Source0: %{name}-%{unmangled_version}.tar.gz

BuildArch: noarch

%if 0%{?use_python3}
BuildRequires:  python3-devel
%else
BuildRequires:  python2-devel
%endif #0%{?use_python3}

%if 0%{?use_systemd}
BuildRequires: systemd
%endif

Requires:  iptables python-setuptools

%description
An Open Source Multi-Threaded and Modular Linux Firewall Manager Service
dedicated to setting Egress firewall rules and simplifying firewall
management.

#################
# Prep Step
#
%prep
%setup -n %{name}-%{unmangled_version}
mkdir SELinux
cp -p silentdune_client/selinux/silentdune.fc silentdune_client/selinux/silentdune.if silentdune_client/selinux/silentdune.te SELinux

#################
# Build Step
#
%build
%if 0%{?use_python3}
%py3_build
%else
%py2_build
%endif

# Build SELinux policy
cd SELinux
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv silentdune.pp silentdune.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -

#################
# Install Step
#
%install
%if 0%{?use_python3}
%py3_install
%else
%py2_install
%endif
#python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

# Move executables from bin to sbin
mv %{buildroot}/%{_bindir} %{buildroot}/%{_sbindir}

# SELinux
for selinuxvariant in %{selinux_variants}
do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  install -p -m 644 SELinux/silentdune.pp.${selinuxvariant} \
    %{buildroot}%{_datadir}/selinux/${selinuxvariant}/silentdune.pp
done

# Handle service setup
%if 0%{?use_systemd}
mkdir -p %{buildroot}%{_unitdir}
cp %{buildroot}%{pythonlib}/silentdune_client/init/sdc-firewall.service.in %{buildroot}%{_unitdir}/sdc-firewall.service
%else
mkdir -p %{buildroot}%{_initddir}
cp %{buildroot}%{pythonlib}/silentdune_client/init/sdc-firewall.init.in %{buildroot}%{_initddir}/sdc-firewall
%endif

#################
# Clean Step
#
%clean
rm -rf $RPM_BUILD_ROOT


###################################
# Base Package with core modules
#
%files
%{_sbindir}/sdc-install
%{_sbindir}/sdc-firewall

%if 0%{?use_systemd}
%{_unitdir}/sdc-firewall.service
%else
%{_initddir}/sdc-firewall
%endif

%{pythonlib}/*.egg-info
%{pythonlib}/silentdune_client/*.p*
%{pythonlib}/silentdune_client/builders
%{pythonlib}/silentdune_client/init
%{pythonlib}/silentdune_client/models
%{pythonlib}/silentdune_client/po
%{pythonlib}/silentdune_client/utils
%{pythonlib}/silentdune_client/selinux


# Top level module directories
%{pythonlib}/silentdune_client/modules/*.p*
%{pythonlib}/silentdune_client/modules/firewall/*.p*
%{pythonlib}/silentdune_client/modules/comm/*.p*
%{pythonlib}/silentdune_client/modules/examples/*.p*
%{pythonlib}/silentdune_client/modules/automation/*.p*

# Core Modules
%{pythonlib}/silentdune_client/modules/firewall/manager

# Python 3 Cache directories
%if 0%{?use_python3}

%{pythonlib}/silentdune_client/__pycache__
%{pythonlib}/silentdune_client/modules/__pycache__
%{pythonlib}/silentdune_client/modules/firewall/__pycache__
%{pythonlib}/silentdune_client/modules/comm/__pycache__
%{pythonlib}/silentdune_client/modules/examples/__pycache__
%{pythonlib}/silentdune_client/modules/automation/__pycache__

%endif #0%{?with_python3}

%post
%if 0%{?use_systemd}
%systemd_post silentdune.service
%else
chkconfig --add sdc-firewall
%endif

%preun
%if 0%{?use_systemd}
%systemd_preun silentdune.service
%else
service sdc-firewall stop
chkconfig --del sdc-firewall
%endif

%postun
%if 0%{?use_systemd}
%systemd_postun_with_restart silentdune.service
%endif

###################################
# Logging Module
#
%package mod-logging
Requires: silentdune
Summary: Example modules for Silent Dune Firewall Service

%description mod-logging
Logging Module for the Silent Dune Firewall Service

%files mod-logging
%{pythonlib}/silentdune_client/modules/firewall/logging

###################################
# Package Examples Module
#
%package mod-examples
Requires: silentdune
Summary: Example modules for Silent Dune Firewall Service

%description mod-examples
Example modules written in python for the Silent Dune Firewall Service

%files mod-examples
%{pythonlib}/silentdune_client/modules/examples

###################################
# Package Silent Dune Server Module
#
%package mod-server
Requires: silentdune mod-logging python-requests python-cryptography python-dateutil
Summary: Remote Server Module for Silent Dune Firewall Service

%description mod-server
Silent Dune server module allows a system to connect to and be remotely
managed by a Silent Dune server.

%files mod-server
%{pythonlib}/silentdune_client/modules/comm/sd_server


###################################
# Package Auto Discovery Module
#
%package mod-autodiscovery
Requires: silentdune
Summary: Auto Discovery Module for Silent Dune Firewall Service

%description mod-autodiscovery
The Auto Discovery module for Silent Dune Firewall Service auto detects
local settings and creates ingress and egress firewall rules for external
services like DNS, DHCP, NTP and SSH.

%files mod-autodiscovery
%{pythonlib}/silentdune_client/modules/automation/auto_discovery

####################################
# Package selinux
#
%package selinux
BuildRequires: checkpolicy, selinux-policy-devel, selinux-policy-doc
Requires: silentdune policycoreutils-python
Requires(post):   /usr/sbin/semodule, /sbin/restorecon, /sbin/fixfiles, silentdune
Requires(postun): /usr/sbin/semodule, /sbin/restorecon, /sbin/fixfiles, silentdune

%if "%{_selinux_policy_version}" != ""
Requires: selinux-policy >= %{_selinux_policy_version}
%endif
Summary: SELinux policy for Silent Dune Firewall Service

%description selinux
SELinux policy for Silent Dune Firewall Service

%files selinux
%defattr(-,root,root,0755)
%doc silentdune_client/selinux/*
%{_datadir}/selinux/*/silentdune.pp

%post selinux
for selinuxvariant in %{selinux_variants}
do
  /usr/sbin/semodule -s ${selinuxvariant} -i \
    %{_datadir}/selinux/${selinuxvariant}/silentdune.pp &> /dev/null || :
done
/sbin/fixfiles -R silentdune restore || :
/sbin/restorecon -R %{_localstatedir}/cache/silentdune || :

%postun selinux
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}
  do
    /usr/sbin/semodule -s ${selinuxvariant} -r silentdune &> /dev/null || :
  done
  /sbin/fixfiles -R silentdune restore || :
  [ -d %{_localstatedir}/cache/silentdune ]  && \
    /sbin/restorecon -R %{_localstatedir}/cache/silentdune &> /dev/null || :
fi



