from collections import defaultdict


###animals from Hill et al. (2012)
african_animals = ['aardvark', 'antelope', 'buffalo', 'camel', 'chameleon', 'cheetah', 'chimpanzee', 'cobra', 'duiker', 'eland', 'elephant', 'gazelle', 'genet', 'giraffe', 'gnu', 'gorilla', 'hippopotamus', 'hyena', 'impala', 'jackal', 'kongoni', 'kudu', 'lemur', 'leopard', 'lion', 'lioness', 'manatee', 'meerkat', 'mongoose', 'monkey', 'okapi', 'oryx', 'ostrich', 'panther', 'rhino', 'rhinoceros', 'steenbok', 'tiger', 'warthog', 'wildebeest', 'zebra']

animals_used_for_fur = ['alpaca','beaver','chamois','chinchilla','ermine','fox','llama','mink','rabbit','sable','vicuna']

arctic_far_north_animals = ['arctic fox','auk','caribou','muskox','penguin','polar bear','reindeer','seal','walrus','woolly mammoth']

australian_animals = ['bandicoot','devil','dingo','duckbill','emu','kangaroo','kiwi','koala',
'possum','platypus','possum','sugar glider','tasmanian devil','wallaby','wallaroo','wombat']

beasts_of_burden = ['ass','burro','camel','colt','donkey','dromedary','horse','llama','mare',
'mule','mustang','ox','pony','trotter','yak']

birds = ['albatross', 'avian', 'bird', 'blackbird', 'bluebird', 'bluefooted booby', 'bluegill', 'bluejay', 'bobolink', 'booby', 'bullfinch', 'bunting', 'buzzard', 'canary', 'cardinal', 'chickadee', 'chicken', 'cock', 'cockatiel', 'cockatoo', 'crow', 'cuckoo', 'dodo', 'dove', 'drake', 'duck', 'duckling', 'eagle', 'eaglet', 'egret', 'emu', 'ewe', 'falcon', 'finch', 'flamingo', 'fowl', 'gander', 'goldfinch', 'goshawk', 'gosling', 'grebe', 'grouse', 'gull', 'harrier', 'hawk', 'heron', 'hummingbird', 'ibis', 'jackdaw', 'jay', 'kingfisher', 'kite', 'kiwi', 'lark', 'loon', 'macaw', 'mallard', 'merlin', 'mockingbird', 'mouse', 'myna', 'nightingale', 'oriole', 'osprey', 'ostrich', 'owl', 'parakeet', 'parrot', 'partridge', 'peacock', 'pelican', 'penguin', 'peregrine', 'pheasant', 'pigeon', 'quail', 'quetzal', 'raven', 'rhea', 'roadrunner', 'robin', 'seagull', 'shrike', 'songbird', 'sparrow', 'spoonbill', 'starling', 'stilt', 'stork', 'swallow', 'swallowtail', 'swan', 'swift', 'tanager', 'thrush', 'toucan', 'trumpeter', 'turkey', 'vulture', 'woodpecker', 'wren']

bovine = ['bison','buffalo','bullock','calf','cattle','cow','heifer','monitor','muskox','steer','water buffalo','yak']

canine = ['akita', 'black lab', 'blood hound', 'bulldog', 'canine', 'chihuahua', 'coyote', 'dachshund', 'dalmatian', 'dog', 'fox', 'golden retriever', 'great dane', 'greyhound', 'harrier', 'husky', 'hyena', 'jackal', 'labrador retriever', 'malamute', 'pembroke welsh corgi', 'poodle', 'pug', 'puggle', 'pup', 'shihtzu', 'siberian husky', 'terrier', 'timber wolf', 'wild dog', 'wolf'] ##removed duplicate wolf

deers = ['blacktailed deer','buck','caribou','deer','doe','eland','elk','fawn','gazelle','gnu','impala','moose','muledeer','reindeer','roe','stag','whitetailed deer','wildebeest']

farm_animals = ['ass','billygoat','bronco','bullock','calf','chick','chicken','cock','colt',
'cow','donkey','ferret','foal','goat','heifer','hen','hog','horse','kid','lamb','mare','miniature pony','billy_goat',
'mule','pig','piglet','pony','potbellied pig','ram','rooster','sheep','snake','sow','spider','stallion',
'turkey'] #added billy_goat

feline = ['bengal tiger','bobcat','bull','cat','cat','cheetah','cougar','crane','jaguar','leopard',
'liger','lion','lynx','mountainlion','ocelot','panther','puma','siamese cat','snow leopard','snow lion','tiger','tomcat','whitetiger','wildcat']

fish = ['angelfish','arrowhead shark','barracuda','bass','betta','blowfish','carp','catfish',
'clownfish','cuttlefish','fish','flounder','freshwater fish','goldfish','great white shark',
'grenadier','grouper','grunt','guppy','herring','jack','koi','lamprey','mackerel','mako shark',
'minnow','parrotfish','pike','pink salmon','piranha','rainbowfish','salmon','saltwater fish',
'seabass','shark','shrimp','smelt','stickleback','sturgeon','swordfish','tilapia','trout','tuna','whale shark']

insectivores = ['aardvark','anteater','armadillo','bat','echidna','hedgehog','mole','shrew']

insects = ['ant','antlion','aphid','bee','beetle','blackwidow','bug','butterfly','caterpillar',
'centipede','cicada','cockroach','cricket','daddy long legs','dolphin','dragonfly','earthworm',
'flea','fly','gnat','grasshopper','grub','honeybee','hornet','insect','June beetle','ladybug','larva',
'leafy','louse','maggot','mealworm','mite','monarch butterfly','mosquito','moth','pill bug',
'praying mantis','scorpion','stick insect','tarantula','termite','tick','wasp','worm','yellow jacket']

north_american_animals = ['badger','bear','beaver','bighorn','bison','blackbear','boar',
'bobcat','brown bear','caribou','chipmunk','cougar','cub','deer','elk','fox','grizzly bear','kodiak bear','moose','mountain goat','mountain lion','puma','rabbit','raccoon','skunk','squirrel','wolf']

pets = ['budgie','canary','cat','cockatiel','cockatoo','dog','gerbil','golden retriever',
'goldfish','guinea pig','guppy','hamster','kitten','labrador retriever','malamute','parakeet',
'parrot','poodle','puppy','rabbit']

primates = ['ape','baboon','bonobo','chimpanzee','gibbon','gorilla','howler monkey',
'human','lemur','loris','marmoset','monkey','orangutan','primates','saki monkey','shrew','snow monkey','spider monkey','titi']

rabbits = ['bunny','coney','hare','jackrabbit','rabbit']

reptiles_amphibians = ['adder','alligator','amphibian','anaconda','anole','asp','black mamba','boa constrictor','bullfrog','caiman','chameleon','cobra','crocodile','diamondback',
'dinosaur','dragon','frog','gardensnake','gecko','godzilla','iguana','komododragon','lizard',
'moccasin','newt','python','rattlesnake','reptile','salamander','serpent','snake','toad','tortoise',
'tree frog','turtle','velociraptor','viper','watersnake']

rodents = ['agouti','beaver','black squirrel','capybara','cavy','chinchilla','chipmunk',
'dormouse','flying squirrel','gerbil','golden marmot','gopher','groundhog','guinea pig',
'hamster','hedgehog','lemming','marmot','mole','mouse','muskrat','naked mole rat','porcupine',
'prairie dog','rat','rodent','shrew','squirrel','woodchuck']

water_animals = ['alga','alligator','anemone','axolotl','beaver','beluga','blue whale',
'boto','brine shrimp','clam','conch','coral','cowry','crab','crawfish','crayfish','dolphin','eel',
'elephant seal','fish','frog','goose','hammerhead shark','humpback whale','jellyfish','killer whale','leech','limpet','lobster','manatee','mantaray','monster','muskrat','mussel','narwhal',
'nautilus','newt','octopus','orca','otter','oyster','penguin','platypus','porpoise','ray','salamander',
'sand dollar','scallop','seahorse','seal','sea lion','sea monkey','shark','slug','snail','sponge',
'squid','starfish','stingray','tadpole','toad','turtle','urchin','whale']

weasels = ['badger','ferret','groundhog','marten','mink','mongoose','otter','polecat','sea otter','skunk','stoat','weasel','wolverine']

ALL_CATEG_NAMES = ['african_animals', 'animals_used_for_fur', 'arctic_far_north_animals', 'australian_animals', 'beasts_of_burden', 'birds', 'bovine', 'canine', 'deers', 'farm_animals', 'feline', 'fish', 'insectivores', 'insects', 'north_american_animals', 'pets', 'primates', 'rabbits', 'reptiles_amphibians', 'rodents', 'water_animals', 'weasels']

ALL_CATEG = [african_animals, animals_used_for_fur, arctic_far_north_animals, australian_animals, beasts_of_burden, birds, bovine, canine, deers, farm_animals, feline, fish, insectivores, insects, north_american_animals, pets, primates, rabbits, reptiles_amphibians, rodents, water_animals, weasels]

CATEG_DICT = {ALL_CATEG_NAMES[i]: ALL_CATEG[i] for i in range(0,len(ALL_CATEG_NAMES))}

ANIMAL_TO_CATEGORIES = defaultdict(list)
for category_name, animals in CATEG_DICT.items():
    for animal in animals:
        ANIMAL_TO_CATEGORIES[animal].append(category_name)