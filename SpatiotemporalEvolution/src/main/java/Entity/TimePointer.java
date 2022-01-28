package Entity;

import Tools.DateUtils;

import java.util.Date;

public class TimePointer {
    private String time;
    private int x;
    private int y;

    public void setTime(String date){ this.time = date; }
    public String getTime(){ return this.time; }

    public void setX(int X){ this.x = X; }
    public int getX(){ return this.x; }

    public void setY(int Y){ this.y = Y; }
    public int getY(){ return this.y; }

    public TimePointer(){}
    public TimePointer(String date,int X,int Y){
        this.time = DateUtils.Date2Str(DateUtils.str2Date(date,"yyyy-MM-dd"),"yyyy/MM/dd");
        this.x = X;
        this.y = Y;
    }
}
