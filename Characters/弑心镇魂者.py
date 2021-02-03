from math import *
from PublicReference.base import *
class 弑心镇魂者主动技能(主动技能):
    锁定护石 = 0
    歼灭次数 = 0
    
class 弑心镇魂者技能0(弑心镇魂者主动技能):
    名称 = '连续射击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据1 = [0, 846, 932, 1018, 1104, 1190, 1276, 1362, 1448, 1534, 1620, 1705, 1791, 1877, 1963, 2049, 2135, 2221, 2307, 2393, 2479, 2565, 2651, 2736, 2822, 2908, 2994, 3080, 3166, 3252, 3338, 3424, 3510, 3596, 3681, 3767, 3853, 3939, 4025, 4111, 4197, 4283, 4369, 4455, 4541, 4626, 4712, 4798, 4884, 4970, 5056, 5142, 5228, 5314, 5400, 5486, 5572, 5657, 5743, 5829, 5915, 6001, 6087, 6173, 6259, 6345, 6431, 6517, 6602, 6688, 6774]
    攻击次数1 = 2
    数据2 = [0, 1129, 1243, 1358, 1472, 1587, 1701, 1816, 1930, 2045, 2160, 2274, 2389, 2503, 2618, 2732, 2847, 2961, 3076, 3191, 3305, 3420, 3534, 3649, 3763, 3878, 3992, 4107, 4221, 4336, 4451, 4565, 4680, 4794, 4909, 5023, 5138, 5252, 5367, 5482, 5596, 5711, 5825, 5940, 6054, 6169, 6283, 6398, 6512, 6627, 6742, 6856, 6971, 7085, 7200, 7314, 7429, 7543, 7658, 7772, 7887, 8002, 8116, 8231, 8345, 8460, 8574, 8689, 8803, 8918, 9033]
    攻击次数2 = 1
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

class 弑心镇魂者技能1(被动技能):
    名称 = '特工秘技'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1 + 0.02 * self.等级, 5)

class 弑心镇魂者技能2(弑心镇魂者主动技能):
    名称 = '双弦斩'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据1 = [0, 1130, 1245, 1359, 1474, 1589, 1703, 1818, 1933, 2047, 2162, 2277, 2392, 2506, 2621, 2736, 2850, 2965, 3080, 3194, 3309, 3424, 3538, 3653, 3768, 3883, 3997, 4112, 4227, 4341, 4456, 4571, 4685, 4800, 4915, 5029, 5144, 5259, 5373, 5488, 5603, 5718, 5832, 5947, 6062, 6176, 6291, 6406, 6520, 6635, 6750, 6864, 6979, 7094, 7208, 7323, 7438, 7553, 7667, 7782, 7897, 8011, 8126, 8241, 8355, 8470, 8585, 8699, 8814, 8929, 9043]
    攻击次数1 = 1
    数据2 = [0, 1695, 1867, 2039, 2211, 2383, 2555, 2727, 2899, 3071, 3244, 3416, 3588, 3760, 3932, 4104, 4276, 4448, 4620, 4792, 4964, 5136, 5308, 5480, 5652, 5824, 5996, 6168, 6340, 6512, 6684, 6856, 7028, 7200, 7372, 7544, 7716, 7888, 8060, 8232, 8404, 8577, 8749, 8921, 9093, 9265, 9437, 9609, 9781, 9953, 10125, 10297, 10469, 10641, 10813, 10985, 11157, 11329, 11501, 11673, 11845, 12017, 12189, 12361, 12533, 12705, 12877, 13049, 13221, 13393, 13565]
    攻击次数2 = 1
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率


class 弑心镇魂者技能3(弑心镇魂者主动技能):
    名称 = '月光挥斩'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据 = [0, 1932, 2128, 2325, 2521, 2717, 2913, 3109, 3305, 3501, 3697, 3893, 4089, 4285, 4481, 4678, 4874, 5070, 5266, 5462, 5658, 5854, 6050, 6246, 6442, 6638, 6835, 7031, 7227, 7423, 7619, 7815, 8011, 8207, 8403, 8599, 8795, 8991, 9188, 9384, 9580, 9776, 9972, 10168, 10364, 10560, 10756, 10952, 11148, 11345, 11541, 11737, 11933, 12129, 12325, 12521, 12717, 12913, 13109, 13305, 13501, 13698, 13894, 14090, 14286, 14482, 14678, 14874, 15070, 15266, 15462]
    攻击次数 = 2
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 弑心镇魂者技能4(被动技能):
    名称 = '小太刀精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
            if self.等级 <= 10:
                return round(1.040 + 0.01 * self.等级, 5)
            if self.等级 > 10:
                return round(1.150 + 0.02 * (self.等级 - 10), 5)
    def 物理攻击力倍率(self, 武器类型):
            if self.等级 <= 10:
                return round(1.040 + 0.01 * self.等级, 5)
            if self.等级 > 10:
                return round(1.150 + 0.02 * (self.等级 - 10), 5)


class 弑心镇魂者技能5(弑心镇魂者主动技能):
    名称 = '满月斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [0, 1159, 1277, 1395, 1512, 1630, 1748, 1865, 1983, 2100, 2218, 2336, 2453, 2571, 2689, 2806, 2924, 3042, 3159, 3277, 3395, 3512, 3630, 3748, 3865, 3983, 4101, 4218, 4336, 4454, 4571, 4689, 4807, 4924, 5042, 5160, 5277, 5395, 5512, 5630, 5748, 5865, 5983, 6101, 6218, 6336, 6454, 6571, 6689, 6807, 6924, 7042, 7160, 7277, 7395, 7513, 7630, 7748, 7866, 7983, 8101, 8219, 8336, 8454, 8572, 8689, 8807, 8924, 9042, 9160, 9277]
    攻击次数1 = 3
    数据2 = [0, 4252, 4683, 5115, 5546, 5978, 6409, 6840, 7272, 7703, 8135, 8566, 8997, 9429, 9860, 10292, 10723, 11154, 11586, 12017, 12449, 12880, 13311, 13743, 14174, 14606, 15037, 15468, 15900, 16331, 16763, 17194, 17625, 18057, 18488, 18920, 19351, 19782, 20214, 20645, 21077, 21508, 21939, 22371, 22802, 23234, 23665, 24096, 24528, 24959, 25391, 25822, 26253, 26685, 27116, 27548, 27979, 28410, 28842, 29273, 29705, 30136, 30567, 30999, 31430, 31862, 32293, 32724, 33156, 33587, 34019]
    攻击次数2 = 1
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.8
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    


class 弑心镇魂者技能6(弑心镇魂者主动技能):
    名称 = '迅步突袭'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据 = [0, 2489, 2742, 2994, 3247, 3499, 3752, 4004, 4257, 4509, 4762, 5015, 5267, 5520, 5772, 6025, 6277, 6530, 6782, 7035, 7288, 7540, 7793, 8045, 8298, 8550, 8803, 9055, 9308, 9561, 9813, 10066, 10318, 10571, 10823, 11076, 11328, 11581, 11834, 12086, 12339, 12591, 12844, 13096, 13349, 13601, 13854, 14107, 14359, 14612, 14864, 15117, 15369, 15622, 15874, 16127, 16380, 16632, 16885, 17137, 17390, 17642, 17895, 18148, 18400, 18653, 18905, 19158, 19410, 19663, 19915]
    攻击次数 = 1
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 弑心镇魂者技能7(弑心镇魂者主动技能):
    名称 = '月影秘步'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据 = [0, 837, 922, 1007, 1091, 1176, 1261, 1346, 1431, 1516, 1601, 1686, 1771, 1856, 1941, 2026, 2111, 2196, 2281, 2365, 2450, 2535, 2620, 2705, 2790, 2875, 2960, 3045, 3130, 3215, 3300, 3385, 3470, 3554, 3639, 3724, 3809, 3894, 3979, 4064, 4149, 4234, 4319, 4404, 4489, 4574, 4659, 4744, 4828, 4913, 4998, 5083, 5168, 5253, 5338, 5423, 5508, 5593, 5678, 5763, 5848, 5933, 6017, 6102, 6187, 6272, 6357, 6442, 6527, 6612, 6697]
    攻击次数 = 6
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 2.0
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.18
            self.CD *= 0.85
        elif x == 1:
            self.倍率 *= 1.27
            self.CD *= 0.85

class 弑心镇魂者技能8(弑心镇魂者主动技能):
    名称 = '锁定射击'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据 = [0, 1152, 1269, 1386, 1503, 1620, 1736, 1853, 1970, 2087, 2204, 2321, 2438, 2555, 2672, 2789, 2906, 3023, 3139, 3256, 3373, 3490, 3607, 3724, 3841, 3958, 4075, 4192, 4309, 4425, 4542, 4659, 4776, 4893, 5010, 5127, 5244, 5361, 5478, 5595, 5711, 5828, 5945, 6062, 6179, 6296, 6413, 6530, 6647, 6764, 6881, 6997, 7114, 7231, 7348, 7465, 7582, 7699, 7816, 7933, 8050, 8167, 8284, 8400, 8517, 8634, 8751, 8868, 8985, 9102, 9219]
    攻击次数 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.6 - 4.2
    锁定护石 = 0
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.05
            self.锁定护石 = 1
        elif x == 1:
            self.倍率 *= 1.14
            self.锁定护石 = 1

class 弑心镇魂者技能9(弑心镇魂者主动技能):
    名称 = '枪刃旋杀'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据1 = [0, 1105, 1217, 1329, 1442, 1554, 1666, 1778, 1890, 2002, 2115, 2227, 2339, 2451, 2563, 2675, 2787, 2900, 3012, 3124, 3236, 3348, 3460, 3573, 3685, 3797, 3909, 4021, 4133, 4246, 4358, 4470, 4582, 4694, 4806, 4918, 5031, 5143, 5255, 5367, 5479, 5591, 5704, 5816, 5928, 6040, 6152, 6264, 6377, 6489, 6601, 6713, 6825, 6937, 7050, 7162, 7274, 7386, 7498, 7610, 7722, 7835, 7947, 8059, 8171, 8283, 8395, 8508, 8620, 8732, 8844]
    攻击次数1 = 1
    数据2 = [0, 947, 1043, 1139, 1236, 1332, 1428, 1524, 1620, 1716, 1812, 1908, 2005, 2101, 2197, 2293, 2389, 2485, 2581, 2678, 2774, 2870, 2966, 3062, 3158, 3254, 3351, 3447, 3543, 3639, 3735, 3831, 3927, 4024, 4120, 4216, 4312, 4408, 4504, 4600, 4696, 4793, 4889, 4985, 5081, 5177, 5273, 5369, 5466, 5562, 5658, 5754, 5850, 5946, 6042, 6139, 6235, 6331, 6427, 6523, 6619, 6715, 6811, 6908, 7004, 7100, 7196, 7292, 7388, 7484, 7581]
    攻击次数2 = 17
    数据3 = [0, 4875, 5370, 5864, 6359, 6854, 7348, 7843, 8338, 8832, 9327, 9822, 10316, 10811, 11305, 11800, 12295, 12789, 13284, 13779, 14273, 14768, 15263, 15757, 16252, 16746, 17241, 17736, 18230, 18725, 19220, 19714, 20209, 20704, 21198, 21693, 22187, 22682, 23177, 23671, 24166, 24661, 25155, 25650, 26145, 26639, 27134, 27628, 28123, 28618, 29112, 29607, 30102, 30596, 31091, 31586, 32080, 32575, 33069, 33564, 34059, 34553, 35048, 35543, 36037, 36532, 37027, 37521, 38016, 38510, 39005]
    攻击次数3 = 2
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 4.5
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))+(self.数据3[self.等级] * self.攻击次数3 * (1 + self.TP成长 * self.TP等级))) * self.倍率


    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 *= 1.92
            self.攻击次数3 *= 0
        elif x == 1:
            self.攻击次数2 *= 2.07
            self.攻击次数3 *= 0

class 弑心镇魂者技能10(弑心镇魂者主动技能):
    名称 = '终极锁定'
    所在等级 = 60
    等级上限 = 60
    基础等级 = 23
    数据 = [0, 5036, 5547, 6058, 6569, 7080, 7591, 8102, 8613, 9124, 9635, 10146, 10657, 11167, 11678, 12189, 12700, 13211, 13722, 14233, 14744, 15255, 15766, 16277, 16788, 17299, 17810, 18321, 18832, 19343, 19854, 20365, 20876, 21387, 21897, 22408, 22919, 23430, 23941, 24452, 24963]
    攻击次数 = 4
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.2
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.07
            self.CD *= 0.90
            self.攻击次数 += 0.6
        elif x == 1:
            self.倍率 *= 1.16
            self.CD *= 0.90
            self.攻击次数 += 0.6

class 弑心镇魂者技能11(被动技能):
    名称 = '使命觉悟'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)

class 弑心镇魂者技能12(弑心镇魂者主动技能):
    名称 = '噬血绝杀'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据 = [0, 27816, 34266, 40717, 47167, 53617, 60067, 66517, 72968, 79418, 85868, 92318, 98768, 105219, 111669, 118119, 124569, 131020, 137470, 143920, 150370, 156820, 163271, 169721, 176171, 182621, 189072, 195522, 201972, 208422, 214872, 221323, 227773, 234223, 240673, 247124, 253574, 260024, 266474, 272924, 279375]
    攻击次数 = 2
    一觉减CD = 0
    冷却关联技能 = ['所有']
    暗杀目标加成 = 1.1
    CD = 145.0
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.暗杀目标加成 * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
    def CD缩减倍率(self, 武器类型):
        return round(1 - self.一觉减CD , 3)
        
class 弑心镇魂者技能13(弑心镇魂者主动技能):
    名称 = '月相轮舞'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [0, 4459, 4912, 5364, 5817, 6269, 6722, 7174, 7626, 8079, 8531, 8984, 9436, 9889, 10341, 10794, 11246, 11699, 12151, 12603, 13056, 13508, 13961, 14413, 14866, 15318, 15771, 16223, 16675, 17128, 17580, 18033, 18485, 18938, 19390, 19843, 20295, 20747, 21200, 21652, 22105, 22557, 23010, 23462, 23915, 24367, 24820, 25272, 25724, 26177, 26629, 27082, 27534, 27987, 28439, 28892, 29344, 29796, 30249, 30701, 31154, 31606, 32059, 32511, 32964, 33416, 33868, 34321, 34773, 35226, 35678]
    攻击次数1 = 2
    数据2 =  [0, 5042, 5554, 6065, 6577, 7088, 7600, 8111, 8623, 9134, 9646, 10158, 10669, 11181, 11692, 12204, 12715, 13227, 13738, 14250, 14762, 15273, 15785, 16296, 16808, 17319, 17831, 18342, 18854, 19366, 19877, 20389, 20900, 21412, 21923, 22435, 22946, 23458, 23970, 24481, 24993, 25504, 26016, 26527, 27039, 27550, 28062, 28574, 29085, 29597, 30108, 30620, 31131, 31643, 32154, 32666, 33178, 33689, 34201, 34712, 35224, 35735, 36247, 36758, 37270, 37781, 38293, 38805, 39316, 39828, 40339]
    攻击次数2 = 2
    数据3 = [0, 6303, 6942, 7581, 8221, 8860, 9500, 10139, 10779, 11418, 12058, 12697, 13336, 13976, 14615, 15255, 15894, 16534, 17173, 17813, 18452, 19091, 19731, 20370, 21010, 21649, 22289, 22928, 23568, 24207, 24846, 25486, 26125, 26765, 27404, 28044, 28683, 29323, 29962, 30601, 31241, 31880, 32520, 33159, 33799, 34438, 35078, 35717, 36356, 36996, 37635, 38275, 38914, 39554, 40193, 40833, 41472, 42111, 42751, 43390, 44030, 44669, 45309, 45948, 46588, 47227, 47866, 48506, 49145, 49785, 50424]
    攻击次数3 = 2
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.0
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))+(self.数据3[self.等级] * self.攻击次数3 * (1 + self.TP成长 * self.TP等级))) * self.倍率


    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20
            self.CD *= 0.90
        elif x == 1:
            self.倍率 *= 1.28
            self.CD *= 0.90

class 弑心镇魂者技能14(弑心镇魂者主动技能):
    名称 = '月光镇魂曲'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据1 = [0, 4385, 4829, 5274, 5719, 6164, 6609, 7054, 7499, 7943, 8388, 8833, 9278, 9723, 10168, 10613, 11058, 11502, 11947, 12392, 12837, 13282, 13727, 14172, 14616, 15061, 15506, 15951, 16396, 16841, 17286, 17730, 18175, 18620, 19065, 19510, 19955, 20400, 20845, 21289, 21734]
    攻击次数1 = 9
    数据2 = [0, 16913, 18629, 20345, 22061, 23777, 25493, 27209, 28925, 30641, 32357, 34072, 35788, 37504, 39220, 40936, 42652, 44368, 46084, 47800, 49516, 51231, 52947, 54663, 56379, 58095, 59811, 61527, 63243, 64959, 66675, 68390, 70106, 71822, 73538, 75254, 76970, 78686, 80402, 82118, 83834]
    攻击次数2 = 1
    CD = 40.0
    是否有护石 = 1
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.攻击次数1 = 1.64*(9 - 3)
        self.攻击次数2 *= 1.75

class 弑心镇魂者技能15(被动技能):
    名称 = '冷酷杀意'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

class 弑心镇魂者技能16(弑心镇魂者主动技能):
    名称 = '毁灭狂欢'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    数据1 = [0, 4306, 4743, 5180, 5617, 6054, 6491, 6927, 7364, 7801, 8238, 8675, 9112, 9549, 9986, 10423, 10860, 11296, 11733, 12170, 12607, 13044, 13481, 13918, 14355, 14792, 15228, 15665, 16102, 16539, 16976, 17413, 17850, 18287, 18724, 19161, 19597, 20034, 20471, 20908, 21345, 21782, 22219, 22656, 23093, 23530, 23966, 24403, 24840, 25277, 25714, 26151, 26588, 27025, 27462, 27899, 28335, 28772, 29209, 29646, 30083, 30520, 30957, 31394, 31831, 32267, 32704, 33141, 33578, 34015, 34452]
    攻击次数1 = 9
    暗杀目标追加攻击次数1 = 2
    数据2 = [0, 8359, 9207, 10055, 10904, 11752, 12600, 13448, 14296, 15144, 15992, 16840, 17688, 18536, 19385, 20233, 21081, 21929, 22777, 23625, 24473, 25321, 26169, 27017, 27865, 28714, 29562, 30410, 31258, 32106, 32954, 33802, 34650, 35498, 36346, 37195, 38043, 38891, 39739, 40587, 41435, 42283, 43131, 43979, 44827, 45675, 46524, 47372, 48220, 49068, 49916, 50764, 51612, 52460, 53308, 54156, 55005, 55853, 56701, 57549, 58397, 59245, 60093, 60941, 61789, 62637, 63485, 64334, 65182, 66030, 66878]
    攻击次数2 = 1
    CD = 45.0
    演出时间 = 1.5
    歼灭次数 = 0
    是否有护石 = 1
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * (self.攻击次数1 + self.暗杀目标追加攻击次数1) * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.倍率 *= 1.33

class 弑心镇魂者技能17(弑心镇魂者主动技能):
    名称 = '精准射击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据 = [0, 4963, 5467, 5971, 6474, 6978, 7481, 7985, 8488, 8992, 9496, 9999, 10503, 11006, 11510, 12014, 12517, 13021, 13524, 14028, 14531, 15035, 15539, 16042, 16546, 17049, 17553, 18057, 18560, 19064, 19567, 20071, 20574, 21078, 21582, 22085, 22589, 23092, 23596, 24100, 24603, 25107, 25610, 26114, 26617, 27121, 27625, 28128, 28632, 29135, 29639, 30143, 30646, 31150, 31653, 32157, 32660, 33164, 33668, 34171, 34675, 35178, 35682, 36185, 36689, 37193, 37696, 38200, 38703, 39207, 39711]
    攻击次数 = 1
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.5
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 弑心镇魂者技能18(弑心镇魂者主动技能):
    名称 = '月相天陨'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    数据1 = [0, 3975, 4897, 5819, 6741, 7663, 8585, 9507, 10429, 11350, 12272, 13194, 14116, 15038, 15960, 16882, 17804, 18726, 19648, 20569, 21491, 22413, 23335, 24257, 25179, 26101, 27023, 27945, 28867, 29788, 30710, 31632, 32554, 33476, 34398, 35320, 36242, 37164, 38086, 39007, 39929, 40851, 41773, 42695, 43617, 44539, 45461, 46383, 47305, 48226, 49148, 50070, 50992, 51914, 52836, 53758, 54680, 55602, 56524, 57445, 58367, 59289, 60211, 61133, 62055, 62977, 63899, 64821, 65743, 66664, 67586]
    攻击次数1 = 21
    数据2 = [0, 44955, 55380, 65805, 76229, 86654, 97078, 107503, 117928, 128352, 138777, 149201, 159626, 170050, 180475, 190900, 201324, 211749, 222173, 232598, 243022, 253447, 263872, 274296, 284721, 295145, 305570, 315995, 326419, 336844, 347268, 357693, 368117, 378542, 388967, 399391, 409816, 420240, 430665, 441089, 451514, 461939, 472363, 482788, 493212, 503637, 514062, 524486, 534911, 545335, 555760, 566184, 576609, 587034, 597458, 607883, 618307, 628732, 639156, 649581, 660006, 670430, 680855, 691279, 701704, 712128, 722553, 732978, 743402, 753827, 764251]
    攻击次数2 = 1
    CD = 180.0
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1)+(self.数据2[self.等级] * self.攻击次数2 )) * self.倍率

    

class 弑心镇魂者技能19(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 弑心镇魂者技能20(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 弑心镇魂者技能21(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

弑心镇魂者技能列表 = []
i = 0
while i >= 0:
    try:
        exec('弑心镇魂者技能列表.append(弑心镇魂者技能'+str(i)+'())')
        i += 1
    except:
        i = -1

弑心镇魂者技能序号 = dict()
for i in range(len(弑心镇魂者技能列表)):
    弑心镇魂者技能序号[弑心镇魂者技能列表[i].名称] = i

弑心镇魂者一觉序号 = 0
弑心镇魂者二觉序号 = 0
弑心镇魂者三觉序号 = 0
for i in 弑心镇魂者技能列表:
    if i.所在等级 == 50:
        弑心镇魂者一觉序号 = 弑心镇魂者技能序号[i.名称]
    if i.所在等级 == 85:
        弑心镇魂者二觉序号 = 弑心镇魂者技能序号[i.名称]
    if i.所在等级 == 100:
        弑心镇魂者三觉序号 = 弑心镇魂者技能序号[i.名称]

弑心镇魂者护石选项 = ['无']
for i in 弑心镇魂者技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        弑心镇魂者护石选项.append(i.名称)

弑心镇魂者符文选项 = ['无']
for i in 弑心镇魂者技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        弑心镇魂者符文选项.append(i.名称)

class 弑心镇魂者角色属性(角色属性):

    实际名称 = '弑心镇魂者'
    角色 = '枪剑士'
    职业 = '特工'

    武器选项 = ['小太刀']
    
    类型选择 = ['物理百分比']
    
    类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 2.00
   
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(弑心镇魂者技能列表)
        self.技能序号= deepcopy(弑心镇魂者技能序号)


    def 技能释放次数计算(self):
        技能释放次数 = []
        for i in self.技能栏:
            if i.名称 == '毁灭狂欢':
                if self.次数输入[self.技能序号[i.名称]] == '/CD':
                    i.歼灭次数 += (int((self.时间输入 - i.演出时间)/i.等效CD(self.武器类型,self.类型) + 1 + i.基础释放次数))
                else:
                    i.歼灭次数 += (round(self.次数输入[self.技能序号[i.名称]],2)+i.基础释放次数)
        for i in self.技能栏:
            if i.是否有伤害==1 and i.名称 != '月影秘步' and i.名称 != '锁定射击':
                if self.次数输入[self.技能序号[i.名称]] == '/CD':
                    技能释放次数.append(int((self.时间输入 - i.演出时间)/i.等效CD(self.武器类型,self.类型) + 1 + i.基础释放次数))
                else:
                    技能释放次数.append(round(self.次数输入[self.技能序号[i.名称]],2))
            elif i.名称 == '月影秘步':
                if self.次数输入[self.技能序号[i.名称]] == '/CD':
                    技能释放次数.append(int((self.时间输入 - i.演出时间)/i.等效CD(self.武器类型,self.类型) + 1 + i.基础释放次数)*3)
                else:
                    技能释放次数.append(round(self.次数输入[self.技能序号[i.名称]],2))
            elif i.名称 == '锁定射击':
                if self.次数输入[self.技能序号[i.名称]] == '/CD' and self.技能栏[self.技能序号['锁定射击']].锁定护石 == 1:
                    技能释放次数.append(int(int((self.时间输入 - i.演出时间)/i.等效CD(self.武器类型,self.类型) + 1 +i.基础释放次数) * 12)+(int(self.技能栏[self.技能序号['毁灭狂欢']].歼灭次数 *6)))
                elif self.次数输入[self.技能序号[i.名称]] == '/CD' and self.技能栏[self.技能序号['锁定射击']].锁定护石 == 0:
                    技能释放次数.append(int((self.时间输入 - i.演出时间)/i.等效CD(self.武器类型,self.类型) + 1 + i.基础释放次数) * 12)
                else:
                    技能释放次数.append(round(self.次数输入[self.技能序号[i.名称]],2))
            else:
                技能释放次数.append(0)
        return 技能释放次数

class 弑心镇魂者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 弑心镇魂者角色属性()
        self.角色属性A = 弑心镇魂者角色属性()
        self.角色属性B = 弑心镇魂者角色属性()
        self.一觉序号 = 弑心镇魂者一觉序号
        self.二觉序号 = 弑心镇魂者二觉序号
        self.三觉序号 = 弑心镇魂者三觉序号
        self.护石选项 = deepcopy(弑心镇魂者护石选项)
        self.符文选项 = deepcopy(弑心镇魂者符文选项)
    def 界面(self):
        super().界面()
        self.一觉减CD开关=QCheckBox('一觉减CD Buff',self.main_frame2)
        self.一觉减CD开关.setChecked(False)
        self.一觉减CD开关.resize(120,20)
        self.一觉减CD开关.move(325,400)
        self.一觉减CD开关.setStyleSheet(复选框样式)

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        if self.一觉减CD开关.isChecked():
            属性.技能栏[属性.技能序号['噬血绝杀']].一觉减CD = 0.1

