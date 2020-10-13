#将txt文件转csv
#奇怪:保存txt时选的utf-8， 导入使用时仍会报错；改成gbk就好了
import csv
with open('E:/Jobs/nlpproject/test_torch/红楼梦KG/triples.csv', 'w+', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
    # 读要转换的txt文件，文件每行各词间以字符分隔
    with open('E:/Jobs/nlpproject/test_torch/红楼梦KG/triples.txt', 'r', encoding='utf-8') as filein:
        for line in filein:
            line_list = line.strip('\n').split(',')   #我这里的数据之间是以, 间隔的
            spamwriter.writerow(line_list)


import csv
import py2neo
from py2neo import Graph,Node,Relationship,NodeMatcher
#账号密码改为自己的即可
g=Graph('http://localhost:7474',user='neo4j',password='1234')
with open('E:/Jobs/nlpproject/project1/红楼梦KG/triples.csv','r',encoding='gbk') as f:  #改为gbk
    reader=csv.reader(f)
    for item in reader:
        if reader.line_num==1:
            continue
        print("当前行数：",reader.line_num,"当前内容：",item)
        #创建图谱[given标准的数据集，都可以创建图]
        start_node=Node("Person",name=item[0])
        end_node = Node("Person", name=item[1])
        relation=Relationship(start_node,item[3],end_node)
        g.merge(start_node,"Person","name")
        g.merge(end_node, "Person", "name")
        g.merge(relation, "Person", "name")

g.run('match (n) detach delete n')

