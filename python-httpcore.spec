%define pypi_name httpcore

Name:       python-%{pypi_name}
Version:    1.0.7
Release:    1
Summary:    A minimal low-level HTTP client
Group:      Development/Python
License:    BSD
URL:        https://pypi.org/project/httpcore
Source0:    https://files.pythonhosted.org/packages/source/h/httpcore/httpcore-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  pkgconfig(python)
BuildSystem: python

%description
The HTTP Core package provides a minimal low-level HTTP client, which does one
thing only. Sending HTTP requests.

%files
%doc README.md CHANGELOG.md
%license LICENSE.md
