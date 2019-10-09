# All the geometries were optimized at the PBE/6-311+g(2d,p) level

dict = {}

#H2
mol="HH"
spin=0
positions = [[0, 0, -0.0259603084],
                [0, 0, 0.7259603084]]
dict[mol] = []
dict[mol] = [spin,positions]
#LiH
mol="LiH"
spin=0
positions= [[0, 0, 0.3962543501],
                [0, 0, 2.0037456499]]
dict[mol] = []
dict[mol] = [spin,positions]
#CH4
mol = "CHHHH"
spin=0
positions = [[-0.0000016290,0.00000,0.0000078502],
                  [-0.0000022937,0.00000,1.0970267936],
                  [1.0342803963,0.00000,-0.3656807611],
                  [-0.5171382367,-0.8957112847,-0.3656769413],
                  [-0.5171382368,0.8957112847,-0.3656769413]]
dict[mol] = []
dict[mol] = [spin,positions]
#NH3
mol = "NHHH"
spin=0
positions = [[-0.7080703847,0.5736644371,-0.2056610779],
                  [0.3140478690,0.6090902876,-0.2439925162],
                  [ -1.0241861213,0.3280701680,-1.1475765240],
                  [-1.0241913630,1.5321151073,-0.0355598819]]
dict[mol] = []
dict[mol] = [spin,positions]
#H2O
mol = "OHH"
spin=0
positions = [[-0.7435290312,-0.0862560218,-0.2491318075],
                  [0.2269625234,-0.0687025898,-0.2099668601],
                  [ -1.0265534922,0.2938386117,0.5988786675]]
dict[mol] = []
dict[mol] = [spin,positions]
#HF
mol="FH"
spin=0
positions= [[0, 0, -0.0161104113],[0, 0, 0.9161104113]]
dict[mol] = []
dict[mol] = [spin,positions]
#Li2
mol="LiLi"
spin=0
positions= [[0, 0, -0.0155360351],[0, 0, 2.7155360351]]
dict[mol] = []
dict[mol] = [spin,positions]
#LiF
mol="LiF"
spin=0
positions= [[0, 0, 0.0578619642],[0, 0, 1.6421380358]]
dict[mol] = []
dict[mol] = [spin,positions]
#Be2
mol="BeBe"
spin=0
positions= [[0, 0, 0.0085515554],[0, 0, 2.4414484446]]
dict[mol] = []
dict[mol] = [spin,positions]
#C2H2
mol = "CHCH"
spin=0
positions = [[ -7.5637480678 ,-4.0853657900,0.00000000],
                  [-8.6353642657,-4.0853657900,0.00000000],
                  [-6.3570037122,-4.0853657900,0.00000000],
                  [-5.2853875143,-4.0853657900,0.00000000]]
dict[mol] = []
dict[mol] = [spin,positions]
#C2H4
mol = "CCHHHH"
spin=0
positions = [[-4.5194036917,0.9995360751,-0.0000241325],
                  [-3.1861963083,0.9995360751,-0.0000241325],
                  [-5.0929778983,0.1325558381,-0.3377273553],
                  [-5.0929780326,1.8664879090,0.3377519084],
                  [ -2.6126221017,0.1325558381,-0.3377273553],
                  [-2.6126219674,1.8664879090,0.3377519084]]
dict[mol] = []
dict[mol] = [spin,positions]
#HCN
mol = "HCN"
spin=0
positions = [[ -2.1652707291,0.9995300000,0.0000000000],
                  [-3.2423025370,0.9995300000,0.0000000000],
                  [-4.4007967339,0.9995300000,0.0000000000]]
dict[mol] = []
dict[mol] = [spin,positions]
#CO
mol="CO"
spin=0
positions= [[0, 0, -0.0185570711],
                [0, 0, 1.1185570711]]
dict[mol] = []
dict[mol] = [spin,positions]
#N2
mol="NN"
spin=0
positions= [[0, 0, -0.0017036831],
                [0, 0, 1.1017036831]]
dict[mol] = []
dict[mol] = [spin,positions]
#NO
mol="NO"
spin=1
positions= [[0, 0, -0.0797720915],
                [0, 0, 1.0797720915]]
dict[mol] = []
dict[mol] = [spin,positions]
#triplet O2
mol="OO"
spin=2
positions= [[0, 0, -0.0114390797],
                [0, 0, 1.2114390797]]
dict[mol] = []
dict[mol] = [spin,positions]
#F2
mol="FF"
spin=0
positions= [[0, 0, -0.0083068123],
                [0, 0, 1.4083068123]]
dict[mol] = []
dict[mol] = [spin,positions]
#P2
mol="PP"
spin=0
positions= [[0, 0, -0.0063578484],
                [0, 0, 1.9063578484]]
dict[mol] = []
dict[mol] = [spin,positions]
#Cl2
mol="ClCl"
spin=0
positions= [[0, 0, -0.0645570711],
                [0, 0, 1.9645570711]]
dict[mol] = []
dict[mol] = [spin,positions]

print(dict)