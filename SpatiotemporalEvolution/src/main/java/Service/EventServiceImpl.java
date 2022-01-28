package Service;

import DAO.*;
import Entity.*;
import Tools.Container;
import Tools.DateUtils;
import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

import java.util.*;

public class EventServiceImpl implements EventService{
    private EventMapper eventMapper;
    private Container container = new Container();

    public void setEventMapper(EventMapper eventMapper) {
        this.eventMapper = eventMapper;
    }

    @Override
    public PageInfo<Event> pageAllEventByClass(int pageNum, int pageSize, String className) {
        PageHelper.startPage(pageNum,pageSize);
        List<Event> list = eventMapper.findAll();
        PageInfo<Event> page = new PageInfo<>(list);
        return page;
    }

    @Override
    public Event getEventByID(int eventID) {
        return eventMapper.findByID(eventID);
    }

    //获取地图展示数据
    @Override
    public JSONArray getMapValue(String start,String end) {
        JSONArray rtn_Locs = new JSONArray();
        JSONObject rtn;
        Map<String,Integer> Loc_Number = new HashMap<>();
        for (Event event: eventMapper.getALL(start,end)) {
            for (String Loc:event.getEventLocation().split(";")){
                if (Loc_Number.containsKey(Loc)){
                    Loc_Number.put(Loc,Loc_Number.get(Loc)+1);
                }else Loc_Number.put(Loc,0);
            }
        }
        for (Map.Entry<String, Integer> entry : Loc_Number.entrySet()){
            rtn = new JSONObject();
            rtn.put("ID",entry.getKey());
            rtn.put("NUMBER",entry.getValue());
            rtn_Locs.add(rtn);
        }
        return rtn_Locs;
    }

    @Override
    public JSONObject getEvents(String start, String end) {
        JSONObject jsonObject = new JSONObject();
        Date startDay = DateUtils.str2Date(start,"yyyy-MM-dd");
        Date endDay = DateUtils.str2Date(end,"yyyy-MM-dd");
        List<String> yearList = DateUtils.getYearList(startDay, endDay);
        JSONObject dateJson = DateUtils.getYearMonthList(startDay, endDay);
        Calendar c1 = Calendar.getInstance();
        for (String year:yearList) {
            int sum = 0;
            JSONArray yearValue = new JSONArray();
            JSONObject monthValue = new JSONObject();
            for (String month:(List<String>)dateJson.get(year)){
                c1.set(Integer.parseInt(year),Integer.parseInt(month),1);
                Date date_start = c1.getTime();
                c1.add(Calendar.MONTH, 1);
                int count = eventMapper.getCount(DateUtils.Date2Str(date_start,"YYYY-MM-DD HH:MM:SS"),DateUtils.Date2Str(c1.getTime(),"YYYY-MM-DD HH:MM:SS"));
                monthValue = new JSONObject();
                monthValue.put("name",month);
                monthValue.put("value",count);
                sum += count;
                yearValue.add(monthValue);
            }
            jsonObject.put(year,yearValue);
            jsonObject.put(year + "sum",sum);
        }
        return jsonObject;
    }

    @Override
    public List<Event> getALLEvents(String start, String end) {
        return eventMapper.getALL(start,end);
    }


    @Override
    public int[] getCountBySClass(List<Weapon> weapons) {
        int Count[] = {0,0,0,0,0,0};
        for (Weapon w:weapons) {
//            Count[0] += practiceEventMapper.findCountByNum("" + w.getWeaponID());
//            Count[1] += transactionEventMapper.findCountByNum("" + w.getWeaponID());
//            Count[2] += conflictEventMapper.findCountByNum("" + w.getWeaponID());
//            Count[3] += rdEventMapper.findCountByNum("" + w.getWeaponID());
//            Count[4] += eventMapper.findCountByNum("" + w.getWeaponID());
//            Count[5] += provocativeEventMapper.findCountByNum("" + w.getWeaponID());
        }
        return Count;
    }

    @Override
    public int[] getCountBySClass(List<Weapon> weapons,String start, String end) {
        int Count[] = {0,0,0,0,0,0};
        for (Weapon w:weapons) {
//            Count[0] += practiceEventMapper.findCountByNumDate("" + w.getWeaponID(),start,end);
//            Count[1] += transactionEventMapper.findCountByNumDate("" + w.getWeaponID(),start,end);
//            Count[2] += conflictEventMapper.findCountByNumDate("" + w.getWeaponID(),start,end);
//            Count[3] += rdEventMapper.findCountByNumDate("" + w.getWeaponID(),start,end);
//            Count[4] += eventMapper.findCountByNumDate("" + w.getWeaponID(),start,end);
//            Count[5] += provocativeEventMapper.findCountByNumDate("" + w.getWeaponID(),start,end);
        }
        return Count;
    }

    @Override
    public JSONArray getAllWeaponID(String start, String end) {
        JSONArray rtn_weapons = new JSONArray();
        JSONObject rtn;
        Map<String,Integer> Weapon_Number = new HashMap<>();
        for (Event event:eventMapper.getALL(start,end)) {
            for (String weapon:event.getRelateWeapon().split(";")){
                String WeaponID = weapon.substring(weapon.lastIndexOf('-') + 1);
                if (Weapon_Number.containsKey(WeaponID)){
                    Weapon_Number.put(WeaponID,Weapon_Number.get(WeaponID)+1);
                }else Weapon_Number.put(WeaponID,1);
            }
        }
        for (Map.Entry<String, Integer> entry : Weapon_Number.entrySet()){
            rtn = new JSONObject();
            rtn.put("ID",entry.getKey());
            rtn.put("NUMBER",entry.getValue());
            rtn_weapons.add(rtn);
        }
        return rtn_weapons;
    }

    @Override
    public JSONArray getAllWeaponIDClass(String start, String end) {
        JSONArray rtn_weapons = new JSONArray();
        JSONObject rtn;
        Map<String,Integer> Weapon_Number = new HashMap<>();
        for (Event event:eventMapper.getALL(start,end)) {
            for (String weapon:event.getRelateWeapon().split(";")){
                String WeaponID = weapon.substring(weapon.lastIndexOf('-') + 1);
                if (Weapon_Number.containsKey(WeaponID)){
                    Weapon_Number.put(WeaponID,Weapon_Number.get(WeaponID)+1);
                }else Weapon_Number.put(WeaponID,1);
            }
        }
        for (Map.Entry<String, Integer> entry : Weapon_Number.entrySet()){
            rtn = new JSONObject();
            rtn.put("ID",entry.getKey());
            rtn.put("NUMBER",entry.getValue());
            rtn.put("CLASSES",1);
            rtn_weapons.add(rtn);
        }
        return rtn_weapons;
    }

    //获取事件发展连接信息
    @Override
    public List<Link> getLinks() {
        List<Link> mylinks = new ArrayList<>();
        return mylinks;
    }

    //获取简单事件与武器之间的关联
    @Override
    public List<Link> getBriefLinks() {
        List<Link> mylinks = new ArrayList<>();
        mylinks.add(new Link("演习","飞机"));
        mylinks.add(new Link("演习","火炮"));
        mylinks.add(new Link("交易","坦克"));
        mylinks.add(new Link("冲突","飞机"));
        return mylinks;
    }

    //获取简单的数据标签
    @Override
    public List<String> getLegend() {
        List<String> legends= Arrays.asList(new String[]{"演习", "交易", "冲突", "研发", "事故", "挑衅"});
        return legends;
    }

    //获取事件发展时间点数据
    @Override
    public List<TimePointer> getTimePointers(String start, String end) {
        List<TimePointer> timePointers = new ArrayList<>();
        int mi = 0;String now="";
        Map<String,Integer> point = new HashMap<String, Integer>();
        for (Event event:getALLEvents(start,end)) {
            now = DateUtils.Date2Str(event.getEventTime(),"yyyy-MM-dd");
            if (point.containsKey(now)){
                point.put(now,point.get(now)+1);
            }else point.put(now,0);
            timePointers.add(new TimePointer(now,point.get(now),4));
        }
        return timePointers;
    }
}
