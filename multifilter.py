def mfit(posled, mf):
    for i in posled:
        pos = sum([(1 if f(i) else 0) for f in mf.fun])
        if mf.jud(pos, len(mf.fun) - pos):
            yield i


class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return neg == 0
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterb = iterable
        self.fun = [f for f in funcs]
        self.jud = judge
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return mfit(self.iterb, self)