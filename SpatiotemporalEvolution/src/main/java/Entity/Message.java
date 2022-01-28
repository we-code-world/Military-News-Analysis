package Entity;

import Tools.DateUtils;

import java.util.Date;

public class Message {
    private int Messageid;        // 消息id
    private int Senderid;         // 发送者id
    private int Newsid;           //新闻id
    private String Content;       //消息文本
    private int Catelogid;        //类别，1-时间，2-地点，3-武器，4-触发词
    private Date DATE;             // 发送时间

    public int getMessageid() {
        return this.Messageid;
    }
    public void setMessageid(int Mid) {
        this.Messageid = Mid;
    }

    public int getSenderid() {
        return this.Senderid;
    }
    public void setSenderid(int SID) {
        this.Senderid = SID;
    }

    public void setNewsid(int id){ this.Newsid = id; }
    public int getNewsid(){ return this.Newsid; }

    public String getContent(){ return this.Content; }
    public void setContent(String content){ this.Content=content; }

    public void setCatelogid(int id){ this.Catelogid = id; }
    public int getCatelogid(){ return this.Catelogid; }

    public Date getDATE(){ return this.DATE; }
    public void setDATE(Date date){ this.DATE=date; }
    public String showDate(){
        return DateUtils.Date2Str(this.DATE,"yyyy-MM-dd  HH:mm:ss");
    }

    public Message(){}
    public Message(String content){
        Messageid=0;
        Senderid=0;
        Newsid = 1;
        Catelogid = 1;
        Content=content;
        DATE=new Date();
    }
}
