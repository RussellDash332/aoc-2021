# Advent of Code 2021

All my Advent of Code 2021 attempts! Mainly in Python.

## Note to Self
```sh
export X=... # day number

# Note that .in files are hidden but it should be within Day-<X>/<X>.in

# Python
cd Day-$X/Python && python3 main.py < ../$X.in && cd ../..

# JavaScript
cd Day-$X/JavaScript && node main.js < ../$X.in && cd ../..

# Java
cd Day-$X/Java && javac Main.java && java Main < ../$X.in && cd ../..

# C++
cd Day-$X/C++ && g++ -o mainc main.cpp && ./mainc < ../$X.in && cd ../..

# Haskell
cd Day-$X/Haskell && runhaskell main.hs && cd ../..

# Rust
cd Day-$X/Rust && rustc main.rs && ./main < ../$X.in && cd ../..
```