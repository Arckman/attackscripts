e = 65537
n = 128299637852747781491257187842028484364103855748297296704808405762229741626342194440837748106022068295635777844830831811978557490708404900063082674039252789841829590381008343327258960595508204744589399243877556198799438322881052857422197506822302290812621883700357890208069551876513290323124813780520689585503
c = 43160414063424128744492209010823042660025171642991046645158489731385945722740307002278661617111192557638773493117905684302084789590107080892369738949935010170735247383608959796206619491522997896941432858113478736544386518678449541064813172833593755715667806740002726487780692635238838746604939551393627585159

p=11326943005628119672694629821649856331564947811949928186125208046290130000912120768861173564277210907403841603312764378561200102283658817695884193223692869
q=11326943005628119672694629821649856331564947811949928186125208046290130000912216246378177299696220728414241927034282796937320547048361486068608744598351187


phi=(p-1)*(q-1)
from Crypto.Util.number import inverse

d=inverse(e,phi)
m=pow(c,d,n)
# print m
print hex(m)[2:-1].decode('hex')