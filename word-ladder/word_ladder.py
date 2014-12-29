class SlowSolution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        alphabet = set(''.join(dict) + start + end)

        def gen_trans(word):
            trans = set()
            for i, c in enumerate(word):
                new_word = list(word)
                for new_c in alphabet - {c}:
                    new_word[i] = new_c
                    trans.add(''.join(new_word))
            return trans

        transformations = {}
        for word in dict:
            for trans in gen_trans(word):
                if trans not in transformations:
                    transformations[trans] = []
                transformations[trans].append(word)

        end_trans = {t: end
                     for t in gen_trans(end)}

        def follow(word, length=1, seen=None, shortest=float('Inf')):
            if word in end_trans:
                return length + 1

            # Don't continue if we already have a shorter path
            if length >= shortest:
                #XXX######################################################################################
                #XXX######################################################################################
                print 'TOO LONG, QUITTING', word
                #XXX######################################################################################
                return None

            if word in transformations:
                if seen is None:
                    seen = {}
                seen = {word}.union(seen)

                for trans in transformations[word]:
                    if trans in seen:
                        continue

                    #XXX######################################################################################
                    #XXX######################################################################################
                    print word, '->', trans, '=', length, '::', shortest
                    print seen
                    print
                    #XXX######################################################################################
                    #XXX######################################################################################

                    follow_length = follow(trans, length + 1, seen, shortest)
                    if not follow_length:
                        continue
                    elif follow_length < shortest:
                        shortest = follow_length

                return shortest if shortest != float('Inf') else 0

            return 0

        return follow(start)


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        alphabet = set(''.join(dict) + start + end)
        dict = set(dict)
        dict.add(start)

        #XXX######################################################################################
        #XXX######################################################################################
        total_valid_paths = [0]
        #XXX######################################################################################
        #XXX######################################################################################

        shortest = [float('Inf')]
        def follow(word, seen, length=1):
            #XXX######################################################################################
            #XXX######################################################################################
            print length
            print
            #XXX######################################################################################
            #XXX######################################################################################

            if word == start:
                #XXX######################################################################################
                total_valid_paths[0] += 1
                #XXX######################################################################################
                return length

            if length > shortest[0]:
                return 0

            for i, c in enumerate(word):
                new_word = list(word)
                for new_c in alphabet - {c}:
                    new_word[i] = new_c
                    trans = ''.join(new_word)
                    if trans in seen:
                        continue
                    if trans in dict:
                        l = follow(trans, seen.union({trans}), length + 1)

                        #XXX######################################################################################
                        #XXX######################################################################################
                        print 'Total valid:', total_valid_paths[0], '... Shortest:', shortest[0]
                        print word, '->', trans, '=', length, '::', shortest[0]
                        print seen
                        print
                        #XXX######################################################################################
                        #XXX######################################################################################

                        if 0 < l < shortest[0]:
                            shortest[0] = l
            return 0 if shortest[0] == float('Inf') else shortest[0]

        #XXX######################################################################################
        #XXX######################################################################################
        print 'following!'
        #XXX######################################################################################
        #XXX######################################################################################
        return follow(end, {end})

    tests = [
        ('hit', 'cog', ["hot","dot","dog","lot","log"],
            5),
        ("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"],
            5),
        ("cet", "ism", ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"],
            10)  #xxx?????
    ]
