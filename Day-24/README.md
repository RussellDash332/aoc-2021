With Python it's just a Z3 fiesta or naive brute force but here's what you can actually see from the **input** itself.

Every 18 lines, it's always in the form of this
```
inp w
add z y
mul x 0
add x z
mod x 26
div z {DIV, 1 OR 26}
add x {ADD, >10 IF DIV==1 ELSE <0}
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y {NUM, >0}
mul y x
```
This is basically
```
z_i = z_{i-1} // DIV * (25*(z_{i-1} % 26 + ADD != w_i) + 1) + (w_i + NUM) * (z_{i-1} % 26 + ADD != w_i)
```
where `w_i` is the i-th digit of the MONAD and `z_0 = 0`.

The value of `(z_{i-1} % 26 + ADD != w_i)` is either 1 or 0 so it's either
```
z_i = z_{i-1} // DIV * 26 + (w_i + NUM)
```
or
```
z_i = z_{i-1} // DIV
```
Since `z_0 = 0`, we can see that `z_1 = w_1 + NUM`. Then it depends whether the value of `ADD` in the second group is +ve or -ve (if +ve it would be easier to decide right :D)

Keep checking until `z_14` and you'll find all the inputs `w_1, w_2, ..., w_14`.

At this point it should be much easier to figure out my hand and math depending on your input!