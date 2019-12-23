class buildConfig(object):
    def __init__(self,isDebug:bool):
        self.incDirs=["/DataDisk/cpp_libs/boost_1_72_0","/DataDisk/cpp_libs/eigen-git-mirror"]
        self.linkDir=["/DataDisk/cpp_libs/boost_1_72_0/stage/lib"]
        self.linkOpt=["pthread" ,"m","dl"]
        self.CC="gcc-9.2"
        self.CXX="g++-9.2"
        self.CCFLAGS=['-std=c++17', '-Wall',"-fpermissive"]
        self.mklroot="/home/robin/intel/mkl"
        if(isDebug):
            self.preDifines=['-DDEBUG']
            self.CCFLAGS.append(['-g'])
        else:
            self.preDifines=['-DNDEBUG']
            self.CCFLAGS.append('-O3')
        self.incDirs.append(self.mklroot+"/include")
        self.linkDir.append(self.mklroot+"/lib/intel64")
        self.linkOpt.append(["mkl_intel_lp64","mkl_sequential" ,"mkl_core"])
        self.preDifines.append("EIGEN_USE_MKL_ALL")