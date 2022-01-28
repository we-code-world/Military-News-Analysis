package Entity;

public class Administrator {
    private int Userid;            //数据库中编号
    private String userName;       //用户名
    private String account;        //用户账号
    private String password;       //用户密码

    public void setUserid(int userid){ this.Userid = userid; }
    public int getUserid(){ return this.Userid; }

    public void setUserName(String thisUserName){ this.userName = thisUserName; }
    public String getUserName(){ return this.userName; }

    public void setAccount(String thisAccount){ this.account = thisAccount; }
    public String getAccount(){ return this.account; }

    public void setPassword(String thisPassword){ this.password = thisPassword; }
    public String getPassword(){ return this.password; }

}
