package Entity;

import Tools.DateUtils;

import java.util.Date;

public class EventBrief {
    private int conflictEventID;
    private Date conflictEventTime;
    private String conflictEventLocation,activeSubject,sufferSubject,conflictEventTrigger,relateWeapon,SentenceID;

    public void setConflictEventID(int conflictEventID){ this.conflictEventID = conflictEventID; }
    public int getConflictEventID(){ return this.conflictEventID; }

    public void setConflictEventTime(Date date){ this.conflictEventTime = date; }
    public Date getConflictEventTime(){ return this.conflictEventTime; }
    public String showDate(){
        return DateUtils.Date2Str(this.conflictEventTime,"yyyy-MM-dd  HH:mm:ss");
    }

    public void setConflictEventLocation(String loc){ this.conflictEventLocation = loc; }
    public String getConflictEventLocation(){ return this.conflictEventLocation; }

    public void setActiveSubject(String activeSubject){ this.activeSubject = activeSubject; }
    public String getActiveSubject(){ return activeSubject; }

    public void setSufferSubject(String sufferSubject){ this.sufferSubject = sufferSubject; }
    public String getSufferSubject(){ return this.sufferSubject; }

    public void setConflictEventTrigger(String trigger){ this.conflictEventTrigger = trigger; }
    public String getConflictEventTrigger(){ return this.conflictEventTrigger; }

    public void setRelateWeapon(String weapon){ this.relateWeapon = weapon; }
    public String getRelateWeapon(){ return this.relateWeapon; }

    public void setSentenceID(String sentenceID){ this.SentenceID = sentenceID; }
    public String getSentenceID(){ return this.SentenceID; }
}
