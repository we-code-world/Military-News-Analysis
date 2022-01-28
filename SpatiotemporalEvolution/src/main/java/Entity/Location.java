package Entity;

public class Location {
    private int PosID;           //地点id
    private String country;      //国家或地区
    private String secondPos;     //二级地点
    private String standardPos;  //标准地点
    private int Level;           //地点级别
    private double longitude;    //经度
    private double latitude;     //纬度

    public void setPosID(int posID){ this.PosID = posID; }
    public int getPosID(){ return this.PosID; }

    public void setCountry(String country){ this.country = country; }
    public String getCountry(){ return this.country; }

    public void setSecondPos(String secondpos){ this.secondPos = secondpos; }
    public String getSecondPos(){ return this.secondPos; }

    public void setStandardPos(String standardPos){ this.standardPos = standardPos; }
    public String getStandardPos(){ return  this.standardPos; }

    public void setLevel(int level){ this.Level = level; }
    public int getLevel(){ return this.Level; }

    public void setLongitude(double longitude){ this.longitude = longitude; }
    public double getLongitude(){ return this.longitude; }

    public void setLatitude(double latitude){ this.latitude = latitude; }
    public double getLatitude(){ return this.latitude; }
}
