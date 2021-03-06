# -*- coding: utf-8 -*-
from multiprocessing import Pool


class Pessoa(object):

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


def imprime_bonitinho(pessoa):
    print "- A pessoa se chama {0} e tem {1} anos".format(pessoa.nome, pessoa.idade)


def me_da_a_idade(pessoa):
    return pessoa.idade


if __name__ == '__main__':
    pool = Pool(5)

    andre = Pessoa("andre", 32)
    fonseca = Pessoa("fonseca", 32)
    daniel = Pessoa("daniel", 16)
    martha = Pessoa("andre", 33)
    alfredo = Pessoa("alfredo", 52)
    sandra = Pessoa("sandra", 50)

    pessoas = [andre, fonseca, daniel, martha, alfredo, sandra]

    idades = pool.map(me_da_a_idade, pessoas)

    print "A maior idade é {0}".format(max(idades))
    print "A menor idade é {0}".format(min(idades))
    print "A soma das idades é {0}".format(sum(idades))
    map(imprime_bonitinho, pessoas)
