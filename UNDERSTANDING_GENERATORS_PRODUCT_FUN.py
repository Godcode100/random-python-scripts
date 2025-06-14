Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
licenses = (
    f'ABC {NUM:04}'
    for NUM in range(100)
    )
for plate in licenses:
    print(plate)

    
ABC 0000
ABC 0001
ABC 0002
ABC 0003
ABC 0004
ABC 0005
ABC 0006
ABC 0007
ABC 0008
ABC 0009
ABC 0010
ABC 0011
ABC 0012
ABC 0013
ABC 0014
ABC 0015
ABC 0016
ABC 0017
ABC 0018
ABC 0019
ABC 0020
ABC 0021
ABC 0022
ABC 0023
ABC 0024
ABC 0025
ABC 0026
ABC 0027
ABC 0028
ABC 0029
ABC 0030
ABC 0031
ABC 0032
ABC 0033
ABC 0034
ABC 0035
ABC 0036
ABC 0037
ABC 0038
ABC 0039
ABC 0040
ABC 0041
ABC 0042
ABC 0043
ABC 0044
ABC 0045
ABC 0046
ABC 0047
ABC 0048
ABC 0049
ABC 0050
ABC 0051
ABC 0052
ABC 0053
ABC 0054
ABC 0055
ABC 0056
ABC 0057
ABC 0058
ABC 0059
ABC 0060
ABC 0061
ABC 0062
ABC 0063
ABC 0064
ABC 0065
ABC 0066
ABC 0067
ABC 0068
ABC 0069
ABC 0070
ABC 0071
ABC 0072
ABC 0073
ABC 0074
ABC 0075
ABC 0076
ABC 0077
ABC 0078
ABC 0079
ABC 0080
ABC 0081
ABC 0082
ABC 0083
ABC 0084
ABC 0085
ABC 0086
ABC 0087
ABC 0088
ABC 0089
ABC 0090
ABC 0091
ABC 0092
ABC 0093
ABC 0094
ABC 0095
ABC 0096
ABC 0097
ABC 0098
ABC 0099

import time
items =[cabbage,sukuma,time.sleep(1),time.sleep(2)]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    items =[cabbage,sukuma,time.sleep(1),time.sleep(2)]
NameError: name 'cabbage' is not defined
items =['cabbage','sukuma',time.sleep(1),time.sleep(2)]
print(items)
['cabbage', 'sukuma', None, None]
sleep=(time.sleep(t) for t in [cabbage,2,3])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    sleep=(time.sleep(t) for t in [cabbage,2,3])
NameError: name 'cabbage' is not defined
cabbage =1
sleep=(time.sleep(t) for t in [cabbage,2,3])
sleep=(time.sleep(t) for t in [cabbage,2,3,time.sleep(4)])

from itertools import product
from string import ascii_uppercase as alphabet
for letters in product (alphabet):
    print(letters)

    
('A',)
('B',)
('C',)
('D',)
('E',)
('F',)
('G',)
('H',)
('I',)
('J',)
('K',)
('L',)
('M',)
('N',)
('O',)
('P',)
('Q',)
('R',)
('S',)
('T',)
('U',)
('V',)
('W',)
('X',)
('Y',)
('Z',)
for letters in product(alphabet):
    letters = "".join(letters)
    print(letters)

    
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
for letters in product(alphabet):
    letters = "".join(letters)
    print(list(letters))

    
['A']
['B']
['C']
['D']
['E']
['F']
['G']
['H']
['I']
['J']
['K']
['L']
['M']
['N']
['O']
['P']
['Q']
['R']
['S']
['T']
['U']
['V']
['W']
['X']
['Y']
['Z']
for letters in product (alphabet,repeat=2):
    print(letters)

    
('A', 'A')
('A', 'B')
('A', 'C')
('A', 'D')
('A', 'E')
('A', 'F')
('A', 'G')
('A', 'H')
('A', 'I')
('A', 'J')
('A', 'K')
('A', 'L')
('A', 'M')
('A', 'N')
('A', 'O')
('A', 'P')
('A', 'Q')
('A', 'R')
('A', 'S')
('A', 'T')
('A', 'U')
('A', 'V')
('A', 'W')
('A', 'X')
('A', 'Y')
('A', 'Z')
('B', 'A')
('B', 'B')
('B', 'C')
('B', 'D')
('B', 'E')
('B', 'F')
('B', 'G')
('B', 'H')
('B', 'I')
('B', 'J')
('B', 'K')
('B', 'L')
('B', 'M')
('B', 'N')
('B', 'O')
('B', 'P')
('B', 'Q')
('B', 'R')
('B', 'S')
('B', 'T')
('B', 'U')
('B', 'V')
('B', 'W')
('B', 'X')
('B', 'Y')
('B', 'Z')
('C', 'A')
('C', 'B')
('C', 'C')
('C', 'D')
('C', 'E')
('C', 'F')
('C', 'G')
('C', 'H')
('C', 'I')
('C', 'J')
('C', 'K')
('C', 'L')
('C', 'M')
('C', 'N')
('C', 'O')
('C', 'P')
('C', 'Q')
('C', 'R')
('C', 'S')
('C', 'T')
('C', 'U')
('C', 'V')
('C', 'W')
('C', 'X')
('C', 'Y')
('C', 'Z')
('D', 'A')
('D', 'B')
('D', 'C')
('D', 'D')
('D', 'E')
('D', 'F')
('D', 'G')
('D', 'H')
('D', 'I')
('D', 'J')
('D', 'K')
('D', 'L')
('D', 'M')
('D', 'N')
('D', 'O')
('D', 'P')
('D', 'Q')
('D', 'R')
('D', 'S')
('D', 'T')
('D', 'U')
('D', 'V')
('D', 'W')
('D', 'X')
('D', 'Y')
('D', 'Z')
('E', 'A')
('E', 'B')
('E', 'C')
('E', 'D')
('E', 'E')
('E', 'F')
('E', 'G')
('E', 'H')
('E', 'I')
('E', 'J')
('E', 'K')
('E', 'L')
('E', 'M')
('E', 'N')
('E', 'O')
('E', 'P')
('E', 'Q')
('E', 'R')
('E', 'S')
('E', 'T')
('E', 'U')
('E', 'V')
('E', 'W')
('E', 'X')
('E', 'Y')
('E', 'Z')
('F', 'A')
('F', 'B')
('F', 'C')
('F', 'D')
('F', 'E')
('F', 'F')
('F', 'G')
('F', 'H')
('F', 'I')
('F', 'J')
('F', 'K')
('F', 'L')
('F', 'M')
('F', 'N')
('F', 'O')
('F', 'P')
('F', 'Q')
('F', 'R')
('F', 'S')
('F', 'T')
('F', 'U')
('F', 'V')
('F', 'W')
('F', 'X')
('F', 'Y')
('F', 'Z')
('G', 'A')
('G', 'B')
('G', 'C')
('G', 'D')
('G', 'E')
('G', 'F')
('G', 'G')
('G', 'H')
('G', 'I')
('G', 'J')
('G', 'K')
('G', 'L')
('G', 'M')
('G', 'N')
('G', 'O')
('G', 'P')
('G', 'Q')
('G', 'R')
('G', 'S')
('G', 'T')
('G', 'U')
('G', 'V')
('G', 'W')
('G', 'X')
('G', 'Y')
('G', 'Z')
('H', 'A')
('H', 'B')
('H', 'C')
('H', 'D')
('H', 'E')
('H', 'F')
('H', 'G')
('H', 'H')
('H', 'I')
('H', 'J')
('H', 'K')
('H', 'L')
('H', 'M')
('H', 'N')
('H', 'O')
('H', 'P')
('H', 'Q')
('H', 'R')
('H', 'S')
('H', 'T')
('H', 'U')
('H', 'V')
('H', 'W')
('H', 'X')
('H', 'Y')
('H', 'Z')
('I', 'A')
('I', 'B')
('I', 'C')
('I', 'D')
('I', 'E')
('I', 'F')
('I', 'G')
('I', 'H')
('I', 'I')
('I', 'J')
('I', 'K')
('I', 'L')
('I', 'M')
('I', 'N')
('I', 'O')
('I', 'P')
('I', 'Q')
('I', 'R')
('I', 'S')
('I', 'T')
('I', 'U')
('I', 'V')
('I', 'W')
('I', 'X')
('I', 'Y')
('I', 'Z')
('J', 'A')
('J', 'B')
('J', 'C')
('J', 'D')
('J', 'E')
('J', 'F')
('J', 'G')
('J', 'H')
('J', 'I')
('J', 'J')
('J', 'K')
('J', 'L')
('J', 'M')
('J', 'N')
('J', 'O')
('J', 'P')
('J', 'Q')
('J', 'R')
('J', 'S')
('J', 'T')
('J', 'U')
('J', 'V')
('J', 'W')
('J', 'X')
('J', 'Y')
('J', 'Z')
('K', 'A')
('K', 'B')
('K', 'C')
('K', 'D')
('K', 'E')
('K', 'F')
('K', 'G')
('K', 'H')
('K', 'I')
('K', 'J')
('K', 'K')
('K', 'L')
('K', 'M')
('K', 'N')
('K', 'O')
('K', 'P')
('K', 'Q')
('K', 'R')
('K', 'S')
('K', 'T')
('K', 'U')
('K', 'V')
('K', 'W')
('K', 'X')
('K', 'Y')
('K', 'Z')
('L', 'A')
('L', 'B')
('L', 'C')
('L', 'D')
('L', 'E')
('L', 'F')
('L', 'G')
('L', 'H')
('L', 'I')
('L', 'J')
('L', 'K')
('L', 'L')
('L', 'M')
('L', 'N')
('L', 'O')
('L', 'P')
('L', 'Q')
('L', 'R')
('L', 'S')
('L', 'T')
('L', 'U')
('L', 'V')
('L', 'W')
('L', 'X')
('L', 'Y')
('L', 'Z')
('M', 'A')
('M', 'B')
('M', 'C')
('M', 'D')
('M', 'E')
('M', 'F')
('M', 'G')
('M', 'H')
('M', 'I')
('M', 'J')
('M', 'K')
('M', 'L')
('M', 'M')
('M', 'N')
('M', 'O')
('M', 'P')
('M', 'Q')
('M', 'R')
('M', 'S')
('M', 'T')
('M', 'U')
('M', 'V')
('M', 'W')
('M', 'X')
('M', 'Y')
('M', 'Z')
('N', 'A')
('N', 'B')
('N', 'C')
('N', 'D')
('N', 'E')
('N', 'F')
('N', 'G')
('N', 'H')
('N', 'I')
('N', 'J')
('N', 'K')
('N', 'L')
('N', 'M')
('N', 'N')
('N', 'O')
('N', 'P')
('N', 'Q')
('N', 'R')
('N', 'S')
('N', 'T')
('N', 'U')
('N', 'V')
('N', 'W')
('N', 'X')
('N', 'Y')
('N', 'Z')
('O', 'A')
('O', 'B')
('O', 'C')
('O', 'D')
('O', 'E')
('O', 'F')
('O', 'G')
('O', 'H')
('O', 'I')
('O', 'J')
('O', 'K')
('O', 'L')
('O', 'M')
('O', 'N')
('O', 'O')
('O', 'P')
('O', 'Q')
('O', 'R')
('O', 'S')
('O', 'T')
('O', 'U')
('O', 'V')
('O', 'W')
('O', 'X')
('O', 'Y')
('O', 'Z')
('P', 'A')
('P', 'B')
('P', 'C')
('P', 'D')
('P', 'E')
('P', 'F')
('P', 'G')
('P', 'H')
('P', 'I')
('P', 'J')
('P', 'K')
('P', 'L')
('P', 'M')
('P', 'N')
('P', 'O')
('P', 'P')
('P', 'Q')
('P', 'R')
('P', 'S')
('P', 'T')
('P', 'U')
('P', 'V')
('P', 'W')
('P', 'X')
('P', 'Y')
('P', 'Z')
('Q', 'A')
('Q', 'B')
('Q', 'C')
('Q', 'D')
('Q', 'E')
('Q', 'F')
('Q', 'G')
('Q', 'H')
('Q', 'I')
('Q', 'J')
('Q', 'K')
('Q', 'L')
('Q', 'M')
('Q', 'N')
('Q', 'O')
('Q', 'P')
('Q', 'Q')
('Q', 'R')
('Q', 'S')
('Q', 'T')
('Q', 'U')
('Q', 'V')
('Q', 'W')
('Q', 'X')
('Q', 'Y')
('Q', 'Z')
('R', 'A')
('R', 'B')
('R', 'C')
('R', 'D')
('R', 'E')
('R', 'F')
('R', 'G')
('R', 'H')
('R', 'I')
('R', 'J')
('R', 'K')
('R', 'L')
('R', 'M')
('R', 'N')
('R', 'O')
('R', 'P')
('R', 'Q')
('R', 'R')
('R', 'S')
('R', 'T')
('R', 'U')
('R', 'V')
('R', 'W')
('R', 'X')
('R', 'Y')
('R', 'Z')
('S', 'A')
('S', 'B')
('S', 'C')
('S', 'D')
('S', 'E')
('S', 'F')
('S', 'G')
('S', 'H')
('S', 'I')
('S', 'J')
('S', 'K')
('S', 'L')
('S', 'M')
('S', 'N')
('S', 'O')
('S', 'P')
('S', 'Q')
('S', 'R')
('S', 'S')
('S', 'T')
('S', 'U')
('S', 'V')
('S', 'W')
('S', 'X')
('S', 'Y')
('S', 'Z')
('T', 'A')
('T', 'B')
('T', 'C')
('T', 'D')
('T', 'E')
('T', 'F')
('T', 'G')
('T', 'H')
('T', 'I')
('T', 'J')
('T', 'K')
('T', 'L')
('T', 'M')
('T', 'N')
('T', 'O')
('T', 'P')
('T', 'Q')
('T', 'R')
('T', 'S')
('T', 'T')
('T', 'U')
('T', 'V')
('T', 'W')
('T', 'X')
('T', 'Y')
('T', 'Z')
('U', 'A')
('U', 'B')
('U', 'C')
('U', 'D')
('U', 'E')
('U', 'F')
('U', 'G')
('U', 'H')
('U', 'I')
('U', 'J')
('U', 'K')
('U', 'L')
('U', 'M')
('U', 'N')
('U', 'O')
('U', 'P')
('U', 'Q')
('U', 'R')
('U', 'S')
('U', 'T')
('U', 'U')
('U', 'V')
('U', 'W')
('U', 'X')
('U', 'Y')
('U', 'Z')
('V', 'A')
('V', 'B')
('V', 'C')
('V', 'D')
('V', 'E')
('V', 'F')
('V', 'G')
('V', 'H')
('V', 'I')
('V', 'J')
('V', 'K')
('V', 'L')
('V', 'M')
('V', 'N')
('V', 'O')
('V', 'P')
('V', 'Q')
('V', 'R')
('V', 'S')
('V', 'T')
('V', 'U')
('V', 'V')
('V', 'W')
('V', 'X')
('V', 'Y')
('V', 'Z')
('W', 'A')
('W', 'B')
('W', 'C')
('W', 'D')
('W', 'E')
('W', 'F')
('W', 'G')
('W', 'H')
('W', 'I')
('W', 'J')
('W', 'K')
('W', 'L')
('W', 'M')
('W', 'N')
('W', 'O')
('W', 'P')
('W', 'Q')
('W', 'R')
('W', 'S')
('W', 'T')
('W', 'U')
('W', 'V')
('W', 'W')
('W', 'X')
('W', 'Y')
('W', 'Z')
('X', 'A')
('X', 'B')
('X', 'C')
('X', 'D')
('X', 'E')
('X', 'F')
('X', 'G')
('X', 'H')
('X', 'I')
('X', 'J')
('X', 'K')
('X', 'L')
('X', 'M')
('X', 'N')
('X', 'O')
('X', 'P')
('X', 'Q')
('X', 'R')
('X', 'S')
('X', 'T')
('X', 'U')
('X', 'V')
('X', 'W')
('X', 'X')
('X', 'Y')
('X', 'Z')
('Y', 'A')
('Y', 'B')
('Y', 'C')
('Y', 'D')
('Y', 'E')
('Y', 'F')
('Y', 'G')
('Y', 'H')
('Y', 'I')
('Y', 'J')
('Y', 'K')
('Y', 'L')
('Y', 'M')
('Y', 'N')
('Y', 'O')
('Y', 'P')
('Y', 'Q')
('Y', 'R')
('Y', 'S')
('Y', 'T')
('Y', 'U')
('Y', 'V')
('Y', 'W')
('Y', 'X')
('Y', 'Y')
('Y', 'Z')
('Z', 'A')
('Z', 'B')
('Z', 'C')
('Z', 'D')
('Z', 'E')
('Z', 'F')
('Z', 'G')
('Z', 'H')
('Z', 'I')
('Z', 'J')
('Z', 'K')
('Z', 'L')
('Z', 'M')
('Z', 'N')
('Z', 'O')
('Z', 'P')
('Z', 'Q')
('Z', 'R')
('Z', 'S')
('Z', 'T')
('Z', 'U')
('Z', 'V')
('Z', 'W')
('Z', 'X')
('Z', 'Y')
('Z', 'Z')
for letters in product (alphabet,repeat=2):
    letters = "".join(letters)
    print(letters)

    
AA
AB
AC
AD
AE
AF
AG
AH
AI
AJ
AK
AL
AM
AN
AO
AP
AQ
AR
AS
AT
AU
AV
AW
AX
AY
AZ
BA
BB
BC
BD
BE
BF
BG
BH
BI
BJ
BK
BL
BM
BN
BO
BP
BQ
BR
BS
BT
BU
BV
BW
BX
BY
BZ
CA
CB
CC
CD
CE
CF
CG
CH
CI
CJ
CK
CL
CM
CN
CO
CP
CQ
CR
CS
CT
CU
CV
CW
CX
CY
CZ
DA
DB
DC
DD
DE
DF
DG
DH
DI
DJ
DK
DL
DM
DN
DO
DP
DQ
DR
DS
DT
DU
DV
DW
DX
DY
DZ
EA
EB
EC
ED
EE
EF
EG
EH
EI
EJ
EK
EL
EM
EN
EO
EP
EQ
ER
ES
ET
EU
EV
EW
EX
EY
EZ
FA
FB
FC
FD
FE
FF
FG
FH
FI
FJ
FK
FL
FM
FN
FO
FP
FQ
FR
FS
FT
FU
FV
FW
FX
FY
FZ
GA
GB
GC
GD
GE
GF
GG
GH
GI
GJ
GK
GL
GM
GN
GO
GP
GQ
GR
GS
GT
GU
GV
GW
GX
GY
GZ
HA
HB
HC
HD
HE
HF
HG
HH
HI
HJ
HK
HL
HM
HN
HO
HP
HQ
HR
HS
HT
HU
HV
HW
HX
HY
HZ
IA
IB
IC
ID
IE
IF
IG
IH
II
IJ
IK
IL
IM
IN
IO
IP
IQ
IR
IS
IT
IU
IV
IW
IX
IY
IZ
JA
JB
JC
JD
JE
JF
JG
JH
JI
JJ
JK
JL
JM
JN
JO
JP
JQ
JR
JS
JT
JU
JV
JW
JX
JY
JZ
KA
KB
KC
KD
KE
KF
KG
KH
KI
KJ
KK
KL
KM
KN
KO
KP
KQ
KR
KS
KT
KU
KV
KW
KX
KY
KZ
LA
LB
LC
LD
LE
LF
LG
LH
LI
LJ
LK
LL
LM
LN
LO
LP
LQ
LR
LS
LT
LU
LV
LW
LX
LY
LZ
MA
MB
MC
MD
ME
MF
MG
MH
MI
MJ
MK
ML
MM
MN
MO
MP
MQ
MR
MS
MT
MU
MV
MW
MX
MY
MZ
NA
NB
NC
ND
NE
NF
NG
NH
NI
NJ
NK
NL
NM
NN
NO
NP
NQ
NR
NS
NT
NU
NV
NW
NX
NY
NZ
OA
OB
OC
OD
OE
OF
OG
OH
OI
OJ
OK
OL
OM
ON
OO
OP
OQ
OR
OS
OT
OU
OV
OW
OX
OY
OZ
PA
PB
PC
PD
PE
PF
PG
PH
PI
PJ
PK
PL
PM
PN
PO
PP
PQ
PR
PS
PT
PU
PV
PW
PX
PY
PZ
QA
QB
QC
QD
QE
QF
QG
QH
QI
QJ
QK
QL
QM
QN
QO
QP
QQ
QR
QS
QT
QU
QV
QW
QX
QY
QZ
RA
RB
RC
RD
RE
RF
RG
RH
RI
RJ
RK
RL
RM
RN
RO
RP
RQ
RR
RS
RT
RU
RV
RW
RX
RY
RZ
SA
SB
SC
SD
SE
SF
SG
SH
SI
SJ
SK
SL
SM
SN
SO
SP
SQ
SR
SS
ST
SU
SV
SW
SX
SY
SZ
TA
TB
TC
TD
TE
TF
TG
TH
TI
TJ
TK
TL
TM
TN
TO
TP
TQ
TR
TS
TT
TU
TV
TW
TX
TY
TZ
UA
UB
UC
UD
UE
UF
UG
UH
UI
UJ
UK
UL
UM
UN
UO
UP
UQ
UR
US
UT
UU
UV
UW
UX
UY
UZ
VA
VB
VC
VD
VE
VF
VG
VH
VI
VJ
VK
VL
VM
VN
VO
VP
VQ
VR
VS
VT
VU
VV
VW
VX
VY
VZ
WA
WB
WC
WD
WE
WF
WG
WH
WI
WJ
WK
WL
WM
WN
WO
WP
WQ
WR
WS
WT
WU
WV
WW
WX
WY
WZ
XA
XB
XC
XD
XE
XF
XG
XH
XI
XJ
XK
XL
XM
XN
XO
XP
XQ
XR
XS
XT
XU
XV
XW
XX
XY
XZ
YA
YB
YC
YD
YE
YF
YG
YH
YI
YJ
YK
YL
YM
YN
YO
YP
YQ
YR
YS
YT
YU
YV
YW
YX
YY
YZ
ZA
ZB
ZC
ZD
ZE
ZF
ZG
ZH
ZI
ZJ
ZK
ZL
ZM
ZN
ZO
ZP
ZQ
ZR
ZS
ZT
ZU
ZV
ZW
ZX
ZY
ZZ
>>> 
>>> licenses = (
...     f'{} {}
...     
SyntaxError: incomplete input
>>> licenses = (
...     f'{"".join(letters)} {num}'
...     for letters in product(alphabet,repeat=3)
...     for num in range(1000)
...     )
...     
