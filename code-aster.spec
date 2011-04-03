%define		astver	10.1.0
%define		medver	2.3.6
%define		medlib	%mklibname med 1
%define		meddev	%mklibname med -d

%define		metisver 4.0
%define		metisdev %mklibname -d metis

%define		scotver 4.0
%define		scotdev	%mklibname scotch -d

Name:		code-aster
Group:		Sciences/Physics
Version:	%{astver}
Release:	%mkrel 6
Summary:	Analysis of of mechanical and civil engineering structures
Source0:	aster-full-src-10.1.0-4.noarch.tar.gz
License:	GPL
URL:		http://www.code-aster.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	flex bison
BuildRequires:	gcc-gfortran
BuildRequires:	hdf5
BuildRequires:	hdf5-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel

Patch0:		med-build.patch
Patch1:		metis-string-format.patch
Patch2:		scotch-string-format.patch

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
%defattr(-,root,root)
%{_bindir}/mdump
%{_bindir}/medconforme
%{_bindir}/medimport
%{_bindir}/xmdump
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
%defattr(-,root,root)
%{_libdir}/*.so.*

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
%defattr(-,root,root)
%{_includedir}/MED*
%{_includedir}/med*
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/*.settings


#-----------------------------------------------------------------------
%package	-n metis
Summary:	Partitioning unstructured graphs and meshes
Group:		Development/Other
License:	BSD like
Version:	%{metisver}

%description	-n metis
METIS is a software package for partitioning unstructured graphs, partitioning 
meshes, and computing fill-reducing orderings of sparse matrices. 

%files		-n metis
%defattr(-,root,root)
%{_bindir}/graphchk
%{_bindir}/kmetis
%{_bindir}/mesh2dual
%{_bindir}/mesh2nodal
%{_bindir}/oemetis
%{_bindir}/onmetis
%{_bindir}/partdmesh
%{_bindir}/partnmesh
%{_bindir}/pmetis
%{_docdir}/metis/manual.ps

#-----------------------------------------------------------------------
%package	-n %{metisdev}
Summary:	Partitioning unstructured graphs and meshes
Group:		Development/Other
License:	BSD like
Version:	%{metisver}
Provides:	metis-devel = %{metisver}-%{release}
Provides:	libmetis-devel = %{metisver}-%{release}

%description	-n %{metisdev}
METIS is a software package for partitioning unstructured graphs, partitioning 
meshes, and computing fill-reducing orderings of sparse matrices. 

%files		-n %{metisdev}
%defattr(-,root,root)
%{_includedir}/metis.h
%dir %{_includedir}/metis
%{_includedir}/metis/*
%{_libdir}/libmetis.a

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
%defattr(-,root,root)
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
%defattr(-,root,root)
%dir %{_includedir}/scotch
%{_includedir}/scotch/*
%{_libdir}/scotch/*.a

#-----------------------------------------------------------------------
%prep
%setup -q -n aster-full-src-%{astver}/SRC
tar zxf med-%{medver}.tar.gz
tar zxf metis-%{metisver}.tar.gz
tar zxf scotch-%{scotver}-1.tar.gz

%patch0 -p2
%patch1 -p2
%patch2 -p2
pushd med-%{medver}
    autoreconf -ifs
popd


#-----------------------------------------------------------------------
%build
pushd med-%{medver}
    %configure --disable-static --enable-shared
    %make
popd

pushd metis-%{metisver}
    perl -pi								\
	-e 's|\?CC\?|%{__cc}|;'						\
	-e 's|\?CFLAGS\?|%{optflags} -fPIC|;'				\
	-e 's|\?LDFLAGS\?|%{ldflags}|;'					\
	Makefile.in
    %make default
popd

pushd scotch_%{scotver}/src
    perl -pi								\
	-e 's|\?CC\?|%{__cc}|;'						\
	-e 's|\?CFLAGS\?|%{optflags} -fPIC|;'				\
	-e 's|^LDFLAGS  = -L../../bin -lm|LDFLAGS = -L../../bin/ -lm %{ldflags}|;'\
	-e 's|\?RANLIB\?|ranlib|;'					\
	-e 's|\?FLEX\?|flex|;'						\
	-e 's|\?YACC\?|yacc|;'						\
	Makefile.inc
    %make
popd

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}

#-----------------------------------------------------------------------
%install
pushd med-%{medver}
    %makeinstall_std							\
	docdir=%{_docdir}/med						\
	testcdir=%{_datadir}/med/bin/testc				\
	testfdir=%{_datadir}/med/bin/testf
popd

pushd metis-%{metisver}
    mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_includedir}/metis	\
	%{buildroot}%{_libdir}  %{buildroot}%{_docdir}/metis
    cp -fa graphchk kmetis mesh2dual mesh2nodal oemetis onmetis		\
	partdmesh partnmesh pmetis %{buildroot}%{_bindir}
    cp -fa libmetis.a %{buildroot}%{_libdir}
    cp -fa Lib/metis.h %{buildroot}%{_includedir}
    cp -fa Lib/{defs,struct,macros,rename,proto}.h			\
	%{buildroot}%{_includedir}/metis
    cp -fa Doc/manual.ps %{buildroot}%{_docdir}/metis
popd

pushd scotch_%{scotver}
    mkdir -p %{buildroot}%{_datadir}/scotch/bin				\
	%{buildroot}%{_includedir}/scotch %{buildroot}%{_libdir}/scotch	\
	%{buildroot}%{_docdir}/scotch
    pushd bin
	cp -fa lib*.a %{buildroot}%{_libdir}/scotch
	cp -f *.h %{buildroot}%{_includedir}/scotch
	cp -f acpl atst gmk_m3 gtst mmk_m3 amk_ccc gmk_msh mord		\
	    amk_fft2 gmk_ub2 mtst amk_grf gcv gmtst amk_hy gmap gord	\
	    amk_m2 gmk_hy gotst mcv amk_p2 gmk_m2 gout mmk_m2		\
	    %{buildroot}%{_datadir}/scotch/bin
    popd
    cp -fa doc/scotch_user4.0.pdf %{buildroot}%{_docdir}/scotch
    cp -far tgt %{buildroot}%{_datadir}/scotch
popd

chmod -R a+r %{buildroot}
