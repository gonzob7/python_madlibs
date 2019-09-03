#------------------------------------------Packages----------------------------------------------------#

import time
import random
from termcolor import colored

#-------------------------------------------Lists------------------------------------------------------#

nounList = ["spiders","money","quiet","wish","room","attraction","tin","bat","wool","songs","home","crow","writer","bit","territory","knife","bead","laugh","table","effect","wrench","tiger","spy","bed","sugar","town","berry","act","believe","dad","airport","clam","wrist","sweater","meeting","finger","grandmother","idea","partner","oatmeal","ice","railway","glove","invention","stream","eggnog","smash","cent","scarf","shirt","attack","crate","marble","adjustment","knot","queen","history","shake","exchange","muscle","appliance","parcel","floor","mine","division","scene","ladybug","cannon","education","pie","work","arm","mitten","tank","wire","bike","hat","riddle","page","apparatus","self","wheel","pipe","crime","connection","stove","machine","weather","trail","sand","vacation","creature","rat","orange","ocean","mist","volleyball","bushes","doll","whistle","grain","lamp","smoke","oranges","wilderness","guide","zipper","coil","flag","baby","daughter","vein","feeling","birds","curve","advertisement","pest","scent","pan","bomb","knee","bee","quicksand","nest","suit","match","trip","liquid","toy","quince","laborer","giants","payment","hook","beef","cemetery","texture","play","face","art","loaf","space","pencil","visitor","hydrant","houses","sticks","sheet","bag","note","market","celery","snail","earth","cast","condition","plantation","trucks","addition","office","grip","bedroom","party","company","playground","rub","can","north","door","view","fang","powder","drawer","range","umbrella","airplane","stem","window","circle","wren","aunt","lumber","run","class","birthday","gate","low","underwear","cakes","sheep","fish","committee","poison","form","ring","harbor","jewel","creator","kettle","leg","waves","fork","field","pigs","dolls","expansion","ship","side","roll","measure","cub","insurance","cough","boat","silk","beds","weight","support","design","eye","humor","yak","wing","whip","language","ear","summer","cloth","skate","cheese","cherries","jail","statement","stick","smile","ants","health","bear","plastic","stranger","need","kitty","rail","camp","bubble","house","rule","engine","geese","bikes","channel","skin","snow","order","jump","fear","things","recess","baseball","bone","crowd","behavior","calendar","wealth","oven","square","hill","burst","wind","actor","tooth","pets","picture","brake","lettuce","swim","prose","stage","business","plane","thing","society","library","wood","coast","stone","observation","bottle","nerve","zebra","nation","rabbits","test","road","government","pump","blow","wall","hose","elbow","trouble","seed","trains","pancake","destruction","crib","coal","throat","cake","treatment","driving","toes","bells","rain","voice","porter","loss","friend","pig","name","neck","building","position","turkey","rest","arch","duck","hands","bucket","mask","route","brass","wound","reward","reading","pies","digestion","existence","animal","top","jellyfish","church","scale","belief","chalk","mailbox","sky","offer","pleasure","planes","maid","station","part","cracker","branch","toothpaste","steam","dogs","men","nose","copper","fuel","development","hot","sneeze","apparel","magic","food","coach","activity","glass","trees","soda","boundary","anger","join","acoustics","caption","club","jam","jeans","cabbage","current","yarn","toad","boot","paper","cattle","increase","cause","vest","science","carriage","plough","property","swing","plate","blade","care","thrill","mom","skirt","toys","spot","guitar","expert","drain","experience","stocking","rhythm","talk","thunder","van","bridge","ink","chance","distance","ground","pen","flowers","grandfather","sign","nut","shade","robin","holiday","cave","minister","rate","meat","camera","system","land","edge","record","transport","calculator","mouth","uncle","grape","ghost","basin","giraffe","straw","hour","zinc","cows","girl","root","team","mother","shoes","flower","ray","pet","trick","group","surprise","turn","word","spring","car","impulse","sponge","friction","letters","level","cable","alarm","desk","snakes","wash","number","coat","dust","seat","rifle","worm","stretch","growth","quiver","rings","chickens","flame","dime","love","haircut","tax","foot","sun","box","cap","lunch","regret","yoke","flock","slave","control","drink","interest","passenger","collar","cats","afterthought","cook","spoon","mind","hate","lace","lip","structure","dress","wine","vessel","soap","stitch","sail","voyage","fowl","water","badge","frog","babies","industry","detail","rice","girls","salt","quarter","gold","hobbies","produce","eggs","judge","debt","suggestion","dirt","week","jelly","request","event","year","rake","color","sea","tray","tomatoes","sound","smell","mice","taste","iron","hospital","servant","shame","battle","mass","profit","moon","rabbit","respect","place","tail","hair","flavor","title","key","mountain","milk","wave","vegetable","death","eyes","relation","silver","hole","value","kittens","sort","distribution","shock","pin","squirrel","instrument","children","soup","yam","pocket","scarecrow","slope","cart","question","hope","bite","rainstorm","spade","boy","plot","yard","juice","amount","truck","aftermath","war","air","sister","cat","unit","fact","mint","chess","linen","lock","walk","horses","crack","fog","mark","degree","seashore","fruit","pickle","pot","twist","crayon","advice","receipt","snake","middle","crook","farm","letter","man","bird","force","bath","tramp","sidewalk","chin","desire","comparison","sofa","snails","gun","steel","competition","donkey","fold","cushion","rose","price","end","back","horn","selection","school","discussion","reason","pull","dinner","night","representative","horse","head","slip","oil","cow","quill","fairies","shape","protest","power","use","plants","toe","afternoon","shelf","verse","credit","cellar","vase","star","dock","heat","stamp","winter","woman","purpose","store","teaching","doctor","corn","knowledge","toothbrush","notebook","argument","rod","shop","point","temper","example","angle","finger","rock","deer","egg","day","punishment","frogs","insect","river","hand","grade","sink","jar","kiss","person","quartz","approval","basket","tongue","base","time","brick","crown","scissors","move","books","beginner","bulb","country","potato","son","button","amusement","butter","sack","meal","shoe","fireman","locket","street","grass","account","women","basketball","cobweb","legs","lunchroom","income","tree","theory","twig","error","line","substance","icicle","metal","plant","pizzas","step","veil","motion","direction","blood","touch","fire","size","dog","monkey","canvas","board","hall","balance","border","way","lake","cover","roof","bell","bait","earthquake","ball","throne","train","breath","volcano","sleep","army","cream","quilt","change","thought","ticket","watch","brother","story","fly","secretary","popcorn","minute","trade","sleet","start","month","drop","trousers","tub","writing","agreement","downtown","string","cherry","stop","memory","frame","zoo","waste","thread","teeth","curtain","discovery","chicken","governor","achiever","cup","cactus","card","island","song","zephyr","screw","birth","arithmetic","tent","look","pear","tendency","morning","dinosaurs","authority","stomach","carpenter","leather","hammer","flight","honey","sisters","peace","front","reaction","thumb","ducks","pollution","harmony","clover","book","cars","wax","decision","furniture","spark","religion","sock","flesh","pail","stew","friends","action","kick","limit","noise","needle","fall","push","sense","show"]
adjectiveList = ["automatic","secret","good","difficult","snobbish","bawdy","spiky","cumbersome","important","youthful","succinct","industrious","sweltering","naughty","outstanding","meaty","short","purple","exciting","lamentable","swift","aware","maddening","subdued","glossy","abusive","rightful","womanly","jumpy","nippy","uppity","unadvised","accessible","nutty","lively","lackadaisical","crowded","powerful","sick","rich","groovy","fixed","whimsical","elite","functional","various","splendid","phobic","extra-small","pointless","obedient","brash","miniature","foregoing","dull","observant","frequent","superficial","uttermost","oval","pumped","rough","waiting","deranged","insidious","macabre","handsomely","wiggly","kindhearted","red","taboo","versed","high-pitched","hollow","glistening","wooden","ragged","itchy","mean","probable","joyous","bouncy","lazy","pathetic","animated","breakable","well-to-do","defeated","watery","perfect","perpetual","selfish","stingy","large","recondite","savory","wild","rhetorical","psychotic","absent","hellish","superb","magnificent","gifted","humdrum","venomous","silent","complete","abundant","quaint","broken","fast","bashful","tricky","ossified","nasty","tangy","picayune","finicky","dear","diligent","outgoing","angry","dramatic","anxious","petite","expensive","spicy","fertile","wicked","synonymous","sore","permissible","nostalgic","flaky","grouchy","scrawny","needless","giant","profuse","teeny-tiny","thirsty","threatening","debonair","charming","utopian","magical","productive","horrible","stupendous","teeny","tacky","heartbreaking","boiling","knowing","discreet","pastoral","rampant","panicky","nutritious","wonderful","frantic","used","cloudy","cultured","upset","ambiguous","rustic","like","vulgar","unbiased","woebegone","nifty","tacit","gullible","numberless","jittery","dusty","spiritual","adventurous","scattered","unequal","quickest","round","dirty","innocent","ritzy","unarmed","cowardly","sour","cynical","ahead","spiffy","dependent","best","clear","evasive","boring","garrulous","shallow","long-term","wise","juicy","square","smelly","closed","alert","afraid","defiant","crabby","medical","inconclusive","painstaking","common","therapeutic","beneficial","goofy","breezy","nauseating","stiff","reflective","soft","prickly","cute","fuzzy","abortive","quack","rambunctious","cold","accidental","dispensable","hypnotic","romantic","minor","dreary","envious","statuesque","truthful","unable","squeamish","earsplitting","reminiscent","scandalous","ready","spotty","tame","separate","repulsive","motionless","living","thick","misty","unused","luxuriant","yielding","green","abstracted","materialistic","early","plastic","daffy","wistful","unsuitable","disastrous","cloistered","dry","mighty","right","military","protective","naive","defective","substantial","fancy","mute","hanging","amused","economic","feigned","yellow","acid","opposite","secretive","ill-informed","little","ethereal","ignorant","loutish","efficient","violent","absorbing","eager","enthusiastic","poised","steady","draconian","worthless","material","rebel","wrathful","psychedelic","vivacious","damaged","willing","forgetful","same","chilly","ordinary","furry","zippy","premium","null","panoramic","thoughtless","glib","scintillating","disagreeable","abaft","wiry","courageous","chemical","deep","healthy","keen","giddy","fresh","three","terrible","orange","complex","nondescript","lonely","sincere","confused","grubby","ratty","super","fabulous","spiteful","foolish","sulky","slimy","dashing","chubby","jealous","moaning","mellow","addicted","hospitable","childlike","skinny","kindly","stereotyped","tranquil","seemly","burly","vague","squalid","dizzy","murky","terrific","bizarre","flagrant","familiar","huge","curved","plucky","five","staking","wide-eyed","eight","acrid","befitting","meek","female","wholesale","sneaky","ruddy","unequaled","absorbed","obscene","puffy","selective","labored","flimsy","exclusive","fumbling","able","certain","tangible","bloody","loose","aggressive","wacky","jazzy","tasteful","sloppy","axiomatic","dark","vengeful","feeble","future","wrong","rude","erratic","irate","mixed","voracious","white","shivering","rotten","fine","awful","hysterical","hungry","abandoned","extra-large","loud","dusty","well-off","melodic","real","handy","abashed","bustling","bent","ill","unwieldy","nonchalant","lying","caring","sharp","stormy","highfalutin","gabby","adaptable","telling","zonked","hesitant","useless","berserk","detailed","waggish","present","cautious","tawdry","proud","grandiose","earthy","jobless","uptight","different","worried","second","educated","honorable","dead","ten","rabid","six","solid","fluttering","icy","well-groomed","icky","racial","colossal","ashamed","cooperative","nine","ripe","quirky","laughable","old-fashioned","enormous","endurable","sassy","festive","sophisticated","public","overt","tidy","idiotic","frail","testy","zesty","rapid","limping","chunky","puzzling","tart","petite","fascinated","stimulating","gleaming","boorish","excellent","tearful","bright","lowly","wealthy","abrupt","vagabond","momentous","knowledgeable","torpid","internal","male","strange","innate","needy","lean","literate","changeable","scientific","tremendous","near","aboriginal","narrow","dynamic","slow","natural","ultra","warlike","remarkable","tender","plant","muddled","physical","demonic","violet","fantastic","enchanted","fair","alike","lyrical","better","grateful","black-and-white","unsightly","bite-sized","sturdy","abrasive","past","zany","gruesome","sedate","redundant","fluffy","greasy","smooth","busy","heavy","mysterious","wandering","pushy","known","illustrious","woozy","responsible","even","relieved","plain","embarrassed","chivalrous","irritating","elegant","deeply","unaccountable","quixotic","apathetic","simplistic","tasteless","acoustic","valuable","scary","uninterested","flowery","uneven","unbecoming","quick","deserted","makeshift","equable","grey","glorious","gentle","screeching","gray","amuck","adorable","greedy","late","robust","lumpy","callous","madly","rare","fragile","fearful","cagey","rural","boundless","heavenly","acidic","cooing","vacuous","lavish","amusing","four","lovely","cruel","tested","humorous","dapper","scarce","unknown","nimble","one","crazy","fallacious","helpless","questionable","alive","bumpy","roasted","abhorrent","shocking","striped","possessive","piquant","last","parched","bitter","graceful","eatable","hapless","handsome","cheap","brawny","mere","delicate","fortunate","arrogant","decorous","knotty","agreeable","helpful","noisy","encouraging","jagged","hard-to-find","verdant","numerous","eminent","lame","devilish","jaded","fanatical","spectacular","witty","unnatural","gamy","disillusioned","exotic","cut","open","necessary","spurious","abnormal","smoggy","barbarous","impolite","spooky","filthy","maniacal","overwrought","stupid","combative","shaggy","shrill","vigorous","drunk","soggy","modern","subsequent","mature","alluring","second-hand","spotted","shut","mundane","excited","distinct","nosy","aboard","empty","depressed","exultant","magenta","great","belligerent","evanescent","available","frightening","ill-fated","slim","oafish","blue","puny","calm","condemned","harsh","zealous","cute","beautiful","moldy","fierce","alcoholic","imminent","deafening","ludicrous","careful","uncovered","hallowed","nervous","shiny","brief","adjoining","auspicious","periodic","dangerous","foamy","unique","creepy","majestic","halting","spotless","harmonious","freezing","annoying","peaceful","sad","volatile","wasteful","godly","level","overconfident","voiceless","pale","understood","enchanting","homely","upbeat","clean","frightened","likeable","electric","adamant","instinctive","billowy","interesting","chief","sore","dysfunctional","thankful","steadfast","obese","annoyed","nice","flat","high","overjoyed","bewildered","blushing","previous","intelligent","infamous","tenuous","futuristic","sordid","abiding","assorted","absurd","well-made","judicious","next","clammy","thoughtful","squealing","useful","tiny","incandescent","light","curvy","old","wet","hot","aback","faulty","husky","parallel","unwritten","hateful","precious","exuberant","thinkable","whispering","somber","merciful","aspiring","free","entertaining","decisive","typical","careless","legal","broad","cuddly","neighborly","coordinated","astonishing","gaudy","far-flung","longing","placid","lucky","swanky","polite","workable","odd","yummy","learned","noxious","gainful","flashy","truculent","true","sparkling","possible","hurt","ablaze","wry","tense","lopsided","stale","serious","thundering","two","ceaseless","actually","plausible","juvenile","roomy","drab","guttural","tired","coherent","milky","erect","awake","utter","skillful","nonstop","raspy","cool","craven","regular","unusual","flippant","third","wretched","ambitious","first","homeless","wary","descriptive","left","cheerful","impartial","obsequious","pink","direful","organic","undesirable","whole","impossible","sticky","aloof","offbeat","alleged","tedious","aquatic","fretful","slippery","silent","paltry","smart","blue-eyed","clumsy","puzzled","temporary","calculating","brave","melted","snotty","towering","ugly","imperfect","acceptable","tightfisted","colorful","domineering","damp","normal","amazing","fearless","guarded","righteous","didactic","hissing","friendly","grieving","sweet","satisfying","oceanic","ubiquitous","tight","special","habitual","quarrelsome","married","tiresome","hard","famous","holistic","many","tan","grotesque","talented","daily","fat","victorious","elfin","lacking","receptive","smiling","delicious","thin","poor","political","capable","unhealthy","adhesive","disgusted","half","painful","gigantic","mushy","tasty","nebulous","pricey","warm","shaky","abject","imaginary","resolute","historical","heady","low","miscreant","massive","delirious","kind","funny","pleasant","new","rigid","obsolete","simple","vast","standing","gusty","incredible","trite","ajar","dazzling","wakeful","classy","loving","resonant","quiet","efficacious","jumbled","overrated","few","lethal","obtainable"]
animalList = ["leopard","panther","wolf","tiger","jaguar","dog","silver-fox","fox","panda","cheetah","otter","puma","lion","seal","bottlenose-dolphin","polar-bear","cougar","golden-retriever","wildcat","deer","owl","koala","grizzly-bear","lynx","golden-eagle","bunny","cat","ocelot","killer-whale","german-shepherd","brown-bear","chipmunk","zebra","hummingbird","horse","saber-toothed-cat","black-bear","labrador-retriever","coyote","elephant","giraffe","kangaroo","rabbit","eagle","reindeer","turtle","bald-eagle","raccoon","gazelle","bear","lemur","chameleon","whale","squirrel","platypus","beaver","hedgehog","tasmanian-tiger","monkey","ferret","blue-jay","hamster","wolverine","dingo","moose","beagle","komodo-dragon","jackal","saint-bernard","lamb","weasel","parrot","antelope","badger","gorilla","hare","tortoise","sloth","porcupine","hyena","guinea-pig","swan","chinchilla","rhinoceros","toucan","prairie-dog","armadillo","elk","cocker-spaniel","mountain-goat","tasmanian-devil","walrus","raven","mink","crocodile","mustang","chimpanzee","roadrunner","pig","llama","lizard","boston-terrier","bat","camel","woodpecker","lovebird","ermine","bison","donkey","alligator","iguana","duck","porpoise","orangutan","pug","octopus","hippopotamus","dachshund","sheep","alpaca","mongoose","musk-deer","ram","mouse","goat","buffalo","rottweiler","osprey","pomeranian","kiwi","kingfisher","turkey","parakeet","yorkshire-terrier","basset-hound","dove","ape","doberman-pinscher","bulldog","snake","capybara","mare","wombat","boxer","woodchuck","king-cobra","blackbird","finch","salamander","chihuahua","ground-hog","baltimore-oriole","pigeon","pelican","kinkajou","pronghorn","impala","crow","kangaroo-rat","opossum","canary","gila-monster","cow","frog","marten","heron","quail","dormouse","poodle","squid","cuckoo","marmoset","newt","condor","anteater","shih-tzu","fish","mynah-bird","civet","cuttlefish","boar","goldfish","bull","gopher","pheasant","muskrat","scorpion","shrike","goose","tapir","king-crab","yak","musk-ox","baboon","ox","roebuck","skunk","ewe","bandicoot","gull","mandrill","egret","mule","shrew","tern","duckbill","aardvark","salmon","rat","zebu","burro","steer","peccary","toad","hog","warthog","mole","tarantula","gnu","shrimp","tuna","scallop"]
clothingList = ["abaya","anorak","apron","ascot-tie","attire","balaclava","ball-gown","bandanna","baseball-cap","bathing-suit","battledress","beanie","bedclothes","bell-bottoms","belt","beret","Bermuda-shorts","bib","bikini","blazer","bloomers","blouse","boa","bonnet","boot","bow","bow-tie","boxer-shorts","boxers","bra","bracelet","brassiere","breeches","briefs","buckle","button","button-down-shirt","caftan","camisole","camouflage","cap","cape","capris","cardigan","chemise","cloak","clogs","clothes","clothing","coat","collar","corset","costume","coveralls","cowboy-boots","cowboy-hat","cravat","crown","cuff","cuff-links","culottes","cummerbund","dashiki","diaper","dinner-jacket","dirndl","drawers","dress","dress-shirt","duds","dungarees","earmuffs","earrings","elastic","evening-gown","fashion","fatigues","fedora","fez","flak-jacket","flannel-nightgown","flannel-shirt","flip-flops","formal-wear","frock","fur","fur-coat","gaiters","galoshes","garb","gabardine","garment","garters","gear","getup","gilet","girdle","glasses","gloves","gown","halter-top","handbag","handkerchief","hat","Hawaiian-shirt","hazmat-suit","headscarf","helmet","hem","high-heels","hoodie","hospital-gown","housecoat","jacket","jeans","jersey","jewelry","jodhpurs","jumper","jumpsuit","kerchief","khakis","kilt","kimono","kit","knickers","lab-coat","lapel","leather-jacket","leggings","leg-warmers","leotard","life-jacket","lingerie","loafers","loincloth","longjohns","long-underwear","miniskirt","mittens","moccasins","muffler","mumu","neckerchief","necklace","nightgown","nightshirt","onesies","outerwear","outfit","overalls","overcoat","overshirt","pajamas","panama-hat","pants","pantsuit","pantyhose","parka","pea-coat","peplum","petticoat","pinafore","pleat","pocket","pocketbook","polo-shirt","poncho","poodle-skirt","porkpie-hat","pullover","pumps","purse","raincoat","ring","robe","rugby-shirt","sandals","sari","sarong","scarf","school-uniform","scrubs","shawl","sheath-dress","shift","shirt","shoe","shorts","shoulder-pads","shrug","singlet","skirt","slacks","slip","slippers","smock","snaps","sneakers","sock","sombrero","spacesuit","Stetson-hat","stockings","stole","suit","sunbonnet","sundress","sunglasses","sun-hat","suspenders","sweater","sweatpants","sweatshirt","sweatsuit","swimsuit","T-shirt","tam","tank-top","teddy","threads","tiara","tie","tie-clip","tights","toga","togs","top","top-coat","top-hat","train","trench-coat","trunks","turtleneck","tutu","trench-coat","trousers","trunks","tube-top","tunic","turban","turtleneck-shirt","tux","tuxedo","tweed-jacket","umbrella","underclothes","undershirt","underwear","uniform","vest","visor","waders","waistcoat","wear","wedding-gown","wetsuit","white-tie","wig","windbreaker","woollens","wrap","yoke","zipper","zoris"]
bodyPartList = ["feet","fist","eyebrow","pinky-finger","lower-leg","waist","arm","ear-lobe","eyelashes","belly-button","lips","bottom","belly","knee","thigh","teeth","jaw","nostril","kidney","stomach","ear","ribs","heel","foot","scalp","abdomen","underarm","calves","gums","big-toe","breast","humerus","toes","spine","shoulder","elbow","toenail","mouth","forehead","fingernail","eyelid","upper-arm","hand","eye","neck","teeth","ankle","nose","collar-bone","groin","wrist","thumb","chin","forearm","hair","finger","shin","back","throat","palm","tongue","cheek","index-finger","hip","chest","shoulder-blade","legs","face"]
pluralNounList = ["children","teeth","feet","people","leaves","mice","geese","halves","knives","wives","lives","elves","loaves","potatoes","tomatoes","cacti","men","fungi","women","fish","deer","sheep","pennies","buses","boxes","boats","houses","cats","dogs","rivers"]
foodList = ["bass","crayfish","bagels","nectarines","mayonnaise","pork","Marsala","red-snapper","grits","sweet-chili-sauce","coconuts","swordfish","macaroni","Romano-cheese","rice","ale","pumpkin-seeds","cider-vinegar","borscht","raw-sugar","bananas","corned-beef","kale","mesclun-greens","bouillon","mustard","Havarti-cheese","cannellini-beans","figs","tartar-sauce","chocolate","snap-peas","sauerkraut","herring","ginger-ale","maple-syrup","amaretto","vegemite","mascarpone","prunes","capers","strawberries","plum-tomatoes","cider","buttermilk","split-peas","aioli","cornstarch","tea","fennel-seeds","pistachios","hoisin-sauce","curry-paste","andouille-sausage","veal","coconut-milk","portabella-mushrooms","pink-beans","creme-fraiche","cashew-nut","snapper","oranges","lentils","zest","lima-beans","ginger","spinach","jelly-beans","sazon","watermelons","geese","bruschetta","mushrooms","almond-extract","broth","adobo","cream","sausages","black-beans","kidney-beans","Canadian-bacon","bean-threads","baking-powder","asiago-cheese","chambord","honey","eel","pumpkins","shitakes","half-and-half","tomato-paste","hamburger","kiwi","summer-squash","leeks","salsa","hot-sauce","tomato-juice","bacon-grease","chai","sherry","tofu","cornmeal","Tabasco-sauce","cloves","blue-cheese","chaurice-sausage","cottage-cheese","olives","brussels-sprouts","papayas","focaccia","baking-soda","Goji-berry","squid","ricotta-cheese","blackberries","cocoa-powder","wine-vinegar","oregano","okra","grapefruits","curry-powder","gouda","brazil-nuts","peaches","steak","celery","green-onions","tonic-water","breadcrumbs","blueberries","ham","apples","angelica","chard","brown-sugar","chestnuts","monkfish","chives","water-chestnuts","octopus","aquavit","melons","dill","chicken-liver","sunflower-seeds","black-eyed-peas","french-fries","breadfruit","lettuce","coconut-oil","barley-sugar","croutons","anchovies","rose-water","ketchup","pig's-feet","rosemary","salmon","fish-sauce","jicama","raspberries","snow-peas","bean-sauce","pancetta","flounder","bacon","cumin","berries","gelatin","marshmallows","bard","spearmint","almonds","acorn-squash","cayenne-pepper","corn-flour","white-chocolate","tomatoes","vanilla","eggplants","tuna","mint","sushi","walnuts","alligator","graham-crackers","remoulade","squash","soy-sauce","horseradish","bay-leaves","yogurt","bean-sprouts","apricots","lemon-Peel","catfish","brandy","swiss-cheese","rum","olive-oil","onions","sweet-potatoes","lamb","white-beans","plums","mozzarella","sea-cucumbers","paprika","wine","tomato-puree","granola","lobsters","basil","sweet-peppers","ancho-chile-peppers","cucumbers","pickles","radishes","powdered-sugar","green-beans","bourbon","habanero-chilies","cilantro","avocados","margarine","pineapples","cheddar-cheese","marmalade","cookies","peanuts","Irish-cream-liqueur","chili-powder","rabbits","Worcestershire-sauce","almond-paste","rice-paper","artichokes","rhubarb","Kahlua","haddock","clams","prawns","sardines","turtle","flour","pine-nuts","peanut-butter","cremini-mushrooms","chicken","orange-peels","sesame-seeds","chutney","condensed-milk","shrimp","honeydew-melons","corn-syrup","pomegranates","gorgonzola","red-cabbage","red-chile-powder","truffles","sour-cream","cream-of-tartar","coffee","duck","mackerel","potato-chips","dumpling","rice-wine","alfredo-sauce","caviar","won-ton-skins","black-olives","barley","raisins","beans","tomato-sauce","liver","red-pepper-flakes","turnips","dried-leeks","chile-peppers","couscous","peas","poultry-seasoning","rice-vinegar","heavy-cream","huckleberries","venison","ice-cream","potatoes","chili-sauce","butter","plantains","lemon-juice","cranberries","grouper","garlic","celery-seeds","cream-cheese","broccoli-raab","guavas","Mandarin-oranges","milk","shallots","bok-choy","pinto-beans","pesto","moo-shu-wrappers","cooking-wine","canola-oil","water","apple-pie-spice","cabbage","custard","panko-bread-crumbs","halibut","carrots","cod","mussels","grapes","wasabi","sugar","beer","pecans","eggs","baguette","Parmesan-cheese","beets","poppy-seeds","lemon-grass","succotash","onion-powder","cauliflower","navy-beans","five-spice-powder","pasta","crabs","passion-fruit","pears","romaine-lettuce","pea-beans","oatmeal","pico-de-gallo","fennel","buckwheat","chicory","artificial-sweetener","flax-seed","mustard-seeds","cinnamon","molasses","turkeys","sage","vinegar","vanilla-bean","hazelnuts","chickpeas","feta-cheese","dates","pheasants","broccoli","parsley","coriander","apple-butter","date-sugar","cantaloupes","prosciutto","unsweetened-chocolate","balsamic-vinegar","brown-rice","barbecue-sauce","garlic-powder","red-beans","salt","Cappuccino-Latte","pepper","arugula","trout","chipotle-peppers","cactus","anchovy-paste","provolone","tortillas","almond-butter","hash-browns","asparagus","brunoise","quail","soybeans","beef","jack-cheese","maraschino-cherries","wild-rice","corn","thyme","parsnips","limes","scallops","curry-leaves","zinfandel-wine","soymilk","English-muffins","lemons","spaghetti-squash","cherries","applesauce","colby-cheese"]
liquidList = ["water","milk","blood","urine","gasoline","wine","honey","coffee","juice","kool-aid","monster","redbull","coke","pepsi","mountain-dew","diet-coke","diet-pepsi","7-up","rootbeer","smoothie","fanta",""]
funnyNoiseList = ["achoo","ahem","bang","bash","bam","bark","bawl","beep","belch","blab","blare","blurt","boing","boink","bonk","bong","boo","boo-hoo","boom","bow-wow","brring","bubble","bump","burp","buzz","cackle","chatter","cheep","chirp","chomp","choo-choo","chortle","clang","clash","clank","clap","clack","clatter","click","clink","clip","clop","cluck","clunk","cough","crackle","crash","creak","croak","crunch","cuckoo","ding","drip","fizz","flick","flop","flutter","giggle","glug","glup","groan","growl","grunt","guffaw","gurgle","hack","haha","hack","hiccup","hiss","hohoho","honk","hoot","howl","huh","hum","jangle","jingle","ker-ching","kerplunk","knock","meow","moan","moo","mumble","munch","murmur","mutter","neigh","oink","ouch","ooze","phew","ping","plink","plop","pluck","plunk","poof","pong","pop","pow","purr","quack","rattle","ribbit","ring","rip","roar","rumble","rush","rustle","screech","shuffle","shush","sizzle","slap","slash","slish","slither","slosh","slurp","smack","snap","snarl","sniff","snip","snore","snort","spit","splash","splat","splatter","splish","splosh","squawk","squeak","squelch","squish","sway","swish","swoosh","thud","thump","thwack","tic-toc","tinkle","trickle","twang","tweet","vroom","whack","whallop","wham","whimper","whip","whirr","whish","whisper","whizz","whoop","whoosh","woof","yelp","yikes","zap","zing","zip","zoom"]
verbINGList = ["running","punching","flying","drinking","riding","breaking","kicking","blowing","fighting","racing","skipping","growing","swimming","sinking","eating","coding","reading","whistling","watching","hitting","hiking","skiing"]
pastTenseList = ["blew","drank","dug","fell","grew","rode","rose","sat","threw","won","ran","sang","sank","swam","woke","wrote","punched","ate"]
pluralAnimalList = ["leopards","panthers","wolves","tigers","jaguars","dogs","pandas","cheetahs","otters","pumas","lions","seals"]

#-----------------------------------------Functions----------------------------------------------------#
def topic1():
    print("Fill in the blanks below with whatever words you like.")
    time.sleep(1)
    print("If at any time you can't think of a word, just input the letter R and the program will generate a random word for you.")
    time.sleep(1)
    print(" ")
    print("The theme is: Amusement Parks")
    time.sleep(1)
    adjective1 = input("Adjective #1: ")
    adjectiveList.append(adjective1)
    if adjective1 == "R" or adjective1 == "r":
        adjective1 = random.choice(adjectiveList)
    time.sleep(.5)
    adjective2 = input("Adjective #2: ")
    adjectiveList.append(adjective2)
    if adjective2 == "R" or adjective2 == "r":
        adjective2 = random.choice(adjectiveList)
    time.sleep(.5)
    adjective3 = input("Adjective #3: ")
    adjectiveList.append(adjective3)
    if adjective3 == "R" or adjective3 == "r":
        adjective3 = random.choice(adjectiveList)
    time.sleep(.5)
    animal1 = input("Animal: ")
    animalList.append(animal1)
    if animal1 == "R" or animal1 == "r":
        animal1 = random.choice(animalList)
    time.sleep(.5)
    clothing = input("Article of clothing: ")
    clothingList.append(clothing)
    if clothing == "R" or clothing == "r":
        clothing = random.choice(clothingList)
    time.sleep(.5)
    noun1 = input("Noun #1: ")
    nounList.append(noun1)
    if noun1 == "R" or noun1 == "r":
        noun1 = random.choice(nounList)
    time.sleep(.5)
    noun2 = input("Noun #2: ")
    nounList.append(noun2)
    if noun2 == "R" or noun2 == "r":
        noun2 = random.choice(nounList)
    time.sleep(.5)
    noun3 = input("Noun #3: ")
    nounList.append(noun3)
    if noun3 == "R" or noun3 == "r":
        noun3 = random.choice(nounList)
    time.sleep(.5)
    noun4 = input("Noun #4: ")
    nounList.append(noun4)
    if noun4 == "R" or noun4 == "r":
        noun4 = random.choice(nounList)
    time.sleep(.5)
    bodyPart = input("Body Part: ")
    bodyPartList.append(bodyPart)
    if bodyPart == "R" or bodyPart == "r":
        bodyPart = random.choice(bodyPartList)
    time.sleep(.5)
    pluralNoun1 = input("Plural Noun #1: ")
    pluralNounList.append(pluralNoun1)
    if pluralNoun1 == "R" or pluralNoun1 == "r":
        pluralNoun1 = random.choice(pluralNounList)
    time.sleep(.5)
    pluralNoun2 = input("Plural Noun #2: ")
    pluralNounList.append(pluralNoun2)
    if pluralNoun2 == "R" or pluralNoun2 == "r":
        pluralNoun2 = random.choice(pluralNounList)
    time.sleep(.5)
    pluralNoun3 = input("Plural Noun #3: ")
    pluralNounList.append(pluralNoun3)
    if pluralNoun3 == "R" or pluralNoun3 == "r":
        pluralNoun3 = random.choice(pluralNounList)
    time.sleep(.5)
    foodType = input("Type of food: ")
    foodList.append(foodType)
    if foodType == "R" or foodType == "r":
        foodType = random.choice(foodList)
    time.sleep(.5)
    liquidType = input("Type of Liquid: ")
    liquidList.append(liquidType)
    if liquidType == "R" or liquidType == "r":
        liquidType = random.choice(liquidList)
    time.sleep(.5)
    print("Thank you for all you inputs, your mad lib is being compiled...")
    time.sleep(3)
    print(" ")
    print("An amusement park is always fun to visit on a hot summer " + colored(noun1, "cyan"))
    print("When you get there, you can wear your " + colored(clothing,"cyan") + " and go")
    print("for a swim. And their are lots of " + colored(adjective1,"cyan") + " things to eat. You can")
    print("start off with a " + colored(adjective2,"cyan") + "-dog on a " + colored(noun2,"cyan") + " with")
    print("mustard, relish, and " + colored(pluralNoun1,"cyan") + " on it. Then you can have a")
    print("buttered ear of " + colored(noun3,"cyan") + " with a nice " + colored(adjective3,"cyan") + " slice of")
    print(colored(foodType,"cyan") + " and a big bottle of cold " + colored(liquidType,"cyan") + ". When you")
    print("are full, it's time to go on the roller coaster, which should settle your")
    print(colored(bodyPart,"cyan") + ". Other amusement park rides are the bumper cars,")
    print("which have little " + colored(pluralNoun2,"cyan") + " that you drive and run into other")
    print(colored(pluralNoun3,"cyan") + ", and the merry-go-round, where you can sit on a big")
    print(colored(animal1,"cyan") + " and try to grab the gold " + colored(noun4,"cyan") +" as you ride past it.")
    print(" ")
    tryAgain = input("Would you like to try again? (Y/N): ")
    if tryAgain == "Y" or tryAgain == "y":
        time.sleep(1)
        print(" ")
        topicScreen()
    elif tryAgain == "N" or tryAgain == "n":
        time.sleep(1)
        print(" ")
        print("Thanks for playing!")

def topic2():
    print("Fill in the blanks below with whatever words you like.")
    time.sleep(1)
    print("If at any time you can't think of a word, just input the letter R and the program will generate a random word for you.")
    time.sleep(1)
    print(" ")
    print("The theme is: Zoo Visit")
    time.sleep(1)
    adjective1 = input("Adjective #1: ")
    adjectiveList.append(adjective1)
    if adjective1 == "R" or adjective1 == "r":
        adjective1 = random.choice(adjectiveList)
    time.sleep(.5)
    adjective2 = input("Adjective #2: ")
    adjectiveList.append(adjective2)
    if adjective2 == "R" or adjective2 == "r":
        adjective2 = random.choice(adjectiveList)
    time.sleep(.5)
    adjective3 = input("Adjective #3: ")
    adjectiveList.append(adjective3)
    if adjective3 == "R" or adjective3 == "r":
        adjective3 = random.choice(adjectiveList)
    time.sleep(.5)
    adjective4 = input("Adjective #4: ")
    adjectiveList.append(adjective4)
    if adjective4 == "R" or adjective4 == "r":
        adjective4 = random.choice(adjectiveList)
    time.sleep(.5)
    animal1 = input("Animal #1: ")
    animalList.append(animal1)
    if animal1 == "R" or animal1 == "r":
        animal1 = random.choice(animalList)
    time.sleep(.5)
    animal2 = input("Animal #2: ")
    animalList.append(animal2)
    if animal2 == "R" or animal2 == "r":
        animal2 = random.choice(animalList)
    time.sleep(.5)
    funnyNoise1 = input("Funny Noise #1: ")
    funnyNoiseList.append(funnyNoiseList)
    if funnyNoise1 == "R" or funnyNoise1 == "r":
        funnyNoise1 = random.choice(funnyNoiseList)
    time.sleep(.5)
    funnyNoise2 = input("Funny Noise #2: ")
    funnyNoiseList.append(funnyNoise2)
    if funnyNoise2 == "R" or funnyNoise2 == "r":
        funnyNoise2 = random.choice(funnyNoiseList)
    time.sleep(.5)
    bodyPart = input("Body Part: ")
    bodyPartList.append(bodyPart)
    if bodyPart == "R" or bodyPart == "r":
        bodyPart = random.choice(bodyPartList)
    time.sleep(.5)
    pluralAnimal = input("Plural Animal: ")
    pluralAnimalList.append(pluralAnimal)
    if pluralAnimal == "R" or pluralAnimal == "r":
        pluralAnimal = random.choice(pluralAnimalList)
    time.sleep(.5)
    pluralNoun1 = input("Plural Noun #1: ")
    pluralNounList.append(pluralNoun1)
    if pluralNoun1 == "R" or pluralNoun1 == "r":
        pluralNoun1 = random.choice(pluralNounList)
    time.sleep(.5)
    pluralNoun2 = input("Plural Noun #2: ")
    pluralNounList.append(pluralNoun2)
    if pluralNoun2 == "R" or pluralNoun2 == "r":
        pluralNoun2 = random.choice(pluralNounList)
    time.sleep(.5)
    pluralNoun3 = input("Plural Noun #3: ")
    pluralNounList.append(pluralNoun3)
    if pluralNoun3 == "R" or pluralNoun3 == "r":
        pluralNoun3 = random.choice(pluralNounList)
    time.sleep(.5)
    liquidType = input("Liquid Type: ")
    liquidList.append(liquidType)
    if liquidType == "R" or liquidType == "r":
        liquidType = random.choice(liquidList)
    print("Thank you for all you inputs, your mad lib is being compiled...")
    time.sleep(3)
    print(" ")
    print("Zoos are places where wild " + colored(pluralNoun1,"cyan") + " are kept in pens or cages")
    print("so that " + colored(pluralNoun2,"cyan") + " can come and look at them. There are two")
    print("zoos in New York, one in the Bronx and one in " + colored(adjective1,"cyan") + " Park.")
    print("The Park zoo is built around a large pond filled with clear sparkling")
    print(colored(liquidType,"cyan") + ". You will see several " + colored(pluralAnimal,"cyan") + " swimming in the")
    print("pond and eating fish. When it is feeding time, all of the animals make")
    print(colored(adjective2,"cyan") + " noises. The elephant goes " + colored(funnyNoise1,"cyan") + "and the")
    print("turtledoves go " + colored(funnyNoise2,"cyan") + ". In one part of the zoo, there")
    print("are " + colored(adjective3,"cyan") + " gorillas who love to eat " + colored(pluralNoun2,"cyan") + ". In another")
    print("building, there is a spotted African " + colored(animal1,"cyan") + " that is so fast it")
    print("can outrun a " + colored(animal2,"cyan") + ". But my favorite animal is the")
    print("hippopotamus. It has a huge " + colored(bodyPart,"cyan") + " and eats 50 pounds")
    print("of " + colored(pluralNoun3,"cyan") + " a day. You would never know that, technically, it's")
    print("nothing but an oversized " + colored(adjective4,"cyan") + " pig.")
    print(" ")
    tryAgain = input("Would you like to try again? (Y/N): ")
    if tryAgain == "Y" or "y":
        time.sleep(1)
        print(" ")
        topicScreen()
    elif tryAgain == "N" or "n":
        time.sleep(1)
        print(" ")
        print("Thanks for playing!")


def topicScreen():
    print("What topic would you like?")
    time.sleep(1)
    print("1.Amusement Park")
    print("2.Zoo")

    time.sleep(.5)
    topicChosen = input("1/2: ")
    time.sleep(1)
    if topicChosen == "1":
        topic1()
    elif topicChosen == "2":
        topic2()

#------------------------------------------Execution-----------------------------------------------------#

print("Welcome to Python Mad Libs!")
time.sleep(1)
topicScreen()
