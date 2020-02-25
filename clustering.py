from math import *
from random import *
from argparse import ArgumentParser



def cluster():
    parser = ArgumentParser(description='travelplanner')
    parser.add_argument('routefile', type=str,
                        help='Please give full pathname to route.csv')
    parser.add_argument('passfile', type=str,
                        help='Please give full pathname to passenger.csv')
    parser.add_argument('--speed', default=10, type=int,
                        help='Give the speed of the bus, lower is faster')
    parser.add_argument('--saveplots', action='store_true',
                        help='Optional, If given, save the plots.')
    arguments = parser.parse_args()
    pft = travelplanner.Journey(arguments.routefile, arguments.passfile,
                                speed=arguments.speed)
    route_for_timetable = travelplanner.Route(arguments.routefile,
                                              speed=arguments.speed)

    k=3

    lines = open('samples.csv', 'r').readlines()
    ps=[]
    for line in lines: ps.append(tuple(map(float, line.strip().split(','))))

    m=[ps[randrange(len(ps))], ps[randrange(len(ps))], ps[randrange(len(ps))]]

    alloc=[None]*len(ps)
    n=0
    while n<10:
      for i in range(len(ps)):
        p=ps[i]
        d=[None] * 3
        d[0]=sqrt((p[0]-m[0][0])**2 + (p[1]-m[0][1])**2)
        d[1]=sqrt((p[0]-m[1][0])**2 + (p[1]-m[1][1])**2)
        d[2]=sqrt((p[0]-m[2][0])**2 + (p[1]-m[2][1])**2)
        alloc[i]=d.index(min(d))
      for i in range(3):
        alloc_ps=[p for j, p in enumerate(ps) if alloc[j] == i]
        new_mean=(sum([a[0] for a in alloc_ps]) / len(alloc_ps), sum([a[1] for a in alloc_ps]) / len(alloc_ps))
        m[i]=new_mean
      n=n+1

    for i in range(3):
      alloc_ps=[p for j, p in enumerate(ps) if alloc[j] == i]
      print("Cluster " + str(i) + " is centred at " + str(m[i]) + " and has " + str(len(alloc_ps)) + " points.")



    if __name__ == "__main__":
        process()