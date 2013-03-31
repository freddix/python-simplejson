%define		module		simplejson

Summary:	Simple, fast, extensible JSON encoder/decoder for Python
Name:		python-%{module}
Version:	3.1.2
Release:	1
License:	MIT or AFL v2.1
Group:		Libraries
Source0:	http://pypi.python.org/packages/source/s/simplejson/%{module}-%{version}.tar.gz
# Source0-md5:	95f89e4a6079946a9bfc7f6424f71e15
URL:		http://undefined.org/python/#simplejson
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
simplejson is a simple, fast, complete, correct and extensible JSON
<http://json.org/> encoder and decoder for Python 2.5+.

%prep
%setup -qn %{module}-%{version}

%build
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean
%{__rm} -rf $RPM_BUILD_ROOT%{py_sitedir}/simplejson/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.rst
%dir %{py_sitedir}/simplejson
%attr(755,root,root) %{py_sitedir}/simplejson/*.so
%{py_sitedir}/simplejson/*.py[co]
