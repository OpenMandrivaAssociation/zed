Name:           zed
Version:        0.144.0
Release:        1
Summary:        A high-performance, multiplayer code editor
License:        AGPL-3.0-or-later AND Apache-2.0 AND GPL-3.0-only
Group:          Development/Tools/IDE
URL:            https://github.com/zed-industries/zed
Source0:        https://github.com/zed-industries/zed/archive/refs/tags/v%{version}-pre/%{name}-%{version}-pre.tar.gz
Source1:        vendor.tar.xz

BuildRequires:  git
BuildRequires:  clang
BuildRequires:  mold
BuildRequires:  rust-packaging
BuildRequires:  hicolor-icon-theme

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
%autosetup -n %{name}-%{version}-pre -p1 -a1
%cargo_prep -v vendor
cat >>.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/KillTheMule/nvim-rs?branch=master"]
git = "https://github.com/KillTheMule/nvim-rs"
branch = "master"
replace-with = "vendored-sources"

[source."git+https://github.com/MDeiml/tree-sitter-markdown?rev=330ecab87a3e3a7211ac69bbadc19eabecdb1cca"]
git = "https://github.com/MDeiml/tree-sitter-markdown"
rev = "330ecab87a3e3a7211ac69bbadc19eabecdb1cca"
replace-with = "vendored-sources"

[source."git+https://github.com/alacritty/alacritty?rev=cacdb5bb3b72bad2c729227537979d95af75978f"]
git = "https://github.com/alacritty/alacritty"
rev = "cacdb5bb3b72bad2c729227537979d95af75978f"
replace-with = "vendored-sources"

[source."git+https://github.com/bilelmoussaoui/ashpd?rev=29f2e1a"]
git = "https://github.com/bilelmoussaoui/ashpd"
rev = "29f2e1a"
replace-with = "vendored-sources"

[source."git+https://github.com/d1y/tree-sitter-go-work"]
git = "https://github.com/d1y/tree-sitter-go-work"
replace-with = "vendored-sources"

[source."git+https://github.com/kvark/blade?rev=21a56f780e21e4cb42c70a1dcf4b59842d1ad7f7"]
git = "https://github.com/kvark/blade"
rev = "21a56f780e21e4cb42c70a1dcf4b59842d1ad7f7"
replace-with = "vendored-sources"

[source."git+https://github.com/npmania/xim-rs?rev=27132caffc5b9bc9c432ca4afad184ab6e7c16af"]
git = "https://github.com/npmania/xim-rs"
rev = "27132caffc5b9bc9c432ca4afad184ab6e7c16af"
replace-with = "vendored-sources"

[source."git+https://github.com/phoenixframework/tree-sitter-heex?rev=2e1348c3cf2c9323e87c2744796cf3f3868aa82a"]
git = "https://github.com/phoenixframework/tree-sitter-heex"
rev = "2e1348c3cf2c9323e87c2744796cf3f3868aa82a"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-text?rev=542b20c"]
git = "https://github.com/pop-os/cosmic-text"
rev = "542b20c"
replace-with = "vendored-sources"

[source."git+https://github.com/rewinfrey/tree-sitter-proto?rev=36d54f288aee112f13a67b550ad32634d0c2cb52"]
git = "https://github.com/rewinfrey/tree-sitter-proto"
rev = "36d54f288aee112f13a67b550ad32634d0c2cb52"
replace-with = "vendored-sources"

[source."git+https://github.com/servo/pathfinder.git?rev=4968e819c0d9b015437ffc694511e175801a17c7"]
git = "https://github.com/servo/pathfinder.git"
rev = "4968e819c0d9b015437ffc694511e175801a17c7"
replace-with = "vendored-sources"

[source."git+https://github.com/tree-sitter/tree-sitter-go?rev=b82ab803d887002a0af11f6ce63d72884580bf33"]
git = "https://github.com/tree-sitter/tree-sitter-go"
rev = "b82ab803d887002a0af11f6ce63d72884580bf33"
replace-with = "vendored-sources"

[source."git+https://github.com/tree-sitter/tree-sitter-jsdoc?rev=6a6cf9e7341af32d8e2b2e24a37fbfebefc3dc55"]
git = "https://github.com/tree-sitter/tree-sitter-jsdoc"
rev = "6a6cf9e7341af32d8e2b2e24a37fbfebefc3dc55"
replace-with = "vendored-sources"

[source."git+https://github.com/tree-sitter/tree-sitter?rev=7b4894ba2ae81b988846676f54c0988d4027ef4f"]
git = "https://github.com/tree-sitter/tree-sitter"
rev = "7b4894ba2ae81b988846676f54c0988d4027ef4f"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/async-pipe-rs?rev=82d00a04211cf4e1236029aa03e6b6ce2a74c553"]
git = "https://github.com/zed-industries/async-pipe-rs"
rev = "82d00a04211cf4e1236029aa03e6b6ce2a74c553"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/font-kit?rev=5a5c4d4"]
git = "https://github.com/zed-industries/font-kit"
rev = "5a5c4d4"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/lsp-types?rev=72357d6f6d212bdffba3b5ef4b31d8ca856058e7"]
git = "https://github.com/zed-industries/lsp-types"
rev = "72357d6f6d212bdffba3b5ef4b31d8ca856058e7"
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
cargo build --release

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
