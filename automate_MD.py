import subprocess as sp

# NVT
# 10 ns
NVT1 = sp.run(["gmx",
               "grompp",
               "-f", "nvt.mdp",
               "-c", "em.gro",
               "-r", "em.gro",
               "-p", "IPA.top",
               "-o", "nvt1.tpr"])

RUN_NVT1 = sp.run(["gmx",
                   "mdrun",
                   "-deffnm", "nvt1",
                   "-v"])

# NPT
# 10 ns
NPT1 = sp.run(["gmx",
               "grompp",
               "-f", "npt.mdp",
               "-c", "nvt1.gro",
               "-r", "nvt1.gro",
               "-p", "IPA.top",
               "-o", "npt1.tpr"])

RUN_NPT1 = sp.run(["gmx",
                   "mdrun",
                   "-deffnm", "npt1",
                   "-v"])

# MD
# 10 ns
MD1 = sp.run(["gmx",
              "grompp",
              "-f", "md.mdp",
              "-c", "npt1.gro",
              "-r", "npt1.gro",
              "-p", "IPA.top",
              "-o", "md1.tpr"])

RUN_MD1 = sp.run(["gmx",
                  "mdrun",
                  "-deffnm", "md1",
                  "-v"])

# MD Continuation
# 10 ns
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

# 10 ns
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

# 20 ns
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
