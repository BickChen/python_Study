# -*- coding: utf-8 -*-
import sys
import os
a = sys.argv
b = open(a[3],'r',encoding='UTF-8')
c = open(a[3]+".new",'w',encoding='UTF-8')

for lint in b:
    if a[1] in lint:
        lint = lint.replace(a[1],a[2])
    c.write(lint)

b.close()
c.close()
os.replace(a[3]+".new",a[3])

