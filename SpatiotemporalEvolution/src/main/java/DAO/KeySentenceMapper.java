package DAO;

import Entity.KeySentence;
import org.apache.ibatis.annotations.Param;

import java.util.List;

public interface KeySentenceMapper {
    //新建一个事件
    int save(KeySentence KeySentence);
    //根据新闻ID和句编号更新关键句表
    int updateByNewsAndNum(KeySentence KeySentence);
    //根据ID更新关键句表
    int updateByID(KeySentence KeySentence);
    //根据ID查找一个事件
    KeySentence findByID(int id);
    //根据ID删除一个事件
    int delete(int id);
    //通过新闻ID和关键句在新闻中的序号查找所有事件
    KeySentence findAllByNewsIDAndNum(@Param("NewsID") int NewsID,@Param("SentenceNum") int SentenceNum);
    //通过新闻ID查找所有事件
    List<KeySentence> findAllByNewsID(int NewsID);
    //查找所有事件
    List<KeySentence> findAll();
}
