### Probably not a useful repo

This repo exists as an answer to a specific stackoverflow question:

https://stackoverflow.com/questions/52490426/in-nixos-how-can-i-install-an-environment-with-the-python-packages-spacy-panda


### Things to notice:

- [hello.py](mypkg/hello.py) imports pandas
- `nix-shell --run helloworld` calls a function in [hello.py](mypkg/hello.py), so presumably you can work with pandas from there

### Only a partial answer:

I tried to get SpaCy working by:

 - adding it to the `withPackages` parameters in default.nix
 - adding it to the top of hello.py

...but then I got errors like this:

```
    copying path '/nix/store/xw87rajixaym61r7nkdc7ra6984bjv6q-python3.7-spacy-2.1.4' from 'https://cache.nixos.org'...
    building '/nix/store/az11zqnbj0j0xk9i9dc8s10sq89rrn2v-python3-3.7.3-env.drv'...
    collision between `/nix/store/5gdfbvyb78sd5ad915xv5ksg0y7jvq7m-python3.7-msgpack-0.6.1/lib/python3.7/site-packages/msgpack/__pycache__/_version.cpython-37.pyc' and `/nix/store/fa9vdzlc0c0c74mdl9671ph563v0z8li-python3.7-msgpack-python-0.6.1/lib/python3.7/site-packages/msgpack/__pycache__/_version.cpython-37.pyc'
    builder for '/nix/store/az11zqnbj0j0xk9i9dc8s10sq89rrn2v-python3-3.7.3-env.drv' failed with exit code 25
```

This is just a warning, and should be safely ignorable (the files are identical, so either can be used safely), but I'm not sure how to ignore it.

This should be fixable by setting `ignoreCollisions = true` in `python37.buildEnv`.  The trouble is that I used `python37.withPackages`.  I did this because [the documentation appears better](https://github.com/NixOS/nixpkgs/issues/5623).

I ran into [this](https://github.com/Cortys/nix-pkgs/blob/master/doc/languages-frameworks/python.md) which says:

> In contrast to `python.buildEnv`, `python.withPackages` does not support the more advanced options such as `ignoreCollisions = true` or `postBuild`. If you need them, you have to use python.buildEnv.

If I figure out how to use buildEnv in the future, I'll update here too.
