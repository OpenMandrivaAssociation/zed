Name:           zed
Version:        0.167.1
Release:        1
Summary:        A high-performance, multiplayer code editor
License:        AGPL-3.0-or-later AND Apache-2.0 AND GPL-3.0-only
Group:          Development/Tools/IDE
URL:            https://zed.dev/
Source0:        https://github.com/zed-industries/zed/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz

BuildRequires:  git
BuildRequires:  clang
BuildRequires:  mold
BuildRequires:  rust-packaging
BuildRequires:	rust >= 1.80.0-2
BuildRequires:  hicolor-icon-theme
BuildRequires:  gettext-devel
# all pkgconfig BR are based on the the build.rs files in the vendor tree
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2) >= 18.5.12
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(zlib)
# it doesnt try to find this one but then it tries to link to it.
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)

# otherwise it downloads a copy of nodejs
Requires:       npm

%description
Code at the speed of thought - Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.

%prep
# Vendored sources
%autosetup -n %{name}-%{version} -p1 -a1
%cargo_prep -v vendor
cat >>.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/ConradIrwin/xkbcommon-rs?rev=fcbb4612185cc129ceeff51d22f7fb51810a03b2"]
git = "https://github.com/ConradIrwin/xkbcommon-rs"
rev = "fcbb4612185cc129ceeff51d22f7fb51810a03b2"
replace-with = "vendored-sources"

[source."git+https://github.com/KillTheMule/nvim-rs?branch=master"]
git = "https://github.com/KillTheMule/nvim-rs"
branch = "master"
replace-with = "vendored-sources"

[source."git+https://github.com/XDeme1/xim-rs?rev=d50d461764c2213655cd9cf65a0ea94c70d3c4fd"]
git = "https://github.com/XDeme1/xim-rs"
rev = "d50d461764c2213655cd9cf65a0ea94c70d3c4fd"
replace-with = "vendored-sources"

[source."git+https://github.com/alacritty/alacritty?rev=91d034ff8b53867143c005acfaa14609147c9a2c"]
git = "https://github.com/alacritty/alacritty"
rev = "91d034ff8b53867143c005acfaa14609147c9a2c"
replace-with = "vendored-sources"

[source."git+https://github.com/kvark/blade?rev=e142a3a5e678eb6a13e642ad8401b1f3aa38e969"]
git = "https://github.com/kvark/blade"
rev = "e142a3a5e678eb6a13e642ad8401b1f3aa38e969"
replace-with = "vendored-sources"

[source."git+https://github.com/microsoft/python-environment-tools.git?rev=ffcbf3f28c46633abd5448a52b1f396c322e0d6c"]
git = "https://github.com/microsoft/python-environment-tools.git"
rev = "ffcbf3f28c46633abd5448a52b1f396c322e0d6c"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-text?rev=542b20c"]
git = "https://github.com/pop-os/cosmic-text"
rev = "542b20c"
replace-with = "vendored-sources"

[source."git+https://github.com/tree-sitter-grammars/tree-sitter-markdown?rev=9a23c1a96c0513d8fc6520972beedd419a973539"]
git = "https://github.com/tree-sitter-grammars/tree-sitter-markdown"
rev = "9a23c1a96c0513d8fc6520972beedd419a973539"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/async-pipe-rs?rev=82d00a04211cf4e1236029aa03e6b6ce2a74c553"]
git = "https://github.com/zed-industries/async-pipe-rs"
rev = "82d00a04211cf4e1236029aa03e6b6ce2a74c553"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/async-stripe?rev=3672dd4efb7181aa597bf580bf5a2f5d23db6735"]
git = "https://github.com/zed-industries/async-stripe"
rev = "3672dd4efb7181aa597bf580bf5a2f5d23db6735"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/cpal?rev=fd8bc2fd39f1f5fdee5a0690656caff9a26d9d50"]
git = "https://github.com/zed-industries/cpal"
rev = "fd8bc2fd39f1f5fdee5a0690656caff9a26d9d50"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/font-kit?rev=40391b7"]
git = "https://github.com/zed-industries/font-kit"
rev = "40391b7"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/lsp-types?rev=72357d6f6d212bdffba3b5ef4b31d8ca856058e7"]
git = "https://github.com/zed-industries/lsp-types"
rev = "72357d6f6d212bdffba3b5ef4b31d8ca856058e7"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/reqwest.git?rev=fd110f6998da16bbca97b6dddda9be7827c50e29"]
git = "https://github.com/zed-industries/reqwest.git"
rev = "fd110f6998da16bbca97b6dddda9be7827c50e29"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/rust-sdks?rev=799f10133d93ba2a88642cd480d01ec4da53408c"]
git = "https://github.com/zed-industries/rust-sdks"
rev = "799f10133d93ba2a88642cd480d01ec4da53408c"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/tree-sitter-go-mod?rev=a9aea5e358cde4d0f8ff20b7bc4fa311e359c7ca"]
git = "https://github.com/zed-industries/tree-sitter-go-mod"
rev = "a9aea5e358cde4d0f8ff20b7bc4fa311e359c7ca"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/tree-sitter-go-work?rev=acb0617bf7f4fda02c6217676cc64acb89536dc7"]
git = "https://github.com/zed-industries/tree-sitter-go-work"
rev = "acb0617bf7f4fda02c6217676cc64acb89536dc7"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/tree-sitter-heex?rev=1dd45142fbb05562e35b2040c6129c9bca346592"]
git = "https://github.com/zed-industries/tree-sitter-heex"
rev = "1dd45142fbb05562e35b2040c6129c9bca346592"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/tree-sitter-yaml?rev=baff0b51c64ef6a1fb1f8390f3ad6015b83ec13a"]
git = "https://github.com/zed-industries/tree-sitter-yaml"
rev = "baff0b51c64ef6a1fb1f8390f3ad6015b83ec13a"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export ZED_UPDATE_EXPLANATION="Please use the package manager to update zed."

# Build CLI
cd crates/cli/
cargo build --release
# Build Editor
cd ../zed/
cargo build --release --verbose

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -D -d -m 0755 %{buildroot}%{_libexecdir}

# https://github.com/zed-industries/zed/blob/main/script/bundle-linux#L59
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/zed %{buildroot}%{_libexecdir}/zed-editor
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/cli %{buildroot}%{_bindir}/zed

# Desktop file
# https://github.com/zed-industries/zed/blob/main/script/bundle-linux#L81
export DO_STARTUP_NOTIFY="true"
export APP_CLI="zed"
export APP_ICON="zed"
export APP_NAME="Zed"
envsubst < "crates/zed/resources/zed.desktop.in" > "crates/zed/resources/zed.desktop"
install -Dm 0644 crates/zed/resources/zed.desktop %{buildroot}%{_datadir}/applications/zed.desktop
install -Dm 0644 assets/icons/logo_96.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/zed.svg

%files
%license LICENSE-*
%doc README.md
%{_bindir}/zed
%{_libexecdir}/zed-editor
%{_datadir}/applications/zed.desktop
%{_datadir}/icons/hicolor/scalable/apps/zed.svg
