#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: f35655a
#
Name     : R-party
Version  : 1.3.17
Release  : 72
URL      : https://cran.r-project.org/src/contrib/party_1.3-17.tar.gz
Source0  : https://cran.r-project.org/src/contrib/party_1.3-17.tar.gz
Summary  : A Laboratory for Recursive Partytioning
Group    : Development/Tools
License  : GPL-2.0
Requires: R-party-lib = %{version}-%{release}
Requires: R-coin
Requires: R-modeltools
Requires: R-mvtnorm
Requires: R-sandwich
Requires: R-strucchange
Requires: R-zoo
BuildRequires : R-TH.data
BuildRequires : R-coin
BuildRequires : R-modeltools
BuildRequires : R-mvtnorm
BuildRequires : R-sandwich
BuildRequires : R-strucchange
BuildRequires : R-zoo
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The core of the package is ctree(), an implementation of
  conditional inference trees which embed tree-structured 
  regression models into a well defined theory of conditional
  inference procedures. This non-parametric class of regression
  trees is applicable to all kinds of regression problems, including
  nominal, ordinal, numeric, censored as well as multivariate response
  variables and arbitrary measurement scales of the covariates. 
  Based on conditional inference trees, cforest() provides an
  implementation of Breiman's random forests. The function mob()
  implements an algorithm for recursive partitioning based on
  parametric models (e.g. linear models, GLMs or survival
  regression) employing parameter instability tests for split
  selection. Extensible functionality for visualizing tree-structured
  regression models is available. The methods are described in

%package lib
Summary: lib components for the R-party package.
Group: Libraries

%description lib
lib components for the R-party package.


%prep
%setup -q -n party
pushd ..
cp -a party buildavx2
popd
pushd ..
cp -a party buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724080993

%install
export SOURCE_DATE_EPOCH=1724080993
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/party/CITATION
/usr/lib64/R/library/party/DESCRIPTION
/usr/lib64/R/library/party/INDEX
/usr/lib64/R/library/party/Meta/Rd.rds
/usr/lib64/R/library/party/Meta/data.rds
/usr/lib64/R/library/party/Meta/demo.rds
/usr/lib64/R/library/party/Meta/features.rds
/usr/lib64/R/library/party/Meta/hsearch.rds
/usr/lib64/R/library/party/Meta/links.rds
/usr/lib64/R/library/party/Meta/nsInfo.rds
/usr/lib64/R/library/party/Meta/package.rds
/usr/lib64/R/library/party/Meta/vignette.rds
/usr/lib64/R/library/party/NAMESPACE
/usr/lib64/R/library/party/NEWS
/usr/lib64/R/library/party/R/party
/usr/lib64/R/library/party/R/party.rdb
/usr/lib64/R/library/party/R/party.rdx
/usr/lib64/R/library/party/data/Rdata.rdb
/usr/lib64/R/library/party/data/Rdata.rds
/usr/lib64/R/library/party/data/Rdata.rdx
/usr/lib64/R/library/party/demo/strucchange-perm.R
/usr/lib64/R/library/party/doc/MOB.R
/usr/lib64/R/library/party/doc/MOB.Rnw
/usr/lib64/R/library/party/doc/MOB.pdf
/usr/lib64/R/library/party/doc/index.html
/usr/lib64/R/library/party/doc/party.R
/usr/lib64/R/library/party/doc/party.Rnw
/usr/lib64/R/library/party/doc/party.pdf
/usr/lib64/R/library/party/doxygen.cfg
/usr/lib64/R/library/party/help/AnIndex
/usr/lib64/R/library/party/help/aliases.rds
/usr/lib64/R/library/party/help/party.rdb
/usr/lib64/R/library/party/help/party.rdx
/usr/lib64/R/library/party/help/paths.rds
/usr/lib64/R/library/party/html/00Index.html
/usr/lib64/R/library/party/html/R.css
/usr/lib64/R/library/party/tests/Distributions.R
/usr/lib64/R/library/party/tests/Distributions.Rout.save
/usr/lib64/R/library/party/tests/Examples/party-Ex.Rout.save
/usr/lib64/R/library/party/tests/LinearStatistic-regtest.R
/usr/lib64/R/library/party/tests/LinearStatistic-regtest.Rout.save
/usr/lib64/R/library/party/tests/Predict-regtest.R
/usr/lib64/R/library/party/tests/Predict-regtest.Rout.save
/usr/lib64/R/library/party/tests/RandomForest-regtest.R
/usr/lib64/R/library/party/tests/RandomForest-regtest.Rout.save
/usr/lib64/R/library/party/tests/TestStatistic-regtest.R
/usr/lib64/R/library/party/tests/TestStatistic-regtest.Rout.save
/usr/lib64/R/library/party/tests/TreeGrow-regtest.R
/usr/lib64/R/library/party/tests/TreeGrow-regtest.Rout.save
/usr/lib64/R/library/party/tests/Utils-regtest.R
/usr/lib64/R/library/party/tests/Utils-regtest.Rout.save
/usr/lib64/R/library/party/tests/bugfixes.R
/usr/lib64/R/library/party/tests/bugfixes.Rout.save
/usr/lib64/R/library/party/tests/mob.R
/usr/lib64/R/library/party/tests/mob.Rout.save
/usr/lib64/R/library/party/tests/t1.RData

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/party/libs/party.so
/V4/usr/lib64/R/library/party/libs/party.so
/usr/lib64/R/library/party/libs/party.so
