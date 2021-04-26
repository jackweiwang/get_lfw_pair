/home/ww/docs/cmake编译opencv参数

cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.4.0/modules \
-D OPENCV_ENABLE_NONFREE=ON \
-D WITH_OPENMP=ON \
-D WITH_TBB=ON \
-D OPENCV_EXTRA_EXE_LINKER_FLAGS=-latomic \
-D ENABLE_PRECOMPILED_HEADERS=OFF \
-D WITH_CUDA=ON \
-D ENABLE_FAST_MATH=1 \
-D CUDA_FAST_MATH=1 \
-D WITH_CUBLAS=1 \
-D BUILD_opencv_python2=no \
-D BUILD_opencv_python3=yes \
-D OPENCV_PYTHON3_VERSION=3.6 \
-D PYTHON3_DEFAULT_EXECUTABLE=/home/ubuntu/.conda/envs/economics/bin/python3.6m \
-D PYTHON3_EXECUTABLE=/home/ubuntu/.conda/envs/economics/bin/python3.6m \
-D PYTHON3_INCLUDE_PATH=/home/ubuntu/.conda/envs/economics/include/python3.6m \
-D PYTHON3_LIBRARY=/home/ubuntu/.conda/envs/economics/lib/libpython3.6m.so \
-D PYTHON3_PACKAGES_PATH=/home/ubuntu/.conda/envs/economics/lib/python3.6/site-packages \
