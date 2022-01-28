package Entity;

public class KeySentence {
    private int SentenceID;
    private int newsID;
    private int SentenceNum;
    private String matchTime,matchLoc,weaponName,EventTrigger;

    public void setSentenceID(int sentenceID){ this.SentenceID = sentenceID; }
    public int getSentenceID(){ return this.SentenceID; }

    public void setNewsID(int newsID){ this.newsID = newsID; }
    public int getNewsID(){ return this.newsID; }

    public void setSentenceNum(int num){ this.SentenceNum = num; }
    public int getSentenceNum(){ return this.SentenceNum; }

    public void setMatchTime(String matchTime){ this.matchTime = matchTime; }
    public String getMatchTime(){ return this.matchTime; }

    public void setMatchLoc(String loc){ this.matchLoc = loc; }
    public String getMatchLoc(){ return this.matchLoc; }

    public void setWeaponName(String weaponName){ this.weaponName = weaponName; }
    public String getWeaponName(){ return this.weaponName; }

    public void setEventTrigger(String trigger){ this.EventTrigger = trigger; }
    public String getEventTrigger(){ return this.EventTrigger; }
}
