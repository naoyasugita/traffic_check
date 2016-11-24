"""
A->D,B->E is run by 1/18s.
other is run by 1/12s
sample:<vehicle id="32400" depart="0"><route edges="gne56 gneE7"/></vehicle>
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


# class Road_a(Road):
#     super().__init__(head_r,tail_r,head_l,tail_l)
#     def create_xml(self,num,time):# time = 18
#         #n_id = 32400
#         global n_id
#         global depart
#         for second in range(num):
#             depart += 1
#             if second % time == 0:
#                 n_id += 1
#                 if n_id % 2 == 0:
#                     f.write('<vehicle id="' + str(n_id) + '" depart="' + str(
#                         depart) + '"><route edges="' + self.head_r + ' ' + self.tail_r + '"/></vehicle>')
#                     f.write("\n")
#                 else:
#                     f.write('<vehicle id="' + str(n_id) + '" depart="' + str(
#                         depart) + '"><route edges="' + self.head_l + ' ' + self.tail_l +
#                             '"/></vehicle>')
#                     f.write("\n")

# class Road_b(object):
#     def __init__(self,head_r,tail_r,head_l,tail_l):
#         self.head_r = head_r
#         self.tail_r = tail_r
#         self.head_l = head_l
#         self.tail_l = tail_l

#     def create_xml(self,num,time):#time = 12
#         #n_id = 32400
#         global n_id
#         global depart
#         for second in range(num):
#             depart += 1
#             if second % time == 0:
#                 n_id += 1
#                 if n_id % 2 == 0:
#                     f.write('<vehicle id="' + str(n_id) + '" depart="' + str(
#                         depart) + '"><route edges="' + self.head_r + ' ' + self.tail_r + '"/></vehicle>')
#                     f.write("\n")
#                 else:
#                     f.write('<vehicle id="' + str(n_id) + '" depart="' + str(
#                         depart) + '"><route edges="' + self.head_l + ' ' + self.tail_l +
#                             '"/></vehicle>')
#                     f.write("\n")

# x = Road_a("A","D","B","E")
# y = Road_b("C","F","G","J")
# x.create_xml(100,18)
# y.create_xml(100,18)


# def create_xml(self,head_r,head_l,tail_r,tail_l):
#     depart = 0.00
#     for second in range(36 * 3600):
#         head_r = "gneE14_0"
#         tail_r = "gneE31_0"
#         head_l = "gneE14_1"
#         tail_l = "gneE31_1"
#         depart += 1
#         if second % 18 == 0:
#             n_id += 1
#             if n_id % 2 == 0:
#                 f.write('<vehicle id="' + str(n_id) + '" depart="' + str(
#                     depart) + '"><route edges="' + head_r + ' ' + tail_r + '"/></vehicle>')
#                 f.write("\n")
#             else:
#                 f.write('<vehicle id="' + str(n_id) + '" depart="' + str(
#                     depart) + '"><route edges="' + head_l + ' ' + tail_l + '"/></vehicle>')
#                 f.write("\n")


#以下,一時間に200台走行

#A -> D

#B -> E
# depart = 0.00
# for second in range(36 * 3600):
#     head_r = "b_r"
#     tail_r = "e_r"
#     head_l = "b_l"
#     tail_l = "e_l"
#     depart += 1
#     if second % 18 == 0:
#         n_id += 1
#         if n_id % 2 == 0:
#             f.write('<vehicle id="' + str(n_id) + '" depart="' + str(depart) + '"><route edges="' + head_r + ' ' + tail_r + '"/></vehicle>')
#             f.write("\n")
#         else:
#             f.write('<vehicle id="' + str(n_id) + '" depart="' + str(depart) + '"><route edges="' + head_l + ' ' + tail_l + '"/></vehicle>')
#             f.write("\n")
#
# #以下,一時間に300台走行
#
# #C -> F
# depart = 0.00
# for second in range(36 * 3600):
#     head_r = "c_r"
#     tail_r = "f_r"
#     head_l = "c_l"
#     tail_l = "f_l"
#     depart += 1
#     if second % 12 == 0:
#         n_id += 1
#         if depart % 2 == 0:
#             f.write('<vehicle id="' + str(n_id) + '" depart="' + str(depart) + '"><route edges="' + head_r + ' ' + tail_r + '"/></vehicle>')
#             f.write("\n")
#         else:
#             f.write('<vehicle id="' + str(n_id) + '" depart="' + str(depart) + '"><route edges="' + head_l + ' ' + tail_l + '"/></vehicle>')
#             f.write("\n")
#
# #G -> J
# depart = 0.00
# for second in range(36 * 3600):
#     head_r = "g_r"
#     tail_r = "j_r"
#     head_l = "g_l"
#     tail_l = "j_l"
#     depart += 1
#     if second % 12 == 0:
#         n_id += 1
#         if depart % 2 == 0:
#             f.write('<vehicle id="' + str(n_id) + '" depart="' + str(depart) + '"><route edges="' + head_r + ' ' + tail_r + '"/></vehicle>')
#             f.write("\n")
#         else:
#             f.write('<vehicle id="' + str(n_id) + '" depart="' + str(depart) + '"><route edges="' + head_l + ' ' + tail_l + '"/></vehicle>')
#             f.write("\n")
#
# #H -> K
# depart = 0.00
# for second in range(36 * 3600):
#     head_r = "h_r"
#     tail_r = "k_r"
#     head_l = "h_l"
#     tail_l = "k_l"
#     depart += 1
#     if second % 12 == 0:
#         n_id += 1
#         if depart % 2 == 0:
#             f.write('<vehicle id="' + str(n_id) + '" depart="' + str(depart) + '"><route edges="' + head_r + ' ' + tail_r + '"/></vehicle>')
#             f.write("\n")
#         else:
#             f.write('<vehicle id="' + str(n_id) + '" depart="' + str(depart) + '"><route edges="' + head_l + ' ' + tail_l + '"/></vehicle>')
#             f.write("\n")
#
# #I -> L
# depart = 0.00
# for second in range(36 * 3600):
#     head_r = "i_r"
#     tail_r = "L_r"
#     head_l = "i_l"
#     tail_l = "L_l"
#     depart += 1
#     if second % 12 == 0:
#         n_id += 1
#         if depart % 2 == 0:
#             f.write('<vehicle id="' + str(n_id) + '" depart="' + str(depart) + '"><route edges="' + head_r + ' ' + tail_r + '"/></vehicle>')
#             f.write("\n")
#         else:
#             f.write('<vehicle id="' + str(n_id) + '" depart="' + str(depart) + '"><route edges="' + head_l + ' ' + tail_l + '"/></vehicle>')
#             f.write("\n")
#
# f.close()