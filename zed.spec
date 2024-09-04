Name:           zed
Version:        0.147.1
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
BuildRequires:	rust >= 1.80.0-2
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

[source."git+https://github.com/ConradIrwin/xkbcommon-rs?rev=fcbb4612185cc129ceeff51d22f7fb51810a03b2"]
git = "https://github.com/ConradIrwin/xkbcommon-rs"
rev = "fcbb4612185cc129ceeff51d22f7fb51810a03b2"
replace-with = "vendored-sources"

[source."git+https://github.com/KillTheMule/nvim-rs?branch=master"]
git = "https://github.com/KillTheMule/nvim-rs"
branch = "master"
replace-with = "vendored-sources"

[source."git+https://github.com/alacritty/alacritty?rev=cacdb5bb3b72bad2c729227537979d95af75978f"]
git = "https://github.com/alacritty/alacritty"
rev = "cacdb5bb3b72bad2c729227537979d95af75978f"
replace-with = "vendored-sources"

[source."git+https://github.com/camdencheek/tree-sitter-go-mod?rev=1f55029bacd0a6a11f6eb894c4312d429dcf735c"]
git = "https://github.com/camdencheek/tree-sitter-go-mod"
rev = "1f55029bacd0a6a11f6eb894c4312d429dcf735c"
replace-with = "vendored-sources"

[source."git+https://github.com/d1y/tree-sitter-go-work?rev=dcbabff454703c3a4bc98a23cf8778d4be46fd22"]
git = "https://github.com/d1y/tree-sitter-go-work"
rev = "dcbabff454703c3a4bc98a23cf8778d4be46fd22"
replace-with = "vendored-sources"

[source."git+https://github.com/npmania/xim-rs?rev=27132caffc5b9bc9c432ca4afad184ab6e7c16af"]
git = "https://github.com/npmania/xim-rs"
rev = "27132caffc5b9bc9c432ca4afad184ab6e7c16af"
replace-with = "vendored-sources"

[source."git+https://github.com/phoenixframework/tree-sitter-heex?rev=6dd0303acf7138dd2b9b432a229e16539581c701"]
git = "https://github.com/phoenixframework/tree-sitter-heex"
rev = "6dd0303acf7138dd2b9b432a229e16539581c701"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-text?rev=542b20c"]
git = "https://github.com/pop-os/cosmic-text"
rev = "542b20c"
replace-with = "vendored-sources"

[source."git+https://github.com/tree-sitter/tree-sitter?rev=7f4a57817d58a2f134fe863674acad6bbf007228"]
git = "https://github.com/tree-sitter/tree-sitter"
rev = "7f4a57817d58a2f134fe863674acad6bbf007228"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/async-pipe-rs?rev=82d00a04211cf4e1236029aa03e6b6ce2a74c553"]
git = "https://github.com/zed-industries/async-pipe-rs"
rev = "82d00a04211cf4e1236029aa03e6b6ce2a74c553"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/blade?rev=7e497c534d5d4a30c18d9eb182cf39eaf0aaa25e"]
git = "https://github.com/zed-industries/blade"
rev = "7e497c534d5d4a30c18d9eb182cf39eaf0aaa25e"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/font-kit?rev=40391b7"]
git = "https://github.com/zed-industries/font-kit"
rev = "40391b7"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/lsp-types?rev=72357d6f6d212bdffba3b5ef4b31d8ca856058e7"]
git = "https://github.com/zed-industries/lsp-types"
rev = "72357d6f6d212bdffba3b5ef4b31d8ca856058e7"
replace-with = "vendored-sources"

[source."git+https://github.com/zed-industries/tree-sitter-markdown?rev=e3855e37f8f2c71aa7513c18a9c95fb7461b1b10"]
git = "https://github.com/zed-industries/tree-sitter-markdown"
rev = "e3855e37f8f2c71aa7513c18a9c95fb7461b1b10"
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
install -m 0755 %{_builddir}/%{name}-%{version}-pre/target/release/zed %{buildroot}%{_libexecdir}/zed-editor
install -m 0755 %{_builddir}/%{name}-%{version}-pre/target/release/cli %{buildroot}%{_bindir}/zed

# Desktop file
# https://github.com/zed-industries/zed/blob/main/script/bundle-linux#L81
export DO_STARTUP_NOTIFY="true"
export APP_CLI="zed"
export APP_ICON="zed"
export APP_NAME="Zed"
#envsubst < "crates/zed/resources/zed.desktop.in" > "crates/zed/resources/zed.desktop"
#install -Dm 0644 crates/zed/resources/zed.desktop %{buildroot}%{_datadir}/applications/zed.desktop
install -Dm 0644 assets/icons/logo_96.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/zed.svg

%files
%license LICENSE-*
%doc README.md
%{_bindir}/zed
%{_libexecdir}/zed-editor
%{_datadir}/applications/zed.desktop
%{_datadir}/icons/hicolor/scalable/apps/zed.svg
