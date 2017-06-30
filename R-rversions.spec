#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rversions
Version  : 1.0.3
Release  : 29
URL      : http://cran.r-project.org/src/contrib/rversions_1.0.3.tar.gz
Source0  : http://cran.r-project.org/src/contrib/rversions_1.0.3.tar.gz
Summary  : Query 'R' Versions, Including 'r-release' and 'r-oldrel'
Group    : Development/Tools
License  : MIT
Requires: R-curl
Requires: R-xml2
BuildRequires : R-curl
BuildRequires : R-xml2
BuildRequires : clr-R-helpers

%description
[![Linux Build Status](https://travis-ci.org/metacran/rversions.svg?branch=master)](https://travis-ci.org/metacran/rversions)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/github/metacran/rversions?svg=true)](https://ci.appveyor.com/project/gaborcsardi/rversions)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/rversions)](http://r-pkg.org/pkg/rversions)
[![CRAN version](http://www.r-pkg.org/badges/version/rversions)](http://r-pkg.org/pkg/xml2)

%prep
%setup -q -c -n rversions

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496612386

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1496612386
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rversions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rversions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rversions
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library rversions
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rversions/DESCRIPTION
/usr/lib64/R/library/rversions/INDEX
/usr/lib64/R/library/rversions/LICENSE
/usr/lib64/R/library/rversions/Meta/Rd.rds
/usr/lib64/R/library/rversions/Meta/features.rds
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
