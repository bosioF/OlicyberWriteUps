import angr
import base64

proj = angr.Project("./MIC", 
    load_options={"auto_load_libs":False},
    main_opts={"base_addr":0})

init = proj.factory.entry_state()
sim = proj.factory.simulation_manager(init)
s = sim.explore(find=0x15CF, avoid=[0x154D, 0x1576])

print("key: " + s.found[0].posix.dumps(0).decode())
