package Entity;

public class User {
    private int Userid;        //数据库中编号
    private String userName;   //用户名
    private String account;    //用户账号
    private String password;   //用户密码
    private int Sex;           //用户性别,1为男，0为女
    private String Email;      //用户邮箱
    private String Telephone;  //用户手机号码
    private String Address;    //用户详细地址
    private String photo;      //用户头像
    private String background; //用户背景

    public User(){}
    public User(User user){
        this.Userid = user.Userid;
        this.userName = user.userName;
        this.account = user.account;
        this.password = user.password;
        this.Sex = user.Sex;
        this.Email = user.Email;
        this.Telephone = user.Telephone;
        this.Address = user.Address;
        this.photo = user.photo;
        this.background = user.background;
    }

    public void setUserid(int userid){ this.Userid = userid; }
    public int getUserid(){ return this.Userid; }

    public void setUserName(String thisUserName){ this.userName = thisUserName; }
    public String getUserName(){ return this.userName; }

    public void setAccount(String thisAccount){ this.account = thisAccount; }
    public String getAccount(){ return this.account; }

    public void setPassword(String thisPassword){ this.password = thisPassword; }
    public String getPassword(){ return this.password; }

    public void setSex(int sex) {
        this.Sex = sex;
    }
    public int getSex(){
        return this.Sex;
    }

    public void setEmail(String email){
        this.Email=email;
    }
    public String getEmail(){
        return this.Email;
    }

    public void setTelephone(String telephone){
        this.Telephone=telephone;
    }
    public String getTelephone(){
        return this.Telephone;
    }

    public void setAddress(String address){
        this.Address=address;
    }
    public String getAddress(){
        return this.Address;
    }

    public void setPhoto(String url){ this.photo = url; }
    public String getPhoto(){ return this.photo; }

    public void setBackground(String back){ this.background = back; }
    public String getBackground(){ return this.background; }
}
