BEIJING TOMORROW
----------------

By Tavis Barr, tavisbarr@gmail.com, Copyright 2016
Licensed under the Gnu Public License V. 2.0
Contact me about other licensing arrangements


This program uses satellite data from the NASA MODIS program, and pollution
data from the US embassy in Beijing to develop a predictor of the next day's
change in pollution based on today's satellite images.

It is not designed as a first-rate forecaster -- it would need several 
improvements for that, including addition of weather data and probably better
training of the models, or for that matter, just including the current
pollution level as a feature -- but rather as a demonstration of how to use
CaffeOnSpark to perform a complete modelling exercise from download to
training to prediction.  The CaffeOnSpark package is not very well documented
as of the time of this writing, so the code serves to illustrate its usage.


SETUP
-----

This program is designed to be run on Spark.  I execute this through the
Eclipse IDE using PyDev, but it can also be done via the command line.  To get
PyDev working with CaffeOnSpark, the following changes need to be made to the
Python interpreter:

(a) The following need to be added to PYTHONPATH, with ${SPARK_HOME} and
${CAFFE_ON_SPARK} replaced with the actual absolute paths:

${SPARK_HOME}
${SPARK_HOME}/python
${SPARK_HOME}/python/lib/py4j-[your_version]-src.zip
${SPARK_HOME}/python/lib/pyspark.zip
${CAFFE_ON_SPARK}/caffe-grid/target/caffeonsparkpythonapi.zip

(b) The following environmental variables need to be added:

SPARK_HOME needs to be set to the root of your Spark installation
PYSPARK_SUBMIT_ARGS needs to be set to the following (YMMV):

--master local[*]       # OR URL if you are running on YARN 
--queue PyDevSpark1.6.1 # Can be called whatever  
--files ${CAFFE_ON_SPARK}/caffe-public/python/caffe/_caffe.so,
        ${CAFFE_ON_SPARK}/caffe-public/distribute/lib/libcaffe.so.1.0.0-rc3  
--jars "${CAFFE_ON_SPARK}/caffe-grid/target/caffe-grid-0.1-SNAPSHOT-jar-with-dependencies.jar,
		${CAFFE_ON_SPARK}/caffe-distri/target/caffe-distri-0.1-SNAPSHOT-jar-with-dependencies.jar" 
--driver-library-path "${CAFFE_ON_SPARK}/caffe-grid/target/caffe-grid-0.1-SNAPSHOT-jar-with-dependencies.jar" 
--driver-class-path "${CAFFE_ON_SPARK}/caffe-grid/target/caffe-grid-0.1-SNAPSHOT-jar-with-dependencies.jar" 
--conf 	spark.driver.extraLibraryPath="${LD_LIBRARY_PATH}:
		${CAFFE_ON_SPARK}/caffe-public/distribute/lib:
		${CAFFE_ON_SPARK}/caffe-distri/distribute/lib"  
--conf 	spark.executorEnv.LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:
		${CAFFE_ON_SPARK}/caffe-public/distribute/lib:
		${CAFFE_ON_SPARK}/caffe-distri/distribute/lib" 
pyspark-shell

These are roughly the same arguments that will need to be made when
invoking pyspark if this program is run from the command line.  Again, 
${CAFFE_ON_SPARK} should be replaced with its actual value.



Running the program takes place in four major steps, each of which uses its
own module.  These are: (1) Downloading the data, (2) Building the LMDB
database, (3) Training the module, and (4) Prediction on today's data.
Additionally, there is a module to train a standard (non-"deep") model
using the Random Forest library on Apache Spark for comparison.  Each of
these modules are described in order.

(1) Downloading the data

The module that is responsible for downloading the satellite data,
tilescraper, is available as a separate package, because it likely has uses
aside from training models etc.  The pollution data are much smaller, and
are pulled in real time using the beijingpollutioncompiler module.  The data
are pulled from the US Embassy web site in Beijing; the Chinese Ministry of
Environmental Protection also publishes data that are more accurate, but these
are more difficult to obtain and also do not go back quite as far.


(2) Building the database

CaffeOnSpark expects the data in one of a handful of datbase formats; I found
LMDB easiest to work with, so I transformed the data into this format to use
them.  Note that the images require to have the index order of the underlying
data changed from the standard image format for Caffe to use them.

Unfortunately, the Python module for Caffe also expects the outcome data to be
an integer; fixing this is a one-line change in the Caffe source code, but I 
did not want to use a non-standard version of Caffe, so I just multiplied the 
changes by 100.

When no satellite data is available, MODIS does not throw an exception but
merely returns a black image.  The pollution data may be blank for some days.
As the CaffeOnSpark trainer is expecting all observations to be valid, days
with such data are discarded at the time the database is built.

The outcome to be predicted is the logarithmic change between today's pollution
level and tomorrow's pollution level.

The features are expected to have a mean of zero, so the mean of each pixel is
subtratcted from every image of the training and test data before it is placed
in the database.

(3) Training the Model

The Python interface to CaffeOnSpark is somewhat limited as of this writing;
in particular, it is necessary to have the configuration of the solver and 
network specified in .prototxt files rather than configured as Python objects
in the code (the Caffe interfaces to define them in the code will work, but
they cannot easily be attached to the CaffeOnSpark configuration).

The steps to train the model are pretty much the same as in the demonstration
examples widely available online; in fact, very little deviation from these
steps is supported by the Python interface to CaffeOnSpark.  The key is that
we obtain our model configuration from a folder in the resource directory,
and also deliver the model there.  When it is finished training, the routine
reports an R-squared of the regression on the test sample.  In any event,
most of the work in this section involves tweaking the .prototxt files to 
improve the model.

(4) Prediction

Once the model is trained, it can be called from the regular Caffe
interface without requiring the overhead of Spark.  After checking that today's
image is not blank, we load it and transform it the same way as the training
images were transformed -- the axes are swapped and the mean is subtracted.
Finally, the test image is expected to be part of a batch, in this case a 
batch of one, so we add an extra dimension to the image array.  

Additionally, we need a slight alteration to the .prototxt file to predict
using this model.  First, the top layers (loss and accuracy) need to be taken
out of the model, otherwise they will be returned and not the prediction.
Finally, the batch size for the test model needs to be set to one.

With that in hand, we are ready to make a prediction.  Obviously, this model
is quite rudimentary.

(5) Comparison

It may be interesting to see how well we can do without using "deep" learning.
The pollutionrflearner downscales the image into a 4x4 grid, and then builds
a random forest over the grid.  The clear challenge in building any model
of this phenomenon is that we have far more features than observations, so we
need to intelligently simplify the features before attempting to train.  In
any event, the random forest model does slightly worse than the "deep" model,
but not substantially so.  Frankly, neither model is highly predictive.

