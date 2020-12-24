from PublicReference.base import *

风暴骑兵等级 = 100 + 5

class 主动技能(主动技能)
    def 等效CD(self, 武器类型,输出类型):
        return round(self.CD  / self.恢复, 1)

class 风暴骑兵技能0(主动技能):
    名称 = 'M3喷火器'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    数据 = [0, 207, 228, 250, 270, 291, 313, 333, 355, 376, 396, 418, 439, 460, 481, 502, 523, 544, 566, 586, 607, 629, 649, 671, 692, 712, 734, 755, 776, 797, 818, 839, 860, 882, 902, 923, 945, 965, 987, 
    1008, 1028, 1050, 1071, 1092, 1113, 1134, 1155, 1176, 1198, 1218, 1239, 1261, 1281, 1303, 1324, 1344, 1366, 1387, 1408, 1429, 1450, 1471, 1492, 1514, 1534, 1555, 1577, 1597, 1619, 1640, 1660]
    攻击次数 = 14
    CD = 7.0
    TP成长 = 0.08
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (self.攻击次数 + (1 if self.TP等级 >= 5 else 0)) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 风暴骑兵技能1(被动技能):
    名称 = '重火器精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['所有']
    关联技能2 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.01 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率2(武器类型)

class 风暴骑兵技能2(主动技能):
    名称 = '加农炮'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    数据 = [0, 1048, 1154, 1261, 1367, 1473, 1580, 1686, 1793, 1899, 2005, 2112, 2218, 2325, 2431, 2537, 2644, 2750, 2857, 2963, 3068, 3176, 3281, 3388, 3494, 3600, 3707, 3813, 3920, 4026, 4132, 4239, 4345, 4452, 
    4558, 4664, 4771, 4877, 4984, 5090, 5196, 5303, 5409, 5516, 5622, 5728, 5835, 5941, 6047, 6154, 6260, 6367, 6473, 6579, 6686, 6791, 6899, 7004, 7110, 7217, 7323, 7430, 7536, 7642, 7749, 7855, 7962, 8068, 8174, 8281, 8387]
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * 2 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 风暴骑兵技能3(主动技能):
    名称 = '反坦克炮'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    数据1 = [0, 137, 150, 164, 179, 192, 206, 219, 233, 248, 261, 275, 289, 303, 317, 331, 344, 358, 373, 386, 400, 414, 428, 442, 456, 469, 484, 498, 511, 525, 539, 553, 567, 581, 594, 609, 623, 636, 650, 
    664, 678, 692, 706, 719, 734, 748, 761, 775, 789, 803, 817, 831, 844, 859, 873, 886, 900, 915, 928, 942, 956, 969, 984, 998, 1011, 1025, 1040, 1053, 1067, 1080, 1094]
    数据2 = [0, 714, 786, 859, 932, 1005, 1077, 1150, 1222, 1295, 1367, 1440, 1512, 1584, 1657, 1729, 1802, 1874, 1947, 2020, 2093, 2165, 2238, 2310, 2382, 2455, 2527, 2600, 2672, 2745, 2817, 2890, 2962, 
    3035, 3108, 3180, 3253, 3325, 3398, 3470, 3543, 3615, 3688, 3760, 3833, 3905, 3977, 4050, 4123, 4196, 4268, 4341, 4413, 4486, 4558, 4631, 4703, 4775, 4848, 4920, 4993, 5065, 5138, 5211, 5284, 5356, 5429, 5501, 5573, 5646, 5718]
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级] * 3) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 风暴骑兵技能4(被动技能):
    名称 = 'APG63'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.14 + 0.01 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


class 风暴骑兵技能5(主动技能):
    名称 = '激光炮'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    数据 = [0, 2541, 2800, 3057, 3315, 3572, 3831, 4089, 4346, 4605, 4863, 5120, 5378, 5636, 5894, 6152, 6409, 6668, 6925, 7183, 7442, 7699, 7957, 8214, 8473, 8731, 8988, 9246, 9504, 9762, 10020, 10277, 10536, 
    10793, 11051, 11310, 11567, 11825, 12083, 12341, 12599, 12856, 13114, 13373, 13630, 13888, 14146, 14404, 14662, 14919, 15178, 15435, 15693, 15952, 16209, 16467, 16724, 16983, 17241, 17498, 17756, 18014, 18272, 
    18530, 18787, 19046, 19304, 19561, 19820, 20077, 20335]
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

class 风暴骑兵技能6(被动技能):
    名称 = '蓄电激光炮'
    所在等级 = 25
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['激光炮']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.25+0.05 * self.等级, 5)

class 风暴骑兵技能7(主动技能):
    名称 = '聚焦喷火器'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    数据 = [0, 199, 219, 240, 260, 280, 300, 321, 341, 361, 381, 402, 422, 442, 462, 483, 503, 523, 543, 564, 584, 604, 624, 645, 665, 685, 705, 726, 746, 766, 786, 807, 827, 847, 867, 888, 908, 928, 948, 
    969, 989, 1009, 1029, 1050, 1070, 1090, 1110, 1131, 1151, 1171, 1191, 1212, 1232, 1252, 1272, 1293, 1313, 1333, 1353, 1373, 1393, 1413, 1433, 1454, 1474, 1494, 1514, 1535, 1555, 1575, 1595]
    攻击次数 = 29
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 风暴骑兵技能8(主动技能):
    名称 = 'FM31榴弹发射器'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    数据 = [0, 819, 903, 985, 1068, 1151, 1235, 1318, 1402, 1484, 1567, 1650, 1734, 1817, 1901, 1983, 2066, 2149, 2233, 2316, 2400, 2482, 2565, 2648, 2732, 2815, 2899, 2981, 3064, 3147, 3231, 3314, 3397, 3480, 3563, 3646, 3730, 3813, 
    3896, 3979, 4062, 4145, 4229, 4311, 4395, 4478, 4561, 4644, 4728, 4810, 4894, 4977, 5059, 5143, 5225, 5309, 5392, 5476, 5558, 5642, 5724, 5808, 5891, 5975, 6057, 6141, 6223, 6307, 6390, 6474, 6556]
    攻击次数 = 8
    CD = 15.0
    TP成长 = 0.20
    TP上限 = 1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.基础释放次数 = 4
            self.攻击次数 = 2
            self.倍率 *= 1.18
            self.CD *= float(4 / 15)
        elif x == 1:
            self.基础释放次数 = 4
            self.攻击次数 = 2
            self.倍率 *= 1.27
            self.CD *= float(4 / 15)
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>M102-CERM弹药</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[FM-31榴弹发射器]<br>"
            temp += "可以补充榴弹<br>"
            temp += "榴弹冷却时间 : 4秒<br>"
            temp += "长按技能键可以连续发射<br>"
            temp += "攻击力 +18%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "装弹数上限 +2 (学习强化技能后 +1)<br>"
            temp += "爆炸范围 +20%"
        elif x == 1:
            temp = "<font color='#FF00FF'>M102-CERM弹药</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[FM-31榴弹发射器]<br>"
            temp += "可以补充榴弹<br>"
            temp += "榴弹冷却时间 : 4秒<br>"
            temp += "长按技能键可以连续发射<br>"
            temp += "攻击力 +18%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "装弹数上限 +2 (学习强化技能后 +1)<br>"
            temp += "爆炸范围 +20%<br>"
            temp += "攻击力 +9%"
        return temp 

class 风暴骑兵技能9(主动技能):
    名称 = 'FM92mk2榴弹'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    数据 = [0, 1137, 1253, 1368, 1485, 1600, 1715, 1831, 1946, 2061, 2177, 2292, 2407, 2524, 2639, 2754, 2870, 2985, 3101, 3216, 3331, 3448, 3563, 3678, 3794, 3909, 4024, 4140, 4255, 4372, 4487, 4602, 4718, 4833, 4948, 5064, 
    5179, 5294, 5411, 5526, 5641, 5757, 5872, 5988, 6103, 6218, 6335, 6450, 6565, 6681, 6796, 6911, 7027, 7142, 7258, 7374, 7489, 7605, 7720, 7835, 7951, 8066, 8182, 8298, 8413, 8528, 8644, 8759, 8875, 8990, 9106]
    攻击次数 = 8
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 风暴骑兵技能10(主动技能):
    名称 = '量子爆弹'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    数据1 = [0, 673, 741, 809, 878, 946, 1013, 1082, 1150, 1219, 1287, 1355, 1424, 1492, 1561, 1629, 1696, 1765, 1833, 1902, 1970, 2038, 2107, 2175, 2244, 2311, 2379, 2448, 2516, 2584, 2653, 2721, 2790, 2858, 2926, 2994, 
    3062, 3130, 3199, 3267, 3336, 3404, 3472, 3541, 3609, 3677, 3745, 3813, 3882, 3950, 4019, 4087, 4155, 4224, 4292, 4359, 4428, 4496, 4565, 4633, 4701, 4770, 4838, 4907, 4975, 5042, 5111, 5179, 5247, 5316, 5384]
    攻击次数1 = 1
    数据2 = [0, 7739, 8525, 9310, 10096, 10881, 11667, 12451, 13237, 14022, 14807, 15593, 16378, 17163, 17948, 18734, 19519, 20305, 21090, 21874, 22660, 23445, 24231, 25016, 25802, 26586, 27371, 28157, 28942, 29728, 30513, 
    31298, 32083, 32868, 33654, 34439, 35225, 36009, 36795, 37580, 38366, 39151, 39936, 40721, 41506, 42292, 43077, 43863, 44647, 45432, 46218, 47003, 47789, 48574, 49359, 50144, 50930, 51715, 52500, 53286, 54070, 54856, 
    55641, 56427, 57212, 57998, 58782, 59567, 60353, 61138, 61924]
    攻击次数2 = 1

    #感电
    数据3 =[0, 10, 10, 10, 10, 10, 10, 11, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 19, 19, 20, 21, 21, 22, 23, 23, 24, 25, 25, 26, 27, 27, 28, 29, 30, 30, 31, 32, 32, 33, 34, 34, 35, 36, 36, 37, 38, 39, 39, 40, 41, 41, 
    42, 43, 43, 44, 45, 45, 46, 47, 47, 48, 49, 50, 50, 51, 52, 52, 53, 54, 54]
    攻击次数3 = 10
    CD = 18.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率
  
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 0
            self.攻击次数2 = 0.16 * 8 * 1.07
            self.攻击次数3 *= 0.16 * 8 * 1.07
            self.CD *= 0.9
        elif x == 1:
            self.攻击次数1 = 0
            self.攻击次数2 = 0.16 * 8 * 1.14
            self.攻击次数3 *= 0.16 * 8 * 1.14
            self.CD *= 0.9
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>原力轰炸</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[量子爆弹]<br>"
            temp += "变更为地毯式轰炸<br>"
            temp += "删除导弹物理攻击力<br>"
            temp += "导弹大小 -65%<br>"
            temp += "每次爆炸攻击力 -84%<br>"
            temp += "爆炸次数 +7次<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -10%<br>"
            temp += "爆炸攻击力 +7%"
        elif x == 1:
            temp = "<font color='#FF00FF'>原力轰炸</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[量子爆弹]<br>"
            temp += "变更为地毯式轰炸<br>"
            temp += "删除导弹物理攻击力<br>"
            temp += "导弹大小 -65%<br>"
            temp += "每次爆炸攻击力 -84%<br>"
            temp += "爆炸次数 +7次<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -10%<br>"
            temp += "爆炸攻击力 +14%"
        return temp 

class 风暴骑兵技能11(主动技能):
    名称 = 'X1压缩量子炮'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    数据 = [0, 17355, 19115, 20876, 22636, 24397, 26159, 27919, 29680, 31440, 33201, 34961, 36722, 38483, 40243, 42004, 43765, 45526, 47286, 49047, 50808, 52568, 54329, 56089, 57850, 59612, 61372, 63133, 64893, 66654, 
    68414, 70175, 71935, 73696, 75457, 77218, 78979, 80739, 82500, 84261, 86021, 87782, 89542, 91303, 93063, 94825, 96586, 98346, 100107, 101867, 103628, 105388, 107149, 108910, 110670, 112432, 114192, 115953, 117714, 
    119474, 121235, 122995, 124756, 126516, 128277, 130039, 131799, 133560, 135320, 137081, 138841]
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.1
            self.CD *= 0.88
        elif x == 1:
            self.倍率 *= 1.18
            self.CD *= 0.88
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>AC.X-1压缩量子炮</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[X-1压缩量子炮]<br>"
            temp += "立即发射并在最远射程处自动蓄气后爆炸<br>"
            temp += "冷却时间 -12%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "爆炸范围 +10%<br>"
            temp += "攻击力 +10%"
        elif x == 1:
            temp = "<font color='#FF00FF'>AC.X-1压缩量子炮</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[X-1压缩量子炮]<br>"
            temp += "立即发射并在最远射程处自动蓄气后爆炸<br>"
            temp += "冷却时间 -12%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "爆炸范围 +10%<br>"
            temp += "攻击力 +18%"
        return temp 

class 风暴骑兵技能12(被动技能):
    名称 = '超温重火器'
    所在等级 = 48
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.04 + 0.02 * self.等级, 5)

class 风暴骑兵技能13(主动技能):
    名称 = '远古粒子炮'
    所在等级 = 50
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 4614, 5685, 6755, 7825, 8895, 9965, 11035, 12105, 13176, 14247, 15317, 16387, 17457, 18527, 19598, 20668, 21738, 22808, 23878, 24948, 26019, 27089, 28159, 29229, 30299, 31369, 32439, 
    33510, 34580, 35650, 36720, 37790, 38860, 39931, 41001, 42071, 43141, 44212, 45282, 46353, 47423, 48493, 49563, 50633, 51703, 52773, 53844, 54914, 55984, 57054, 58124, 59194, 60265, 61335, 62405, 
    63475, 64545, 65615, 66685, 67756, 68826, 69896, 70966, 72036, 73106, 74176, 75248, 76318, 77388, 78458]
    攻击次数1 = 0
    数据2 = [0, 5366, 6610, 7855, 9099, 10344, 11588, 12833, 14077, 15322, 16566, 17809, 19054, 20298, 21543, 22787, 24032, 25276, 26521, 27765, 29010, 30254, 31499, 32743, 33987, 35231, 36476, 37720, 
    38965, 40209, 41454, 42698, 43943, 45187, 46432, 47676, 48921, 50165, 51409, 52653, 53898, 55142, 56387, 57631, 58876, 60120, 61365, 62609, 63853, 65098, 66342, 67586, 68830, 70075, 71319, 72564, 
    73808, 75053, 76297, 77542, 78786, 80031, 81275, 82520, 83763, 85008, 86252, 87497, 88741, 89986, 91230]
    攻击次数2 = 10
    CD = 159.5
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 风暴骑兵技能14(主动技能):
    名称 = '等离子放射器'
    所在等级 = 60
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    数据 = [0, 411, 452, 494, 536, 577, 619, 660, 702, 744, 785, 827, 869, 910, 952, 994, 1035, 1077, 1119, 1160, 1202, 1244, 1285, 1327, 1369, 1410, 1452, 1493, 1535, 1577, 1618, 1661, 1703, 1744, 1786, 1828, 1869, 1911, 1953, 1994, 
    2036, 2078, 2119, 2161, 2202, 2244, 2286, 2327, 2369, 2411, 2452, 2494, 2536, 2577, 2619, 2661, 2702, 2744, 2786, 2827, 2869, 2911, 2952, 2994, 3035, 3077, 3120, 3160, 3203, 3245, 3286]
    攻击次数 = 37
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 0.94
            self.CD *= 0.60
        elif x == 1:
            self.倍率 *= 0.85
            self.CD *= 0.60

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>高功率等离子体发生器</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[等离子放射器]<br>"
            temp += "立即发射等离子放射器<br>"
            temp += "发射位置残留电场<br>"
            temp += "总攻击力 +8%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -40%<br>"
            temp += "总攻击力 -23%"
        elif x == 1:
            temp = "<font color='#FF00FF'>高功率等离子体发生器</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[等离子放射器]<br>"
            temp += "立即发射等离子放射器<br>"
            temp += "发射位置残留电场<br>"
            temp += "总攻击力 +8%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -40%<br>"
            temp += "总攻击力 -14%"
        return temp  

class 风暴骑兵技能15(主动技能):
    名称 = 'FM92mk2SW榴弹'
    所在等级 = 70
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    数据 = [0, 29856, 32880, 35920, 38944, 41968, 45016, 48032, 51056, 54104, 57120, 60144, 63192, 66208, 69256, 72280, 75296, 78344, 81368, 84384, 87432, 90456, 93496, 96520, 99544, 102584, 105608, 108632, 111672, 
    114696, 117720, 120760, 123784, 126832, 129848, 132872, 135920, 138936, 141960, 145008, 148024, 151072, 154096, 157112, 160160, 163184, 166200, 169248, 172272, 175288, 178336, 181360, 184408, 187424, 190448, 
    193496, 196512, 199536, 202584, 205600, 208624, 211672, 214688, 217736, 220760, 223776, 226824, 229848, 232864, 235912, 238936]
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率
    
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.27
            self.CD *= 0.9

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>MIBC诱导装置</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[FM-92 mk2 SW榴弹]<br>"
            temp += "删除长按技能键操作<br>"
            temp += "诱导范围扩大为长按操作可调整的范围<br>"
            temp += "攻击力 +14%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -10%<br>"
            temp += "攻击力 +5%</font>"
        elif x == 1:
            temp = "<font color='#FF00FF'>MIBC诱导装置</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[FM-92 mk2 SW榴弹]<br>"
            temp += "删除长按技能键操作<br>"
            temp += "诱导范围扩大为长按操作可调整的范围<br>"
            temp += "攻击力 +14%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -10%<br>"
            temp += "攻击力 +13%</font>"
        return temp            

class 风暴骑兵技能16(被动技能):
    名称 = '重武装改造'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)

class 风暴骑兵技能17(主动技能):
    名称 = 'FSC7'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    数据1 = [0, 2020, 2226, 2431, 2635, 2840, 3046, 3250, 3455, 3660, 3865, 4070, 4274, 4480, 4686, 4890, 5095, 5300, 5505, 5710, 5915, 6119, 6325, 6530, 6734, 6941, 7146, 7350, 7555, 7761, 7965, 8170, 
    8375, 8580, 8785, 8990, 9194, 9400, 9606, 9810, 10016, 10220, 10425, 10630, 10834, 11040, 11245, 11449, 11654, 11860, 12065, 12270, 12476, 12680, 12885, 13090, 13295, 13500, 13705, 13909, 14115, 14320, 
    14524, 14731, 14936, 15140, 15345, 15549, 15755, 15960, 16164]
    攻击次数1 = 1
    数据2 = [0, 3839, 4229, 4618, 5007, 5396, 5786, 6176, 6565, 6955, 7344, 7735, 8123, 8512, 8902, 9291, 9682, 10071, 10461, 10849, 11238, 11629, 12018, 12408, 12797, 13187, 13575, 13966, 14355, 14744, 
    15134, 15524, 15913, 16302, 16692, 17081, 17472, 17861, 18250, 18639, 19028, 19419, 19808, 20198, 20587, 20977, 21365, 21755, 22145, 22534, 22924, 23314, 23704, 24092, 24482, 24871, 25260, 25651, 26040, 
    26430, 26818, 27208, 27598, 27988, 28377, 28766, 29155, 29545, 29935, 30324, 30714]
    攻击次数2 = 10
    CD = 40.0
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * self.倍率
    
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.28
            self.CD *= 0.9

class 风暴骑兵技能18(主动技能):
    名称 = 'PT15原始型压缩炮'
    备注 = '(向前)'
    所在等级 = 80
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    数据 = [0, 50432, 55548, 60664, 65781, 70896, 76013, 81130, 86246, 91362, 96478, 101595, 106710, 111827, 116944, 122060, 127176, 132292, 137409, 142525, 147641, 152758, 157874, 162990, 168107, 173223, 
    178339, 183455, 188572, 193689, 198804, 203921, 209037, 214153, 219269, 224386, 229503, 234618, 239735, 244851, 249967, 255084, 260200, 265317, 270432, 275549, 280666, 285781, 290898, 296014, 301131, 
    306247, 311363, 316480, 321595, 326712, 331829, 336945, 342061, 347177, 352294, 357409, 362526, 367643, 372759, 377875, 382991, 388108, 393224, 398340, 403457]
    CD = 45.0

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.倍率

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35

class 风暴骑兵技能19(主动技能):
    名称 = '火力全开'
    所在等级 = 85
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    data1 = [0, 556, 684, 814, 943, 1071, 1201, 1329, 1459, 1588, 1716, 1846, 1974, 2104, 2232, 2361, 2491, 2619, 2749, 2877, 3007, 3135, 3264, 3394, 3522, 3652, 3780, 3909, 4038, 4167, 4297, 4425, 4554, 
            4683, 4812, 4941, 5070, 5199, 5328, 5457, 5586, 5715, 5844, 5973, 6102, 6231, 6360, 6488, 6618, 6747, 6876, 7005, 7133, 7263, 7391, 7521, 7650, 7779, 7908, 8036, 8166, 8294, 8424, 8553, 8681, 8811, 8939, 9069, 9198, 9326, 9456]
    data2 = [0, 4137, 5096, 6055, 7014, 7974, 8932, 9892, 10852, 11811, 12770, 13729, 14689, 15649, 16607, 17567, 18526, 19485, 20445, 21404, 22364, 23322, 24282, 25242, 26200, 27160, 28119, 29078, 30038,
            30997, 31957, 32915, 33875, 34835, 35793, 36753, 37712, 38672, 39631, 40590, 41550, 42508, 43468, 44428, 45387, 46346, 47305, 48265, 49223, 50183, 51143, 52102, 53061, 54020, 54980, 55940, 56898, 57858, 
            58817, 59776, 60736, 61695, 62654, 63613, 64573, 65533, 66491, 67451, 68410, 69369, 70329]
    data3 = [0, 2364, 2912, 3460, 4008, 4557, 5105, 5653, 6200, 6748, 7298, 7845, 8393, 8941, 9489, 10038, 10586, 11134, 11682, 12230, 12779, 13327, 13875, 14423, 14971, 15520, 16068, 16616, 17164, 17712, 
            18261, 18809, 19357, 19905, 20453, 21001, 21550, 22098, 22646, 23194, 23742, 24291, 24839, 25387, 25935, 26483, 27032, 27580, 28128, 28676, 29224, 29773, 30321, 30869, 31417, 31964, 32514, 33062, 33609, 
            34157, 34705, 35254, 35802, 36350, 36898, 37446, 37995, 38543, 39091, 39639, 40187]
    data4 = [0, 492, 606, 720, 835, 949, 1062, 1177, 1291, 1405, 1520, 1634, 1748, 1863, 1976, 2090, 2205, 2319, 2433, 2548, 2662, 2775, 2890, 3004, 3118, 3233, 3347, 3461, 3576, 3689, 3803, 3918, 4032, 
            4146, 4261, 4375, 4489, 4604, 4717, 4831, 4946, 5060, 5174, 5289, 5403, 5516, 5631, 5745, 5859, 5974, 6088, 6202, 6317, 6430, 6544, 6659, 6773, 6887, 7002, 7116, 7229, 7344, 7458, 7572, 7687, 7801, 7915, 8030, 8143, 8257, 8372]
    data5 = [0, 347, 427, 508, 589, 670, 750, 830, 912, 992, 1072, 1153, 1234, 1315, 1395, 1475, 1557, 1637, 1718, 1798, 1878, 1960, 2040, 2120, 2201, 2282, 2363, 2443, 2523, 2605, 2685, 2765, 2846, 2927, 
            3008, 3088, 3168, 3249, 3330, 3410, 3491, 3571, 3653, 3733, 3813, 3894, 3975, 4056, 4136, 4216, 4298, 4378, 4458, 4539, 4619, 4701, 4781, 4861, 4942, 5023, 5103, 5184, 5264, 5346, 5426, 5506, 5587, 5668, 5749, 5829, 5909]
    data6 = [0, 590, 728, 865, 1001, 1138, 1276, 1413, 1550, 1686, 1824, 1961, 2098, 2235, 2372, 2509, 2646, 2783, 2921, 3057, 3194, 3331, 3469, 3606, 3742, 3879, 4016, 4154, 4291, 4427, 4564, 4702, 
            4839, 4976, 5112, 5250, 5387, 5524, 5661, 5798, 5935, 6072, 6209, 6347, 6483, 6620, 6757, 6895, 7032, 7168, 7305, 7443, 7580, 7717, 7853, 7991, 8128, 8265, 8402, 8539, 8676, 8813, 8950, 9088, 9224, 9361, 9498, 9636, 9773, 9909, 10046]
    data7 = [0, 29549, 36402, 43254, 50106, 56958, 63811, 70663, 77515, 84367, 91220, 98072, 104924, 111776, 118629, 125481, 132333, 139185, 146038, 152890, 159741, 166593, 173445, 180298, 187150, 194002, 
            200854, 207707, 214559, 221411, 228263, 235116, 241968, 248820, 255672, 262524, 269377, 276229, 283081, 289933, 296786, 303638, 310490, 317342, 324195, 331047, 337899, 344751, 351604, 358456, 365307, 
            372159, 379011, 385864, 392716, 399568, 406420, 413273, 420125, 426977, 433829, 440682, 447534, 454386, 461238, 468091, 474943, 481795, 488647, 495500, 502352]
    数据 = [data1, data2, data3, data4, data5, data6, data7]
    次数 = [17, 4, 4, 47, 37, 40, 1]
    #  次数可能有波动
    #  17 右上端辅助激光炮攻击力
    #  4 主激光炮攻击力
    #  4 左下端辅助激光炮攻击力
    #  47 左下端格林机枪攻击力
    #  37 右下端榴弹发射器攻击力
    #  40 火箭炮导弹爆炸攻击力
    #  1 火箭炮爆炸攻击力
    CD = 198.0

    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(7):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * self.倍率

class 风暴骑兵技能20(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 风暴骑兵技能21(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    学习间隔 = 2
    等级精通 = 1
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 风暴骑兵技能22(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((风暴骑兵等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

风暴骑兵技能列表 = []
i = 0
while i >= 0:
    try:
        exec('风暴骑兵技能列表.append(风暴骑兵技能'+str(i)+'())')
        i += 1
    except:
        i = -1

风暴骑兵技能序号 = dict()
for i in range(len(风暴骑兵技能列表)):
    风暴骑兵技能序号[风暴骑兵技能列表[i].名称] = i

风暴骑兵一觉序号 = 0
风暴骑兵二觉序号 = 0
风暴骑兵三觉序号 = 0
for i in 风暴骑兵技能列表:
    if i.所在等级 == 50:
        风暴骑兵一觉序号 = 风暴骑兵技能序号[i.名称]
    if i.所在等级 == 85:
        风暴骑兵二觉序号 = 风暴骑兵技能序号[i.名称]
    if i.所在等级 == 100:
        风暴骑兵三觉序号 = 风暴骑兵技能序号[i.名称]

风暴骑兵护石选项 = ['无']
for i in 风暴骑兵技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        风暴骑兵护石选项.append(i.名称)

风暴骑兵符文选项 = ['无']
for i in 风暴骑兵技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        风暴骑兵符文选项.append(i.名称)

class 风暴骑兵角色属性(角色属性):

    实际名称 = '风暴骑兵'
    角色 = '神枪手(女)'
    职业 = '枪炮师'

    武器选项 = ['手炮']
    
    类型选择 = ['物理百分比']
    
    类型 = '物理百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量']

    主BUFF = 1.957
   
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(风暴骑兵技能列表)
        self.技能序号= deepcopy(风暴骑兵技能序号)

class 风暴骑兵(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 风暴骑兵角色属性()
        self.角色属性A = 风暴骑兵角色属性()
        self.角色属性B = 风暴骑兵角色属性()
        self.一觉序号 = 风暴骑兵一觉序号
        self.二觉序号 = 风暴骑兵二觉序号
        self.三觉序号 = 风暴骑兵三觉序号
        self.护石选项 = deepcopy(风暴骑兵护石选项)
        self.符文选项 = deepcopy(风暴骑兵符文选项)
