%define		astver	10.1.0
%define		medver	2.3.6
%define		medlib	%mklibname med 1
%define		meddev	%mklibname med -d

Name:		code-aster
Group:		Sciences/Physics
Version:	%{astver}
Release:	%mkrel 1
Summary:	Analysis of of mechanical and civil engineering structures
Source0:	aster-full-src-10.1.0-4.noarch.tar.gz
License:	GPL
URL:		http://www.code-aster.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	gcc-gfortran
BuildRequires:	hdf5
BuildRequires:	hdf5-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel

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
%{_bindir}/*
%dir %{_datadir}/med
%{_datadir}/med/*
%dir %{_docdir}/med
%{_docdir}/med/*

#-----------------------------------------------------------------------
%package	-n %{medlib}
Summary:	Data exchanges in multi-physics simulation work
Group:		Development/Other
Version:	%{medver}
Requires:	%{medlib} = %{version}-%{release}

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
Provides:	med-devel = %{version}-%{release}
Provides:	libmed-devel = %{version}-%{release}
Requires:	%{medlib} = %{version}-%{release}

%description	-n %{meddev}
Data exchanges have become a necessity in the studies of multi-physics
simulation work by different scientific computing software. To achieve
these exchanges, it is necessary to develop code between gateways software.

%files		-n %{meddev}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/*.settings

#-----------------------------------------------------------------------
%prep
%setup -q -n aster-full-src-%{astver}/SRC
tar zxf med-%{medver}.tar.gz

#-----------------------------------------------------------------------
%build
pushd med-%{medver}
    CC=%__cc								\
    %configure2_5x --disable-static --enable-shared
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
