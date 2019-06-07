from observer_pattern.example1.kpi import Kpi
from observer_pattern.example1.obs1 import Obs1
from observer_pattern.example1.obs2 import Obs2

kpi = Kpi()

obs1 = Obs1(kpi)
obs2 = Obs2(kpi)

kpi.set_kpis(1, 4, 4)
kpi.set_kpis(2, 6, 7)

print('detaching obs2')
kpi.detach(obs2)
kpi.set_kpis(10, 11, 22)