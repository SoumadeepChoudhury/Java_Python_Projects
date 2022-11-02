# # ################# WRITE ###################
# # import csv
# # fh=open("tt.csv","w",newline='\r\n')
# # cwriter=csv.writer(fh)
# # comdata=[['Name','Points','Rank'],['Shradha',4500,23],['Nishchay',4500,31]]
# # cwriter.writerows(comdata)
# # fh.close()
# # ################# READ ##################
# # import csv
# # with open('tt.csv','r',newline='\r\n') as fh:
# #     cread=csv.reader(fh)
# #     for i in cread:
# #         print(i)




# keysets="0123456789abcdef"
# valuesets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_=-"
# values=[]
# keys=[]
# for i in keysets:
#     for j in keysets:
#         keys.append(i+j)

# import random
# val=""
# for i in range(0,256):
#     val=random.choice(valuesets)+random.choice(valuesets)
#     while (val in values):
#         val=random.choice(valuesets)+random.choice(valuesets)
#     values.append(val)

# PRIVATEKEYS=dict(zip(keys,values))
# print(PRIVATEKEYS)
PRIVATEKEYS={'00': 'sE', '01': 'Vg', '02': '6z', '03': 'sp', '04': 'hS', '05': 'q4', '06': 'e6', '07': '2L', '08': 'Y5', '09': '68', '0a': 'P=', '0b': '3L', '0c': '9B', '0d': 'kT', '0e': 'QM', '0f': 'jg', '10': 'Xn', '11': 'E6', '12': 'wr', '13': '63', '14': '9=', '15': 'FB', '16': 'S0', '17': 'di', '18': 'im', '19': '03', '1a': 'p6', '1b': 'Y-', '1c': 'AR', '1d': 'Ls', '1e': 'Z6', '1f': 'Vy', '20': 'Ml', '21': 'HX', '22': 'g-', '23': 'l-', '24': 'tF', '25': '5Y', '26': 'Hd', '27': 'JC', '28': 'bs', '29': 'iw', '2a': 'Ol', '2b': 'YZ', '2c': 'Ks', '2d': 'GH', '2e': 'hY', '2f': 'Kx', '30': 'fM', '31': '30', '32': '6D', '33': '7u', '34': 'DO', '35': 'jN', '36': 'BE', '37': '78', '38': 'vx', '39': '-4', '3a': 'Da', '3b': '-l', '3c': '9Q', '3d': 'X1', '3e': 'vu', '3f': '2p', '40': 'lT', '41': 'tm', '42': 'Nd', '43': 'Pa', '44': 'jI', '45': 'U=', '46': 'ZN', '47': 'Bz', '48': 'UK', '49': 'Nr', '4a': 'Ll', '4b': '6x', '4c': 'P0', '4d': 'wN', '4e': 'kO', '4f': 'Jz', '50': '61', '51': 'ol', '52': '=5', '53': 'aQ', '54': 'n0', '55': 'e0', '56': 'Xf', '57': 'Es', '58': 'Is', '59': 'Aq', '5a': 'Id', '5b': '5P', '5c': 'IN', '5d': 'FY', '5e': '_y', '5f': 'Jj', '60': 'tR', '61': 'pG', '62': 'mL', '63': '0v', '64': '7e', '65': '4J', '66': 'Lt', '67': 'JB', '68': 'Sk', '69': 'L7', '6a': 'Ds', '6b': 'iS', '6c': 'Xj', '6d': 'jx', '6e': 'lK', '6f': '=w', '70': 'yE', '71': '11', '72': '_n', '73': 'ey', '74': 'i8', '75': '5y', '76': 'BQ', '77': '7m', '78': 'Um', '79': 'Ny', '7a': 'hm', '7b': 'lR', '7c': 'ky', '7d': 'd1', '7e': 'FM', '7f': 'fl', '80': 'fo', '81': 'r1', '82': 'R1', '83': 'rG', '84': 'Gf', '85': 'gD', '86': 'Qg', '87': 'k5', '88': 'nq', '89': 'xt', '8a': 'n-', '8b': 'MS', '8c': '22', '8d': 'BX', '8e': 'qi', '8f': '3t', '90': '6i', '91': 'Af', '92': '=b', '93': 'Yi', '94': 'gQ', '95': '9q', '96': 'GW', '97': 'b3', '98': 'CN', '99': 'Wb', '9a': 'Xu', '9b': '-t', '9c': 'd2', '9d': 'yN', '9e': 'XA', '9f': 'GV', 'a0': 't-', 'a1': 'Qi', 'a2': 'Cr', 'a3': '5C', 'a4': 'rr', 'a5': '90', 'a6': 'ca', 'a7': '94', 'a8': 'Gz', 'a9': 'sw', 'aa': '_M', 'ab': 'it', 'ac': 'nK', 'ad': 'nv', 'ae': 'Zk', 'af': 'OB', 'b0': '5k', 'b1': 'KE', 'b2': 'yR', 'b3': 'YM', 'b4': 'j6', 'b5': 'nd', 'b6': '2a', 'b7': 'Ym', 'b8': '-6', 'b9': 'LS', 'ba': 'rD', 'bb': 'vE', 'bc': 'MH', 'bd': 'kN', 'be': 'ZS', 'bf': 'mP', 'c0': 'Xi', 'c1': 'TO', 'c2': 'DY', 'c3': '-u', 'c4': 'Ba', 'c5': '4c', 'c6': 'Nq', 'c7': 'xS', 'c8': 'p5', 'c9': 'hM', 'ca': 'Ue', 'cb': 'ug', 'cc': 'no', 'cd': '8U', 'ce': 'Fq', 'cf': 'JD', 'd0': 'qM', 'd1': 'p=', 'd2': 'v3', 'd3': '19', 'd4': '9m', 'd5': '2l', 'd6': 'mA', 'd7': '3H', 'd8': 'dJ', 'd9': 'cd', 'da': 'g8', 'db': '1z', 'dc': 'tC', 'dd': '4P', 'de': 'MJ', 'df': '3=', 'e0': '2b', 'e1': '3c', 'e2': 'up', 'e3': 'sD', 'e4': 'Wk', 'e5': '5O', 'e6': '-0', 'e7': '4Z', 'e8': 'HM', 'e9': 'HG', 'ea': 'Zo', 'eb': 'Yk', 'ec': 'X-', 'ed': 'w=', 'ee': 'Mr', 'ef': 'U6', 'f0': 'vH', 'f1': 'fp', 'f2': 'ha', 'f3': 'xd', 'f4': 'D7', 'f5': 'PR', 'f6': '79', 'f7': 'LU', 'f8': '9P', 'f9': 'Ln', 'fa': 'Sd', 'fb': '_1', 'fc': 'UM', 'fd': 'ry', 'fe': '3D', 'ff': 'bU'}
# print(len(PRIVATEKEYS))


