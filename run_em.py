import subprocess as sp

# Give initial filenames
initial_filename = "conf.gro"
top_filename = "topol.top"
energy_minim_filename = "minim.mdp"

gromppRun1 = sp.run(["gmx",
                     "grompp",
                     "-f", energy_minim_filename,
                     "-c", initial_filename,
                     "-p", top_filename,
                     "-o", "em1.tpr"],
                    capture_output=True)

MDRun1 = sp.run(["gmx",
                 "mdrun",
                 "-deffnm", "em1",
                 "-v"],
                capture_output=True)

MDout1 = MDRun1.stderr
output1 = MDout1.splitlines()
disp1 = output1[-7:-3]
PE1 = float(disp1[1][-14:])

msg_start = '-----------------------EM Run 1-----------------------'
sp.run(["echo", msg_start])
for line in disp1:
    sp.run(["echo", line])

for i in range(2, 1000):
    filename = "em" + str(i - 1) + ".gro"
    out = "em" + str(i) + ".tpr"
    outname = "em" + str(i)

    gromppRun2 = sp.run(["gmx",
                         "grompp",
                         "-f", "minim.mdp",
                         "-c", filename,
                         "-p", top_filename,
                         "-o", out],
                        capture_output=True)

    MDRun2 = sp.run(["gmx",
                     "mdrun",
                     "-deffnm", outname,
                     "-v"],
                    capture_output=True)

    MDout2 = MDRun2.stderr
    output2 = MDout2.splitlines()
    disp2 = output2[-7:-3]
    PE2 = float(disp2[1][-14:])

    msg_start = '-----------------------EM Run' + \
        ' ' + str(i) + '-----------------------'
    sp.run(["echo", msg_start])
    for line in disp2:
        sp.run(["echo", line])

    if PE2 == PE1:
        sp.run(["echo", "-------------------------Done!-------------------------"])
        break
    PE1 = PE2
