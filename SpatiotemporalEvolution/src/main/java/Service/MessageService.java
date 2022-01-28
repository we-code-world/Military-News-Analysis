package Service;

import Entity.Message;

import java.util.List;

public interface MessageService {
    //保存一条消息
    int save(Message message);
    //创建一条消息
    int create(String content, int UserID, int newsid, int catelogid);
    //删除一条消息
    int delete(int id);
    // 查询用户收到的消息列表
    List<Message> findAll();
    //根据短信息id查一条短信息
    Message findMessageByID(int id);
    //根据用户查找消息列表
    List<Message> findByUser(int uid);
}
