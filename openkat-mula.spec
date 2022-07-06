Name:           openkat-mula
Version:        main
Release:        0%{?dist}
Summary:        The OpenKAT system scanner scheduler

License:        EUPL 1.2
URL:            https://openkat.nl
Source0:        https://github.com/minvws/nl-kat-mula/archive/refs/heads/main.zip
Patch0:         pyproject.patch

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:       rabbitmq

%global _description %{expand:
openkat-mula is responsible for scheduling the execution of tasks.
}

%description %_description

%prep
%autosetup -p1 -n nl-kat-mula-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files scheduler

%check
%pyproject_check_import
# no pytest yet, it fails

%files -n openkat-mula -f %{pyproject_files}
/usr/bin/openkat-mula

%doc README.md
%license LICENSE

%changelog
* Wed Jul 6 2022 supakeen <cmdr@supakeen.com>
- Initial version of the package.
