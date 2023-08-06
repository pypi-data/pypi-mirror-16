import os
from syn.base import Attr
from mock import MagicMock
from nose.tools import assert_raises
from depman import dependency as depd
from syn.base_utils import assert_equivalent, assign
from depman import Dependency, Dependencies, Apt, Pip
from depman import apt as aptd
from depman import pip as pipd

#-------------------------------------------------------------------------------

DIR = os.path.dirname(os.path.abspath(__file__))
DEPS1 = os.path.join(DIR, '../deps1.yml')
DEPS2 = os.path.join(DIR, '../deps2.yml')
DEPS3 = os.path.join(DIR, '../deps3.yml')
DEPS4 = os.path.join(DIR, '../deps4.yml')
DEPS5 = os.path.join(DIR, '../deps5.yml')

#-------------------------------------------------------------------------------
# Utilities

def test_command():
    assert depd.command('pwd').strip() == os.path.abspath(os.getcwd())

def test_status():
    assert depd.status('true') == 0
    assert depd.status('false') == 1

#-------------------------------------------------------------------------------
# Dependency

def test_dependency():
    assert depd.DEPENDENCY_KEYS == dict(apt = Apt,
                                        pip = Pip)
    assert depd.DEPENDENCY_ORDERS == dict(apt = Apt.order,
                                          pip = Pip.order)
    

    dep = Dependency('foo')
    assert dep.name == 'foo'
    assert_raises(NotImplementedError, dep.check)
    assert_raises(NotImplementedError, dep.satisfy)

    assert_equivalent(Dependency.from_conf('foo'), dep)
    assert_raises(TypeError, Dependency.from_conf, [])
    assert_raises(TypeError, Dependency.from_conf, dict(a = 1, b = 2))

    class Foo(Dependency):
        _attrs = dict(a = Attr(int),
                      b = Attr(int))

    assert_equivalent(Foo.from_conf(dict(foo = dict(a = 1, b = 2))),
                      Foo('foo', a = 1, b = 2))

#-------------------------------------------------------------------------------
# Dependencies

def test_dependencies():
    def assert_listeq(A, B):
        for a in A:
            assert a in B
        for b in B:
            assert b in A

    with open(DEPS1, 'rt') as f:
        deps = Dependencies.from_yaml(f)
        
    contexts = dict(dev = [Apt('libxml2-dev'),
                           Apt('libxslt1-dev'),
                           Pip('lxml')],
                    prod = [Pip('PyYAML')])
    assert_equivalent(deps, Dependencies(contexts=contexts))

    assert_listeq(deps.deps_from_context('all'),
                  deps.contexts.dev + deps.contexts.prod)

    assert deps.deps_from_context('dev') == deps.contexts.dev
    assert deps.deps_from_context('prod') == deps.contexts.prod
    assert_raises(ValueError, deps.deps_from_context, 'foo')

    with open(DEPS2, 'rt') as f:
        deps2 = Dependencies.from_yaml(f)

    contexts = dict(dev = [Apt('gcc', order=0),
                           Apt('make')])

    assert_equivalent(deps2, Dependencies(contexts = contexts))
    assert deps2.deps_from_context('all') == deps2.contexts.dev
    assert deps2.deps_from_context('dev') == deps2.contexts.dev
    assert_raises(ValueError, deps2.deps_from_context, 'prod')

    with open(DEPS3, 'rt') as f:
        deps3 = Dependencies.from_yaml(f)

    contexts = dict(prod = [Pip('six'),
                            Pip('syn', version='0.0.7',
                                always_upgrade=True)])

    assert_equivalent(deps3, Dependencies(contexts=contexts))
    assert deps3.deps_from_context('all') == deps3.contexts.prod
    assert_raises(ValueError, deps3.deps_from_context, 'dev')
    assert deps3.deps_from_context('prod') == deps3.contexts.prod

    with open(DEPS4, 'rt') as f:
        deps4 = Dependencies.from_yaml(f)

    assert 'includes' not in deps4.contexts

    assert_listeq(deps4.deps_from_context('c1'),
                  deps4.contexts.c1 + deps4.contexts.c2 +
                  deps4.contexts.c3 + deps4.contexts.c4)

    assert_listeq(deps4.deps_from_context('c2'),
                  deps4.contexts.c2 + deps4.contexts.c3)

    assert_listeq(deps4.deps_from_context('c3'), deps4.contexts.c3)
    assert_listeq(deps4.deps_from_context('c4'), deps4.contexts.c4)
    assert_listeq(deps4.deps_from_context('c5'), deps4.contexts.c5)

    assert_raises(AssertionError, Dependencies,
                  contexts = dict(c1 = [Apt('make')],
                                  c2 = [Pip('six')]),
                  includes = dict(c1 = ['c2', 'c3']))
    
    assert_raises(AssertionError, Dependencies,
                  contexts = dict(c1 = [Apt('make')],
                                  c2 = [Pip('six')]),
                  includes = dict(c3 = ['c2', 'c2']))

    with open(DEPS5, 'rt') as f:
        deps5 = Dependencies.from_yaml(f)
   
    with assign(aptd, 'status', MagicMock(return_value=1)):
        with assign(Pip, 'freeze', dict()):
            from depman.apt import Install, Update
            from depman.pip import Install as PipInstall

            ops = deps5.satisfy('prod', execute=False)
            assert ops == [Update(order=Apt.order),
                           Install('a', 'b', 'c', 'd', order=Apt.order),
                           PipInstall('a', 'b', 'c', order=Pip.order)]
            
            with assign(aptd, 'command', MagicMock()):
                with assign(pipd, 'command', MagicMock()):
                    deps5.satisfy('prod')

                    assert aptd.command.call_count == 2
                    aptd.command.assert_any_call('apt-get update')
                    aptd.command.assert_any_call('apt-get install -y a b c d')

                    assert pipd.command.call_count == 1
                    pipd.command.assert_any_call('pip install --upgrade a b c')

#-------------------------------------------------------------------------------
