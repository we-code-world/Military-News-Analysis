package Tools;

import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

public class DateUtils {
    /**
     * 把日期字符串转为java.util.Date类型
     */
    public static Date str2Date(String dateStr, String parttern) {
        SimpleDateFormat sdf = new SimpleDateFormat(parttern);
        Date date = null;
        try {
            date = sdf.parse(dateStr);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return date;
    }

    /**
     * 把java.util.Date类型转为日期字符串
     */
    public static String Date2Str(Date date, String parttern) {
        SimpleDateFormat sdf=new SimpleDateFormat(parttern);
        String dateStr =null;
        try {
            dateStr = sdf.format(date);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return dateStr;
    }
    /**
     * 把java.util.Date类型获取年月字符串数组
     */
    public static List<String> getMonthList(Date start, Date end) {
        List<String> dateStrs = new ArrayList<>();
        SimpleDateFormat dfy = new SimpleDateFormat("yyyy");
        SimpleDateFormat dfm = new SimpleDateFormat("MM");
        int startYear = Integer.parseInt(dfy.format(start));
        int endYear = Integer.parseInt(dfy.format(end));
        int startMonth = Integer.parseInt(dfm.format(start));
        int endMonth = Integer.parseInt(dfm.format(end));
        for (int j=startMonth;j<=12;j++){
            dateStrs.add(""+startYear+"."+j);
        }
        for (int i=startYear+1;i<endYear;i++){
            for (int j=1;j<=12;j++){
                dateStrs.add(""+i+"."+j);
            }
        }
        for (int j=1;j<=endMonth;j++){
            dateStrs.add(""+startYear+"."+j);
        }
        return dateStrs;
    }
    /**
     * 把java.util.Date类型获取年字符串数组
     */
    public static List<String> getYearList(Date start, Date end) {
        List<String> dateStrs = new ArrayList<>();
        SimpleDateFormat dfy = new SimpleDateFormat("yyyy");
        int startYear = Integer.parseInt(dfy.format(start));
        int endYear = Integer.parseInt(dfy.format(end));
        for (int i=startYear;i<=endYear;i++){
                dateStrs.add(""+i);
        }
        return dateStrs;
    }
    /**
     * 把java.util.Date类型获取年字符串数组
     */
    public static JSONObject getYearMonthList(Date start, Date end) {
        JSONObject dateJSONObject = new JSONObject();
        List<String> monthStrs =new ArrayList<>();
        SimpleDateFormat dfy = new SimpleDateFormat("yyyy");
        SimpleDateFormat dfm = new SimpleDateFormat("MM");
        int startYear = Integer.parseInt(dfy.format(start));
        int endYear = Integer.parseInt(dfy.format(end));
        int startMonth = Integer.parseInt(dfm.format(start));
        int endMonth = Integer.parseInt(dfm.format(end));
        for (int j=startMonth;j<=12;j++){
            monthStrs.add("" + j);
        }
        dateJSONObject.put(startYear,monthStrs);
        for (int i=startYear+1;i<endYear;i++){
            monthStrs =new ArrayList<>();
            for (int j=1;j<=12;j++){
                monthStrs.add("" + j);
            }
            dateJSONObject.put(i,monthStrs);
        }
        monthStrs =new ArrayList<>();
        for (int j=1;j<=endMonth;j++){
            monthStrs.add("" + j);
        }
        dateJSONObject.put(endYear,monthStrs);
        return dateJSONObject;
    }
    /**
     * 把java.util.Date类型获取年月日字符串数组
     */
    public static List<String> getYearMonthDayList(Date start, Date end) {
        List<String> dayStrs =new ArrayList<>();
        SimpleDateFormat dfy = new SimpleDateFormat("yyyy");
        SimpleDateFormat dfm = new SimpleDateFormat("MM");
        SimpleDateFormat dfd = new SimpleDateFormat("dd");
        int startYear = Integer.parseInt(dfy.format(start));
        int endYear = Integer.parseInt(dfy.format(end));
        int startMonth = Integer.parseInt(dfm.format(start));
        int endMonth = Integer.parseInt(dfm.format(end));
        int startDay = Integer.parseInt(dfd.format(start));
        int endDay = Integer.parseInt(dfd.format(end));
        Calendar now = Calendar.getInstance();
        now.set(startYear,startMonth,startDay);
        while (true){
            now.add(Calendar.DATE,1);
            dayStrs.add(Date2Str(now.getTime(),"yyyy/MM/dd"));
            if (now.YEAR==endYear && now.MONTH==endMonth && now.DATE==endDay)break;
        }
        return dayStrs;
    }
    /**
     * 把java.util.Date类型获取年月日字符串数组
     */
    public static List<String> getYearMonthDayList(String start, String end){
        return getYearMonthDayList(str2Date(start,"yyyy-MM-dd"),str2Date(end,"yyyy-MM-dd"));
    }
    /**
     * 把java.util.Date类型获取年月字符串数组
     */
    public static List<String> getMonthList(String start, String end){
        return getMonthList(str2Date(start,"yyyy-MM-dd"),str2Date(end,"yyyy-MM-dd"));
    }
    /**
     * 把java.util.Date类型获取年字符串数组
     */
    public static List<String> getYearList(String start, String end){
        return getYearList(str2Date(start,"yyyy-MM-dd"),str2Date(end,"yyyy-MM-dd"));
    }
}
