Name:		python-sphinx-design
Version:	0.6.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-design/sphinx_design-%{version}.tar.gz
Summary:	A sphinx extension for designing beautiful, view size responsive web components.
URL:		https://pypi.org/project/sphinx-design/
License:	None
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

%description
A sphinx extension for designing beautiful, view size responsive web components.

%prep
%autosetup -p1 -n sphinx_design-%{version}

%files
%{py_sitedir}/sphinx_design
%{py_sitedir}/sphinx_design-*.*-info
