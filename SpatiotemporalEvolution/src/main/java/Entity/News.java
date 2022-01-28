package Entity;

import Tools.DateUtils;

import java.util.Date;

public class News {
    private int newsID;
    private Date newsTime;
    private String newsTittle, url,newsSource,newsPos;

    public void setNewsID(int newsID){ this.newsID = newsID; }
    public int getNewsID(){ return this.newsID; }

    public void setNewsTime(Date newsTime){ this.newsTime = newsTime; }
    public Date getNewsTime(){ return this.newsTime; }
    public String showDate(){
        return DateUtils.Date2Str(this.newsTime,"yyyy-MM-dd  HH:mm:ss");
    }

    public void setNewsTittle(String tittle){ this.newsTittle = tittle; }
    public String getNewsTittle(){ return this.newsTittle; }

    public void setUrl(String url){ this.url = url; }
    public String getUrl(){ return this.url; }

    public void setNewsSource(String source){ this.newsSource = source; }
    public String getNewsSource(){ return this.newsSource; }

    public void setNewsPos(String pos){ this.newsPos = pos; }
    public String getNewsPos(){ return this.newsPos; }
}
