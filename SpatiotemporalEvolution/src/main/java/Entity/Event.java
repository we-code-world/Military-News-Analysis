package Entity;

import Tools.DateUtils;

import java.util.Date;

public class Event {
    public String name;
    public int number;
    private int eventID;
    private Date eventTime;
    private String eventLocation,eventTrigger,relateWeapon,SentenceID;

    public Event(){
        name="";
        number=0;
    }
    public Event(String name, int number){
        this.name=name;
        this.number=number;
    }

    public void setEventID(int id){ this.eventID = id; }
    public int getEventID(){ return this.eventID; }

    public void setEventTime(Date date){ this.eventTime = date; }
    public Date getEventTime(){ return this.eventTime; }
    public String showDate(){
        return DateUtils.Date2Str(this.eventTime,"yyyy-MM-dd  HH:mm:ss");
    }

    public void setEventLocation(String loc){ this.eventLocation = loc; }
    public String getEventLocation(){ return this.eventLocation; }

    public void setEventTrigger(String trigger){ this.eventTrigger = trigger; }
    public String getEventTrigger(){ return this.eventTrigger; }

    public void setRelateWeapon(String weapon){ this.relateWeapon = weapon; }
    public String getRelateWeapon(){ return this.relateWeapon; }

    public void setSentenceID(String sentenceID){ this.SentenceID = sentenceID; }
    public String getSentenceID(){ return this.SentenceID; }
}
