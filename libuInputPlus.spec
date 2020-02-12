Name:     libuInputPlus
Version:  0.1.3
Release:  1
Summary:  Library for ydotool
License:  MIT
URL:      https://github.com/YukiWorkshop/libuInputPlus
Source0:  https://github.com/YukiWorkshop/libuInputPlus/archive/%{name}-%{version}.tar.gz

BuildRequires: cmake make gcc-c++

%description
Library required for ydotool

%prep
%autosetup

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make

%make_install

%files
%{_libdir}/libuInputPlus*
%{_libdir}/pkgconfig/*
%{_includedir}/*

%doc README.md

%license LICENSE

%changelog
* Mon Feb 10 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.3-1
- Initial version of the package
