from Crypto.Util.number import long_to_bytes

q, g1, g2 = (11470138098838773708030299067136047693985643409815055516364871317327807079521448915691685861415122090973650886160077675041872096255748644205171133021906581, 9003006990024217063418664322777899522670868744045338331471978102179370394474853183714250130931554683355264178666457178650493068973801371784999138015238547453749424028274489114585764789308403838869831793702683055071173043908501825323408800075943216778848624188993802253540272113542566555235758627924849465755, 30695053705787686472472089155075095431127414292070142108805891966899174910016207338925506877338039048732660872227095162264783032128353875687957732364446829529016135710433244740911334142919786084768834847576132678567406621995101556008456435289394712500552159569603814760663616101003363895634860119112142269162)
c, d, h = (62572684725806894633586610615555438660666327604574745430523129443353203741333665013245481230291882424665624338985554261478237771606647897845135142653244638464685570875207814153416503585503925102728571870862182981033391874409025876512065824758130737528657900932174208689266905409179402578538193660600147750113, 94029223758268708352102192422440162767870804423975089069088248832848614219351791559263601965084669160768031520801300153726001634980378144336422845556730611136140004899433851809390498552707062227591477204514367460310682961082004129024693435750135162313211632453329071272457875479610259166199541093368812125045, 50546540341085183415507224936518334604711685964263124636999686702641843511526498465503345467344453227152141303306529827793131490409927342367015067738979646228265647844945577289329681465107016274742563276607069587247288006071083319178678116112323261983438570338257546673823953641540087649018945691148808316116)
u1, u2, e, v = (66632231289696916498285744488845451715582410560959664362376408153108822964495865314170681131564221586163510188707866747493009792773246026296295260588843205215987204857932632870501507382694713022567107225945263382833368108671994546572920764961586825776755698210529190557793100332440397787587706932207789464864, 26408095134663528500664412256487603687548175155691166565932027521869413617755977983165272255540517119118965365249178341574587065778241561420394915544865049925431873958770030809884807139930587373248835600492147330200411060282492337946039880419852646795835198191689491199652656496211371256925270464458514331290, 101779018321251004961503893067852392494032175313676341971933813562690601201049627319810964899541774655240383027183030100700931356585491608048963758475299378515600412667747084376055408260103075443439098427841624479011278421745216305490763225917976494875336023420375195767279649898103001780201840295749797205385, 49098523663716219607067754871590190086859837322977055818571648252226592771075819679359644599145589292387378845420713446784750292673726883433316163559256923745928820467969285587045703168504193179219204667226012683942476607629593072121411526819606369760943150813129965762758247721838129337194068576186848749438)

z = (((h-1)*pow((g1-1)//q, -1, q**2)) % q**2)//q
m = (e * pow(pow(u1, z, q**2), -1, q**2) % q**2)
print(long_to_bytes(m))
