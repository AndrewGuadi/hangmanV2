from enum import Enum



class Letters(Enum):
    a = ('🄰', 'A')
    b = ('🄱', 'B')
    c = ('🄲', 'C')
    d = ('🄳', 'D')
    e = ('🄴', 'E')
    f = ('🄵', 'F')
    g = ('🄶', 'G')
    h = ('🄷', 'H')
    i = ('🄸', 'I')
    j = ('🄹', 'J')
    k = ('🄺', 'K')
    l = ('🄻', 'L')
    m = ('🄼', 'M')
    n = ('🄽', 'N')
    o = ('🄾', 'O')
    p = ('🄿', 'P')
    q = ('🅀', 'Q')
    r = ('🅁', 'R')
    s = ('🅂', 'S')
    t = ('🅃', 'T')
    u = ('🅄', 'U')
    v = ('🅅', 'V')
    w = ('🅆', 'W')
    x = ('🅇', 'X')
    y = ('🅈', 'Y')
    z = ('🅉', 'Z')


    @property
    def unused(self):
        return self.value[1]

    @property
    def dead(self):
        return self.value[0]