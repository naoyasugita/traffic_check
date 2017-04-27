"""
A->D,B->E run by 1/18s.
other is run by 1/12s
sample data:<vehicle id="32400" depart="0"><route edges="gne56 gneE7"/></vehicle>
"""

f = open("traffic_data.xml","w")
n_id = 32400
depart = 0.00

class Road(object):
    def __init__(self,head_r,tail_r,head_l,tail_l):
        self.head_r = head_r
        self.tail_r = tail_r
        self.head_l = head_l
        self.tail_l = tail_l

    def create_xml(self,num,time):# time = 18,12
        n_id = 32400
        global n_idi
        global depart
        for second in range(num):
            depart += 1
            if second % time == 0:
                n_id += 1
                if n_id % 2 == 0:
                    f.write('<vehicle id="' + str(n_id) + '" depart="' + str(
                        depart) + '"><route edges="' + self.head_r + ' ' + self.tail_r + '"/></vehicle>')
                    f.write("\n")
                else:
                    f.write('<vehicle id="' + str(n_id) + '" depart="' + str(
                        depart) + '"><route edges="' + self.head_l + ' ' + self.tail_l +
                            '"/></vehicle>')
                    f.write("\n")

m = Road("a","b","c","d")
n = Road("e","f","g","h")
m.create_xml(1000,18)
n.create_xml(1000,12)

f.close()
