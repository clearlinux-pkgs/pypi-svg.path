#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : svg.path
Version  : 4.1
Release  : 22
URL      : https://files.pythonhosted.org/packages/2e/62/b13cfccfe2de368169d1f0a13ec205a670122fa75e6be9de66cebaff690c/svg.path-4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2e/62/b13cfccfe2de368169d1f0a13ec205a670122fa75e6be9de66cebaff690c/svg.path-4.1.tar.gz
Summary  : SVG path objects and parser
Group    : Development/Tools
License  : MIT
Requires: svg.path-license = %{version}-%{release}
Requires: svg.path-python = %{version}-%{release}
Requires: svg.path-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
========
        
        svg.path is a collection of objects that implement the different path
        commands in SVG, and a parser for SVG path definitions.
        
        
        Usage
        -----
        
        There are four path segment objects, ``Line``, ``Arc``, ``CubicBezier`` and
        ``QuadraticBezier``.`There is also a ``Path`` object that acts as a
        collection of the path segment objects.
        
        All coordinate values for these classes are given as ``complex`` values,
        where the ``.real`` part represents the X coordinate, and the ``.imag`` part

%package license
Summary: license components for the svg.path package.
Group: Default

%description license
license components for the svg.path package.


%package python
Summary: python components for the svg.path package.
Group: Default
Requires: svg.path-python3 = %{version}-%{release}

%description python
python components for the svg.path package.


%package python3
Summary: python3 components for the svg.path package.
Group: Default
Requires: python3-core
Provides: pypi(svg.path)

%description python3
python3 components for the svg.path package.


%prep
%setup -q -n svg.path-4.1
cd %{_builddir}/svg.path-4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613517008
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/svg.path
cp %{_builddir}/svg.path-4.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/svg.path/d14a2577da362843bb255e84ec3c2dd4bfd47f50
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/svg.path/d14a2577da362843bb255e84ec3c2dd4bfd47f50

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
