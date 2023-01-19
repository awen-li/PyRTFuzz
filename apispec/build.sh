
BASE_DIR=`pwd`

# 1. PyGen
cd PyGen && ./build.sh && cd -


# 2. PySpec
cd PySpec/StcSpec && ./build.sh && cd -
cd PySpec/DynSpec && ./build.sh && cd -
