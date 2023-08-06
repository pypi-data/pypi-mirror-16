========
Plumbium
========
---------------------
Goes around pipelines
---------------------

Plumbium is a Python package for wrapping scripts so that their inputs and
outputs are preserved in a consistent way.

Example
-------

.. code:: python

    from plumbium import call, record, pipeline
    from plumbium.artefacts import TextFile


    @record()
    def pipeline_stage_1(f):
        call(['/bin/cat', f.filename])


    @record()
    def pipeline_stage_2(f):
        call(['/bin/cat', f.filename])


    def my_pipeline(file1, file2):
        pipeline_stage_1(file1)
        pipeline_stage_2(file2)


    def example_pipeline():
        pipeline.run(
            'example',
            my_pipeline,
            '/my/data/directory',
            TextFile('month00/data.txt'), TextFile('month12/data.txt')
        )


    if __name__ == '__main__':
        example_pipeline()


Installation
------------

::
    
    git clone https://github.com/jstutters/plumbium.git
    cd plumbium
    pip install .

Contribute
----------

- Issue Tracker: `github.com/jstutters/plumbium/issues <http://github.com/jstutters/plumbium/issues>`_
- Source Code: `github.com/jstutters/plumbium <http://github.com/jstutters/plumbium>`_

Support
-------

If you are having problems, please let me know by submitting an issue in the tracker.
