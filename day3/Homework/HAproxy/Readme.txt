HAproxy配置文件操作：
1. 根据用户输入输出对应的backend下的server信息
2. 可添加backend 和sever信息
3. 可修改backend 和sever信息
4. 可删除backend 和sever信息
5. 操作配置文件前进行备份
6 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作
配置文件 参考 http://www.cnblogs.com/alex3714/articles/5717620.html


已完成功能：1,2,4,5,6

使用说明：运行程序，提示需要输入的操作，显示文件中存在的网址:y    查询网址对应的server信息：s
            增加backend和server信息：a       删除backend的server信息：d      退出：q

注意：增加和删除时输入的网址信息必须为指定的格式，否则会报错！！！
       指定格式：{'backend': 'www.oldboy.org','record':{'server': '100.1.7.9','weight': 20,'maxconn': 30}}
        其中www.oldboy.org更换为你需要操作的网址，100.1.7.9更换为你需要操作的ip，20更换为你的weight，30更换为你的maxconn。