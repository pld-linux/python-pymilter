#
# Conditional build:
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

# NOTES:
# - 'module' should match the Python import path (first component?)
# - 'egg_name' should equal to Python egg name
# - 'pypi_name' must match the Python Package Index name
%define		module		pymilter
Summary:	Python interface to sendmail milter API
Name:		python-%{module}
Version:	1.0.5
Release:	2
License:	BSD-like
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pymilter/%{module}-%{version}.tar.gz
# Source0-md5:	b5d2498b42331de66c973c3f44fb7ff5
URL:		https://pymilter.org/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to sendmail milter API

%description -l pl.UTF-8

%package -n python3-%{module}
Summary:	Python interface to sendmail milter API
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
Python interface to sendmail milter API

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{py_sitedir}/milter.so
%{py_sitedir}/*.py[co]
%dir %{py_sitedir}/Milter
%{py_sitedir}/Milter/*.py[co]
%{py_sitedir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{py3_sitedir}/milter.cpython*.so
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
%{py3_sitedir}/*.py
%{py3_sitedir}/__pycache__
%dir %{py3_sitedir}/Milter
%{py3_sitedir}/Milter/*.py
%{py3_sitedir}/Milter/__pycache__
%endif
