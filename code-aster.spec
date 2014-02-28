%define		astver	11.5.0
%define		astmin	-3

%define		medver	3.0.7
%define		medlib	%mklibname med 1
%define		meddev	%mklibname med -d

%define		scotver 5.1.11
%define		scotdev	%mklibname scotch -d
%define		scotsuf _esmumps
%define		scotmin	-2

Name:		code-aster
Group:		Sciences/Physics
Version:	%{astver}
Release:	1
Summary:	Analysis of of mechanical and civil engineering structures
Source0:	http://www.code-aster.org/FICHIERS/aster-full-src-%{astver}%{astmin}.noarch.tar.gz
License:	GPL
URL:		http://www.code-aster.org/


BuildRequires:	flex bison
BuildRequires:	gcc-gfortran
BuildRequires:	hdf5
BuildRequires:	hdf5-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	pkgconfig(python2)

Patch0:		med-build.patch
Patch1:		scotch-string-format.patch
Patch2:		med-3.0.7-link-against-python27.patch

#-----------------------------------------------------------------------
%description
Code_Aster: how and why?

Why?

EDF guarantees the technical and economical capabilities of its electricity
production means, from the conception to the end of operational life. The
safety and availability requirements infer the need to verify the correct
operation, maintenance and replacements conditions of machines through
numerical simulation. The analysis of real behaviour and the risks associated
with mechanical and civil engineering structures require knowledge over non
linear models of mechanical and thermal phenomena. Code_Aster has been
developed to satisfy these needs.

With Whom?

The main team is responsible for the coherence and quality (from the
architecture to the exploitation) of the code. A development network
provides models adapted to different materials and mechanical components
found in electrical industry equipment. Led by EDF-R&D, this network contains
industrial and university researchers as well as project coordinators. It
aims at giving on time the results of the innovations that are essential to
evaluate the problems of the system under use and of new projects. The
Code_Aster Users' Day shows the vitality of the network.

How?

The industrialisation of models, the adaptation of achievements and the
qualification take advantage of 18 years of development. The configuration
management tool allows the involved researchers to verify the coherence of
new modifications, their conformity with the rules and non-regression policy
of the modified code (over 1,800 tests performed in configuration). prior to
their integration within the code. The architecture of Code_Aster (a FORTRAN
base associated to object language) depends on a memory/disk image manager,
a command supervisor and a finite element calculation engine (the algorithms
are built independently from the elements formulation).

#-----------------------------------------------------------------------
%package	-n med
Summary:	Data exchanges in multi-physics simulation work
Group:		System/Libraries
Version:	%{medver}

%description	-n med
Data exchanges have become a necessity in the studies of multi-physics
simulation work by different scientific computing software. To achieve
these exchanges, it is necessary to develop code between gateways software.

%files		-n med
%{_bindir}/mdump*
%{_bindir}/medconforme
%{_bindir}/medimport
%{_bindir}/xmdump*
%dir %{_datadir}/med
%{_datadir}/med/*
%dir %{_docdir}/med
%{_docdir}/med/*

#-----------------------------------------------------------------------
%package	-n %{medlib}
Summary:	Data exchanges in multi-physics simulation work
Group:		Development/Other
Version:	%{medver}
Requires:	%{medlib} = %{medver}-%{release}

%description	-n %{medlib}
Data exchanges have become a necessity in the studies of multi-physics
simulation work by different scientific computing software. To achieve
these exchanges, it is necessary to develop code between gateways software.

%files		-n %{medlib}
%{_libdir}/libmed.so.*

#-----------------------------------------------------------------------
%package	-n %{meddev}
Summary:	Data exchanges in multi-physics simulation work
Group:		Development/Other
Version:	%{medver}
Provides:	med-devel = %{medver}-%{release}
Provides:	libmed-devel = %{medver}-%{release}
Requires:	%{medlib} = %{medver}-%{release}

%description	-n %{meddev}
Data exchanges have become a necessity in the studies of multi-physics
simulation work by different scientific computing software. To achieve
these exchanges, it is necessary to develop code between gateways software.

%files		-n %{meddev}
%{_includedir}/MED*
%{_includedir}/med*
%{_includedir}/swig/*
%{_libdir}/libmed*.so
%{_libdir}/libmed*.settings

%package -n	python-med
Summary:	Python bindings for med
Group:		Development/Python

%files -n	python-med
%{python_sitearch}/med

#-----------------------------------------------------------------------
%package	-n scotch
Summary:	Mapping, partitioning, and sparse matrix block ordering
Group:		Development/Other
License:	LGPL
Version:	%{scotver}

%description	-n scotch
A software package and a software library devoted to static mapping,
partitioning, and sparse matrix block ordering of graphs and meshes.

%files		-n scotch
%dir %{_datadir}/scotch
%{_datadir}/scotch/*
%dir %{_docdir}/scotch
%{_docdir}/scotch/*

#-----------------------------------------------------------------------
%package	-n %{scotdev}
Summary:	Mapping, partitioning, and sparse matrix block ordering
Group:		Development/Other
License:	LGPL
Version:	%{scotver}
Provides:	scotch-devel = %{scotver}-%{release}
Provides:	libscotch-devel = %{scotver}-%{release}

%description	-n %{scotdev}
A software package and a software library devoted to static mapping,
partitioning, and sparse matrix block ordering of graphs and meshes.

%files		-n %{scotdev}
%dir %{_includedir}/scotch
%{_includedir}/scotch/*
%{_libdir}/scotch/*.a

#-----------------------------------------------------------------------
%prep
%setup -q -n aster-full-src-%{astver}/SRC
tar zxf med-%{medver}.tar.gz
tar zxf scotch-%{scotver}%{scotsuf}%{scotmin}.tar.gz

%patch0 -p2
%patch1 -p2
%patch2 -p2

pushd med-%{medver}
    autoreconf -ifs
popd


#-----------------------------------------------------------------------
%build
pushd med-%{medver}
    %configure --disable-static --enable-shared --with-hdf5=%{_prefix} FLIBS=-lgfortran
    %make
popd

pushd scotch-%{scotver}%{scotsuf}/src
    perl -pi								\
	-e 's|\?CC\?|%{__cc}|;'						\
	-e 's|\?CFLAGS\?|-pthread %{optflags}|;'			\
	-e 's|^(LDFLAGS\s+=.*)|$1 %{ldflags}|;'				\
	-e 's|\?RANLIB\?|ranlib|;'					\
	-e 's|\?FLEX\?|flex|;'						\
	-e 's|\?YACC\?|yacc|;'						\
	Makefile.inc
    %make
popd

#-----------------------------------------------------------------------
%install
pushd med-%{medver}
    %makeinstall_std							\
	docdir=%{_docdir}/med						\
	testcdir=%{_datadir}/med/bin/testc				\
	testfdir=%{_datadir}/med/bin/testf				\
	usescasesdir=%{_datadir}/med/bin/usescases			\
	unittestsdir=%{_datadir}/med/bin/unittests
    pushd %{buildroot}%{_includedir}
	mv -f 2.3.6 med-2.3.6
    popd
popd

pushd scotch-%{scotver}%{scotsuf}
    mkdir -p %{buildroot}%{_datadir}/scotch/bin				\
	%{buildroot}%{_includedir}/scotch %{buildroot}%{_libdir}/scotch	\
	%{buildroot}%{_docdir}/scotch
    cp -fa lib/lib*.a %{buildroot}%{_libdir}/scotch
    cp -f include/*.h %{buildroot}%{_includedir}/scotch
    pushd bin
	cp -f acpl atst gmk_m3 gtst mmk_m3 amk_ccc gmk_msh mord		\
	    amk_fft2 gmk_ub2 mtst amk_grf gcv gmtst amk_hy gmap gord	\
	    amk_m2 gmk_hy gotst mcv amk_p2 gmk_m2 gout mmk_m2		\
	    %{buildroot}%{_datadir}/scotch/bin
    popd
    cp -fa doc/*.pdf %{buildroot}%{_docdir}/scotch
    cp -far tgt %{buildroot}%{_datadir}/scotch
popd

chmod -R a+r %{buildroot}

# Symlink points to BuildRoot: /usr/bin/mdump
ln -sf mdump3 %{buildroot}%{_bindir}/mdump
ln -sf xmdump3 %{buildroot}%{_bindir}/xmdump

rm -r %{buildroot}%{_bindir}/testpy

