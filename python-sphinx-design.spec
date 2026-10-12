%define module sphinx-design
%define oname sphinx_design

Name:		python-sphinx-design
Summary:	A sphinx extension for designing beautiful, view size responsive web components
Version:	0.7.0
Release:	2
License:	MIT
Group:		Development/Python
URL:		https://github.com/executablebooks/sphinx-design
Source0:	https://github.com/executablebooks/sphinx-design/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildOption(prep):	-p1
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
A sphinx extension for designing beautiful, view size responsive web components.

%files
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
