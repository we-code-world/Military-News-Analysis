package Service;

import DAO.MessageMapper;
import Entity.Message;

import java.util.List;

public class MessageServiceImpl implements MessageService {
    MessageMapper messageMapper;
    public void setMessageMapper(MessageMapper messageMapper){
        this.messageMapper=messageMapper;
    }
    //保存一条消息
    public int save(Message message){
        return messageMapper.save(message);
    }

    @Override
    public int create(String content, int UserID, int newsid, int catelogid) {
        Message msg = new Message(content);
        msg.setSenderid(UserID);
        msg.setNewsid(newsid);
        msg.setCatelogid(catelogid);
        return save(msg);
    }

    //删除一条消息
    public int delete(int id){
        return messageMapper.delete(id);
    }
    // 查询用户收到的消息列表
    public List<Message> findAll(){
        return messageMapper.findAll();
    }
    //根据短信息id查一条短信息
    public Message findMessageByID(int id){
        return messageMapper.findMessageByID(id);
    }
    //根据用户查找消息列表
    public List<Message> findByUser(int uid){ return messageMapper.findByUser(uid); }
}
