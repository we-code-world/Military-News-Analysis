package Entity;

public class UserInfo extends User {
    private int Days;
    private int Feedback;
    private int Download;

    public UserInfo(){}
    public UserInfo(User user){
        super(user);
        this.Days = 0;
        this.Feedback = 0;
        this.Download = 0;
    }
    public void setDays(int num){ this.Days = num; }
    public int getDays(){ return this.Days; }

    public void setFeedback(int num){ this.Feedback = num; }
    public int getFeedback(){ return this.Feedback; }

    public void setDownload(int num){ this.Download = num; }
    public int getDownload(){ return this.Download; }
}
