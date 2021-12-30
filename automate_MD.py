import subprocess as sp

# Runs NVT 
NVT  = sp.run(["gmx",
               "grompp",
               "-f", "nvt.mdp",
               "-c", "em.gro",
               "-r", "em.gro",
               "-p", "topol.top",
               "-o", "nvt.tpr"])

RUN_NVT  = sp.run(["gmx",
                   "mdrun",
                   "-deffnm", "nvt",
                   "-v"])

# Runs NPT
NPT  = sp.run(["gmx",
               "grompp",
               "-f", "npt.mdp",
               "-c", "nvt.gro",
               "-r", "nvt.gro",
               "-p", "topol.top",
               "-o", "npt.tpr"])

RUN_NPT  = sp.run(["gmx",
                   "mdrun",
                   "-deffnm", "npt",
                   "-v"])

# Runs MD
MD1 = sp.run(["gmx",
              "grompp",
              "-f", "md.mdp",
              "-c", "npt.gro",
              "-r", "npt.gro",
              "-p", "topol.top",
              "-o", "md1.tpr"])

RUN_MD1 = sp.run(["gmx",
                  "mdrun",
                  "-deffnm", "md1",
                  "-v"])

# MD Continuation
# Appends 10 ns to the initial MD run
MD2 = sp.run(["gmx",
              "convert-tpr",
              "-s", "md1.tpr",
              "-extend", "10000",
              "-o", "md2.tpr"])

RUN_MD2 = sp.run(["gmx",
                  "mdrun",
                  "-deffnm", "md2",
                  "-cpi", "md1.cpt",
                  "-noappend",
                  "-v"])

# Appends 10 ns more to the previous MD run
MD3 = sp.run(["gmx",
              "convert-tpr",
              "-s", "md2.tpr",
              "-extend", "10000",
              "-o", "md3.tpr"])

RUN_MD3 = sp.run(["gmx",
                  "mdrun",
                  "-deffnm", "md3",
                  "-cpi", "md2.cpt",
                  "-noappend",
                  "-v"])

# Appends 20 ns more to the previous MD run
MD4 = sp.run(["gmx",
              "convert-tpr",
              "-s", "md3.tpr",
              "-extend", "20000",
              "-o", "md4.tpr"])

RUN_MD4 = sp.run(["gmx",
                  "mdrun",
                  "-deffnm", "md4",
                  "-cpi", "md3.cpt",
                  "-noappend",
                  "-v"])
