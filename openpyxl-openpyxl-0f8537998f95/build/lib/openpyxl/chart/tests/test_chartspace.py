from __future__ import absolute_import
# Copyright (c) 2010-2017 openpyxl

import pytest

from openpyxl.xml.functions import fromstring, tostring
from openpyxl.tests.helper import compare_xml

@pytest.fixture
def ChartContainer():
    from ..chartspace import ChartContainer
    return ChartContainer


class TestChartContainer:

    def test_ctor(self, ChartContainer):
        container = ChartContainer()
        xml = tostring(container.to_tree())
        expected = """
        <chart>
          <plotArea></plotArea>
          <dispBlanksAs val="gap"></dispBlanksAs>
        </chart>
        """
        diff = compare_xml(xml, expected)
        assert diff is None, diff


    def test_from_xml(self, ChartContainer):
        src = """
        <chart>
          <plotArea></plotArea>
          <dispBlanksAs val="gap"></dispBlanksAs>
        </chart>
        """
        node = fromstring(src)
        container = ChartContainer.from_tree(node)
        assert container == ChartContainer()


@pytest.fixture
def PlotArea():
    from ..chartspace import PlotArea
    return PlotArea


class TestPlotArea:

    def test_ctor(self, PlotArea):
        chartspace = PlotArea()
        xml = tostring(chartspace.to_tree())
        expected = """
        <plotArea />
        """
        diff = compare_xml(xml, expected)
        assert diff is None, diff


    def test_from_xml(self, PlotArea):
        src = """
        <plotArea />
        """
        node = fromstring(src)
        chartspace = PlotArea.from_tree(node)
        assert chartspace == PlotArea()


@pytest.fixture
def DataTable():
    from ..chartspace import DataTable
    return DataTable


class TestDataTable:

    def test_ctor(self, DataTable):
        table = DataTable()
        xml = tostring(table.to_tree())
        expected = """
        <dTable />
        """
        diff = compare_xml(xml, expected)
        assert diff is None, diff


    def test_from_xml(self, DataTable):
        src = """
        <dTable />
        """
        node = fromstring(src)
        table = DataTable.from_tree(node)
        assert table == DataTable()


@pytest.fixture
def Surface():
    from .._3d import Surface
    return Surface


class TestSurface:

    def test_ctor(self, Surface):
        surface = Surface()
        xml = tostring(surface.to_tree())
        expected = """
        <surface />
        """
        diff = compare_xml(xml, expected)
        assert diff is None, diff


    def test_from_xml(self, Surface):
        src = """
        <surface />
        """
        node = fromstring(src)
        surface = Surface.from_tree(node)
        assert surface == Surface()


@pytest.fixture
def View3D():
    from .._3d import View3D
    return View3D


class TestView3D:

    def test_ctor(self, View3D):
        view = View3D()
        xml = tostring(view.to_tree())
        expected = """
        <view3D>
          <rotX val="15"></rotX>
          <rotY val="20"></rotY>
          <rAngAx val="1"></rAngAx>
        </view3D>
        """
        diff = compare_xml(xml, expected)
        assert diff is None, diff


    def test_from_xml(self, View3D):
        src = """
        <view3D>
          <rotX val="15"/>
          <rotY val="20"/>
          <rAngAx val="0"/>
          <perspective val="30"/>
        </view3D>
        """
        node = fromstring(src)
        view = View3D.from_tree(node)
        assert view == View3D(rotX=15, rotY=20, rAngAx=False, perspective=30)


@pytest.fixture
def PivotFormat():
    from ..chartspace import PivotFormat
    return PivotFormat


class TestPivotFormat:

    def test_ctor(self, PivotFormat):
        fmt = PivotFormat()
        xml = tostring(fmt.to_tree())
        expected = """
        <pivotFmt>
           <idx val="0" />
        </pivotFmt>
        """
        diff = compare_xml(xml, expected)
        assert diff is None, diff


    def test_from_xml(self, PivotFormat):
        src = """
        <pivotFmt>
           <idx val="0" />
        </pivotFmt>
        """
        node = fromstring(src)
        fmt = PivotFormat.from_tree(node)
        assert fmt == PivotFormat()


@pytest.fixture
def PivotFormatList():
    from ..chartspace import PivotFormatList
    return PivotFormatList


class TestPivotFormatList:

    def test_ctor(self, PivotFormatList):
        fmt = PivotFormatList()
        xml = tostring(fmt.to_tree())
        expected = """
        <pivotFmts />
        """
        diff = compare_xml(xml, expected)
        assert diff is None, diff


    def test_from_xml(self, PivotFormatList):
        src = """
        <pivotFmts />
        """
        node = fromstring(src)
        fmt = PivotFormatList.from_tree(node)
        assert fmt == PivotFormatList()


@pytest.fixture
def Protection():
    from ..chartspace import Protection
    return Protection


class TestProtection:

    def test_ctor(self, Protection):
        prot = Protection()
        xml = tostring(prot.to_tree())
        expected = """
        <protection />
        """
        diff = compare_xml(xml, expected)
        assert diff is None, diff


    def test_from_xml(self, Protection):
        src = """
        <protection>
          <chartObject val="1" />
        </protection>
        """
        node = fromstring(src)
        prot = Protection.from_tree(node)
        assert prot == Protection(chartObject=True)


@pytest.fixture
def PivotSource():
    from ..chartspace import PivotSource
    return PivotSource


class TestPivotSource:

    def test_ctor(self, PivotSource):
        src = PivotSource(name="pivot source", fmtId=1)
        xml = tostring(src.to_tree())
        expected = """
        <pivotSource>
          <name>pivot source</name>
          <fmtId>1</fmtId>
        </pivotSource>
        """
        diff = compare_xml(xml, expected)
        assert diff is None, diff


    def test_from_xml(self, PivotSource):
        src = """
        <pivotSource>
          <name>pivot source</name>
          <fmtId>1</fmtId>
        </pivotSource>
        """
        node = fromstring(src)
        src = PivotSource.from_tree(node)
        assert src == PivotSource(name="pivot source", fmtId=1)


@pytest.fixture
def ExternalData():
    from ..chartspace import ExternalData
    return ExternalData


class TestExternalData:

    def test_ctor(self, ExternalData):
        data = ExternalData(id='rId1')
        xml = tostring(data.to_tree())
        expected = """
        <externalData id="rId1"/>
        """
        diff = compare_xml(xml, expected)
        assert diff is None, diff


    def test_from_xml(self, ExternalData):
        src = """
        <externalData id="rId1"/>
        """
        node = fromstring(src)
        data = ExternalData.from_tree(node)
        assert data == ExternalData(id="rId1")
