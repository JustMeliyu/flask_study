# encoding: utf-8
"""
https://blog.csdn.net/ifollowrivers/article/details/73614549
https://blog.csdn.net/zwz2011303359/article/details/63262541
B+树是由平衡二叉树演化而来
二叉查找树
    左子树的键值小于根的键值, 右子树的键值大于根的键值


平衡二叉树(AVL Tree)
    在满足二叉树的条件下, 还满足任意节点的两个子树深度差最多为1

    如果在AVL树中进行插入或删除节点,可能导致AVL树失去平衡,这种失去平衡的二叉树可以概括为四种姿态：
        LL(左左)、RR(右右)、LR(左右)、RL(右左)

    这四种失去平衡的姿态都有各自的定义：
        LL：LeftLeft,也称“左左”. 插入或删除一个节点后,根节点的左孩子(Left Child)的左孩子(Left Child)还有非空节点,
        导致根节点的左子树高度比右子树高度高2,AVL树失去平衡. 
        RR：RightRight,也称“右右”. 插入或删除一个节点后,根节点的右孩子(Right Child)的右孩子(Right Child)还有非空节点,
        导致根节点的右子树高度比左子树高度高2,AVL树失去平衡. 
        LR：LeftRight,也称“左右”. 插入或删除一个节点后,根节点的左孩子(Left Child)的右孩子(Right Child)还有非空节点,
        导致根节点的左子树高度比右子树高度高2,AVL树失去平衡. 
        RL：RightLeft,也称“右左”. 插入或删除一个节点后,根节点的右孩子(Right Child)的左孩子(Left Child)还有非空节点,
        导致根节点的右子树高度比左子树高度高2,AVL树失去平衡. 
    恢复平衡:
        LL: 右旋恢复
        RR: 左旋恢复
        LR: 根节点的左孩子先左旋, 根节点后右旋
        RL: 根节点的右孩子先右旋, 根节点后左旋


平衡多路查找树(B-Tree)：
    B-Tree是为磁盘等外存储设备设计的一种平衡查找树;
    系统从磁盘读取数据到内存时, 是以 磁盘块 为单位; 位于同一个磁盘快的数据会被一次性读取出来, 而不是想要什么取什么;
    InnoDB存储引擎中有页的概念, 页是其磁盘管理的最小单位. InnoDB存储引擎中每个页的大小默认是16kb.
    而系统一个磁盘块的存储空间往往没有那么大, 因此InnoDB每次申请磁盘空间时, 都会是若干地址连续磁盘块来达到页的大小16KB,
    InnoDB在把磁盘数据读入到磁盘时会以页为单位, 在查询数据时, 如果一个页中的每条数据都能帮助定位数据记录的位置, 将会减少磁盘I/O次数, 提高查询效率
    一棵m阶的B-Tree有如下特性：
        1. 每个节点最多有m个孩子. 
        2. 除了根节点和叶子节点外,其它每个节点至少有Ceil(m/2)个孩子. 
        3. 若根节点不是叶子节点,则至少有2个孩子
        4. 所有叶子节点都在同一层,且不包含其它关键字信息
        5. 每个非终端节点包含n个关键字信息(P0,P1,…Pn, k1,…kn)
        6. 关键字的个数n满足：ceil(m/2)-1 <= n <= m-1
        7. ki(i=1,…n)为关键字,且关键字升序排序. 
        8. Pi(i=1,…n)为指向子树根节点的指针. P(i-1)指向的子树的所有节点关键字均小于ki,但都大于k(i-1)
    B-Tree相对于AVL, 缩减了节点个数(即增大每个节点的数据, 进而增大每个节点的大小, 减少每页中磁盘块的个数, 实现减少磁盘I/O次数),
    使每次磁盘I/O取读内存的数据都发挥了作用


B+Tree:
    是对B-Tree的优化, 更适合外存储索引结构, InnoDB就是用的B+Tree索引
    B+Tree是相对于B-Tree, 是没有把data值存储在每一个节点中, 在非叶子节点, 只存储键与指针, 从而可以增加每个节点的键数量,
    增大每页的有效查找效率, 减少树的深度, 减少I/O次数
    与B-Tree的区别:
        1: 非叶子节点只存储键值信息;
        2: 所有叶子节点之间都有一个链指针;
        3: 数据记录都存放在叶子节点中;
        4: 非叶子节点的子树指针与关键字个数相同;   该条是错误的
        5: 非叶子节点的子树指针P[i], ;        指向关键字值属于[K[i], K[i+1]), 左闭右开(好像又不是这样, 父节点中的元素是子节点中最大或最小的元素)
    通常在B+Tree上有两个头指针, 一个指向根节点, 一个指向关键字最小的叶子节点, 而且每个叶子检点之间都是一种链式环结构.
    因此可以对B+Tree进行两种查找运算:
        1: 对主键的范围查找和分页查找
        2: 从根节点开始, 进行随机查找
    一般B+Tree的深度都在2-4层, 所以I/O查找次数一般都在1-3次操作

    范围查找更方便, B-Tree只能通过频繁的中序查找, 寻找范围内的数据;
    而B+Tree则可以先找到范围内最小的元素, 再通过链表依次查询;

    数据库中的B+Tree索引可以分为聚集索引（clustered index）和辅助索引（secondary index）。
    上面的B+Tree示例图在数据库中的实现即为聚集索引，聚集索引的B+Tree中的叶子节点存放的是整张表的行记录数据。
    辅助索引与聚集索引的区别在于辅助索引的叶子节点并不包含行记录的全部数据，而是存储相应行数据的聚集索引键，即主键。
    当通过辅助索引来查询数据时，InnoDB存储引擎会遍历辅助索引找到主键，然后再通过主键在聚集索引中找到完整的行记录数据。


HASH索引:
    就是通过一定的HASH算法, 将键值转化为另一个HASH值, 检索时不需要逐级去查找, 只需一次HASH算法即可定位到相应位置, 速度非常快;
    与B+索引的区别:
        1: 如果是等值查询, 则HASH索引速度要快得多, 前提是键值不存在大量重复的值.
        如果键值不唯一, 就需要先找到键值所在的位置, 然后根据链表往后扫描, 直到找到相应数据;
        2: B+索引的关键字检索效率比较平均, 不像B树那样波动较大.
        在有大量键值的情况下, 哈希索引效率也会降低, 因为会存在哈希碰撞;
        3: 如果是范围查询检索, HASH索引就毫无用武之地, 因为本来是有序的, 但结果HASH函数转化后, 就会变成无序.
        就没办法利用索引完成范围查找;
        4: HASH索引也没有办法完成排序, 或则是像 'like' 的模糊查询.(这种部分模糊查询, 其本质也是范围查询);
        5: HASH索引也不支持多列联合索引的最左匹配规则.



http://www.cnblogs.com/ymj0906/p/4240856.html
https://www.cnblogs.com/softidea/p/5977860.html
唯一索引与主键索引:
唯一索引:
    索引列中所有的值是唯一的, 如果数据库之前存在重复值, 再对该字段添加唯一索引, 会被拒绝;

主键索引:
    主键索引是唯一索引的一种, 数据库中一列用来唯一标识某行的数据, 当在查询中使用主键索引时, 还允许使用快速访问;

比较:
    1: 主键索引不能为空, 而唯一索引可以;
    2: 主键索引可以是几列的组合;
    3: 主键可以做外键, 唯一索引不可以;
    4: 主键索引每个表只能右一个;
    5: 对于主键, 大多数数据库都会只能建立唯一索引;


覆盖索引:
    索引包含所有满足查询的结果的索引称为覆盖索引, 也就是不需要回表操作
    使用explain 查询, type是 index, EXTRA是 USING INDEX, 即为覆盖索引
回表:
    如果索引中的列在select 子句中, 就不需要回表
    如果select 子句中存在大量的非索引项, 索引就需要到相应的表当中找到相应的列的信息, 这就叫回表


https://www.cnblogs.com/hustzzl/p/6075495.html
http://www.cnblogs.com/hailexuexi/archive/2011/11/20/2256020.html
https://www.cnblogs.com/zhp-king/p/7250810.html
https://blog.csdn.net/fly2nn/article/details/61924599
使用explain, type表示查询级别, 有无使用索引, 结果由好到坏:
    system > const > eq_ref > ref > fulltext > ref_or_null > index_merge > unique_subquery > index_subquery > range > index > ALL
    至少达到range级别, 最好达到ref级别, 否则可能出现性能问题
EXTRA类型如下:
判断是否使用了索引, 包括索引的方式
Using index condition: 需要回表
Using index: 覆盖索引, 不需要回表, 不读取数据文件, 只从索引文件获取数据
Using where: 只负责过滤, 与是否需要读取数据文件或索引文件没有关系
Using filesort: 看到这个的时候, 查询就需要优化了. MYSQL需要进行额外的步骤来发现如何对返回的行排序.
                它根据连接类型以及存储排序键值和匹配条件的全部行的行指针来 排序全部行
Using temporary: 看到这个的时候, 查询需要优化了. 这里, MYSQL需要创建一个临时表来存储结果,
                 这通常发生在对不同的列集进行ORDER BY上, 而不是GROUP BY


索引失效的情况:
https://www.cnblogs.com/shynshyn/p/7887742.html
    1: 索引不存储null值
    2: 不适合键值较少的列(性别等)
    3: 前导模糊查询不能利用索引(比如like '%xxx%', 但是'xxx%'是可以的)
    4: 索引失效的几种情况
        a: 条件中有or
        b: 对于多列索引, 如果不是使用的第一部分(最左前缀原则)
        c: like查询以 % 开头
        d: 如果列类型是字符串, 那么一定要在条件中使用引号引起来, 否则不使用索引
        e: 如果mysql 估计使用全表扫描要比使用索引快, 则不会使用索引(索引列存在大量重复的值)

"""