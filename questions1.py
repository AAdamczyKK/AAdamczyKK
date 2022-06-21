import random
import re

questions = ('''
1. Analiza opodatkowania zbycia zorganizowanej części przedsiębiorstwa przez podatnika będącego osobą
fizyczną. 
2. Osoba fizyczna prowadząca podatkową księgę przychodów i rozchodów i będąca czynnym podatnikiem VAT 
dokonuje zbycia rzeczy ruchomej stanowiącej środek trwały w okresie amortyzacji – po dwóch latach od 
daty jego nabycia. Proszę dokonać analizy skutków podatkowych takiej transakcji. 
3. Analiza obowiązków ewidencyjnych ciążących na podatnikach prowadzących kantory. 
4. Analiza opodatkowania usług pośrednictwa finansowego przy udzielaniu kredytów. 
5. Analiza opodatkowania przekazania lub udzielenia licencji do praw autorskich i obowiązków w związku z 
16
tym ciążących na podatniku będącym osobą fizyczną. 
6. Analiza możliwości, warunków i stawek opodatkowania usług transportowych ryczałtem od przychodów 
ewidencjonowanych.
7. Warunki uznania wierzytelności za nieściągalne w zakresie podatków dochodowych i podatku od towarów 
i usług – analiza porównawcza. 
8. Aport wnoszony przez osobę prawną do spółki jawnej – analiza podatkowa.
9. Sprzedaż przez wspólnika ogółu praw i obowiązków w spółce jawnej a wystąpienie wspólnika z takiej spółki 
– analiza skutków podatkowych. 
10. Sprzedaż zorganizowanej części przedsiębiorstwa a sprzedaż poszczególnych jego składników – analiza 
porównawcza skutków podatkowych. 
11. Likwidacja spółki z o.o. a likwidacja spółki jawnej – analiza porównawcza skutków podatkowych. 
12. Analiza opodatkowania podatkiem dochodowym wartości majątku otrzymanego przez udziałowca 
będącego osobą fizyczną oraz udziałowca będącego osobą prawną w związku z likwidacją spółki 
kapitałowej. 
13. Odpisy amortyzacyjne od nowych oraz używanych środków trwałych – analiza podobieństw i różnic. 
14. Dobrowolne i przymusowe zbycie akcji/udziałów w celu umorzenia – analiza porównawcza skutków 
podatkowych. 
15. Analiza porównawcza pojęcia „działalność gospodarcza” na gruncie ustaw podatkowych. 
16. Analiza skutków podatkowych wypłaty dywidendy przez spółkę mającą siedzibę na terytorium RP na 
rzecz udziałowca mającego rezydencję podatkową na terytorium jednego z państw należących do 
Europejskiego Obszaru Gospodarczego. 
17. Analiza skutków podatkowych odpłatnego zbycia akcji/udziałów w spółkach na podstawie typowej umowy w 
sprawie unikania podwójnego opodatkowania zawartej przez Polskę. 
18. Analiza porównawcza metod unikania podwójnego opodatkowania z perspektywy planowania podatkowego. 
19. Zakład zagraniczny a spółka zależna – analiza z perspektywy planowania podatkowego. 
20. Hybrydowe formy wykonywania działalności gospodarczej z perspektywy planowania podatkowego. 
21. Analiza możliwości i warunków dokonywania zabezpieczenia na majątku podatnika przed wydaniem decyzji 
wymiarowych. 
22. Świadczenia nieodpłatne i częściowo odpłatne w podatkach dochodowych – analiza porównawcza skutków 
podatkowych. 
23. Dwa podmioty powiązane A sp. z o.o. (pożyczkodawca) oraz B. sp. z o.o. (pożyczkobiorca) podpisały 
umowę pożyczki oprocentowanej w wysokości 1% p. a. Jeżeli organ podatkowy poweźmie wątpliwości co 
do rynkowego poziomu uzgodnionych odsetek, to jakie będą konsekwencje podatkowe dla podatników A i 
B? 
24. Świadczenie pracy na rzecz spółki jawnej przez jej wspólnika – analiza skutków podatkowych. 
25. Analiza konsekwencji świadomego nieewidencjonowania przez podatnika 10% ogółu przychodów w 
podatkowej księdze przychodów i rozchodów. 
26. Jakie metody weryfikacji cen transferowych mogą być zastosowane w przypadku transakcji pomiędzy 
polskim podmiotem o ograniczonych funkcjach i ryzyku, który produkuje i sprzedaje wyroby do podmiotu 
powiązanego? Jakie czynniki należy wziąć pod uwagę przy dokonywaniu wyboru najwłaściwszej metody z 
perspektywy przepisów o cenach transferowych? 
27. Jakie metody weryfikacji cen transferowych mogą być zastosowane w przypadku transakcji pomiędzy 
podmiotem o ograniczonych funkcjach i ryzyku, który dystrybuuje na rynku polskim towary nabywane 
od podmiotu powiązanego? Jakie czynniki należy wziąć pod uwagę przy dokonywaniu wyboru 
najwłaściwszej metody z perspektywy przepisów o cenach transferowych? 
28. Analiza porównawcza metody koszt plus i metody marży transakcyjnej netto. 
29. Analiza wyceny transferów wewnętrznych pomiędzy przedsiębiorstwem i jego zagranicznym zakładem. 
30. Porównaj zakres obowiązków w zakresie dokumentacji cen transferowych w następujących przypadkach: 
 Podmiot A: Przychody 10 mln zł, należy do grupy kapitałowej sporządzającej skonsolidowane 
sprawozdanie finansowe i wykazującej przychody 250 mln zł. Podmiot nie korzysta ze zwolnień
podatkowych, ani nie poniósł straty podatkowej za rok podatkowy. Podmiot zawiera następujące transakcje 
z podmiotami powiązanymi: 1) zakupu licencji od podmiotu powiązanego X – wartość transakcji netto 1,8 
mln zł, 2) sprzedaż towarów do podmiotu Y o wartości netto 4 mln zł, 3) sprzedaż towarów do podmiotu Z o 
wartości netto 5,5 mln zł, 4) zakup usług informatycznych od polskiego podmiotu powiązanego 
niekorzystającego ze zwolnień podatkowych i który nie poniósł straty podatkowej za rok podatkowy – 
wartość transakcji netto 2,1 mln zł. 
 Podmiot B: Przychody 15 mln zł, należy do grupy kapitałowej sporządzającej skonsolidowane 
sprawozdanie finansowe i wykazującej przychody 180 mln zł. Podmiot nie korzysta ze zwolnień
podatkowych, poniósł stratę podatkową za rok podatkowy w wysokości 0,2 mln zł. Podmiot zawiera 
następujące transakcje z podmiotami powiązanymi: 1) sprzedaż nieruchomości na rzecz polskiego podmiotu 
powiązanego niekorzystającego ze zwolnień podatkowych i który nie poniósł straty podatkowej za rok 
podatkowy - wartość transakcji netto 10,5 mln zł, 2) świadczenie usług księgowych na rzecz podmiotu 
C - wartość transakcji netto 1,5 mln zł, 3) świadczenie usług księgowych na rzecz podmiotu D - wartość
transakcji netto 0,9 mln zł, 4) sprzedaż sprzętu komputerowego (serwery) na rzecz zagranicznego podmiotu 
17
powiązanego - wartość transakcji netto 2,1 mln zł. 
31. Analiza skutków podatkowych zawarcia umowy małżeńskiej o rozdzielności majątkowej. 
32. Analiza momentu powstania przychodu i momentu powstania obowiązku podatkowego w podatku od 
towarów i usług dla wykonanej usługi budowlanej, prawidłowo udokumentowanej fakturą VAT, w 
sytuacji gdy zapłata nastąpiła 60-go dnia od wykonania usługi. 
33. Analiza podatkowa działalności statutowej stowarzyszenia wpisanego do rejestru prowadzonego przez 
właściwego wojewodę jako instytucja kultury. 
34. Analiza opodatkowania podatkiem od towarów i usług lekarza internisty, który prowadzi gabinet 
prywatny, jednocześnie wykonuje obowiązki biegłego sądowego oraz posiada i wykonuje uprawnienia 
lekarza medycyny pracy. 
35. Nieodpłatne korzystanie przez pracownika z samochodu służbowego dla celów prywatnych – analiza 
skutków podatkowych. 
36. Typowy magazyn towarowy a magazyn konsygnacyjny – analiza podatkowa podobieństw i różnic. 
37. Analiza porównawcza warunków stosowania 0% stawki podatku od towarów i usług w eksporcie i 
wewnątrzwspólnotowej dostawie towarów. 
38. Dochód ze źródeł nieujawnionych a dochód określony w drodze oszacowania – analiza porównawcza. 
39. Analiza porównawcza opodatkowania wspólników spółki komandytowo-akcyjnej. 
40. Fundusz inwestycyjny zamknięty – analiza z perspektywy podatków dochodowych i podatku od towarów i 
usług. 
41. Analiza porównawcza metod rozliczania różnic kursowych. 
42. Analiza podatkowa opłacalności tzw. leasingu operacyjnego jako formy finansowania w porównaniu z 
kredytem bankowym. 
43. Finansowanie inwestycji rzeczowej z dotacji wolnej od podatku – analiza opłacalności. 
44. Analiza podatkowa opłacalności finansowania zewnętrznego spółki kapitałowej przez jej udziałowca. 
45. Analiza podatkowa opłacalności finansowania zewnętrznego spółki niebędącej osobą prawną przez jej 
wspólnika.
46. Hybrydyzacja podatkowa w planowaniu podatkowym. 
47. Wybór roku podatkowego przez spółkę kapitałową z perspektywy planowania podatkowego. 
48. Wybór formy wpłaty zaliczek na podatek dochodowy od osób fizycznych z perspektywy planowania 
podatkowego. 
49. Wpływ opodatkowania na opłacalność inwestycji rzeczowych (przykłady, efekt tarczy podatkowej, paradoks 
podatkowy). 
50. Wpływ wyboru przez przedsiębiorcę amortyzacji według metody degresywnej, zamiast metody liniowej 
na wartość bieżącą netto projektu inwestycyjnego. Odpowiedź uzasadnij, przyjmując, że w okresie 
planowania przedsiębiorca uzyskuje wyłącznie dochody podatkowe. 
51. Wpływ podatków dochodowych oraz majątkowych na płynność finansową przedsiębiorstwa. Efekty polityki 
wykazywania dochodów (efekt stawki podatkowej, efekt progresji, efekty odsetkowe). 
52. Analiza polityki wykazywania dochodów przy taryfach proporcjonalnych. 
53. Analiza polityki wykazywania dochodów przy taryfach progresywnych. 
54. Analiza mechanizmu odroczenia opodatkowania (przykłady transakcji, skutki podatkowe). 
55. Transakcje typu share deal a transakcje asset deal – analiza porównawcza skutków podatkowych.
56. Połączenie per incorporationem a połączenie per unionem – analiza porównawcza skutków podatkowych. 
57. Podział przez wydzielenie a sprzedaż zorganizowanej części przedsiębiorstwa – analiza porównawcza 
skutków podatkowych. 
58. Analiza zasad opodatkowania niepodzielonych zysków przy przekształceniu spółki kapitałowej w spółkę
niebędącą osobą prawną. 
59. Analiza różnic przejściowych między wynikiem finansowym a wynikiem podatkowym. 
60. Analiza różnic trwałych między wynikiem finansowym a wynikiem podatkowym. 
61. Korzyści podatkowe oraz czynniki ryzyka podatkowego związanego z działalnością wykonywaną na terenie 
specjalnej strefy ekonomicznej. 
62. Mały przedsiębiorca zamierza dokonać inwestycji rzeczowej na terenie jednej ze specjalnych stref 
ekonomicznych. Podstawowa intensywność pomocy publicznej dla tego regionu wynosi 25%. Planowane 
średnioroczne koszty pracy nowo zatrudnionych pracowników (łącznie ze składkami ZUS finansowanymi 
przez płatnika) wynoszą 500.000 zł. Proszę określić maksymalną wartość pomocy publicznej dla tego 
przedsiębiorcy, przyjmując w razie potrzeby dodatkowe założenia. 
63. Udzielenie przez wspólnika pożyczki spółce kapitałowej a udzielenie przez wspólnika pożyczki spółce 
osobowej – analiza porównawcza obciążeń podatkiem od czynności cywilnoprawnych. 
64. Analiza porównawcza opodatkowania podatkiem od towarów i usług detalicznej oraz hurtowej sprzedaży 
konsol do gier. 
65. Analiza porównawcza skutków podatkowych darowizny otrzymanej przez spółkę kapitałową oraz osobę
fizyczną prowadzącą samodzielnie pozarolniczą działalność gospodarczą. 
66. Osoba fizyczna otrzymała w drodze darowizny samochód ciężarowy, który wykorzystuje w 
prowadzonej przez siebie pozarolniczej działalności gospodarczej. Dokonaj analizy skutków 
podatkowych związanych z nabyciem i bieżącym jego użytkowaniem. 
18
67. Spółka z o.o. prowadzi działalność produkcyjną. W danym roku podatkowym spółka zamierza rozpocząć
budowę nowej hali produkcyjnej na działce zlokalizowanej przy drodze, która nie posiada wydzielonego 
zjazdu. W celu uzyskania pozwolenia na budowę spółka została zobowiązana do opracowania na własny 
koszt projektu wybudowania skrzyżowania oraz przekazania gruntów, na których prowadzona będzie 
inwestycja oraz wykonanych na nich naniesień na rzecz Skarbu Państwa. Dokonaj analizy konsekwencji 
podatkowych dla spółki związanych z realizacją tej inwestycji oraz nieodpłatnym przekazaniem gruntów. 
68. Porównaj obowiązki sprawozdawcze osoby prawnej oraz osoby fizycznej prowadzącej samodzielnie 
działalność gospodarczą w zakresie podatku od nieruchomości. 
69. Analiza opodatkowania umowy cash-poolingu zawartej a) wyłącznie pomiędzy podmiotami – 
podatnikami podatku dochodowego od osób prawnych – mającymi rezydencję podatkową na terenie 
Rzeczpospolitej Polskiej, b) pomiędzy podmiotami – podatnikami podatku dochodowego od osób 
prawnych – mającymi rezydencję podatkową na terenie Rzeczpospolitej Polskiej oraz poza terenem 
Rzeczpospolitej Polskiej (zarówno w Unii Europejskiej, jak i poza Unią Europejską). 
70. Planowanie podatkowe w obszarze podatku od towarów i usług w jednostkach samorządu terytorialnego.
71. Koncepcja centralizacji rozliczeń dla celów podatku od towarów i usług w jednostkach samorządu 
terytorialnego. 
72. Analiza aspektów podatkowych na gruncie podatku od towarów i usług dotyczących przeprowadzania 
inwestycji w jednostkach samorządu terytorialnego. 
73. Wpływ sposobu finansowania inwestycji polegającej na wytworzeniu środka trwałego będącego budowlą
na moment rozpoznania kosztu podatkowego w podatkach dochodowych oraz wysokość podatku do 
nieruchomości. 
74. Osoba prawna jest właścicielem magazynu i placu służącego do postoju ciężarówek przy magazynie. Jak 
będzie dokonywana amortyzacja placu na gruncie podatku dochodowego? Jakie problemy związane z 
opodatkowaniem placu mogą powstać w podatku od nieruchomości? Jakie problemy związane z placem 
mogą powstać na tle podatku od przychodów z budynków, o którym mowa w art. 24b ustawy o podatku 
dochodowym od osób prawnych. 
75. Prowadzenie działalności gospodarczej w mieszkaniu wykorzystywanym przez podatnika także do celów 
mieszkaniowych – analiza problemów podatkowych. 
76. Podatnik-przedsiębiorca będący osobą fizyczną dokonał zakupu samochodu ciężarowego o dopuszczalnej 
masie całkowitej 9 ton, którego będzie używał w toku swojej działalności gospodarczej. Jakie 
konsekwencje podatkowe ten zakup wywoła? Jakich obowiązków formalnych musi dopełnić? 
77. Podatnik-przedsiębiorca będący osobą prawną zakończył w sierpniu roku X prace budowlane związane z 
inwestycją w postaci budowy obiektu z biurami na wynajem. Wartość samych prac budowlanych wynosiła 
50 mln PLN. Budowa była finansowana z kredytu. Następnie rozpoczęto wyposażanie obiektu w 
urządzenia techniczne, aranżowano przestrzenie wspólne, kładziono posadzki czasami dopasowane do 
indywidualnych oczekiwań najemców, etc. Ten etap prac został zakończony w lutym roku X+1. W marcu 
X+1 do wynajętych biur zaczęli wprowadzać się najemcy. Proszę określić skutki podatkowe związane z 
rozpoczęciem użytkowania obiektu na gruncie podatku dochodowego i podatku od nieruchomości (a w 
szczególności zasady amortyzacji budynku i jego wyposażenia). 
78. W sklepie spożywczym prowadzonym przez osobę fizyczną prawdopodobnie skradziono towar o 
wartości ok 5.000 PLN. Ujęto sprawcę kradzieży towaru o wartości tylko 100 PLN. W trakcie rozkładania 
towaru i jego przechowywania zniszczeniu uległ towar o wartości 1.000 PLN. Natomiast towar o wartości 
6.000 PLN wyrzucono, ponieważ upłynął termin jego przydatności do spożycia. Proszę określić
konsekwencje powyższych zdarzeń z punktu widzenia podatku od towarów i usług oraz podatku 
dochodowego. 
79. Przedstaw korzyści w podatku dochodowym od osób prawnych wynikające z działalności badawczorozwojowej prowadzonej przez jego podatnika. 
80. Porównaj zasady zaliczania do kosztów uzyskania przychodów kosztów finansowania dłużnego na 
przykładzie osoby prawnej oraz osoby fizycznej prowadzącej samodzielnie pozarolniczą działalność
gospodarczą. 
81. Przedstaw zasady opodatkowania podmiotów w podatku dochodowym od osób prawnych 9% stawką
podatku. 
82. Zasady opodatkowania podatkiem dochodowym od dochodów z niezrealizowanych zysków powstałych przy 
zmianie rezydencji podatkowej dla osób fizycznych i osób prawnych.
83. Warunki stosowania zwolnień w podatku dochodowym od niezrealizowanych zysków dla osób fizycznych i 
osób prawnych. 
84. Należyta staranność płatnika a dobra wiara w rozumieniu przepisów o dodatkowym zobowiązaniu 
podatkowym.
85. Analiza porównawcza klauzuli ogólnej przeciwko unikaniu opodatkowania oraz tzw. małych klauzul 
przeciwko unikaniu opodatkowania zawartych w ustawach o podatkach dochodowych. 
86. Podatkowe skutki wydatków i świadczeń „okołoepidemicznych”. 
87. Nabycie środków trwałych w celu produkcji towarów związanych z przeciwdziałaniem pandemii COVID19 a odpisy amortyzacyjne w podatku dochodowym (przesłanki umożliwiające dokonanie jednorazowego 
odpisu amortyzacyjnego, katalog towarów mogących spełniać założenie produkcji związanej z 
19
przeciwdziałaniem COVID-19, limity odpisów amortyzacyjnych). 
88. Preferencje w podatkach dochodowych dla podatników prowadzących działalność badawczo-rozwojową
(B+R). 
89. Przekazanie darowizn na walkę z pandemią COVID-19 a odliczenie w podatku dochodowym (darczyńca, 
obdarowany, cel i forma darowizny). 
90. Podwyższone limity niektórych zwolnień przedmiotowych w PIT wprowadzone ustawą COVID-19. 
91. Stawka VAT 0% dla darowizn towarów związanych z ochroną zdrowia w ramach walki z COVID-19. 
92. Rezygnacja z uproszczonej formy wpłacania zaliczek w przypadku ponoszenia negatywnych konsekwencji 
ekonomicznych z powodu COVID-19. 
93. Preferencje w podatku od nieruchomości stosowane w związku z ponoszeniem negatywnych konsekwencji 
ekonomicznych z powodu COVID-19. 
''')

# sentences = [s.split(". ", maxsplit=1)[1].strip() for s in questions]
# print(sentences)


# modified_q = sentences[sentences.find(". ")+1:]
# print(modified_q)
ss = questions.split(".")

XD = random.choice(ss)

XD1 = re.sub(" +", " ", XD)
print(XD)