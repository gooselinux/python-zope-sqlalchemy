%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-zope-sqlalchemy
Version:        0.4
Release:        3%{?dist}
Summary:        Minimal Zope/SQLAlchemy transaction integration

Group:          Development/Languages
License:        ZPLv2.1
URL:            http://pypi.python.org/pypi/zope.sqlalchemy
Source0:        http://pypi.python.org/packages/source/z/zope.sqlalchemy/zope.sqlalchemy-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel python-setuptools-devel
Requires:       python-transaction
Requires:       python-sqlalchemy >= 0.4.7
Requires:       python-zope-interface

%description
The aim of this package is to unify the plethora of existing packages
integrating SQLAlchemy with Zope's transaction management. As such it seeks
only to provide a data manager and makes no attempt to define a zopeish way to
configure engines.


%prep
%setup -q -n zope.sqlalchemy-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/*



%changelog
* Mon Jun 28 2010 David Malcolm <dmalcolm@redhat.com> - 0.4-3
- fix license metadata
Resolves: rhbz#608095

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Luke Macken <lmacken@redhat.com> - 0.4-1
- Update to 0.4

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.3-2
- Rebuild for Python 2.6

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> - 0.3-1
- Initial package
