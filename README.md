## I: Automate iterative commands for energy minimisation in GROMACS using python's subprocess module.

The execution looks like this:
```console
foo@bar:~$ python3 run_em.py
-----------------------EM Run 1-----------------------
Steepest Descents converged to Fmax < 200 in 5126 steps
Potential Energy  =  6.1504507e+03
Maximum force     =  1.8860858e+02 on atom 5817
Norm of force     =  7.0307388e+00
-----------------------EM Run 2-----------------------
Steepest Descents converged to Fmax < 200 in 7 steps
Potential Energy  =  6.1888301e+03
Maximum force     =  1.9466061e+02 on atom 5817
Norm of force     =  3.0374401e+01
-----------------------EM Run 3-----------------------
Steepest Descents converged to Fmax < 200 in 7 steps
Potential Energy  =  6.1892344e+03
Maximum force     =  1.9481195e+02 on atom 5817
Norm of force     =  3.0381862e+01
-----------------------EM Run 4-----------------------
Steepest Descents converged to Fmax < 200 in 7 steps
Potential Energy  =  6.1892192e+03
Maximum force     =  1.9481198e+02 on atom 5817
Norm of force     =  3.0381814e+01
-----------------------EM Run 5-----------------------
Steepest Descents converged to Fmax < 200 in 7 steps
Potential Energy  =  6.1892192e+03
Maximum force     =  1.9481198e+02 on atom 5817
Norm of force     =  3.0381814e+01
-------------------------Done!-------------------------
foo@bar:~$ 
```
## II: Automate running NVT, NPT and MD (piecewise) using ```automate_MD.py```.

## III: Plot .xvg files from GROMACS using ```get_xvg.py```

