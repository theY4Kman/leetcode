Well, this should've been really simple, but I don't understand my rounding issues. For example:

    10 6 9 3 + -11 * / * 17 + 5 +

Becomes the infix:

    10 * 6 / ((9 + 3) * -11) + 17 + 5

Which equals 21.545454 (repeating). If I round this up, it matches the expected 22.

But with the same logic, the postfix

    4 13 5 / +

Becomes the infix

    4 + 13 / 5

Which equals 6.6, and rounding up is 7, which does NOT match the expected 6.

So, I went into the discussion to find it's just Python's division, whereby Python always rounds down. So, `3 / 2` is `1` (rounding down 1.5), but `-3 / 2` is `-2` (rounding down -1.5). The solution is to use floats just for division, and do the truncation myself.
