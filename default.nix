with import <nixpkgs> {};

( let mypkg = python37.pkgs.buildPythonPackage rec {
      pname = "mypkg";
      version = "0.0.1";
      src = ./.;
    };

  in python37.withPackages (ps: [mypkg ps.pandas])
).env
