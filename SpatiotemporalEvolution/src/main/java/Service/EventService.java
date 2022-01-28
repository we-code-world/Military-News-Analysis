package Service;

import DAO.*;
import Entity.*;
import com.github.pagehelper.PageInfo;
import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

import java.util.List;

public interface EventService {
    void setEventMapper(EventMapper eventMapper);

    PageInfo<Event> pageAllEventByClass(int pageNum, int pageSize, String className);

    Event getEventByID(int eventID);

    //获取地图展示数据
    JSONArray getMapValue(String start,String end);

    //获取practice对应Object
    JSONObject getEvents(String start, String end);

    //获取事件集
    List<Event> getALLEvents(String start, String end);

    //根据武器小类别获取武器数
    int[] getCountBySClass(List<Weapon> weapons);

    //根据武器小类别获取武器数
    int[] getCountBySClass(List<Weapon> weapons,String start, String end);

    //获取所有武器ID
    JSONArray getAllWeaponID(String start, String end);

    //获取所有武器ID
    JSONArray getAllWeaponIDClass(String start, String end);

    //获取事件发展连接信息
    List<Link> getLinks();

    //获取简单事件与武器之间的关联
    List<Link> getBriefLinks();

    //获取简单的数据标签
    List<String> getLegend();

    //获取事件发展时间点数据
    List<TimePointer> getTimePointers(String start, String end);
}
