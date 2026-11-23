import json,os,urllib.request as R
U=os.environ["MAKEFUN_ENV_URL"]
def post(p,b):
 return json.load(R.urlopen(R.Request(U+p,json.dumps(b).encode(),{"content-type":"application/json"})))
A=abs;V=(0,100,320,330,500,900,0);PS=[]
for s in("<<<<FFFF>>@B==>A<<<@=;:<=>>8<<<<","246648<<6<>?6=?@6<?@6=>?48<=2466","8::::<<<:<=>:==>:<>>:>>>:=<<8:::","64426442644264428664:888@@<<@B><"):
 t=[(ord(c)-60)*5 for c in s];PS.append([t[(i//8)*4+min(i%8,7-i%8)]for i in range(64)])
PS[3:3]=[[0]*64,[0]*64]
NO=(-21,-19,-12,-8,8,12,19,21);BO=(-11,-9,9,11);RO=(-10,-1,1,10);K8=BO+RO
CM={95:12,91:13,98:14,25:3,21:7,28:11};TT={};PL=[];nodes=0;X=Exception;F="abcdefgh";G=-200000
def vv(p,s):t=A(p);i=s-2*(s//10)-17;return(V[t]+PS[t-1][i if p>0 else i^56])*p//A(p)
def att(B,s,by):
 if by in(B[s+9*by],B[s+11*by]):return 1
 for ds,t in((NO,2),(K8,6),(BO,3),(RO,4)):
  for o in ds:
   x=s+o
   if t<3 or t==6:
    if B[x]==by*t:return 1
   else:
    while not B[x]:x+=o
    if B[x]in(by*t,by*5):return 1
def gen(P,cap=0):
 B,c=P[0],P[1];ms=[];ap=ms.append
 for s in range(21,99):
  p=B[s]
  if p in(0,99)or p*c<0:continue
  t=A(p)
  if t==1:
   d=-10*c
   for o in(d-1,d,d+1):
    u=s+o;q=B[u]
    if o==d and q:continue
    if o!=d and(q*c>=0 or q==99):continue
    if u<29 or u>90:
     for pr in(5,2):ap(s|u<<7|pr<<14)
    elif o!=d or not cap:
     ap(s|u<<7)
     if o==d and s//10==(8 if c>0 else 3)and not B[s+2*d]:ap(s|s+2*d<<7)
  else:
   ds=(NO,BO,RO,K8)[min(t-2,3)]
   for o in ds:
    u=s+o
    while B[u]!=99:
     q=B[u]
     if q*c<0 or not q and not cap:ap(s|u<<7)
     if q or not 2<t<6:break
     u+=o
 if not cap:
  kh=P[4][c<0]
  for to,bit,em,pa in((kh+2,1 if c>0 else 4,(kh+1,kh+2),(kh,kh+1,kh+2)),(kh-2,2 if c>0 else 8,(kh-3,kh-2,kh-1),(kh,kh-1,kh-2))):
   if P[2]&bit and all(not B[x]for x in em)and all(not att(B,x,-c)for x in pa):ap(kh|to<<7)
 return ms
def make(P,m):
 B=P[0][:];fr=m&127;to=m>>7&127;pr=m>>14;p=B[fr];t=A(p);col=p//A(p);cap=B[to];sc=P[3]
 if cap:sc-=vv(cap,to)
 n=col*pr if pr else p;sc+=vv(n,to)-vv(p,fr);B[to]=n;B[fr]=0
 Q=[B,-col,P[2]&CM.get(fr,15)&CM.get(to,15),sc,P[4][:]]
 if t==6:Q[4][col<0]=to
 if t==6 and A(to-fr)==2:rf,rt=(to+1,to-1)if to%10==7 else(to-2,to+1);B[rt]=B[rf];B[rf]=0
 return Q
def qs(P,a,b):
 global nodes;nodes+=1
 if nodes>120000:1/0
 st=P[3]*P[1]
 if st>=b:return st
 a=max(a,st)
 B=P[0];ms=gen(P,1)
 ms.sort(key=lambda m:-A(B[m>>7&127]))
 for m in ms:
  Q=make(P,m)
  if att(Q[0],Q[4][P[1]<0],Q[1]):continue
  sc=-qs(Q,-b,-a)
  if sc>=b:return sc
  if sc>a:a=sc
 return a
def sr(P,d,a,b,ply):
 if d<=0:return qs(P,a,b)
 B=P[0];k=(tuple(B),P[1],P[2])
 if ply>0 and k in PL:return 0
 tm=TT.get(k,0);PL.append(k);ms=gen(P)
 ms.sort(key=lambda m:(m!=tm,-(V[A(B[m>>7&127])]*16-A(B[m&127]))if B[m>>7&127]else -2 if m>>14 else 0))
 best=G;bm=0
 for m in ms:
  Q=make(P,m)
  if att(Q[0],Q[4][P[1]<0],Q[1]):continue
  sc=-sr(Q,d-1,-b,-a,ply+1)
  if sc>best:best=sc;bm=m
  if sc>a:a=sc
  if a>=b:break
 PL.pop()
 if best==G:return G//2+ply if att(B,P[4][P[1]<0],-P[1])else 0
 TT[k]=bm;return best
def root(P,legal):
 global nodes;nodes=0
 D={uci(m):m for m in gen(P)};PL.append((tuple(P[0]),P[1],P[2]));ms=[D[u]for u in legal if u in D]
 if len(ms)<2:return ms[0]
 bm=ms[0];d=1
 while 1:
  a=G;cb=bm
  try:
   for m in ms:
    sc=-sr(make(P,m),d-1,G,-a,1)
    if sc>a:a=sc;cb=m
   bm=cb
  except X:break
  d+=1
 return bm
def setfen(f):
 w=f.split();B=[99]*20+([99]+[0]*8+[99])*8+[99]*20;r=0;i=0;sc=0;kp=[95,25]
 for c in w[0]:
  if c.isdigit():i+=int(c)
  elif c=='/':r+=1;i=0
  else:
   p="pnbrqk".index(c.lower())+1;s=(r+2)*10+i+1;B[s]=p if c.isupper() else -p;i+=1;q=B[s];sc+=vv(q,s)
   if A(q)==6:kp[q<0]=s
 cst=sum(1<<i for i,c in enumerate("KQkq")if c in w[2])
 return[B,1 if w[1]=='w'else -1,cst,sc,kp]
def uci(m):f=m&127;t=m>>7&127;return F[f%10-1]+str(10-f//10)+F[t%10-1]+str(10-t//10)+("nbrq"[(m>>14)-2]if m>>14 else"")
while 1:
 g=post("/game",{})
 if g["status"]=="done":break
 TT.clear()
 while g["status"]=="your_move":
  P=setfen(g["fen"]);PL*=0;u=uci(root(P,g["legal_moves"]));g=post("/move",{"game":g["game"],"move":u})
