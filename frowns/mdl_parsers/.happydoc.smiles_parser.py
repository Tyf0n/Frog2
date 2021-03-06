(S'fa88e291bffe5dd7442840208568ad01'
p1
(ihappydoclib.parseinfo.moduleinfo
ModuleInfo
p2
(dp3
S'_namespaces'
p4
((dp5
S'ParseError'
p6
(ihappydoclib.parseinfo.classinfo
ClassInfo
p7
(dp8
g4
((dp9
(dp10
tp11
sS'_filename'
p12
S'../python/frowns/mdl_parsers/smiles_parser.py'
p13
sS'_docstring'
p14
S''
sS'_class_member_info'
p15
(lp16
sS'_name'
p17
g6
sS'_parent'
p18
g2
sS'_comment_info'
p19
(dp20
(S'molecule_generator'
tp21
S" quick scans for closure tokens\n it's easier for us to do the bond checks here\n than in the molecule generator.  Hopefully this\n will save us some time.\n"
p22
ssS'_base_class_info'
p23
(lp24
S'Exception'
p25
asS'_configuration_values'
p26
(dp27
sS'_class_info'
p28
g9
sS'_function_info'
p29
g10
sS'_comments'
p30
S''
sbs(dp31
S'molecule_generator'
p32
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p33
(dp34
g4
((dp35
(dp36
tp37
sS'_exception_info'
p38
(dp39
sS'_parameter_names'
p40
(S'tokens'
p41
S'generator'
p42
tp43
sS'_parameter_info'
p44
(dp45
g41
(NNNtp46
sg42
(I1
S'Generator.Generator'
Ntp47
ssg12
g13
sg14
S''
sg17
g32
sg18
g2
sg19
g20
sg26
(dp48
sg28
g35
sg29
g36
sg30
g22
sbsS'_make_element_symbols_pattern'
p49
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p50
(dp51
g4
((dp52
(dp53
tp54
sg38
(dp55
sg40
(tsg44
(dp56
sg12
g13
sg14
S''
sg17
g49
sg18
g2
sg19
g20
sg26
(dp57
sg28
g52
sg29
g53
sg30
S''
sbsS'tokenizer'
p58
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p59
(dp60
g4
((dp61
(dp62
tp63
sg38
(dp64
S'ParseError("Caught error starting at %s" %( repr( s ), ) )'
p65
NsS'ParseError("Could not parse starting with %s" %( repr( s ), ) )'
p66
Nssg40
(S's'
tp67
sg44
(dp68
S's'
(NNNtp69
ssg12
g13
sg14
S''
sg17
g58
sg18
g2
sg19
g20
sg26
(dp70
sg28
g61
sg29
g62
sg30
S''
sbsS'_special_order_cmp'
p71
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p72
(dp73
g4
((dp74
(dp75
tp76
sg38
(dp77
sg40
(S'a'
S'b'
tp78
sg44
(dp79
S'a'
(NNNtp80
sS'b'
(NNNtp81
ssg12
g13
sg14
S''
sg17
g71
sg18
g2
sg19
g20
sg26
(dp82
sg28
g74
sg29
g75
sg30
S''
sbstp83
sS'_import_info'
p84
(ihappydoclib.parseinfo.imports
ImportInfo
p85
(dp86
S'_named_imports'
p87
(dp88
sS'_straight_imports'
p89
(lp90
S're'
p91
aS'string'
p92
aS'Generator'
p93
asbsg12
g13
sg14
S'"""\natom := [cnosp]\natom := \'B\' | \'C\' | \'N\' | \'O\' | \'F\' | \'P\' | \'S\' | \'Cl\' |  \'Br\' |  \'I\'\natom := \'[\' mass? symbol chiral? hcount? charge? \']\'\n\nsymbol := a lot of names ...\n\nhcount := \'H\' \\d+\nmass := \\d+\n\nchiral := \'@\'  (chiral_repeat | chiral_count | chiral_name)\nchiral_repeat := \'@\'+\nchiral_count := \\d+\nchiral_name := TH[12] | AL[12] | SP[123] | TB(1[0-9]?|20?|[3-9]) |\n                OH(1[0-9]?|2[0-9]?|30?|[4-9])\n\ncharge := "+" ("+"+ | \\d+)?\ncharge := "-" ("-"+ | \\d+)?\n\nbond := [=#/\\\\:~-]\n\ndot := \\.\n\nclosure = \\d | \'%\'\\d\\d?\n\nstart -> atom\n#start -> dot     # not allowed by Daylight\n\natom -> atom     # CC\natom -> bond     # C=C\natom -> branch_out  # CCC(C)C   (the \'C(\')\natom -> branch_in   # CCC(C)C   (the \'C)\')\natom -> dot      # C.C\natom -> closure  # c1ccccc1\n\nbond -> atom     # C=C\nbond -> closure  # C1CCCCC-1\nbond -> branch_out   # CCC=(O)CC  # but no branch_in\n\nbranch_out -> atom   # CC(C)C\nbranch_in -> atom\nbranch_out -> bond   # CC(=O)C(C)=O\nbranch_in -> bond\nbranch_out -> dot    # C(.C).C\nbranch_in -> dot\nbranch_in -> branch_out  # CCC(C)(C)CC\nbranch_in -> branch_in   # CC(C(C))C\n\ndot -> atom      # C.C\n#dot -> dot       # not allowed by Daylight\n\nclosure -> atom   # c1ccccc1\nclosure -> bond   # C1.C1#C\nclosure -> closure # C12C3C4C1C5C4C3C25\nclosure -> branch # C1.C1(C)C\nclosure -> dot    # c1ccccc1.O\n\n"""'
p94
sg17
S'smiles_parser'
p95
sg18
Nsg19
g20
sg26
(dp96
S'include_comments'
p97
I1
sS'cacheFilePrefix'
p98
S'.happydoc.'
p99
sS'useCache'
p100
I1
sS'docStringFormat'
p101
S'StructuredText'
p102
ssg28
g5
sg29
g31
sg30
S''
sbt.