import unittest

from minq import *


class LSCanary(object):
    """
    Use this as a dummy stream initializer to make sure streams aren't
    issuing queries when they shouldn't
    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __iter__(self):
        raise RuntimeError('this should not be called unless stream is queried')


class TestStreamBasics(unittest.TestCase):
    def test_stream_iterable(self):
        test = Stream('hello world'.split())
        assert any([i for i in test])

    def test_stream_execute(self):
        test = Stream('hello world'.split())
        assert test.execute() == ['hello', 'world']

    def test_stream_chain(self):
        test1 = Stream("hello world".split())
        test2 = Stream(test1)
        assert test2.execute() == ['hello', 'world']

    # the following tests use LSCanary
    # to prove that the queries aren't called at
    # definition time

    def test_stream_only(self):
        source = Stream(LSCanary(type='dagNode'))
        filtered = source.only('camera')
        assert isinstance(filtered, OfType)

    def test_stream_where_arbitrary(self):
        source = Stream(LSCanary(type='dagNode'))
        filtered = source.where(lambda p: True)
        assert isinstance(filtered, Where)

    def test_stream_whereMany(self):
        source = Stream(LSCanary(type='dagNode'))
        filtered = source.where(native.tx < 1)
        assert isinstance(filtered, WhereMany)

    def test_stream_itemWhere(self):
        source = Stream(LSCanary(type='dagNode'))
        filtered = source.where(item.tx < 1)
        assert isinstance(filtered, Where)

    def test_stream_customWhere(self):
        source = Stream(LSCanary(type='dagNode'))
        filtered = source.where(custom.tx < 1)
        assert isinstance(filtered, Where)

    def test_stream_get(self):
        source = Stream(LSCanary(type='dagNode'))
        parents = source.get(Parents)
        assert isinstance(parents, Parents)

    # testing NodeType derived classes
    def test_long_names(self):
        for klass in (Transforms, Meshes, Cameras, Lights):
            for node in klass():
                assert "|" in node

    def test_long_name_filters(self):
        example = Stream(['persp', 'top']).only(Transforms)
        for name in example:
            assert "|" in name

    def test_nonexistents_disappear(self):
        example = Stream(['top', 'i_dont_exist']).only(Transforms)
        assert example.execute() == ['|top']

    def test_bad_names_except(self):
        # currently we don't stop maya's default behavior,
        # which is to except on bad names in an LS call.
        # if that changes, change the test accordingly
        example = Stream(['top', '!?@#%!``']).only(Transforms)
        self.assertRaises(RuntimeError, example.execute)

    def test_objects_only_filter(self):
        example = Stream(['top.orthographic', 'fred.doesntexist']).only(Objects)
        assert example.execute() == ['|top|topShape']

    def test_get_parents(self):
        example = Stream(['topShape']).get(Parents)
        assert example.execute() == ['|top']

    def test_get_children(self):
        example = Stream(['|top']).get(Children)
        assert example.execute() == ['|top|topShape']

    def test_get_history(self):
        try:
            test_object, test_shape = cmds.polyCube()
            history = Stream([test_object]).get(Children).get(History)
            assert test_shape in history.execute()

        finally:
            cmds.delete(test_object, test_shape)

    def test_get_future(self):
        try:
            test_object, test_shape = cmds.polyCube()
            history = Stream([test_shape]).long().get(Future)
            child = Stream([test_object]).get(Children)
            assert len(history.execute()) > 1
            assert len((child & history).execute()) == 1

        finally:
            cmds.delete(test_object, test_shape)

    def test_item(self):
        example = item.tx > 1
        assert example.comp == 1
        assert example.operator == operator.gt
        assert example.attribute == 'tx'
        assert example.strict == False
        assert example.query_type == Where

    def test_custom_query(self):
        example = custom.user_defined == 0
        assert example.query_type == Where

    def test_native_query(self):
        example = native.user_defined == 0
        assert example.query_type == WhereMany

    def test_strict_eval(self):
        try:
            test_object, test_shape = cmds.polyCube()
            cmds.addAttr(test_object, ln='test_attr')
            pretest = custom.test_attr == 0
            assert pretest.eval(test_object)
            prestest_2 = custom.dont_exist == 0
            assert not prestest_2.eval(test_object)
            strict_test = custom.dont_exist == 0
            strict_test.strict = True
            self.assertRaises(Exception, strict_test, test_object)


        finally:
            cmds.delete(test_object, test_shape)

    def test_item_eval(self):
        example = item.orthographic == True
        assert example.eval('side')
        # this will fail if for some reason the side camera is not set to orthographic

    def test_item_has(self):
        try:
            cmds.file(new=True, f=True)
            cmds.createNode('transform')
            cmds.polyCube()
            result = list(Transforms().where(item.has(Children)))
            assert len(result) == 5
        finally:
            cmds.file(new=True, f=True)

    def test_item_has_mot(self):
        try:
            cmds.file(new=True, f=True)
            cmds.polyCube()
            result = list(Shapes().where_not(item.has(Parents)))
            assert len(result) == 0
        finally:
            cmds.file(new=True, f=True)

    def test_item_has_attr(self):
        try:
            cmds.file(new=True, f=True)
            cmds.polyCube()
            result = list(Shapes().where(item.has_attr("orthographic")))
            assert len(result) == 4
        finally:
            cmds.file(new=True, f=True)

    def test_get_attributes(self):
        cameras = Cameras().get(Attribute, 'orthographic').execute()
        for cam in ("|top", "|side", "|persp", "|front"):
            assert cam + cam + "Shape.orthographic" in cameras

    def test_get_values(self):
        orthos = Cameras().get(Attribute, 'orthographic').get(Values).execute()
        cams = Cameras().execute()
        for c, o in zip(cams, orthos):
            assert cmds.getAttr(c + ".orthographic") == o

    def test_join(self):
        cams = Cameras().cache()
        cam_orthos = cams.get(Attribute, 'focalLength')

    def test_only_namespaces(self):
        try:
            cmds.file(new=True, force=True)
            p1 = cmds.polyCube()
            ns = cmds.namespace(add="test")
            cmds.namespace(set="test")
            p2 = cmds.polyCube()
            assert len(Meshes().execute()) == 2
            assert len(Meshes().only(namespace="test").execute()) == 1

        finally:
            cmds.file(new=True, force=True)

    def test_only_nested_namespaces(self):
        try:
            cmds.file(new=True, force=True)
            p1 = cmds.polyCube()
            ns = cmds.namespace(add="test1")
            cmds.namespace(set="test1")
            p2 = cmds.polyCube()
            ns2 = cmds.namespace(add="test2")
            cmds.namespace(set="test2")
            p3 = cmds.polyCube()

            assert len(Meshes().only(namespace=":").execute()) == 1  # root
            assert len(Meshes().only(namespace=":test1").execute()) == 2  # test and test2
            assert len(Meshes().only(namespace=":test1:test2").execute()) == 1  # test2 only
            assert len(Meshes().only(namespace="test2").execute()) == 1  # test 2 only
            assert len(Meshes().only(namespace=":test2").execute()) == 0  # fails, test2 is not root
            assert len(Meshes().only(namespace=".").execute()) == 2  # all namespaces
            assert len(Meshes().only(namespace="").execute()) == 3  # namespaces or not

        finally:
            cmds.file(new=True, force=True)

    def test_having(self):
        try:
            cmds.file(new=True, f=True)
            cmds.polyCube(name='no_attrib')
            cmds.polyCube(name='has_attrib')
            cmds.addAttr(ln='custom_attrib')
            with_attrib = Transforms().having('custom_attrib')
            assert '|has_attrib' in with_attrib
            assert '|no_attrib' not in with_attrib

        finally:
            cmds.file(new=True, force=True)


def run_test():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStreamBasics)
    unittest.TextTestRunner(verbosity=2).run(suite)


run_test()
