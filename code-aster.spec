%define		hdfver	1.8.14

%define		astver	13.6.0
%define		astmin	-1

%define		medver	3.3.1
%define		mlmaj	1
%define		medlib	%mklibname med %{mlmaj}
%define		meddev	%mklibname med -d

%define		mlCmaj	1
%define		medlibC	%mklibname medlibC %{mlCmaj}

%define		mlimaj	0
%define		medlibi	%mklibname medlibimport %{mlimaj}

%define		scotver 6.0.4
%define		scotdev	%mklibname scotch -d
%define		scotsuf -aster
%define		scotmin	5

Name:		code-aster
Group:		Sciences/Physics
Version:	%{astver}
Release:	2
Summary:	Analysis of of mechanical and civil engineering structures
Source0:	http://www.code-aster.org/FICHIERS/aster-full-src-%{astver}%{astmin}.noarch.tar.gz
Patch1:		med-3.3.1_cmake.patch
License:	GPL
URL:		http://www.code-aster.org/


BuildRequires:	flex bison
BuildRequires:	gcc-gfortran
BuildRequires:	hdf5
BuildRequires:	hdf5-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	pkgconfig(python3)

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

#-----------------------------------------------------------------------
%package	-n %{medlib}
Summary:	Data exchanges in multi-physics simulation work
Group:		Development/Other
Version:	%{medver}

%description	-n %{medlib}
Data exchanges have become a necessity in the studies of multi-physics
simulation work by different scientific computing software. To achieve
these exchanges, it is necessary to develop code between gateways software.

%files		-n %{medlib}
%{_libdir}/libmed.so.%{mlmaj}*

#-----------------------------------------------------------------------
%package -n	%{medlibC}
Summary:	Data exchanges in multi-physics simulation work
Group:		Development/Other
Version:	%{medver}

%description -n	%{medlibC}
Data exchanges have become a necessity in the studies of multi-physics
simulation work by different scientific computing software. To achieve
these exchanges, it is necessary to develop code between gateways software.

%files -n	%{medlibC}
%{_libdir}/libmedC.so.%{mlCmaj}*

#-----------------------------------------------------------------------
%package	-n %{medlibi}
Summary:	Data exchanges in multi-physics simulation work
Group:		Development/Other
Version:	%{medver}

%description	-n %{medlibi}
Data exchanges have become a necessity in the studies of multi-physics
simulation work by different scientific computing software. To achieve
these exchanges, it is necessary to develop code between gateways software.

%files		-n %{medlibi}
%{_libdir}/libmedimport.so.%{mlimaj}*


#-----------------------------------------------------------------------
%package	-n %{meddev}
Summary:	Data exchanges in multi-physics simulation work
Group:		Development/Other
Version:	%{medver}
Provides:	med-devel = %{medver}-%{release}
Requires:	%{medlib} = %{medver}-%{release}

%description	-n %{meddev}
Data exchanges have become a necessity in the studies of multi-physics
simulation work by different scientific computing software. To achieve
these exchanges, it is necessary to develop code between gateways software.

%files		-n %{meddev}
%{_includedir}/med*
%{_libdir}/libmed*.so
%{_libdir}/libmedfwrap.a
%{_libdir}/cmake/MEDFile

%package -n	python-med
Summary:	Python bindings for med
Group:		Development/Python
Version:	%{medver}

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
tar zxf hdf5-%{hdfver}.tar.gz
tar zxf med-%{medver}.tar.gz
tar zxf scotch-%{scotver}%{scotsuf}%{scotmin}.tar.gz

pushd med-%{medver}
%patch1 -p1
popd

#-----------------------------------------------------------------------
%build
export CC=gcc
export CXX=g++

pushd hdf5-%{hdfver}
   %cmake -DBUILD_SHARED_LIBS=OFF -DBUILD_STATIC_LIBS=ON -DCMAKE_INSTALL_PREFIX=../../hdf5
   %make 
   %makeinstall
popd

pushd med-%{medver}
libmedCRA=`grep -E "libmed_la_LDFLAGS.*version-info\s+([0-9]+:[0-9]+:[0-9]+)" src/Makefile.am | grep -Eo "[0-9]+:[0-9]+:[0-9]+"`
libmedSOVER=`echo $libmedCRA | awk -F':' '{print $1-$3}'`
libmedLIBVER=`echo $libmedCRA | awk -F':' '{print $1-$3"."$3"."$2}'`
libmedcCRA=`grep -E "libmedC_la_LDFLAGS.*version-info\s+([0-9]+:[0-9]+:[0-9]+)" src/Makefile.am | grep -Eo "[0-9]+:[0-9]+:[0-9]+"`
libmedcSOVER=`echo $libmedcCRA | awk -F':' '{print $1-$3}'`
libmedcLIBVER=`echo $libmedcCRA | awk -F':' '{print $1-$3"."$3"."$2}'`
libmedimportCRA=`grep -E "libmedimport_la_LDFLAGS.*version-info\s+([0-9]+:[0-9]+:[0-9]+)" tools/medimport/Makefile.am | grep -Eo "[0-9]+:[0-9]+:[0-9]+"`
libmedimportSOVER=`echo $libmedimportCRA | awk -F':' '{print $1-$3}'`
libmedimportLIBVER=`echo $libmedimportCRA | awk -F':' '{print $1-$3"."$3"."$2}'`

    %cmake -DHDF5_ROOT_DIR=$RPM_BUILD_DIR/aster-full-src-13.6.0/SRC/hdf5 \
    -DMEDFILE_BUILD_PYTHON=1 \
    -DPYTHON_EXECUTABLE=%{__python3} \
    -DPYTHON_INCLUDE_DIR=%{_includedir}/python%{python3_version}m/ \
    -DPYTHON_LIBRARY=%{_libdir}/libpython%{python3_version}m.so \
    -DLIBMED_SOVER=$libmedSOVER -DLIBMED_LIBVER=$libmedLIBVER \
    -DLIBMEDC_SOVER=$libmedcSOVER -DLIBMEDC_LIBVER=$libmedcLIBVER \
    -DLIBMEDIMPORT_SOVER=$libmedimportSOVER -DLIBMEDIMPORT_LIBVER=$libmedimportLIBVER

    %make
popd

pushd scotch-%{scotver}/src
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
pushd med-%{medver}/build
    %makeinstall_std							
popd

pushd scotch-%{scotver}
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

# Install docs through %%doc
mkdir installed_docs
mv %{buildroot}%{_docdir}/* installed_docs

# Remove test-suite files
rm -rf %{buildroot}%{_bindir}/testc
rm -rf %{buildroot}%{_bindir}/testf
rm -rf %{buildroot}%{_bindir}/testpy

chmod -R a+r %{buildroot}

# Symlink points to BuildRoot: /usr/bin/mdump
ln -sf mdump3 %{buildroot}%{_bindir}/mdump
ln -sf xmdump3 %{buildroot}%{_bindir}/xmdump

