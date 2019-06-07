KPI_DATA = (('open', 1), ('new', 3), ('closed', 3))

for kpi_d in KPI_DATA:
    if kpi_d[0] == 'open':
        print('open tickets %s' % kpi_d[1])
    elif kpi_d[0] == 'new':
        print('new tickets %s' % kpi_d[1])
    elif kpi_d[0] == 'closed':
        print('closed tickets %s' % kpi_d[1])
