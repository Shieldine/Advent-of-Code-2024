# Day 17 part 2

We have: 2,4 1,3 7,5 1,5 0,3 4,3 5,5 3,0

What happens, step by step:

- b = a % 8
- b = b ^ 3
- c = a >> b
- b = b^5
- a = a >> 3
- b = b ^ c
- output b % 8
- loop if a != 0

a needs to be large enough to produce 16 numbers - so big.

we divide a by 8 in each loop (3 Bits shift), a needs to be 0 in the last one
since we output b and want it to output the input, b needs to assume the numbers of the input step by step.
we need to go backwards
