export PATH=E:/FPGA/vivado/Vivado/2018.3/msys64/usr/bin;E:/FPGA/vivado/Vivado/2018.3/msys64/mingw64/bin;E:/FPGA/vivado/Vivado/2018.3/bin;E:/FPGA/vivado/Vivado/2018.3/win64/bin;E:/FPGA/vivado/Vivado/2018.3/win64/tools/bin;E:/FPGA/vivado/Vivado/2018.3/bin;E:/FPGA/vivado/Vivado/2018.3/lib/win64.o;E:/FPGA/vivado/Vivado/2018.3/tps/win64/jre9.0.4/bin/server;E:/FPGA/vivado/Vivado/2018.3/tps/win64/jre9.0.4/bin;E:/FPGA/vivado/SDK/2018.3/bin;E:/FPGA/vivado/Vivado/2018.3/ids_lite/ISE/bin/nt64;E:/FPGA/vivado/Vivado/2018.3/ids_lite/ISE/lib/nt64;E:\FPGA\vivado\Vivado\2018.3\bin\..\msys64\mingw64\bin;E:\FPGA\vivado\Vivado\2018.3\bin\..\msys64\usr\bin;E:/FPGA/vivado/Vivado/2018.3/msys64/usr/bin;E:/FPGA/vivado/Vivado/2018.3/msys64/mingw64/bin;E:/FPGA/vivado/Vivado/2018.3/win64/bin;E:/FPGA/vivado/Vivado/2018.3/win64/tools/bin;C:\Program Files\Common Files\Oracle\Java\javapath;D:\vmware16\bin\;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;D:\Git\cmd;D:\googledownload\ctags-2022-07-18_p5.9.20220717.0-4-gac824e6-x64;C:\Program Files\dotnet\;D:\anaconda;D:\anaconda\Scripts;D:\fpga_softkits\putty\;D:\mingw\bin;D:\Tools\iverilog\bin;E:\modelsim\win64\LICENSE.TXT;C:\Users\liuzhouquan\AppData\Local\Programs\Python\Python310\Scripts\;C:\Users\liuzhouquan\AppData\Local\Programs\Python\Python310\;C:\Users\liuzhouquan\AppData\Local\Microsoft\WindowsApps;D:\vscode\Microsoft VS Code\bin;D:\Tools\iverilog\gtkwave\bin;;D:\pycharm\PyCharm 2021.3.1\bin;E:\modelsim\win64;D:\idea\IntelliJ IDEA 2022.3.1\bin;E:/FPGA/vivado/Vivado/2018.3\tps\mingw\6.2.0\win64.o\nt\bin;E:/FPGA/vivado/Vivado/2018.3\tps\mingw\6.2.0\win64.o\nt\libexec\gcc\x86_64-w64-mingw32\6.2.0;E:/FPGA/vivado/Vivado/2018.3/win64/tools/fpo_v7_0;E:/FPGA/vivado/Vivado/2018.3/win64/tools/fft_v9_1;E:/FPGA/vivado/Vivado/2018.3/win64/tools/opencv;E:/FPGA/vivado/Vivado/2018.3/win64/tools/fir_v7_0;E:/FPGA/vivado/Vivado/2018.3/win64/tools/dds_v6_0;E:/FPGA/vivado/Vivado/2018.3/win64/lib/csim;E:/FPGA/vivado/Vivado/2018.3/win64/tools/fpo_v7_0;E:/FPGA/vivado/Vivado/2018.3/win64/tools/fft_v9_1;E:/FPGA/vivado/Vivado/2018.3/win64/tools/opencv;E:/FPGA/vivado/Vivado/2018.3/win64/tools/fir_v7_0;E:/FPGA/vivado/Vivado/2018.3/win64/tools/dds_v6_0;E:/FPGA/vivado/Vivado/2018.3/win64/lib/csim
export LD_LIBRARY_PATH=E:/FPGA/vivado/Vivado/2018.3/win64/tools/gdb_v7_2;E:/FPGA/vivado/Vivado/2018.3/win64/tools/graphviz/lib;E:/FPGA/vivado/Vivado/2018.3/win64/bin;E:/FPGA/vivado/Vivado/2018.3/win64/tools/gdb_v7_2;E:/FPGA/vivado/Vivado/2018.3/win64/tools/graphviz/lib;E:/FPGA/vivado/Vivado/2018.3/win64/bin;E:/FPGA/vivado/Vivado/2018.3/win64/tools/fpo_v7_0;E:/FPGA/vivado/Vivado/2018.3/win64/tools/fft_v9_1;E:/FPGA/vivado/Vivado/2018.3/win64/tools/opencv;E:/FPGA/vivado/Vivado/2018.3/win64/tools/fir_v7_0;E:/FPGA/vivado/Vivado/2018.3/win64/tools/dds_v6_0;E:/FPGA/vivado/Vivado/2018.3/win64/lib/csim;E:/FPGA/vivado/Vivado/2018.3/win64/tools/fpo_v7_0;E:/FPGA/vivado/Vivado/2018.3/win64/tools/fft_v9_1;E:/FPGA/vivado/Vivado/2018.3/win64/tools/opencv;E:/FPGA/vivado/Vivado/2018.3/win64/tools/fir_v7_0;E:/FPGA/vivado/Vivado/2018.3/win64/tools/dds_v6_0;E:/FPGA/vivado/Vivado/2018.3/win64/lib/csim
export HDI_APPROOT=E:/FPGA/vivado/Vivado/2018.3
export XILINX_OPENCL_CLANG=E:/FPGA/vivado/Vivado/2018.3/win64/tools/clang
export RDI_PLATFORM=win64
bugpoint -mlimit=32000  --load libhls_support.so  --load libhls_bugpoint.so  -hls -strip  -function-uniquify -auto-function-inline -globaldce  -ptrArgReplace -mem2reg -instcombine -dce  -reset-lda  -loop-simplify -indvars -licm -loop-dep  -loop-bound -licm -loop-simplify -flattenloopnest  -array-flatten -gvn -instcombine -dce  -array-map -dce -func-legal  -gvn -adce -instcombine -cfgopt -simplifycfg -loop-simplify   -array-burst -promote-global-argument -dce  -axi4-lower -array-seg-normalize  -basicaa -aggrmodref-aa -globalsmodref-aa -aggr-aa -gvn -gvn  -basicaa -aggrmodref-aa -globalsmodref-aa -aggr-aa -dse -adse -adce -licm  -inst-simplify -dce  -globaldce -instcombine -array-stream -eliminate-keepreads -instcombine  -dce   -deadargelim -doublePtrSimplify  -doublePtrElim -dce -doublePtrSimplify -promote-dbg-pointer  -dce -scalarrepl -mem2reg -disaggr -norm-name -mem2reg  -instcombine  -dse -adse -adce -ptrLegalization -dce -auto-rom-infer -array-flatten -dce -instcombine -check-doubleptr  -loop-rot -constprop -cfgopt -simplifycfg -loop-simplify -indvars -pointer-simplify -dce -loop-bound  -loop-simplify -loop-preproc  -constprop -global-constprop -gvn -mem2reg -instcombine -dce  -loop-bound  -loop-merge -dce  -bitwidthmin  -deadargelim -dce  -canonicalize-dataflow -dce  -scalar-propagation -deadargelim -globaldce -mem2reg  -read-loop-dep  -interface-preproc -directive-preproc -interface-gen  -bram-byte-enable  -deadargelim -inst-simplify -dce  -gvn -mem2reg -instcombine -dce -adse  -loop-bound  -instcombine -cfgopt -simplifycfg -loop-simplify  -clean-region -io-protocol  -find-region -mem2reg  -bitop-raise  -inst-simplify -inst-rectify -instcombine -adce -deadargelim  -loop-simplify -phi-opt -bitop-raise  -cfgopt -simplifycfg -strip-dead-prototypes  -interface-lower -bitop-lower -intrinsic-lower -auto-function-inline  -basicaa -aggrmodref-aa -globalsmodref-aa -aggr-aa  -inst-simplify -simplifycfg   -loop-simplify  -mergereturn -inst-simplify -inst-rectify  -dce -load-elim -bitop-lower  -loop-rewind -pointer-simplify -dce -cfgopt  -dce -bitwidth -loop-bound -loop-dep -read-loop-dep -dce  -check-stream -norm-name -legalize  -validate-dataflow -inst-clarity  D:/personal_srcs/homework/ip_cnn_conv/conv_hls/solution1/.autopilot/db/a.o.2.bc
llvm-dis bugpoint-reduced-simplified.bc 
