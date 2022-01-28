## 数据库设计

##### 1、新闻表（news）

| 字段名   | 含义         | 类型       | 备注                 |
| -------- | ------------ | ---------- | -------------------- |
| ID*      | 新闻ID       | INT        | *                    |
| Tittle   | 新闻标题     | CHAR（30） | 根据实际情况需要调整 |
| Time     | 新闻报道时间 | Datetime   |                      |
| Url      | 原文链接     | CHAR（50） | 从链接中看出网站来源 |
| Source   | 新闻来源     | CHAR（10） | 新闻来源             |
| Position | 原文地址     | CHAR（20） | 本地存储地址         |

##### 2、时间转换表（TimeTranslater）

| 字段名 | 含义     | 类型     | 备注 |
| ------ | -------- | -------- | ---- |
| ID*    | 地点ID   | INT      | *    |
| Source | 文本时间 | CHAR(50) |      |
| Target |          | CHAR(50) |      |

##### 3、地点转换表（LocationTranslater）

| 字段名 | 含义     | 类型     | 备注 |
| ------ | -------- | -------- | ---- |
| ID*    | 地点ID   | INT      | *    |
| Source | 文本地点 | CHAR(50) | 国家 |
| Target | 原始地点 | CHAR(50) | 地点 |

##### 4、标准武器表（weapons）

| 字段名        | 含义       | 类型      | 备注         |
| ------------- | ---------- | --------- | ------------ |
| weaponID*     | 武器ID     | INT       | *            |
| weaponName    | 武器名称   | CHAR(50)  |              |
| weaponClass   | 武器类别   | CHAR(20)  |              |
| weaponSClass  | 武器小类别 | CHAR(20)  | 武器二级分类 |
| weaponCountry | 武器生产国 | CHAR(200) |              |

##### 5、地点信息表（Locations）

| 字段名    | 含义     | 类型     | 备注 |
| --------- | -------- | -------- | ---- |
| ID*       | 地点ID   | INT      | *    |
| First     | 一级地点 | CHAR(50) | 国家 |
| Second    | 原始地点 | CHAR(50) | 地点 |
| standard  | 标准地点 | CHAR(50) |      |
| longitude | 经度     | DOUBLE   |      |
| latitude  | 纬度     | DOUBLE   |      |

##### 6、武器信息表（Weapons）

| 字段名  | 含义     | 类型     | 备注         |
| ------- | -------- | -------- | ------------ |
| ID*     | 武器ID   | INT      | *            |
| Source  | 原始表述 | CHAR(20) |              |
| Target  | 目标武器 | INT      | 标准武器编号 |
| Level   | 武器等级 | INT      |              |
| Country | 所属国家 | CHAR(50) |              |

##### 7、事件表（Event）

| 字段名       | 含义     | 类型     | 备注                                     |
| ------------ | -------- | -------- | ---------------------------------------- |
| ID*          | 事件编号 | INT      | *                                        |
| Type         | 事件类型 | CHAR(10) |                                          |
| Time         | 发生时间 | DATE     |                                          |
| StartTime    | 开始时间 | DATE     |                                          |
| EndTime      | 结束时间 | DATE     |                                          |
| Location     | 地点     | CHAR(20) |                                          |
| Subject      | 主体     | CHAR(20) |                                          |
| Object       | 客体     | CHAR(20) |                                          |
| Country      | 相关国家 | CHAR(20) |                                          |
| Organization | 相关组织 | CHAR(20) |                                          |
| Trigger      | 触发词   | CHAR(20) |                                          |
| Weapon       | 相关武器 | CHAR(20) |                                          |
| Status       | 事件状态 | INT      | 1，未开始；2，进行中；3，已完成；4，未知 |
| Polarity     | 事件极性 | INT      | 0，肯定；1，可能；2，否定                |
| Sentence     | 句子编号 | INT      |                                          |

##### 8、用户信息表（user）

| 字段名     | 含义   | 类型     | 备注              |
| ---------- | ------ | -------- | ----------------- |
| Userid*    | 用户ID | INT      | *                 |
| userName   | 用户名 | CHAR(20) |                   |
| account    | 账号   | CHAR(20) |                   |
| password   | 密码   | CHAR(20) |                   |
| Sex        | 性别   | int      | 1为男，0为女      |
| Email      | 邮箱   | CHAR(20) |                   |
| Telephone  | 电话   | CHAR(12) |                   |
| Address    | 地址   | CHAR(50) |                   |
| Photo      | 头像   | CHAR(30) | img文件夹下的路径 |
| Background | 背景   | CHAR(30) | img文件夹下的路径 |

##### 9、管理员信息表（administrator）

| 字段名   | 含义   | 类型     | 备注 |
| -------- | ------ | -------- | ---- |
| Userid*  | 用户ID | INT      | *    |
| userName | 用户名 | CHAR(20) |      |
| account  | 账号   | CHAR(20) |      |
| password | 密码   | CHAR(20) |      |

 
