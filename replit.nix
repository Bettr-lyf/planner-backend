{pkgs}: {
  deps = [
    pkgs.vim
    pkgs.postgresql
    pkgs.libuv
    pkgs.cacert
    pkgs.glibcLocales
    pkgs.rustc
    pkgs.libiconv
    pkgs.cargo
    pkgs.libxcrypt
  ];
}
