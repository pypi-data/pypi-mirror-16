"""
The dataset module has functions for loading a variety of datasets that
are properly formated for use with CobwebTrees and their derivatives.
"""

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division
from os.path import dirname
from os.path import join
import json

def _load_json(filename):
    """
    Loads a json file and returns a python object generated from parsing the
    json.
    """
    module_path = dirname(__file__)
    with open(join(module_path, 'data_files', filename)) as dat:
        output = json.load(dat)
    return output

def _load_file(filename):
    """
    Reads the rows of a file and returns them as an array.
    """
    module_path = dirname(__file__)
    with open(join(module_path, 'data_files', filename)) as dat:
        output = [row[:-1] for row in dat]
    return output

def load_forest_fires():
    """
    Load the forest fires dataset.

    This is an example of instances with :ref:`Nominal<val-nom>` and
    :ref:`Numeric<val-num>` values and :ref:`Constant<attr-const>` attributes.

    This dataset was downloaded from the `UCI machine learning repository
    <http://archive.ics.uci.edu/ml/datasets/Forest+Fires>`__.
    We processed the data to be in dictionary format with human readable
    labels. 

    >>> import pprint
    >>> data = load_forest_fires()
    >>> print(len(data))
    517
    >>> pprint.pprint(data[0])
    {'DC': 94.3,
     'DMC': 26.2,
     'FFMC': 86.2,
     'ISI': 5.1,
     'RH': 51.0,
     'area': 0.0,
     'day': 'fri',
     'month': 'mar',
     'rain': 0.0,
     'temp': 8.2,
     'wind': 6.7,
     'x-axis': 7.0,
     'y-axis': 5.0}

    """
    return _load_json('forest_fires.json')

def load_congressional_voting():
    """
    Load the voting dataset.

    This is an example of instances with only :ref:`Nominal<val-nom>` values
    and :ref:`Constant<attr-const>` attributes but some attributes are
    occasionally missing.

    This dataset was downloaded from the `UCI machine learning repository
    <http://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records>`__.
    We processed the data to be in dictionary format with human readable
    labels. 

    >>> import pprint
    >>> data = load_congressional_voting()
    >>> print(len(data))
    435
    >>> pprint.pprint(data[0])
    {'Class Name': 'republican',
     'adoption-of-the-budget-resolution': 'n',
     'aid-to-nicaraguan-contras': 'n',
     'anti-satellite-test-ban': 'n',
     'crime': 'y',
     'duty-free-exports': 'n',
     'education-spending': 'y',
     'el-salvador-aid': 'y',
     'export-administration-act-south-africa': 'y',
     'handicapped-infants': 'n',
     'immigration': 'y',
     'mx-missile': 'n',
     'physician-fee-freeze': 'y',
     'religious-groups-in-schools': 'y',
     'superfund-right-to-sue': 'y',
     'water-project-cost-sharing': 'y'}

    """
    return _load_json('congressional_voting.json')

def load_iris():
    """
    Load the iris dataset.

    This is an example of instances with :ref:`Nominal<val-nom>` and
    :ref:`Numeric<val-num>` values and :ref:`Constant<attr-const>` attributes.

    This dataset was downloaded from the `UCI machine learning repository
    <https://archive.ics.uci.edu/ml/datasets/Iris>`__. We processed the data
    to be in dictionary format with human readable labels. 

    >>> import pprint
    >>> data = load_iris()
    >>> print(len(data))
    150
    >>> pprint.pprint(data[0])
    {'class': 'Iris-setosa',
     'petal length': 1.4,
     'petal width': 0.2,
     'sepal length': 5.1,
     'sepal width': 3.5}

    """
    return _load_json('iris.json')

def load_mushroom():
    """Load the mushroom dataset.

    This is an example of instances with only :ref:`Nominal<val-nom>` values
    and :ref:`Constant<attr-const>` attributes.

    This dataset was downloaded from the `UCI machine learning repository
    <https://archive.ics.uci.edu/ml/datasets/Mushroom>`__. We processed the data
    to be in dictionary format with human readable labels. 

    >>> import pprint
    >>> data = load_mushroom()
    >>> print(len(data))
    8124
    >>> pprint.pprint(data[0])
    {'bruises?': 'yes',
     'cap-color': 'brown',
     'cap-shape': 'convex',
     'cap-surface': 'smooth',
     'classification': 'poisonous',
     'gill-attachment': 'free',
     'gill-color': 'black',
     'gill-size': 'narrow',
     'gill-spacing': 'closed',
     'habitat': 'urban',
     'odor': 'pungent',
     'population': 'scattered',
     'ring-number': 'one',
     'ring-type': 'pendant',
     'spore-print-color': 'black',
     'stalk-color-above-ring': 'white',
     'stalk-color-below-ring': 'white',
     'stalk-root': 'equal',
     'stalk-shape': 'enlarging',
     'stalk-surface-above-ring': 'smooth',
     'stalk-surface-below-ring': 'smooth',
     'veil-color': 'white',
     'veil-type': 'partial'}
    """
    return _load_json('mushrooms.json')

def load_rb_com_11():
    """Load the RumbleBlocks, Center of Mass Level 11, dataset.

    This is an example of instances with all the attribute and value types
    described in the :ref:`instance-rep`.

    >>> import pprint
    >>> data = load_rb_com_11()
    >>> print(len(data))
    251
    >>> pprint.pprint(data[0])
    {'_guid': 'ea022d3d-5c9e-46d7-be23-8ea718fe7816',
     '_human_cluster_label': '0',
     'component0': {'b': 1.0, 'l': 0.0, 'r': 1.0, 't': 2.0, 'type': 'cube0'},
     'component1': {'b': 3.0, 'l': 2.0, 'r': 3.0, 't': 4.0, 'type': 'cube0'},
     'component14': {'b': 4.0, 'l': 1.0, 'r': 4.0, 't': 5.0, 'type': 'ufoo0'},
     'component2': {'b': 1.0, 'l': 1.0, 'r': 4.0, 't': 2.0, 'type': 'plat0'},
     'component3': {'b': 2.0, 'l': 1.0, 'r': 4.0, 't': 3.0, 'type': 'plat0'},
     'component4': {'b': 0.0, 'l': 0.0, 'r': 5.0, 't': 1.0, 'type': 'rect0'}}
    """
    return _load_json('rb_com_11_continuous.json')

def load_rb_s_07():
    """Load the RumbleBlocks, Symmetry Level 7, dataset.

    This is an example of instances with all the attribute and value types
    described in the :ref:`instance-rep`.

    >>> import pprint
    >>> data = load_rb_s_07()
    >>> print(len(data))
    141
    >>> pprint.pprint(data[0])
    {'_guid': '660ac76d-93b3-4ce7-8a15-a3213e9103f5',
     'component0': {'b': 0.0, 'l': 0.0, 'r': 3.0, 't': 1.0, 'type': 'plat0'},
     'component1': {'b': 1.0, 'l': 1.0, 'r': 2.0, 't': 4.0, 'type': 'plat90'},
     'component8': {'b': 4.0, 'l': 0.0, 'r': 3.0, 't': 5.0, 'type': 'ufoo0'},
     'success': '0'}
    """
    return _load_json('rb_s_07_continuous.json')

def load_rb_s_13():
    """Load the RumbleBlocks, Symmetry Level 13, dataset.

    This is an example of instances with all the attribute and value types
    described in the :ref:`instance-rep`.

    >>> import pprint
    >>> data = load_rb_s_13()
    >>> print(len(data))
    249
    >>> pprint.pprint(data[0])
    {'_guid': '684b4ce5-0f55-481c-ae9a-1474de8418ea',
     '_human_cluster_label': '0',
     'component0': {'b': 3.0, 'l': 2.0, 'r': 3.0, 't': 4.0, 'type': 'cube0'},
     'component1': {'b': 4.0, 'l': 2.0, 'r': 3.0, 't': 5.0, 'type': 'cube0'},
     'component14': {'b': 0.0, 'l': 0.0, 'r': 4.0, 't': 1.0, 'type': 'trap0'},
     'component15': {'b': 5.0, 'l': 1.0, 'r': 3.0, 't': 6.0, 'type': 'ufoo0'},
     'component2': {'b': 1.0, 'l': 0.0, 'r': 3.0, 't': 2.0, 'type': 'plat0'},
     'component3': {'b': 2.0, 'l': 0.0, 'r': 3.0, 't': 3.0, 'type': 'plat0'}}
    """
    return _load_json('rb_s_13_continuous.json')

def load_rb_wb_03():
    """Load the RumbleBlocks, Wide Base Level 03, dataset.

    This is an example of instances with all the attribute and value types
    described in the :ref:`instance-rep`.

    >>> import pprint
    >>> data = load_rb_wb_03()
    >>> print(len(data))
    254
    >>> pprint.pprint(data[0])
    {'_guid': 'aa5eff72-0572-4eff-a007-3def9a82ba5b',
     '_human_cluster_label': '0',
     'component0': {'b': 2.0, 'l': 2.0, 'r': 3.0, 't': 3.0, 'type': 'cube0'},
     'component1': {'b': 2.0, 'l': 3.0, 'r': 4.0, 't': 3.0, 'type': 'cube0'},
     'component11': {'b': 3.0, 'l': 1.0, 'r': 4.0, 't': 4.0, 'type': 'ufoo0'},
     'component2': {'b': 1.0, 'l': 2.0, 'r': 5.0, 't': 2.0, 'type': 'plat0'},
     'component3': {'b': 0.0, 'l': 0.0, 'r': 5.0, 't': 1.0, 'type': 'rect0'}}
    """
    return _load_json('rb_wb_03_continuous.json')

def load_rb_s_07_human_predictions():
    """Load the Human Predictions Data for the RumbleBlocks, Symmetry Level 7,
    dataset.

    This is data collected from mechanical turk, where workers were tasked with
    predicting a concept label (success) given a picture of the tower. The
    element contains labels for the data and subsequent rows contain the actual
    data.

    >>> import pprint
    >>> data = load_rb_s_07_human_predictions()
    >>> print(len(data))
    601
    >>> pprint.pprint(data[0:2])
    ['user_id,instance_guid,time,order,prediction,correctness',
     '1,2fda0bde-95a7-4bda-9851-785275c3f56d,2015-02-15 '
     '19:21:14.327344+00:00,1,0,1']
    """
    return _load_file('human_s_07_success_predictions.csv')
