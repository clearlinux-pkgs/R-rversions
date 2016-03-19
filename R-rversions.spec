#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rversions
Version  : 1.0.2
Release  : 13
URL      : http://cran.r-project.org/src/contrib/rversions_1.0.2.tar.gz
Source0  : http://cran.r-project.org/src/contrib/rversions_1.0.2.tar.gz
Summary  : Query 'R' Versions, Including 'r-release' and 'r-oldrel'
Group    : Development/Tools
License  : MIT
Requires: R-xml2
Requires: R-curl
BuildRequires : R-curl
BuildRequires : R-xml2
BuildRequires : clr-R-helpers

%description
[![Linux Build Status](https://travis-ci.org/metacran/rversions.svg?branch=master)](https://travis-ci.org/metacran/rversions)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/github/metacran/rversions?svg=true)](https://ci.appveyor.com/project/gaborcsardi/rversions)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/rversions)](http://cran.rstudio.com/web/packages/rversions/index.html)
[![CRAN version](http://www.r-pkg.org/badges/version/rversions)](http://cran.rstudio.com/web/packages/rversions/index.html)

%prep
%setup -q -c -n rversions

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library rversions
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library rversions


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rversions/DESCRIPTION
/usr/lib64/R/library/rversions/INDEX
/usr/lib64/R/library/rversions/LICENSE
/usr/lib64/R/library/rversions/Meta/Rd.rds
/usr/lib64/R/library/rversions/Meta/hsearch.rds
/usr/lib64/R/library/rversions/Meta/links.rds
/usr/lib64/R/library/rversions/Meta/nsInfo.rds
/usr/lib64/R/library/rversions/Meta/package.rds
/usr/lib64/R/library/rversions/NAMESPACE
/usr/lib64/R/library/rversions/NEWS.md
/usr/lib64/R/library/rversions/R/rversions
/usr/lib64/R/library/rversions/R/rversions.rdb
/usr/lib64/R/library/rversions/R/rversions.rdx
/usr/lib64/R/library/rversions/README.md
/usr/lib64/R/library/rversions/help/AnIndex
/usr/lib64/R/library/rversions/help/aliases.rds
/usr/lib64/R/library/rversions/help/paths.rds
/usr/lib64/R/library/rversions/help/rversions.rdb
/usr/lib64/R/library/rversions/help/rversions.rdx
/usr/lib64/R/library/rversions/html/00Index.html
/usr/lib64/R/library/rversions/html/R.css
