Summary:	Static reflection for enums
Summary(pl.UTF-8):	Statyczna refleksja dla enumów
Name:		magic_enum
Version:	0.9.7
Release:	2
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/Neargye/magic_enum/releases
Source0:	https://github.com/Neargye/magic_enum/releases/download/v%{version}/%{name}-v%{version}.tar.gz
# Source0-md5:	41a2538250647e56fa67568c9948b849
URL:		https://github.com/Neargye/magic_enum
BuildRequires:	cmake >= 3.14
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	rpmbuild(macros) >= 1.605
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Header-only C++17 library provides static reflection for enums, work
with any enum type without any macro or boilerplate code.

%description -l pl.UTF-8
Składająca się z samych nagłówków biblioteka C++17, zapewniająca
statyczną refleksję dla typów enum i pracę z dowolnym typem enum bez
żadnych makr czy powtarzalnego kodu.

%package devel
Summary:	Static reflection for enums
Summary(pl.UTF-8):	Statyczna refleksja dla enumów
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:7

%description devel
Header-only C++17 library provides static reflection for enums, work
with any enum type without any macro or boilerplate code.

%description devel -l pl.UTF-8
Składająca się z samych nagłówków biblioteka C++17, zapewniająca
statyczną refleksję dla typów enum i pracę z dowolnym typem enum bez
żadnych makr czy powtarzalnego kodu.

%prep
%setup -q -c

%build
# use cmake to get both cmake and pkg-config support (meson installs only pkg-config file)
%cmake -B build \
	-DCMAKE_INSTALL_INCLUDEDIR=include

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# catkin/colcon support, not needed
%{__rm} $RPM_BUILD_ROOT%{_datadir}/magic_enum/package.xml
rmdir $RPM_BUILD_ROOT%{_datadir}/magic_enum

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md SECURITY.md
%{_includedir}/magic_enum
%{_npkgconfigdir}/magic_enum.pc
%{_datadir}/cmake/magic_enum
