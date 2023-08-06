from cffi import FFI
from enum import Enum
from contextlib import contextmanager


ffi = FFI()
ffi.cdef("""
// Copied from https://github.com/yandex/tomita-parser/blob/master/src/bindings/c/mystem/iface.h
typedef void MystemAnalysesHandle;
typedef void MystemLemmaHandle;
typedef void MystemFormsHandle;
typedef void MystemFormHandle;
typedef unsigned short int TSymbol;

MystemAnalysesHandle* MystemAnalyze(TSymbol* word, int len);
void MystemDeleteAnalyses(MystemAnalysesHandle* analyses);
int MystemAnalysesCount(MystemAnalysesHandle* analyses);

MystemLemmaHandle* MystemLemma(MystemAnalysesHandle* analyses, int i);

TSymbol* MystemLemmaText(MystemLemmaHandle* lemma);
int     MystemLemmaTextLen(MystemLemmaHandle* lemma);
TSymbol* MystemLemmaForm(MystemLemmaHandle* lemma);
int     MystemLemmaFormLen(MystemLemmaHandle* lemma);
int     MystemLemmaQuality(MystemLemmaHandle* lemma);
char*   MystemLemmaStemGram(MystemLemmaHandle* lemma);
char**  MystemLemmaFlexGram(MystemLemmaHandle* lemma);
int     MystemLemmaFlexGramNum(MystemLemmaHandle* lemma);
int     MystemLemmaFlexLen(MystemLemmaHandle* lemma);
int     MystemLemmaRuleId(MystemLemmaHandle* lemma);

MystemFormsHandle* MystemGenerate(MystemLemmaHandle* lemma);
void MystemDeleteForms(MystemFormsHandle* forms);
int MystemFormsCount(MystemFormsHandle* forms);

MystemFormHandle* MystemForm(MystemFormsHandle* forms, int i);

TSymbol* MystemFormText(MystemFormHandle* form);
int     MystemFormTextLen(MystemFormHandle* form);
char*   MystemFormStemGram(MystemFormHandle* form);
char**  MystemFormFlexGram(MystemFormHandle* form);
int     MystemFormFlexGramNum(MystemFormHandle* form);
""")
mystem = ffi.dlopen("libmystem_c_binding.so")

class Quality(Enum):

    # Based on https://github.com/yandex/tomita-parser/blob/5a56099c7f56c23c32933d4bc3163920c7b7a6fb/src/FactExtract/Parser/lemmerlib/lemma.h#L110

    Dictionary  = 0 # слово из словаря
    Bastard     = 1 # не словарное
    Sob         = 2 # из "быстрого словаря"
    Prefixoid   = 4 # словарное + стандартный префикс (авто- мото- кино- фото-) всегда в компании с Bastard или Sob
    Foundling   = 8 # непонятный набор букв, но проходящий в алфавит
    BadRequest  = 16 # доп. флаг.: "плохая лемма" при наличии "хорошей" альтернативы ("махать" по форме "маша")
    FromEnglish = 65536 # переведено с английского
    ToEnglish   = 131072 # переведено на английский
    Untranslit  = 262144 # "переведено" с транслита
    Overrode    = 1048576 # текст леммы был перезаписан
    Fix         = 16777216 # слово из фикс-листа

LEMMA_QUALITY_LOOKUP_MAP = {
    name.value: name for _, name in Quality.__members__.items()
}

class Grammeme(Enum):

    # Based on https://github.com/yandex/tomita-parser/blob/5a56099c7f56c23c32933d4bc3163920c7b7a6fb/src/library/lemmer/dictlib/yx_gram_enum.h

    Invalid = 0
    Before = 126

    Postposition = 127 # POSTP
    First = Postposition # same as Postposition 
    Adjective = 128   # A      # Nomenus
    Adverb = 129      # ADV
    Composite = 130   # COM(P)
    Conjunction = 131 # CONJ
    Interjunction = 132 # INTJ
    Numeral = 133     # NUM
    Particle = 134    # PCL
    Preposition = 135 # PRE(P)
    Substantive = 136 # S
    Verb = 137        # V
    AdjNumeral = 138  # ANUM
    AdjPronoun = 139  # APRO
    AdvPronoun = 140  # ADVPRO
    SubstPronoun = 141 # SPRO
    Article = 142     # артикли
    PartOfIdiom = 143 # части идиом (прежде всего иностр. слов)
    LastPartOfSpeech = PartOfIdiom # same as PartOfIdiom
    Reserved = 144    # зарезервировано    # особые пометы
    Abbreviation = 145 # сокращения
    IrregularStem = 146 # чередование в корне (или супплетивизм)
    Informal = 147    # разговорная форма
    Distort = 148     # искаженная форма
    Contracted = 149  # стяжённая форма (фр. q' и т.п.)
    Obscene = 150     # обсц
    Rare = 151        # редк
    Awkward = 152     # затр
    Obsolete = 153    # устар
    SubstAdjective = 154 # адъект
    FirstName = 155   # имя
    Surname = 156     # фам
    Patr = 157        # отч
    Geo = 158         # гео
    Proper = 159      # собств
    Present = 160     # наст  # Tempus
    Notpast = 161     # непрош
    Past = 162        # прош
    Future = 163      # буд. время (фр., ит.)
    Past2 = 164       # фр. passe simple, ит. passato remoto
    Nominative = 165  # им    # Casus
    Genitive = 166    # род
    Dative = 167      # дат
    Accusative = 168  # вин
    Instrumental = 169 # твор
    Ablative = 170    # пр
    Partitive = 171   # парт(вин2)
    Locative = 172    # местн(пр2)
    Vocative = 173    # звательный
    Singular = 174    # ед    # Numerus
    Plural = 175      # мн
    Gerund = 176      # деепр # Modus
    Infinitive = 177  # инф
    Participle = 178  # прич
    Indicative = 179  # изъяв
    Imperative = 180  # пов
    Conditional = 181 # усл. наклонение (фр. =ит.)
    Subjunctive = 182 # сослаг. накл. (фр. =ит.)
    Short = 183       # кр    # Gradus
    Full = 184        # полн
    Superlative = 185 # прев
    Comparative = 186 # срав
    Possessive = 187  # притяж
    Person1 = 188     # 1-л   # Personae
    Person2 = 189     # 2-л
    Person3 = 190     # 3-л
    Feminine = 191    # жен   # Gender (genus)
    Masculine = 192   # муж
    Neuter = 193      # сред
    MasFem = 194      # мж
    Perfect = 195     # сов   # Perfectum-imperfectum (Accept)
    Imperfect = 196   # несов
    Passive = 197     # страд # Voice (Genus)
    Active = 198      # действ
    Reflexive = 199   # возвратные
    Impersonal = 200  # безличные
    Animated = 201    # од    # Animated
    Inanimated = 202  # неод
    Praedic = 203     # прдк
    Parenth = 204     # вводн
    Transitive = 205  # пе     #transitivity
    Intransitive = 206 # нп
    Definite = 207    # опред. члены   #definiteness
    Indefinite = 208  # неопред. члены

    SimConj = 209       # сочинит. (для союзов)
    SubConj = 210       # подчинит. (для союзов)
    PronounConj = 211   # местоимение-союз ("я знаю, _что_ вы сделали прошлым летом")
    CorrelateConj = 212 # вторая зависимая часть парных союзов - "если ... _то_ ... ", "как ... _так_ и ..."

    AuxVerb = 213       #вспомогательный глагол в аналитической форме ("_будем_ думать")

GRAMMEMES_LOOKUP_MAP = {
    tag.value: tag for _, tag in Grammeme.__members__.items()
}

def string_as_symbols(string):
    return list(map(ord, string))

def symbols_as_string(string, length):
    return "".join(list(map(chr, (string[i] for i in range(length)))))

def get_stem_grammemes(grammemes):
    return grammemes_as_ints(ffi.string(grammemes))

def get_flex_grammemes(grammemes, length):
    return list(map(grammemes_as_ints, (ffi.string(grammemes[i]) for i in range(length))))

def grammemes_as_ints(grammemes):
    return list(map(int, bytearray(grammemes)))

def pretty_grammemes(grammemes):
    for grammeme in grammemes:
        yield GRAMMEMES_LOOKUP_MAP[grammeme]

class Analyses(object):

    def __init__(self, word):
        self.symbols = ffi.new("unsigned short int[]", string_as_symbols(word))
        self.handle = mystem.MystemAnalyze(self.symbols, len(self.symbols))

    def __len__(self):
        return mystem.MystemAnalysesCount(self.handle)

    def __getitem__(self, i):
        return Lemma(self.handle, i)

    def __iter__(self):
        for i in range(len(self)):
            yield Lemma(self.handle, i)

    def __del__(self):
        mystem.MystemDeleteAnalyses(self.handle)

class Lemma(object):

    def __init__(self, analyses, i):
        self.handle = mystem.MystemLemma(analyses, i)
        self.forms = LemmaForms(self.handle)

    def __len__(self):
        return mystem.MystemLemmaTextLen(self.handle)

    def __str__(self):
        return symbols_as_string(
            mystem.MystemLemmaText(self.handle),
            mystem.MystemLemmaTextLen(self.handle)
        )

    @property
    def form(self):
        return symbols_as_string(
            mystem.MystemLemmaForm(self.handle),
            mystem.MystemLemmaFormLen(self.handle)
        )

    @property
    def quality(self):
        return LEMMA_QUALITY_LOOKUP_MAP[
            mystem.MystemLemmaQuality(self.handle)
        ]
    

    @property
    def stem_grammemes(self):
        return list(
            pretty_grammemes(
                get_stem_grammemes(
                    mystem.MystemLemmaStemGram(self.handle)
                )
            )
        )

    @property
    def flex_grammemes(self):
        return list(
            map(list,
                map(pretty_grammemes,
                    get_flex_grammemes(
                        mystem.MystemLemmaFlexGram(self.handle),
                        mystem.MystemLemmaFlexGramNum(self.handle)
                    )
                )
            )
        )

    @property
    def flex_length(self):
        return mystem.MystemLemmaFlexLen(self.handle)
    
    @property
    def rule_id(self):
        return mystem.MystemLemmaRuleId(self.handle)

class LemmaForms(object):

    def __init__(self, lemma):
        self.handle = mystem.MystemGenerate(lemma)

    def __getitem__(self, i):
        return LemmaForm(self.handle, i)

    def __iter__(self):
        for i in range(len(self)):
            yield LemmaForm(self.handle, i)

    def __len__(self):
        return mystem.MystemFormsCount(self.handle)

    def __del__(self):
        mystem.MystemDeleteForms(self.handle)

class LemmaForm(object):

    def __init__(self, forms, i):
        self.handle = mystem.MystemForm(forms, i)

    def __len__(self):
        return mystem.MystemFormTextLen(self.handle)

    def __str__(self):
        text = mystem.MystemFormText(self.handle)
        return symbols_as_string(text, len(self))

    @property
    def stem_grammemes(self):
        return list(
            pretty_grammemes(
                get_stem_grammemes(
                    mystem.MystemFormStemGram(self.handle)
                )
            )
        )

    @property
    def flex_grammemes(self):
        return list(
            map(list,
                map(pretty_grammemes,
                    get_flex_grammemes(
                        mystem.MystemFormFlexGram(self.handle),
                        mystem.MystemFormFlexGramNum(self.handle)
                    )
                )
            )
        )

@contextmanager
def analyze(word):
    analyses = Analyses(word)
    yield analyses
    del analyses
