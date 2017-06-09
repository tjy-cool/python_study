subproess 的属性
args            # shell命令
bufsize=-1      # 指定缓冲区，0无缓冲，1行缓冲，其他缓冲区大小，负值为系统缓冲
executable=None,    #
stdin=None      #   标准输入
stdout=None     #   标准输出
stderr=None     #   标准错误
preexec_fn=None #   只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
close_fds=_PLATFORM_DEFAULT_CLOSE_FDS
shell=False     # 同上
cwd=None        # 用于设置子进程的当前目录
env=None        # 用于指定子进程的环境变量。如果env=None,子进程的环境变量将从父进程中继承
universal_newlines=False    # 不同系统的行换行符不同，True同意使用 \n
startupinfo=None    # 只在windows有效，将被传递的底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，子进程的优先级等等
creationflags=0     # 同上
restore_signals=True
start_new_session=False
pass_fds=()