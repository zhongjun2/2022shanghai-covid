# -*- coding:utf-8 -*-

info_data =  """
    该应用数据取自[上海市卫生健康委员会](https://wsjkw.sh.gov.cn/xwfb/index.html)每日发布的疫情数据.
    - 每日疫情走势数据,采用官方通报的数据,但并未考虑历史报警感染者转归情况.
    - 自3月18日后, 感染信息披露主体由感染者变为感染社区. 因而无法得知各小区具体感染人数. 空间分布图点的大小对应的是社区被通报的天数.
    - 经纬度数据调用高德 API 转换而得.
    - 本轮疫情期间项目将保持运行,数据实时更新.
    - **一切数据以上海卫建委官方发布为准**
    """

info_contact = """
    - 有任何关于本项目建议或者问题, 可[邮件](kevin_meng@yeah.net)与我联系.
    - 项目源码已发布到 [GItHub](https://github.com/kevin-meng/2022shanghai-covid), 欢迎 Star.
    """

# 预防类
questions_v1 = [{"question":"Q1-01：邻居感染了，我该怎么办？",
            "answer":"""
                    首先不要恐慌。等待有关部门如CDC(中国疾病预防控制中心)或居委的通知。
                    
                    在此期间注意好环境通风，规范佩戴口罩，保持安全的社交距离。
                    
                    此外有条件可以进行核酸或抗原检测。
                    """,
            "note":"信息来源： 【视频】[复旦大学附属中山医院传染病科与感染管理科——胡必杰主任](https://mp.weixin.qq.com/s/_sthbGMedalaZ4FtYjhjNg). 建议查看原文视频",
            },
            {"question":"Q1-02：我怎么知道，是否已经得了新冠？",
            "answer":"""
                    奥密克戎较2年以前的新冠原始病毒有很大不同，真正肺炎的比例很低，绝大部分的CT检测都是显示正常，
                    大部分感染者也都为无症状，少部分感染者有发烧症状。现在确诊新冠的“金标准”就是核酸检测。
                    但是普通市民无法实现每天都核酸检测，所以还有个办法是抗原检测。

                    抗原检测的优点是可自己检测，但不足之处在于灵敏度相对低，尤其在发病的第一天潜伏期以及发病一周以后，
                    它的检测结果往往会显示阴性。但在起病以后1~2天起的连续5天之内，是病毒传染性很高的一段时间，
                    抗原检测可以测出阳性，及时发现病例。
                    
                    所以建议大家**家中常备抗原试剂盒**，
                    当自己有怀疑或周围有发烧人群时候可以测试一下，必要的时候可以多次检测。
                    
                    ---
                    """,
            "note":"信息来源： 【视频】[复旦大学附属中山医院传染病科与感染管理科——胡必杰主任](https://mp.weixin.qq.com/s/_sthbGMedalaZ4FtYjhjNg). 建议查看原文视频",
            },
            {"question":"Q1-03：我在公司上班，如何预防新冠？",
            "answer":"""
                    在当下，规范佩戴口罩、通风、手卫生以及物表消毒是非常重要的。
                     - 现在每天新增的无症状感染者非常多，可能随时会有感染的风险，这时候要当心是否会被一起办公的同事感染，尤其是办公空间比较狭小的情况下。
                     - 上班中被感染的高风险因素是用餐，因为要不可避免地摘掉口罩，特别建议大家一定要错峰就餐。

                     ---
                     """,
            "note":"信息来源： 【视频】[复旦大学附属中山医院传染病科与感染管理科——胡必杰主任](https://mp.weixin.qq.com/s/_sthbGMedalaZ4FtYjhjNg). 建议查看原文视频",
            },
            {"question":"Q1-04：奥密克戎有200种后遗症吗？会致死吗？",
            "answer":"""
                    这种说法是大大夸大了它的后遗症。

                    作为一种病毒感染，奥密克戎和两年前经常侵犯下呼吸道的病毒类型相比，主要局限于上呼吸道。

                    只要患者免疫功能正常，后遗症很少会出现，基本上可以完全康复。

                    目前奥密克戎感染者95%以上是无症状和轻型，普通型也只有3-5%，重型和危重型罕见。

                    ---
                    """,
            "note":"信息来源： 【视频】[复旦大学附属中山医院传染病科与感染管理科——胡必杰主任](https://mp.weixin.qq.com/s/_sthbGMedalaZ4FtYjhjNg). 建议查看原文视频",
            },
            {"question":"Q1-05：如何使用新冠抗原试剂自测？教程",
            "answer":"新冠病毒抗原自测 [检测文字+视频教程](https://mp.weixin.qq.com/s/VfdxENLfEwJSCuTeW15nwg)",
            "note":"信息来源 健康上海12320",
            },
            {"question":"Q1-06：抗原检测对无症状有用吗？还用去医院测核酸吗？",
            "answer":"""
                    **抗原检测，可筛出病毒载量很高的感染者**.

                    抗原检测阴性人员，不能证明没有感染；抗原检测阳性人员，一般即代表感染。

                    一般情况下，只有连续多日内多次测试均为阴性，才表示没有被感染到

                    ---
                    """,
            "note":"信息来源：上海市卫健委[2022-03-15通知](http://wsjkw.sh.gov.cn/crbfz/20220315/3ed6593d38ef4a4483147a6f5340bf87.html)",
            },
            {"question":"Q1-07：新冠病毒抗原自测后的废弃物是什么垃圾？该怎么扔？",
            "answer":"""
                    - **社区居民**
                    * 检测结果**阴性的**，所有鼻拭子、取样管、检测卡作为一般垃圾放入密封袋中，有条件的情况下，可对密封袋进行消毒，而后投放至干垃圾桶内。
                    * 检测结果**阳性的**，密封装袋后，在人员转运时一并交由医疗机构按照医疗废物处理。
                 - **隔离观察人员**
                    * 检测结果不论阴性还是阳性，所有使用后的采样拭子、采样管、检测卡等装入密封袋中，由工作人员按照医疗废弃物处理。

                    ---
                     """,
            "note":"上海发布：[2022-03-27发布](https://mp.weixin.qq.com/s/7yh_lupJw7AOM4MMWi18rg)",
            },    
            ]


# 感染隔离类
questions_v2 = [
            {"question":"Q2-01：如果被通知明天隔离，应该马上准备什么？",
            "answer":"[文章](https://mp.weixin.qq.com/s/cuHQqadjw9gyq_TlBYaJag)的评论区有已隔离朋友的补充信息，大家可进一步调整。",
            "image":["./files/dingxiang.jpg"],
            "note":"信息来源：[丁香医生2022-04-02文章](https://mp.weixin.qq.com/s/cuHQqadjw9gyq_TlBYaJag)",
            },
            {"question":"Q2-02：我是密接，通常要隔离多久？",
            "answer":"""
                     虽然奥密克戎的潜伏期相对较短：**短则1天，平均3天，最长要6-7天左右**。

                     但目前按照国家的要求，依然需要14+7（集中隔离+居家医学观察）。

                     ---
                     """,
            "note":"信息来源： 【视频】[复旦大学附属中山医院传染病科与感染管理科——胡必杰主任](https://mp.weixin.qq.com/s/_sthbGMedalaZ4FtYjhjNg). 建议查看原文视频",
            },
            {"question":"Q2-03：在密接隔离点，如何避免交叉感染？",
            "answer":"""
                    隔离期间应听从安排，不要擅自离开房间，如在走廊中散步等行为是绝对禁止的。

                    同时提高免疫功能，尤其在隔离期间，保持良好的心情和充足的睡眠，适当在屋里进行一些活动，这些都可以增强你的抵抗力，有利于抵抗病毒。

                    ---
                    """,
            "note":"信息来源： 【视频】[复旦大学附属中山医院传染病科与感染管理科——胡必杰主任](https://mp.weixin.qq.com/s/_sthbGMedalaZ4FtYjhjNg). 建议查看原文视频",
            },
            {"question":"Q2-04：奥密克戎，用什么药物治疗？",
            "answer":"""
                    无症状和轻型为主，基本不用药。有喉咙痛、肌肉酸痛、发热症状的，可以用感冒退热药。
            
                    很少数人可能合并细菌感染，口服抗菌药物即可。有高危因素的，比如高龄患者，对这些人群我们要重点保护。
                    如有感染，通过专家评估，起病5天内，使用奈玛特韦/利托那韦片（Paxlovid）可有效抑制发展为重症、避免患者死亡。
                        
                    同时，中医中药也能发挥重要的作用，在高危人群中早期使用，可以有效遏制病情加重。
                    
                    ---
                    """,
            "note":"信息来源： 【视频】[复旦大学附属中山医院传染病科与感染管理科——胡必杰主任](https://mp.weixin.qq.com/s/_sthbGMedalaZ4FtYjhjNg). 建议查看原文视频",
            },
            {"question":"Q2-05：我确诊新冠了，要隔离多久？",
            "answer":"核酸转阴，间隔24小时以上，连续2次就可以出院，从起病到核酸转阴通常2周左右，后阶段基本无传染性。",
            "note":"信息来源： 【视频】[复旦大学附属中山医院传染病科与感染管理科——胡必杰主任](https://mp.weixin.qq.com/s/_sthbGMedalaZ4FtYjhjNg). 建议查看原文视频",
            },
            {"question":"Q2-06：出了隔离治疗点，衣物要怎么处理？",
            "answer":"""
                    有扔掉或烧毁的说法，这是不必要的。
            
                    常温下病毒在很多物体表面存活时间1-2天，极端情况下6天。
                    
                    建议将：衣物放在行李箱或塑料袋，放几天就没有传染性了。
                    
                    ---
                    """,
            "note":"信息来源： 【视频】[复旦大学附属中山医院传染病科与感染管理科——胡必杰主任](https://mp.weixin.qq.com/s/_sthbGMedalaZ4FtYjhjNg). 建议查看原文视频",
            },]


# 感人瞬间
warmly_moments_list = [{"content":"防疫工作者正在家中上空中课堂的孩子开设绿色通道。[原文>>>](https://mp.weixin.qq.com/s/-HTPhOBRVPwpHEi1qGv37g)",
                 "images":"./files/love/2022-03-17-p6.jpg",
                },
                {"content":"早上5点多，沪东新村街道的几位阿姨早起为医护人员准备了暖胃的粥、酱菜、蛋卷，让她们元气满满上“战场”。[原文>>>](https://mp.weixin.qq.com/s/-HTPhOBRVPwpHEi1qGv37g)",
                 "images":"./files/love/2022-03-17-p4.jpg",
                },
                {"content":"川沙新镇一社区，未雨绸缪，为居民在检测区域搭起了“超大号”雨棚。[原文>>>](https://mp.weixin.qq.com/s/-HTPhOBRVPwpHEi1qGv37g)",
                 "images":"./files/love/2022-03-17-p3.jpg",
                },
                {"content":"特殊天气下，居民们撑着色彩各异的雨伞有序排队检测，这井然有序的场面更难能可贵。高空看去，成了小区里一道靓丽的风景线。[原文>>>](https://mp.weixin.qq.com/s/-HTPhOBRVPwpHEi1qGv37g)",
                 "images":"./files/love/2022-03-17-p2.jpg",
                },
                {"content":"下雨天，居民自发为医护人员挂起防水布。[原文>>>](https://mp.weixin.qq.com/s/-HTPhOBRVPwpHEi1qGv37g)",
                 "images":"./files/love/2022-03-17-p1.jpg",
                },
                {"content":"医务人员、志愿者通力协作，上门为小区老弱病残等特殊居民检测核酸。[原文>>>](https://mp.weixin.qq.com/s/-HTPhOBRVPwpHEi1qGv37g)",
                 "images":"./files/love/2022-03-17-p7.png",
                },
                {"content":"“幸好有中山医生！”封控小区里的中山人。因小区封控居家的中山医院医生也在竭尽所能为抗疫贡献自己的一份力量[原文>>>](https://mp.weixin.qq.com/s/9Fsqj4Jp9WZIFTKw-8jJ4Q)",
                 "images":"./files/love/202203-30-p1.png",
                },
                {"content":"""
                    用脚力换取居民的方便和采样的效率的90后“大白”为聋哑人家庭上门采样。

                    浦南医院的“大白”们来到了浦兴路街道，小区志愿者俞彬告诉90后“大白”费蒙燕，周阿姨一家三口都是聋哑人，而且都上了年纪。
                    “用脚力换取居民的方便和采样的效率，怎么都是合算的。
                    ”于是在大雨中，“大白”们和志愿者来到了周阿姨家中，扫码、采样、保存样本……周阿姨感激地打了一连串手语，
                    虽然大家只看懂了“竖大拇指”，但都感受到了她满满的谢意。 
                    [原文>>>](https://mp.weixin.qq.com/s/oRurB79_9d7DJeyP-gRH0Q)""",
                 "images":"./files/love/2022-03-13-p1.jpg",
                },
                {"content":"""
                     3月16日子时，集结出发的白衣战士们。

                     上海市决定，3月16、17日两天48小时内，对重点区域内的人员（已处于管控区域内的人员除外）进行2次核酸筛查。
                     这48小时，真的是每一秒钟都填得满满的。大上海忽然慢了下来。而直面病毒的白衣战士此时不能慢，变身“大白”与病毒展开赛跑。
                     [原文>>>](https://mp.weixin.qq.com/s/oRurB79_9d7DJeyP-gRH0Q)""",
                 "images":"./files/love/2022-03-13-p2.jpg",
                },
                {"content":"""
                    为了高效的去上门采样，防疫人员用马夹袋制作了“风雨袋”。

                    居民区会有老人或者行动不便的人，需要“大白”上门进行核酸采样。核酸采样需要的基本工具有PDA、试管和鼻咽拭子、还有消毒液。
                    但是大白服没有口袋，如果手持这么多东西，采样的时候就会面临“无手可用”的问题。
                    于是检测小姐姐自制风雨袋，更高效的上门为行动不便的人，完成核酸检测工作。
                    [原文>>>](https://mp.weixin.qq.com/s/mYOpEGI5ldKIPfwRCyGqsg)""",
                 "images":"./files/love/2022-03-20-p1.jpg",
                },
                {"content":"康桥镇各核酸采样点的工作人员、志愿者们，为了让前来核酸检测的居村更好操作，主动为他撑伞。[原文>>>](https://mp.weixin.qq.com/s/vk1ppDCVnwmMIlQ0SCZXDQ)",
                 "images":"./files/love/2022-03-20-p2.jpg",
                },
                {"content":"周浦镇在文化中心广场搭建起135顶帐篷，为前来接受核酸检测的居民遮风挡雨。蓝色帐篷宛如“贪吃蛇”，颇为壮观。[原文>>>](https://mp.weixin.qq.com/s/vk1ppDCVnwmMIlQ0SCZXDQ)",
                 "images":"./files/love/2022-03-20-p3.jpg",
                },
                {"content":"上钢派出所民警积极协助居民核酸检测，任由雨水打湿了衣服，依然坚守岗位，有序指挥居民排队，保持1米间隔距离。[原文>>>](https://mp.weixin.qq.com/s/vk1ppDCVnwmMIlQ0SCZXDQ)",
                 "images":"./files/love/2022-03-20-p4.jpg",},
                {"content":"雨水已打湿志愿者的发丝，他们仍然为市民打伞，护你周全。。[原文>>>](https://mp.weixin.qq.com/s/vk1ppDCVnwmMIlQ0SCZXDQ)",
                 "images":"./files/love/2022-03-20-p6.jpg",},
                {"content":"张江镇核酸检测点的医务人员收到了一份特殊的礼物，纸条上的字，让人的心都暖化了。。[原文>>>](https://mp.weixin.qq.com/s/vk1ppDCVnwmMIlQ0SCZXDQ)",
                 "images":"./files/love/2022-03-20-p5.jpg",},
                {"content":"在泥城镇荷风翠庭小区内，志愿者们用沙袋应对“暴雨模式”，铺设出特殊的一米线，为居民们搭起一座“暖心桥”。。[原文>>>](https://mp.weixin.qq.com/s/vk1ppDCVnwmMIlQ0SCZXDQ)",
                 "images":"./files/love/2022-03-20-p7.jpg",},
                 
            ]
