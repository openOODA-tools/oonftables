Name:           oonftables
Version:        0.1.0
Release:        1%{?dist}
Summary:        Manages atomic nftables rulesets for egress control and packet logging.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oonftables
Source0:        oonftables-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oonftables is a sovereign, capability-bounded NFT ENGINE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oonftables
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oonftables-uninstall

%files
/usr/bin/oonftables
/usr/bin/oonftables-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
