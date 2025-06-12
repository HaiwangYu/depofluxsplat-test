
```bash
source setup.sh
```


```bash
lar -n1 -c prod_cosmics_protodunehd.fcl -o gen.root
lar -n1 -c standard_g4_protodunehd.fcl gen.root -o g4.root
lar -n1 -c pdhd_wirecell_sim_deposplat.fcl g4.root
lar -n1 -c deposplat.fcl g4.root
```

```bash
./js.sh json wcls-sim-drift-deposplat.jsonnet
```


```bash
source ../venv/basic/bin/activate
python plot.py
```